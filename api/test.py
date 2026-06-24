
import base64
import hashlib
import hmac
import json
import time
import secrets
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

# Фиксированный префикс
PREFIX = "2aa1bUQAAA"

# Секретный ключ (у Likee свой)
SECRET_KEY = secrets.token_bytes(32)

def base64_standard_no_padding(data):
    """
    Кодирует в стандартный Base64 и УДАЛЯЕТ все символы '+', '/', '='
    Остаются только буквы и цифры!
    """
    b64 = base64.b64encode(data).decode('ascii')
    # Удаляем все небуквенно-цифровые символы
    b64 = ''.join(c for c in b64 if c.isalnum())
    return b64

def generate_aes_token(user_id):
    """
    Вариант 1: AES шифрование + чистый Base64 без спецсимволов
    """
    payload = {
        'uid': user_id,
        'exp': int(time.time()) + 3600,
        'iat': int(time.time())
    }
    json_data = json.dumps(payload).encode('utf-8')
    
    # AES-CBC с случайным IV
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(SECRET_KEY), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    
    # PKCS7 padding
    pad_len = 16 - (len(json_data) % 16)
    padded_data = json_data + bytes([pad_len] * pad_len)
    
    encrypted = encryptor.update(padded_data) + encryptor.finalize()
    
    # Склеиваем IV + зашифрованные данные
    token_bytes = iv + encrypted
    
    # Кодируем в чистый Base64 (без + / =)
    token_b64 = base64_standard_no_padding(token_bytes)
    
    return PREFIX + token_b64

def generate_hmac_token(user_id):
    """
    Вариант 2: Данные + HMAC подпись (без спецсимволов)
    """
    payload = {
        'uid': user_id,
        'exp': int(time.time()) + 3600,
        'nonce': secrets.token_hex(8)
    }
    json_data = json.dumps(payload).encode('utf-8')
    
    # Кодируем данные в чистый Base64
    data_b64 = base64_standard_no_padding(json_data)
    
    # Создаем подпись
    signature = hmac.new(SECRET_KEY, json_data, hashlib.sha256).digest()
    sig_b64 = base64_standard_no_padding(signature)
    
    return PREFIX + data_b64 + sig_b64

def generate_random_token(user_id):
    """
    Вариант 3: Случайные байты + ID пользователя
    """
    random_bytes = secrets.token_bytes(32)
    user_bytes = str(user_id).encode('utf-8')
    combined = random_bytes + user_bytes
    
    token_b64 = base64_standard_no_padding(combined)
    return PREFIX + token_b64

def generate_hex_token(user_id):
    """
    Вариант 4: HEX кодировка (только 0-9 и A-F)
    """
    payload = {
        'uid': user_id,
        'exp': int(time.time()) + 3600,
        'nonce': secrets.token_hex(8)
    }
    json_data = json.dumps(payload).encode('utf-8')
    
    # Шифруем AES
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(SECRET_KEY), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    
    pad_len = 16 - (len(json_data) % 16)
    padded_data = json_data + bytes([pad_len] * pad_len)
    
    encrypted = encryptor.update(padded_data) + encryptor.finalize()
    
    # Склеиваем и переводим в HEX (только 0-9 A-F)
    token_hex = (iv + encrypted).hex()
    
    return PREFIX + token_hex

def generate_custom_base64_token(user_id):
    """
    Вариант 5: Свой алфавит Base64 (только буквы и цифры)
    Как в Likee - перемешивание символов без спецсимволов
    """
    # Стандартный алфавит Base64: ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/
    # Убираем +/ и заменяем на другие буквы/цифры
    CUSTOM_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    
    payload = {
        'uid': user_id,
        'exp': int(time.time()) + 3600,
        'salt': secrets.token_hex(16)
    }
    json_data = json.dumps(payload).encode('utf-8')
    
    # Простое шифрование XOR с ключом (для демонстрации)
    key = SECRET_KEY[:16]
    encrypted = bytes([json_data[i % len(json_data)] ^ key[i % len(key)] for i in range(len(json_data))])
    
    # Кодируем в кастомный Base64
    def custom_b64encode(data):
        result = []
        for i in range(0, len(data), 3):
            chunk = data[i:i+3]
            if len(chunk) == 3:
                n = (chunk[0] << 16) | (chunk[1] << 8) | chunk[2]
                result.append(CUSTOM_ALPHABET[(n >> 18) & 63])
                result.append(CUSTOM_ALPHABET[(n >> 12) & 63])
                result.append(CUSTOM_ALPHABET[(n >> 6) & 63])
                result.append(CUSTOM_ALPHABET[n & 63])
            elif len(chunk) == 2:
                n = (chunk[0] << 8) | chunk[1]
                result.append(CUSTOM_ALPHABET[(n >> 10) & 63])
                result.append(CUSTOM_ALPHABET[(n >> 4) & 63])
                result.append(CUSTOM_ALPHABET[(n << 2) & 63])
            else:
                n = chunk[0]
                result.append(CUSTOM_ALPHABET[(n >> 2) & 63])
                result.append(CUSTOM_ALPHABET[(n << 4) & 63])
        return ''.join(result)
    
    token = custom_b64encode(encrypted)
    return PREFIX + token

def analyze_token(token):
    """
    Анализирует токен и показывает его характеристики
    """
    if not token.startswith(PREFIX):
        print("❌ Неверный префикс")
        return
    
    dynamic = token[len(PREFIX):]
    print(f"📊 Длина динамической части: {len(dynamic)} символов")
    print(f"📊 Общая длина токена: {len(token)} символов")
    
    # Проверяем символы
    has_plus = '+' in dynamic
    has_slash = '/' in dynamic
    has_equal = '=' in dynamic
    has_dash = '-' in dynamic
    has_underscore = '_' in dynamic
    
    print(f"🔍 Содержит '+': {has_plus}")
    print(f"🔍 Содержит '/': {has_slash}")
    print(f"🔍 Содержит '=': {has_equal}")
    print(f"🔍 Содержит '-': {has_dash}")
    print(f"🔍 Содержит '_': {has_underscore}")
    
    # Проверяем, только ли буквы и цифры
    only_alnum = dynamic.isalnum()
    print(f"✅ Только буквы и цифры: {only_alnum}")
    
    # Первые 20 символов
    print(f"🔑 Первые 20 символов: {dynamic[:20]}...")
    
    return dynamic

# Демонстрация
if __name__ == "__main__":
    user_id = 1227260487
    
    print("="*80)
    print("ОРИГИНАЛЬНЫЕ ТОКЕНЫ LIKE:")
    print("1. 2aa1bUAAAAM19GQ8Pq13GYGSYtrmGtIBefgO9jOLNksVGv5IB1gb8h3QlZZoRR71xx5rJTs4q2KiD5ozNRYQ7yemzWUt4Kqq31O8ER")
    print("2. 2aa1bUQAAAt2QOMbXuLDheSniyrAVMJ254PgLaCi1FkUOY6dVU5qS4Eh50iD4vqc98Zd84LgYvuuxVnSKjaTx2DJ9KjvzhKkmyeeEl")
    print("="*80)
    
    print("\n🔐 ГЕНЕРИРУЕМ ТОКЕНЫ ТОЛЬКО ИЗ БУКВ И ЦИФР:\n")
    
    print("1️⃣ AES шифрование + чистый Base64:")
    t1 = generate_aes_token(user_id)
    print(t1)
    analyze_token(t1)
    
    print("\n2️⃣ HMAC подпись + чистый Base64:")
    t2 = generate_hmac_token(user_id)
    print(t2)
    analyze_token(t2)
    
    print("\n3️⃣ Случайные байты + ID:")
    t3 = generate_random_token(user_id)
    print(t3)
    analyze_token(t3)
    
    print("\n4️⃣ HEX кодировка (только 0-9 и A-F):")
    t4 = generate_hex_token(user_id)
    print(t4)
    analyze_token(t4)
    
    print("\n5️⃣ Кастомный Base64 (свой алфавит):")
    t5 = generate_custom_base64_token(user_id)
    print(t5)
    analyze_token(t5)
    
    print("\n" + "="*80)
    print("💡 ВЫВОД:")
    print("✅ Все сгенерированные токены содержат ТОЛЬКО буквы и цифры")
    print("✅ Нет символов + / = - _")
    print("✅ Это соответствует формату Likee")
    print("="*80)

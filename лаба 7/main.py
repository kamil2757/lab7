# import re
#
# def count_words(text: str) -> int:
#     """Подсчитывает количество слов в тексте."""
#     return len(text.split())
#
# def count_words_clean(text: str) -> int:
#     """Подсчитывает слова, игнорируя пунктуацию."""
#     words = re.findall(r'\b\w+\b', text)
#     return len(words)
#
# text_1 = "Привет, мир! Как дела?"
# print(f"Слов (с пунктуацией): {count_words(text_1)}")       # 4
# print(f"Слов (без пунктуации): {count_words_clean(text_1)}") # 4
# print()


# import re
# def is_palindrome(text: str) -> bool:
#     """Проверяет, является ли строка палиндромом."""
#     # Очистка: только буквы и цифры, нижний регистр
#     cleaned = re.sub(r'[^\w]', '', text.lower())
#     return cleaned == cleaned[::-1]
#
# tests_palindrome = [
#     "А роза упала на лапу Азора",
#     "Madam, I'm Adam",
#     "Hello, World!",
#     "12321",
#     "racecar"
# ]
#
# for text in tests_palindrome:
#     result = "палиндром" if is_palindrome(text) else "не палиндром"
#     print(f"'{text}' - {result}")
# print()


# def caesar_cipher(text: str, shift: int) -> str:
#     """Шифрует текст шифром Цезаря."""
#     result = []
#     for char in text:
#         if char.isalpha():
#             base = ord('A') if char.isupper() else ord('a')
#             shifted = (ord(char) - base + shift) % 26 + base
#             result.append(chr(shifted))
#         else:
#             result.append(char)
#     return "".join(result)
#
# original = "Hello, World!"
# encrypted = caesar_cipher(original, 3)
# print(f"Оригинал: {original}")
# print(f"Зашифровано: {encrypted}") # Khoor, Zruog!
#
# decrypted = caesar_cipher(encrypted, -3)
# print(f"Расшифровано: {decrypted}") # Hello, World!
# print()
#
#

# import re
# def validate_email(email: str) -> bool:
#     """Проверяет корректность email."""
#     pattern = r'^[\w.+-]+@[\w-]+\.[\w-]+$'
#     return bool(re.match(pattern, email))
#
# def validate_phone(phone: str) -> bool:
#     """Проверяет корректность российского телефона."""
#     pattern = r'^\+7[\s-]+?(\d{3})?[\s-]+?(\d{2})[\s-]+?(\d{2})$'
#     return bool(re.match(pattern, phone))
#
# def validate_url(url: str) -> bool:
#     """Проверяет корректность URL."""
#     pattern = r'^https://[\w-]+\.[\w-]+$'
#     return bool(re.match(pattern, url))
#
# tests_validation = [
#     ("email", "ivan@example.com", validate_email),
#     ("email", "invalid@", validate_email),
#     ("phone", "+7 (999) 123-45-67", validate_phone),
#     ("url", "https://example.com", validate_url),
#     ("url", "not-a-url", validate_url),
# ]
#
# for type_, value, validator in tests_validation:
#     result = "✓" if validator(value) else "X"
#     print(f"{result} {type_}: {value}")
# print()

# students = [
#     ("Иван", 25, 4.5),
#     ("Мария", 22, 4.85),
#     ("Пётр", 30, 4.2),
#     ("Анна", 20, 4.95),
# ]
#
# # Заголовок
# print(f"{'Имя':<10} {'Возраст':>8} {'Балл':>8}")
# print("-" * 28)
#
# # Данные
# for name, age, gpa in students:
#     print(f"{name:<10} {age:>8} {gpa:>8.2f}")
#
# # Итого
# print("-" * 28)
# avg_gpa = sum(s[2] for s in students) / len(students)
# print(f"{'Средний балл':<10} {'':>8} {avg_gpa:>8.2f}")


# text = input('Введите текст:')
#
# def findMaxWord(text):
#     words = text.split()
#
#     max_word = words[0]
#     for w in words:
#         if len(w) > len(max_word):
#             max_word = w
#     return max_word
# print(findMaxWord(text))


# errors_lst = []
# with open('logs.log', 'r', encoding='utf-8') as f:
#     for l in f:
#         if '[ERROR]' in l:
#             errors_lst.append(l)
# print(errors_lst)

# punctuations = [
#     '.', ',', '!', '?', ';', ':', '-', '—', '"', "'", '«', '»',
#     '(', ')', '[', ']', '{', '}', '<', '>', '…',
#     '@', '#', '$', '%', '^', '&', '*', '_', '+', '=', '/', '\\', '|', '~', '`'
# ]
#
# with open('текст.txt', 'r', encoding='utf-8') as f:
#     text = f.read()
#     for p in punctuations:
#         text = text.replace(p, ' ').replace(p, ' ')
#     text = text.lower().split()
#
#     dct = {}
#     for word in set(text):
#         dct[word.lower()] = text.count(word)
#     res = sorted(dct.items(), key=lambda x:x[1], reverse=True)
#
# l = 10
# if len(text) < 10: l = len(text)
# for i in range(10):
#     print(f'{i+1}. {res[i][0]}: {res[i][1]}')


# def func(text, key, mode='зашифровать'):
#     alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
#     text = text.lower()
#     key = key.lower()
#
#     result = ""
#     key_index = 0
#     for char in text:
#         if char in alphabet:
#             char_pos = alphabet.index(char)
#
#             # из-за того что остаток от деления, то число никогда не будет > len(key)
#             key_char = key[key_index % len(key)]
#             key_pos = alphabet.index(key_char)
#
#             if mode == 'зашифровать':
#                 new_pos = (char_pos + key_pos) % 33
#             else:
#                 new_pos = (char_pos - key_pos) % 33
#
#             result += alphabet[new_pos]
#             key_index += 1
#         else:
#             result += char
#
#     return result
#
# original = "привет мир"
# key = "ключ"
#
# encrypted = func(original, key, 'зашифровать')
# decrypted = func(encrypted, key, 'расшифровать')
#
# print(f"Оригинал:    {original}")
# print(f"Ключ:        {key}")
# print(f"Зашифровано: {encrypted}")
# print(f"Расшифровано: {decrypted}")


def validate_json_manual(text):
    text = text.strip()

    if len(text) < 2:
        return False

    print(text)

    if not ((text[0] == "{" and text[-1] == '}') or \
            (text[0] == "[" and text[-1] == ']')):
        return False

    if "'" in text:
        return False

    if ",}" in text or ",]" in text:
        return False

    if "True" in text or "False" in text or "None" in text:
        return False

    return True

text = '{"name": "Иван", "age": 25}'
if validate_json_manual(text):
    print(f"наверн, JSON: {text}")
else:
    print(f"не JSON: {text}")
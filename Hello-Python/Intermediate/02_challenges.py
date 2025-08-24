# Clase en vídeo: https://youtu.be/TbcEqkabAWU?t=4142

### Challenges ###

"""
EL FAMOSO "FIZZ BUZZ”:
Escribe un programa que muestre por consola (con un print) los
números de 1 a 100 (ambos incluidos y con un salto de línea entre
cada impresión), sustituyendo los siguientes:
- Múltiplos de 3 por la palabra "fizz".
- Múltiplos de 5 por la palabra "buzz".
- Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""


"""
Clase 02 — Challenges (retos de programación)

Propósito pedagógico:
- Resolver problemas comunes de programación.
- Practicar lógica y estructuras de control en Python.

Cómo ejecutar:
- python3 Hello-Python/Intermediate/02_challenges.py
"""

from __future__ import annotations


def fizzbuzz() -> None:
    for index in range(1, 101):
        if index % 3 == 0 and index % 5 == 0:
            print("fizzbuzz")
        elif index % 3 == 0:
            print("fizz")
        elif index % 5 == 0:
            print("buzz")
        else:
            print(index)


def is_anagram(word_one: str, word_two: str) -> bool:
    if word_one.lower() == word_two.lower():
        return False
    return sorted(word_one.lower()) == sorted(word_two.lower())


def fibonacci() -> None:
    prev = 0
    next = 1

    for index in range(0, 50):
        print(prev)
        fib = prev + next
        prev = next
        next = fib


def is_prime() -> None:
    for number in range(1, 101):
        if number >= 2:
            is_divisible = False
            for index in range(2, number):
                if number % index == 0:
                    is_divisible = True
                    break
            if not is_divisible:
                print(number)


def reverse(text: str) -> str:
    text_len = len(text)
    reversed_text = ""
    for index in range(0, text_len):
        reversed_text += text[text_len - index - 1]
    return reversed_text


if __name__ == "__main__":
    fizzbuzz()
    print(is_anagram("Amor", "Roma"))
    fibonacci()
    is_prime()
    print(reverse("Hola mundo"))

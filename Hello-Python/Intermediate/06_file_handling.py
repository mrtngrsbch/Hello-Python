"""
Clase 06 — File Handling (manejo de archivos)

Propósito pedagógico:
- Aprender a leer, escribir y manipular diferentes tipos de archivos.
- Practicar con archivos .txt, .json y .csv.

Cómo ejecutar:
- python3 Hello-Python/Intermediate/06_file_handling.py
"""

from __future__ import annotations
import xml
import csv
import json
import os


def demo_file_handling() -> None:
    # .txt file
    txt_file = open("my_file.txt", "w+")
    txt_file.write(
        "Mi nombre es Brais\nMi apellido es Moure\n35 años\nY mi lenguaje preferido es Python")

    txt_file.seek(0)
    print(txt_file.read())

    txt_file.seek(0)
    print(txt_file.read(10))
    print(txt_file.readline())
    print(txt_file.readline())

    for line in txt_file.readlines():
        print(line)

    txt_file.write("\nAunque también me gusta Kotlin")
    txt_file.seek(0)
    print(txt_file.read())
    txt_file.close()

    with open("my_file.txt", "a") as my_other_file:
        my_other_file.write("\nY Swift")

    # .json file
    json_file = open("my_file.json", "w+")
    json_test = {
        "name": "Brais",
        "surname": "Moure",
        "age": 35,
        "languages": ["Python", "Swift", "Kotlin"],
        "website": "https://moure.dev"
    }
    json.dump(json_test, json_file, indent=2)
    json_file.close()

    with open("my_file.json") as my_other_file:
        for line in my_other_file.readlines():
            print(line)

    json_dict = json.load(open("my_file.json"))
    print(json_dict)
    print(type(json_dict))
    print(json_dict["name"])

    # .csv file
    csv_file = open("my_file.csv", "w+")
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["name", "surname", "age", "language", "website"])
    csv_writer.writerow(["Brais", "Moure", 35, "Python", "https://moure.dev"])
    csv_writer.writerow(["Roswell", "", 2, "COBOL", ""])
    csv_file.close()

    with open("my_file.csv") as my_other_file:
        for line in my_other_file.readlines():
            print(line)


if __name__ == "__main__":
    demo_file_handling()

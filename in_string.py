def check_vowels():
    nombre = input("Ingrese nombre: ")
    if "a" in nombre or "A" in nombre:
        print(f"Contiene a: {True}")
    else:
        print(f"Contiene a: {False}")
    if "e" in nombre or "E" in nombre:
        print(f"Contiene e: {True}")
    else:
        print(f"Contiene e: {False}")
    if "i" in nombre or "I" in nombre:
        print(f"Contiene i: {True}")
    else:
        print(f"Contiene i: {False}")
    if "o" in nombre or "O" in nombre:
        print(f"Contiene o: {True}")
    else:
        print(f"Contiene o: {False}")
    if "u" in nombre or "U" in nombre:
        print(f"Contiene u: {True}")
    else:
        print(f"Contiene u: {False}")
    # Código a implementar utilizando input.


# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_in_string_test.py` o `python tp3_in_string_test.py`

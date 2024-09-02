def contar_letra_a(s):
    return s.lower().count('a')

# String a ser verificada
string = input("Informe uma string: ")

quantidade = contar_letra_a(string)
print(f"A letra 'a' ocorre {quantidade} vezes na string.")
print("Bienvenido al detector de palíndromos")
print("Para salir escribe salir")

def no_space(texto):
    new_texto = ""
    for char in texto:
        if char != " ":
            new_texto += char
    return new_texto


def reverse(texto):
    texto_reverso = ""
    for char in texto:
        texto_reverso = char + texto_reverso
    return texto_reverso


def es_palindromo(texto):
    texto = no_space(texto)
    new_texto = reverse(texto)
    return texto == new_texto


text = ""
while True:
    
    text = input("Ingrese la frase o palabra: ")
    if text.lower() == "salir":
        break
    #print("Esta frase:"{text})
    if es_palindromo(text):
        print(f"esta frase '{text}' es palindromo")
    else:
        print(f"esta frase '{text}' no es palindromo")


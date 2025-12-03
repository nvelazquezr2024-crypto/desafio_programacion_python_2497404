# identifica si dos palabras son anagramas 
def anagrama(palabra1, palabra2):
    """
    :param palabra1: La primera palabra a comparar.
    :type palabra1: str
    :param palabra2: La segunda palabra a comparar.
    :type palabra2: str
    :return: True si las palabras son anagramas, False en caso contrario.
    :rtype: bool
    identifica si dos palabras son anagramas

    """
    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()
    return sorted(palabra1) == sorted(palabra2)


print(anagrama("hola", "loha"))
print(anagrama("roma", "amor"))
print(anagrama("hola", "lohA"))

# funcion slugify 

def slugify(texto):
    """
    :param texto: El texto a convertir en slug.
    :type texto: str
    :return: El texto convertido en slug.
    :rtype: str
    """
    texto = texto.lower()
    texto = texto.replace(" ", "-")
    texto = texto.replace("", "")
    return texto  

print(slugify("Hola Mundo"))
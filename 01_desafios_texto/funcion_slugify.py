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
    texto = texto.replace("á", "a")
    texto = texto.replace("é", "e")
    texto = texto.replace("í", "i")
    texto = texto.replace("ó", "o")
    texto = texto.replace("ú", "u")
    texto = texto.replace("ü", "u")
    texto = texto.replace("ñ", "n")
    texto = texto.replace("!", "")
    texto = texto.replace("?", "")
    
  
    return texto

print(slugify("Hola Mundo español!"))
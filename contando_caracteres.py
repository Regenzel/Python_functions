def count_chars():
    '''El usuario inserta una cadena y devuelve su longitud'''
    chars = input("Inserte una cadena de caracteres: ")
    print(chars + " = " + str(len(chars)) + " chars")

count_chars()
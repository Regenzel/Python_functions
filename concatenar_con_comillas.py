def quote_and_author():
    '''Pide al usuario que escriba una cita celebre y un autor y devuelve la cita 
    entre comillas y el autor'''
    quote = input("Inserte la cita celebre: ")
    author = input("Inserte su correspondiente autor: ")
    final_quote = '"'
    print(final_quote + quote + final_quote, "-" + author)

quote_and_author()


def custom_history():
    '''Pide un nombre, un verbo, un adverbio, un adjetivo, y devuelve 
    una historia con esas palabras insertadas.'''
    name = input("Inserte un nombre: ")
    verb = input("Inserte un verbo: ")
    adverb = input("Inserte un adverbio: ")
    adjective = input("Inserte un adjetivo: ")
    return print(f"""Un día, {name} se despertó con ganas de {verb}.
    Lo hizo tan {adverb} que incluso el sol parecía más {adjective} de lo normal.
    Nadie entendía cómo {name} podía convertir una mañana cualquiera en una aventura,
    pero así era siempre: cada vez que decidía {verb}, el día cambiaba por completo""")

custom_history()

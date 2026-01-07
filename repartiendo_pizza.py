def pizza_one_each():
    """
    Pregunta al usuario por personas y cantidad de pizzas y devuelve cuantas porciones corresponden a cada persona
    """
    number = True
    while number:
        persons = input("¿Numero de personas?: ")
        pizzas = input("¿Numero de pizzas?: ")
        if (persons.isnumeric() and pizzas.isnumeric()) and int(persons) > 0 and int(pizzas) > 0: 
            print(f"- {persons} personas con {pizzas} pizzas.")
            print(f"- Cada persona toma {(int(pizzas)*8) // int(persons)} porciones.")
            print(f"- Sobran {(int(pizzas)*8) % int(persons)}.")
            number = False
        else:
            print("--Inserte un numero entero--")
        

pizza_one_each()

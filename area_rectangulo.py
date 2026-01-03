
def room_area():
    """Funcion que pide al usuario la profundidad y el ancho de una habitacion, y devuelve sus metros y yardas cuadrados/as"""
    number = True
    while number:
        depth = input("¿Que profundidad tiene la habitación? (en metros): ")
        width = input("¿Que ancho tiene la habitacion? (en metros): ")
        if depth.isnumeric() or width.isnumeric():
            square_meters = float(depth) * float(width)
            square_yards = square_meters * 1.19599
            print(f"Los metros cuadrados son: {square_meters}\nLas yardas cuadradas son: {square_yards} ")
            number = False
        else:
            print("Inserte unicamente valores numericos")

room_area()
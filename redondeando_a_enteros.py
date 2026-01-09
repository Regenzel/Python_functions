from math import ceil

def room_area():
    """Funcion que pide al usuario la profundidad y el ancho de una habitacion, y devuelve sus metros y yardas cuadrados/as"""
    number = True
    while number:
        depth = input("¿Que profundidad tiene la habitación? (en metros): ")
        width = input("¿Que ancho tiene la habitacion? (en metros): ")
        if depth.isnumeric() and width.isnumeric() and float(depth) > 0 and float(width) > 0:
            square_meters = float(depth) * float(width)
            number = False
            return square_meters
        else:
            print("--Inserte unicamente valores numericos y mayores que 0--")

def paint_liters(room_square_meters):
    """La función recibe los metros cuadrados y devuelve cuantos litros y botes de pintura necesitas para pintarlos."""
    LITERS_PER_ROOM = room_square_meters * 5 / 100
    BOTTLES_PER_ROOM = room_square_meters * 1 / 100
    print(f"Necesitaras {LITERS_PER_ROOM} litros de pintura para pintar {room_square_meters} metros cuadrados de techo.")
    print(f"Tendrás que comprar {ceil(BOTTLES_PER_ROOM)} botes de pintura.")

paint_liters(room_area())
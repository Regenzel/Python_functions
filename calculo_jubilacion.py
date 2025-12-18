from datetime import date

def how_much_for_retirement():
    '''Recibe pidiendo al usuario que edad tiene y a que edad se jubilará, y devuelve los años que le quedan para jubilarse.'''
    year = input("¿Cuantos años tienes?: ")
    when_you_retire = input ("¿A que edad te jubilaras?: ")
    actual_year = date.today().year
    y = int(when_you_retire) - int(year)
    final_y = actual_year + int(when_you_retire)
    if y < 0:
       return print("Ya puede retirarse")

    return print(f"- Te quedan {y} años para jubilarte.\n- Estamos en {actual_year}, te jubilarás en {final_y}.")

how_much_for_retirement()
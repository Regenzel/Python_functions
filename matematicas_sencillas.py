'''Pide al usuario 2 numeros con una serie de reglas, y devuelve su suma, resta, producto y division.'''
are_numbers = False

while are_numbers == False:
    number1 = input("¿Cual es el primer numero que quieres calcular?: ")
    number2 = input("¿Y el segundo?: ")
    if number1.isnumeric() > 0 and number2.isnumeric() > 0:
        are_numbers = True
    else:
        print("Inserte solamente numeros validos (Que sea un numero y que sea mayor que 0)")
    
plus = float(number1) + float(number2)
minus = float(number1) - float(number2)
product = float(number1) * float(number2)
division = float(number1) / float(number2)
print(f"La suma de los numeros es: {plus} \nLa resta es: {minus}\nLa multiplicacion es: {product} \nLa division es: {division}")


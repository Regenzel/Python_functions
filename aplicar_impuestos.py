def custom_tax_calculator():
    """Función que calcula 3 precios con las tasas elegidas y
    devuelve el total con tasas y sin ellas."""
    continue_program = True

    print("---Calculadora de impuestos---")
    while continue_program:
        tax = input("*¿Cual es el porcentaje de impuestos?: ")
        first_price = input("*¿Cual es el primer precio?: ")
        second_price = input("*¿Cual es el segundo precio?: ")
        third_price = input("*¿Cual es el tercer precio?: ")
        try:
            FINAL_TAX = (float(tax) / 100) + 1
            print(f"-Total sin impuestos: {float(first_price) + float(second_price) + float(third_price)}€")
            print(f"-Total con impuestos: {(float(first_price)* FINAL_TAX) + (float(second_price) * FINAL_TAX) + (float(third_price) * FINAL_TAX)}€")
            continue_program = False
        except ValueError:
            print("**Introduzca solo valores numéricos**")        

custom_tax_calculator()
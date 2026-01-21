def convert_money():
    convert_taxes = {"España": 1.0,                
    "Francia": 1.0,
    "Alemania": 1.0,
    "Italia": 1.0,
    "Estados Unidos": 0.93,       # 1 USD -> EUR
    "Reino Unido": 1.16,          # 1 GBP -> EUR
    "Mexico": 0.054,              # 1 MXN -> EUR
    "Argentina": 0.0011,          # 1 ARS -> EUR
    "Brasil": 0.185,              # 1 BRL -> EUR
    "Chile": 0.00095,             # 1 CLP -> EUR
    "Colombia": 0.00024,          # 1 COP -> EUR
    "Japon": 0.00625,             # 1 JPY -> EUR
    "China": 0.128,               # 1 CNY -> EUR
    "Canada": 0.68,               # 1 CAD -> EUR
    "Australia": 0.61}

    country_coin = {"España": "Euro",
    "Francia": "Euro",
    "Alemania": "Euro",
    "Italia": "Euro",
    "Estados Unidos": "Dólar estadounidense",
    "Reino Unido": "Libra esterlina",
    "Mexico": "Peso mexicano",
    "Argentina": "Peso argentino",
    "Brasil": "Real brasileño",
    "Chile": "Peso chileno",
    "Colombia": "Peso colombiano",
    "Japon": "Yen japonés",
    "China": "Yuan chino",
    "Canada": "Dólar canadiense",
    "Australia": "Dólar australiano"}
    cont = True
    while cont:
        country = input("¿De que pais quieres convertir la moneda? ")
        if country in convert_taxes.keys():
            how_much = input(f"¿Cuantos {country_coin.get(country)} quiere convertir a Euros: ")
            if how_much.isnumeric():
                convert = float(how_much) * 0.86
                cont = False
            else:
                print("Inserte un valor numerico")
        else:
            print("Inserte un país válido")
    return print(f"{how_much} {country_coin.get(country)} a una tasa de cambio de {convert_taxes.get(country)}\n--Total {convert} Euros")

convert_money() 
import re

def main():
    # Reconoce palabras como HOLA BOT, pero no la palabra HOLA sola
    patron = re.compile("HOLA\s(.+)")

    # Reconoce palabras como HOLA BOT, Y la palabra HOLA sola
    # patron = re.compile("HOLA\s?(.*)")

    ui = ""
    while ui.upper() != "SALIR":
        ui = input("> ")
        if patron.findall(ui.upper()):
            response = "Saludos, usuario"
        else:
            response = "No tengo todavía una respuesta para esa entrada."
        print(response)

if __name__ == "__main__":
    main()
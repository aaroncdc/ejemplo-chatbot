import re

def main():
    patron = re.compile("(.*)ME LLAMO\s(.+)$")
    ui = ""
    while ui.upper() != "SALIR":
        ui = input("> ")
        coincidencia = patron.findall(ui.upper())
        if len(coincidencia) > 0:
            response = "¡Hola, " + coincidencia[0][1] + "!"
        else:
            response = "No tengo todavía una respuesta para esa entrada."
        print(response)

if __name__ == "__main__":
    main()
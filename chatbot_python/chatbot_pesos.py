import re

def procesar_regla(msg, respuesta):
    operadores = {
        " _ ":"\s([^\s]+)\s",
        " * ":"\s(.+)\s",
        " ? ":"\s?([^\s]+)?\s",
        " ^ ":"\s(.*)?\s",
        "_ ":"^([^\s]+)\s",
        "* ":"^(.+)\s",
        "? ":"([^\s]+)?\s?",
        "^ ":"^(.*)?\s?",
        " _":"\s([^\s]+)$",
        " *":"\s(.+)$",
        " ?":"\s([^\s]+)?$",
        " ^":"\s(.*)$"
    }
    valor = 0
    patron = msg.lstrip().upper()

    if "*" in msg or "_" in msg or "*" in msg or "?" in msg:
        palabras = msg.split(" ")
        for p in palabras:
            if p == "*":
                valor = valor + 90
            elif p == "_":
                valor = valor + 5
            elif p == "?":
                valor = valor + 10
            elif p == "^":
                valor = valor + 100
            else:
                valor = valor + 1
    else:
        valor = 1000 + len(msg.split(" "))

    for op in operadores.keys():
        patron = patron.replace(op, operadores[op])
    patron = re.sub(r"^(\*)$", "(.+)", patron)
    patron = re.sub(r"^(\_)$", "^([^\\\\s]+)$", patron)
    patron = re.sub(r"^(\^)$", "^(.*)?$", patron)
    patron = re.sub(r"^(\?)$", "^([^\\\\s]+)?$", patron)
    return re.compile(patron), valor, respuesta

def main():
    #(REGLA, RESPUESTA)
    patrones = [("ME GUSTA EL FÚTBOL", "A mi también"), ("ME GUSTA *", 'Pues a mi no')]
    diccionario = []
    for patron in patrones:
        diccionario.insert(len(diccionario), procesar_regla(patron[0], patron[1]))
    ui = ""
    while ui.upper() != "SALIR":
        ui = input("> ")
        maxvalor = 0
        preferido = None
        for patron in diccionario:
            coincidencia = patron[0].findall(ui.upper())
            if len(coincidencia) > 0:
                if patron[1] > maxvalor:
                    maxvalor = patron[1]
                    preferido = patron[2]
        if preferido == None:
            response = "No tengo todavía una respuesta para esa entrada."
        else:
            response = preferido
        print(response)

if __name__ == "__main__":
    main()
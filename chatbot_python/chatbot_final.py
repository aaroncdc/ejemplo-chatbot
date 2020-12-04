# chatbot_final.py
# Programa desarrollado por Aarón CdC
# http://www.elinformati.co

# Imports de librerías estandard
import re
import xml.etree.ElementTree as ET
import random
import os

# Diccionario de patrones
diccionario = []

# Función que procesa las reglas
def procesar_regla(msg):
    # REGEX para los operadores de las reglas
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
    # Peso de la regla
    valor = 0
    # Obtenemos el patrón
    patron = msg.lstrip().upper()

    # Cálculo del peso del patrón
    if "*" in msg or "_" in msg or "*" in msg or "?" in msg:
        palabras = msg.split(" ")
        for p in palabras:
            if p == "*":
                valor = valor + 95
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

    # Reemplazamos cada operador de la regla con su correspondiente valor REGEX
    for op in operadores.keys():
        patron = patron.replace(op, operadores[op])
    patron = re.sub(r"^(\*)$", "(.+)", patron)
    patron = re.sub(r"^(\_)$", "^([^\\\\s]+)$", patron)
    patron = re.sub(r"^(\^)$", "^(.*)?$", patron)
    patron = re.sub(r"^(\?)$", "^([^\\\\s]+)?$", patron)
    return re.compile(patron), valor

# Función para procesar el código XML con los patrones.
def procesar_xml():
    for archivo in os.listdir('.'):
        # Cargamos SÓLO los archivos XML
        if archivo.endswith(".xml"):
            documento = ET.parse(archivo)
            # Localizamos todas las reglas y las procesamos
            reglas = documento.getroot().findall('regla')
            for p in reglas:
                print("Procesando: %s" % p.find('patron').text)
                datos = procesar_regla(p.find('patron').text)
                resp = p.findall('respuesta')
                respuestas = []
                for r in resp:
                    respuestas.insert(len(respuestas), r.text)
                patron = {
                    "patron":datos[0],
                    "valor":datos[1],
                    "respuestas":respuestas
                }
                # Una vez procesadas, las introducimos en el diccionario.
                diccionario.insert(len(diccionario), patron)


# Función principal
def main():
    # Cargamos los archivos XML
    procesar_xml()
    ui = ""
    # Pedimos al usuario una entrada de texto y la procesamos, hasta que el usuario
    # introduzca la palabra SALIR.
    while ui.upper() != "SALIR":
        ui = input("> ")
        maxvalor = 0
        preferido = None
        # Buscamos un patrón en el diccionario para la entrada del usuario
        for patron in diccionario:
            coincidencia = patron["patron"].findall(ui.upper())
            if len(coincidencia) > 0:
                if patron["valor"] > maxvalor:
                    maxvalor = patron["valor"]
                    preferido = random.choice(patron["respuestas"])
        # Si no encontramos ninguna respuesta, el bot responde con una respuesta predefinida.
        if preferido == None:
            response = "No tengo todavía una respuesta para esa entrada."
        else:
            response = preferido
        print(response)

# Punto de entrada del programa
if __name__ == "__main__":
    main()
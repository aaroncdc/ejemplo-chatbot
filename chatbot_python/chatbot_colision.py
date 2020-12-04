import re

def main():
    patrones = []
    patrones.insert(len(patrones), {
        "patron":re.compile("ME GUSTA EL FÚTBOL"),
        "respuesta":"A mi también me gusta el fútbol"
        })
    patrones.insert(len(patrones), {
        "patron":re.compile("ME GUSTA\s(.+)$"),
        "respuesta":"Pues a mi no me gusta."
        })
    ui = ""
    print(patrones)
    while ui.upper() != "SALIR":
        ui = input("> ")
        response = None
        #coincidencia1 = patron1.findall(ui.upper())
        for patron in patrones:
            coincidencia = patron["patron"].findall(ui.upper())
            if len(coincidencia) > 0:
                response = patron["respuesta"]
        if response == None:
            response = "No tengo todavía una respuesta para esa entrada."
        print(response)

if __name__ == "__main__":
    main()
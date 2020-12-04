ui = ""
while ui.upper() != "SALIR":
    ui = input("> ")
    if ui.upper() == "HOLA":
        response = "Saludos"
    elif ui.upper() == "QUE TAL?":
        response = "Pues muy bien, ¿Y tú?"
    else:
        response = "No tengo todavía una respuesta para esa entrada."
    print(response)
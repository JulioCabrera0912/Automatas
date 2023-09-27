import tkinter as tk

q01 = "M"

q02 = "N"

q1 = ["T", "U", "V", "W", "X", "Y", "Z"]

q2 = ["A", "B", "C", "D", "E", "F", "G",
      "H", "I", "J", "K", "L", "M", "N",
      "O", "P", "Q", "R", "S", "T"]

q3 = ["-"]

digitos = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
digitos0 = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

q21 = ["A", "B", "C", "D", "E", "F", "G",
      "H", "I", "J", "K", "L", "M", "N",
      "O", "P", "Q", "R", "S", "T", "U",
      "V", "W", "X", "Y", "Z"]

def validar_Cadena():
    estadoInicial = entrada.get()
    EntradaCadena = []
    EntradaCadena.append(estadoInicial)
    elemento = EntradaCadena[0]
    cadena = list(elemento)
    
    print(cadena)
    
    recorrido= ["Estado inicial q0 -> "]

    if len(cadena) == 9:
        if (cadena[0] == q01):
            recorrido.append("q1 ->")
            recorrido_label.config(text=recorrido)
            if (cadena[1] in q1):
                recorrido.append("q3 ->")
                recorrido_label.config(text=recorrido)
                if (cadena[2] in q3):
                    recorrido.append("q4 ->")
                    recorrido_label.config(text=recorrido)
                    if (cadena[3] in digitos):
                        if (cadena[3] == "0"):
                            recorrido.append("q9 ->")
                            recorrido_label.config(text=recorrido)
                            if (cadena[4] == "0"):
                                recorrido.append("q10 ->")
                                recorrido_label.config(text=recorrido)
                                if (cadena[5] == "0"):
                                    recorrido.append("q11 ->")
                                    recorrido_label.config(text=recorrido)
                                    if (cadena[6] in digitos0):
                                        recorrido.append("q12 ->")
                                        recorrido_label.config(text=recorrido)
                                        if (cadena[7] in q3):
                                            recorrido.append("q21 ->")
                                            recorrido_label.config(text=recorrido)
                                            if (cadena[8] in q21):
                                                resultado.config(text="Cadena válida")
                                                recorrido.append("q22 -> Estado de aceptación")
                                                recorrido_label.config(text=recorrido)
                                            else:
                                                resultado.config(text = "Cadena inválida, vuelve a ingresar otra cadena")
                                                recorrido_label.config(text="")
                                        else:
                                            resultado.config(text = "Cadena inválida, vuelve a ingresar otra cadena")
                                            recorrido_label.config(text="")
                                    else:
                                        resultado.config(text = "Cadena inválida, vuelve a ingresar otra cadena")
                                        recorrido_label.config(text="")
                                elif (cadena[5] in digitos0):
                                    recorrido.append("q14 ->")
                                    recorrido_label.config(text=recorrido)
                                    if(cadena[6] in digitos):
                                        recorrido.append("q12 ->")
                                        recorrido_label.config(text=recorrido)
                                        if (cadena[7] in q3):
                                            recorrido.append("q21 ->")
                                            recorrido_label.config(text=recorrido)
                                            if (cadena[8] in q21):
                                                resultado.config(text="Cadena válida")
                                                recorrido.append("q22 -> Estado de aceptación")
                                                recorrido_label.config(text=recorrido)
                                            else:
                                                resultado.config(text = "Cadena inválida, vuelve a ingresar otra cadena")
                                                recorrido_label.config(text="")
                                        else:
                                            resultado.config(text = "Cadena inválida, vuelve a ingresar otra cadena")
                                            recorrido_label.config(text="")
                                    else:
                                        resultado.config(text = "Cadena inválida, vuelve a ingresar otra cadena")
                                        recorrido_label.config(text="")
                                else:
                                    resultado.config(text = "Cadena inválida, vuelve a ingresar otra cadena")
                                    recorrido_label.config(text="")
                            elif (cadena[4] in digitos0):
                                recorrido.append("q13 ->")
                                recorrido_label.config(text=recorrido)
                                if(cadena[5] in digitos):
                                    recorrido.append("q14 ->")
                                    recorrido_label.config(text=recorrido)
                                    if(cadena[6] in digitos):
                                        recorrido.append("q12 ->")
                                        recorrido_label.config(text=recorrido)
                                        if (cadena[7] in q3):
                                            recorrido.append("q21 ->")
                                            recorrido_label.config(text=recorrido)
                                            if (cadena[8] in q21):
                                                resultado.config(text="Cadena válida")
                                                recorrido.append("q22 -> Estado de aceptación")
                                                recorrido_label.config(text=recorrido)
                                            else:
                                                resultado.config(text = "Cadena inválida, vuelve a ingresar otra cadena")
                                                recorrido_label.config(text="")
                                        else:
                                            resultado.config(text = "Cadena inválida, vuelve a ingresar otra cadena")
                                            recorrido_label.config(text="")
                                    else:
                                        resultado.config(text = "Cadena inválida, vuelve a ingresar otra cadena")
                                        recorrido_label.config(text="")
                                else:
                                    resultado.config(text = "Cadena inválida, vuelve a ingresar otra cadena")
                                    recorrido_label.config(text="")
                            else:
                                resultado.config(text = "Cadena inválida, vuelve a ingresar otra cadena")
                                recorrido_label.config(text="")
                        elif (cadena[3] in digitos0):
                            recorrido.append("q5 ->")
                            recorrido_label.config(text=recorrido)
                            if (cadena[4] in digitos0):
                                recorrido.append("q6 ->")
                                recorrido_label.config(text=recorrido)
                                if(cadena[5] in digitos0):
                                    recorrido.append("q7 ->")
                                    recorrido_label.config(text=recorrido)
                                    if(cadena[6] in digitos0):
                                        recorrido.append("q8 ->")
                                        recorrido_label.config(text=recorrido)
                                        if (cadena[7] in q3):
                                            recorrido.append("q21 ->")
                                            recorrido_label.config(text=recorrido)
                                            if (cadena[8] in q21):
                                                resultado.config(text="Cadena válida")
                                                recorrido.append("q22 -> Estado de aceptación")
                                                recorrido_label.config(text=recorrido)
                                            else:
                                                resultado.config(text = "Cadena inválida, vuelve a ingresar otra cadena")
                                                recorrido_label.config(text="")
                                        else:
                                            resultado.config(text = "Cadena inválida, vuelve a ingresar otra cadena")
                                            recorrido_label.config(text="")
                                    elif(cadena[6] == "0"):
                                        recorrido.append("q20 ->")
                                        recorrido_label.config(text=recorrido)
                                        if (cadena[7] in q3):
                                            recorrido.append("q21 ->")
                                            recorrido_label.config(text=recorrido)
                                            if (cadena[8] in q21):
                                                resultado.config(text="Cadena válida")
                                                recorrido.append("q22 -> Estado de aceptación")
                                                recorrido_label.config(text=recorrido)
                                            else:
                                                resultado.config(text = "Cadena inválida, vuelve a ingresar otra cadena")
                                                recorrido_label.config(text="")
                                        else:
                                            resultado.config(text = "Cadena inválida, vuelve a ingresar otra cadena")
                                            recorrido_label.config(text="")
                                    else:
                                        resultado.config(text = "Cadena inválida, vuelve a ingresar otra cadena")
                                        recorrido_label.config(text="")
                                elif(cadena[5] == "0"):
                                    recorrido.append("q18 ->")
                                    recorrido_label.config(text=recorrido)
                                    if(cadena[6] in digitos0):
                                        recorrido.append("q20 ->")
                                        recorrido_label.config(text=recorrido)
                                        if (cadena[7] in q3):
                                            recorrido.append("q21 ->")
                                            recorrido_label.config(text=recorrido)
                                            if (cadena[8] in q21):
                                                resultado.config(text="Cadena válida")
                                                recorrido.append("q22 -> Estado de aceptación")
                                                recorrido_label.config(text=recorrido)
                                            else:
                                                resultado.config(text = "Cadena inválida, vuelve a ingresar otra cadena")
                                                recorrido_label.config(text="")
                                        else:
                                            resultado.config(text = "Cadena inválida, vuelve a ingresar otra cadena")
                                            recorrido_label.config(text="")
                                    elif(cadena[6] == "0"):
                                        recorrido.append("q19 ->")
                                        recorrido_label.config(text=recorrido)
                                        if (cadena[7] in q3):
                                            recorrido.append("q21 ->")
                                            recorrido_label.config(text=recorrido)
                                            if (cadena[8] in q21):
                                                resultado.config(text="Cadena válida")
                                                recorrido.append("q22 -> Estado de aceptación")
                                                recorrido_label.config(text=recorrido)
                                            else:
                                                resultado.config(text = "Cadena inválida, vuelve a ingresar otra cadena")
                                                recorrido_label.config(text="")
                                        else:
                                            resultado.config(text = "Cadena inválida, vuelve a ingresar otra cadena")
                                            recorrido_label.config(text="")
                                    else:
                                        resultado.config(text = "Cadena inválida, vuelve a ingresar otra cadena")
                                        recorrido_label.config(text="")
                                else:
                                    resultado.config(text = "Cadena inválida, vuelve a ingresar otra cadena")
                                    recorrido_label.config(text="")
                            elif (cadena[4] == "0"):
                                recorrido.append("q15 ->")
                                recorrido_label.config(text=recorrido)
                                if (cadena[5] == "0"):
                                    recorrido.append("q16 ->")
                                    recorrido_label.config(text=recorrido)
                                    if(cadena[6] == "0"):
                                        recorrido.append("q17 ->")
                                        recorrido_label.config(text=recorrido)
                                        if (cadena[7] in q3):
                                            recorrido.append("q21 ->")
                                            recorrido_label.config(text=recorrido)
                                            if (cadena[8] in q21):
                                                resultado.config(text="Cadena válida")
                                                recorrido.append("q22 -> Estado de aceptación")
                                                recorrido_label.config(text=recorrido)
                                            else:
                                                resultado.config(text = "Cadena inválida, vuelve a ingresar otra cadena")
                                                recorrido_label.config(text="")
                                        else:
                                            resultado.config(text = "Cadena inválida, vuelve a ingresar otra cadena")
                                            recorrido_label.config(text="")
                                    elif(cadena[6] in digitos0):
                                        recorrido.append("q19 ->")
                                        recorrido_label.config(text=recorrido)
                                        if (cadena[7] in q3):
                                            recorrido.append("q21 ->")
                                            recorrido_label.config(text=recorrido)
                                            if (cadena[8] in q21):
                                                resultado.config(text="Cadena válida")
                                                recorrido.append("q22 -> Estado de aceptación")
                                                recorrido_label.config(text=recorrido)
                                            else:
                                                resultado.config(text = "Cadena inválida, vuelve a ingresar otra cadena")
                                                recorrido_label.config(text="")
                                        else:
                                            resultado.config(text = "Cadena inválida, vuelve a ingresar otra cadena")
                                            recorrido_label.config(text="")
                                    else:
                                        resultado.config(text = "Cadena inválida, vuelve a ingresar otra cadena")
                                        recorrido_label.config(text="")
                                elif (cadena[5] in digitos0):
                                    recorrido.append("q18 ->")
                                    recorrido_label.config(text=recorrido)
                                    if (cadena[6] == "0"):
                                        recorrido.append("q19 ->")
                                        recorrido_label.config(text=recorrido)
                                        if (cadena[7] in q3):
                                            recorrido.append("q21 ->")
                                            recorrido_label.config(text=recorrido)
                                            if (cadena[8] in q21):
                                                resultado.config(text="Cadena válida")
                                                recorrido.append("q22 -> Estado de aceptación")
                                                recorrido_label.config(text=recorrido)
                                            else:
                                                resultado.config(text = "Cadena inválida, vuelve a ingresar otra cadena")
                                                recorrido_label.config(text="")
                                        else:
                                            resultado.config(text = "Cadena inválida, vuelve a ingresar otra cadena")
                                            recorrido_label.config(text="")
                                    elif(cadena[6] in digitos0):
                                        recorrido.append("q20 ->")
                                        recorrido_label.config(text=recorrido)
                                        if (cadena[7] in q3):
                                            recorrido.append("q21 ->")
                                            recorrido_label.config(text=recorrido)
                                            if (cadena[8] in q21):
                                                resultado.config(text="Cadena válida")
                                                recorrido.append("q22 -> Estado de aceptación")
                                                recorrido_label.config(text=recorrido)
                                            else:
                                                resultado.config(text = "Cadena inválida, vuelve a ingresar otra cadena")
                                                recorrido_label.config(text="")
                                        else:
                                            resultado.config(text = "Cadena inválida, vuelve a ingresar otra cadena")
                                            recorrido_label.config(text="")
                                    else:
                                        resultado.config(text = "Cadena inválida, vuelve a ingresar otra cadena")
                                        recorrido_label.config(text="")
                                else:
                                    resultado.config(text = "Cadena inválida, vuelve a ingresar otra cadena")
                                    recorrido_label.config(text="")
                            else:
                                resultado.config(text = "Cadena inválida, vuelve a ingresar otra cadena")
                                recorrido_label.config(text="")
                        else:
                            resultado.config(text = "Cadena inválida, vuelve a ingresar otra cadena")
                            recorrido_label.config(text="")
                    else:
                        resultado.config(text = "Cadena inválida, vuelve a ingresar otra cadena")
                        recorrido_label.config(text="")
                else:
                    resultado.config(text = "Cadena inválida, vuelve a ingresar otra cadena")
                    recorrido_label.config(text="")
            else:
                resultado.config(text = "Cadena inválida, vuelve a ingresar otra cadena")
                recorrido_label.config(text="")
        elif (cadena[0] == q02):
                recorrido.append("q2 ->")
                recorrido_label.config(text=recorrido)
                if (cadena[1] in q2):
                    recorrido.append("q3 ->")
                    recorrido_label.config(text=recorrido)
                    if (cadena[2] in q3):
                        recorrido.append("q4 ->")
                        recorrido_label.config(text=recorrido)
                        if (cadena[3] in digitos):
                            if (cadena[3] == "0"):
                                recorrido.append("q9 ->")
                                recorrido_label.config(text=recorrido)
                                if (cadena[4] == "0"):
                                    recorrido.append("q10 ->")
                                    recorrido_label.config(text=recorrido)
                                    if (cadena[5] == "0"):
                                        recorrido.append("q11 ->")
                                        recorrido_label.config(text=recorrido)
                                        if (cadena[6] in digitos0):
                                            recorrido.append("q12 ->")
                                            recorrido_label.config(text=recorrido)
                                            if (cadena[7] in q3):
                                                recorrido.append("q21 ->")
                                                recorrido_label.config(text=recorrido)
                                                if (cadena[8] in q21):
                                                    resultado.config(text="Cadena válida")
                                                    recorrido.append("q22 -> Estado de aceptación")
                                                    recorrido_label.config(text=recorrido)
                                                else:
                                                    resultado.config(text = "Cadena inválida, vuelve a ingresar otra cadena")
                                                    recorrido_label.config(text="")
                                            else:
                                                resultado.config(text = "Cadena inválida, vuelve a ingresar otra cadena")
                                                recorrido_label.config(text="")
                                        else:
                                            resultado.config(text = "Cadena inválida, vuelve a ingresar otra cadena")
                                            recorrido_label.config(text="")
                                    elif (cadena[5] in digitos0):
                                        recorrido.append("q14 ->")
                                        recorrido_label.config(text=recorrido)
                                        if(cadena[6] in digitos):
                                            recorrido.append("q12 ->")
                                            recorrido_label.config(text=recorrido)
                                            if (cadena[7] in q3):
                                                recorrido.append("q21 ->")
                                                recorrido_label.config(text=recorrido)
                                                if (cadena[8] in q21):
                                                    resultado.config(text="Cadena válida")
                                                    recorrido.append("q22 -> Estado de aceptación")
                                                    recorrido_label.config(text=recorrido)
                                                else:
                                                    resultado.config(text = "Cadena inválida, vuelve a ingresar otra cadena")
                                                    recorrido_label.config(text="")
                                            else:
                                                resultado.config(text = "Cadena inválida, vuelve a ingresar otra cadena")
                                                recorrido_label.config(text="")
                                        else:
                                            resultado.config(text = "Cadena inválida, vuelve a ingresar otra cadena")
                                            recorrido_label.config(text="")
                                    else:
                                        resultado.config(text = "Cadena inválida, vuelve a ingresar otra cadena")
                                        recorrido_label.config(text="")
                                elif (cadena[4] in digitos0):
                                    recorrido.append("q13 ->")
                                    recorrido_label.config(text=recorrido)
                                    if(cadena[5] in digitos):
                                        recorrido.append("q14 ->")
                                        recorrido_label.config(text=recorrido)
                                        if(cadena[6] in digitos):
                                            recorrido.append("q12 ->")
                                            recorrido_label.config(text=recorrido)
                                            if (cadena[7] in q3):
                                                recorrido.append("q21 ->")
                                                recorrido_label.config(text=recorrido)
                                                if (cadena[8] in q21):
                                                    resultado.config(text="Cadena válida")
                                                    recorrido.append("q22 -> Estado de aceptación")
                                                    recorrido_label.config(text=recorrido)
                                                else:
                                                    resultado.config(text = "Cadena inválida, vuelve a ingresar otra cadena")
                                                    recorrido_label.config(text="")
                                            else:
                                                resultado.config(text = "Cadena inválida, vuelve a ingresar otra cadena")
                                                recorrido_label.config(text="")
                                        else:
                                            resultado.config(text = "Cadena inválida, vuelve a ingresar otra cadena")
                                            recorrido_label.config(text="")
                                    else:
                                        resultado.config(text = "Cadena inválida, vuelve a ingresar otra cadena")
                                        recorrido_label.config(text="")
                                else:
                                    resultado.config(text = "Cadena inválida, vuelve a ingresar otra cadena")
                                    recorrido_label.config(text="")
                            elif (cadena[3] in digitos0):
                                recorrido.append("q5 ->")
                                recorrido_label.config(text=recorrido)
                                if (cadena[4] in digitos0):
                                    recorrido.append("q6 ->")
                                    recorrido_label.config(text=recorrido)
                                    if(cadena[5] in digitos0):
                                        recorrido.append("q7 ->")
                                        recorrido_label.config(text=recorrido)
                                        if(cadena[6] in digitos0):
                                            recorrido.append("q8 ->")
                                            recorrido_label.config(text=recorrido)
                                            if (cadena[7] in q3):
                                                recorrido.append("q21 ->")
                                                recorrido_label.config(text=recorrido)
                                                if (cadena[8] in q21):
                                                    resultado.config(text="Cadena válida")
                                                    recorrido.append("q22 -> Estado de aceptación")
                                                    recorrido_label.config(text=recorrido)
                                                else:
                                                    resultado.config(text = "Cadena inválida, vuelve a ingresar otra cadena")
                                                    recorrido_label.config(text="")
                                            else:
                                                resultado.config(text = "Cadena inválida, vuelve a ingresar otra cadena")
                                                recorrido_label.config(text="")
                                        elif(cadena[6] == "0"):
                                            recorrido.append("q20 ->")
                                            recorrido_label.config(text=recorrido)
                                            if (cadena[7] in q3):
                                                recorrido.append("q21 ->")
                                                recorrido_label.config(text=recorrido)
                                                if (cadena[8] in q21):
                                                    resultado.config(text="Cadena válida")
                                                    recorrido.append("q22 -> Estado de aceptación")
                                                    recorrido_label.config(text=recorrido)
                                                else:
                                                    resultado.config(text = "Cadena inválida, vuelve a ingresar otra cadena")
                                                    recorrido_label.config(text="")
                                            else:
                                                resultado.config(text = "Cadena inválida, vuelve a ingresar otra cadena")
                                                recorrido_label.config(text="")
                                        else:
                                            resultado.config(text = "Cadena inválida, vuelve a ingresar otra cadena")
                                            recorrido_label.config(text="")
                                    elif(cadena[5] == "0"):
                                        recorrido.append("q18 ->")
                                        recorrido_label.config(text=recorrido)
                                        if(cadena[6] in digitos0):
                                            recorrido.append("q20 ->")
                                            recorrido_label.config(text=recorrido)
                                            if (cadena[7] in q3):
                                                recorrido.append("q21 ->")
                                                recorrido_label.config(text=recorrido)
                                                if (cadena[8] in q21):
                                                    resultado.config(text="Cadena válida")
                                                    recorrido.append("q22 -> Estado de aceptación")
                                                    recorrido_label.config(text=recorrido)
                                                else:
                                                    resultado.config(text = "Cadena inválida, vuelve a ingresar otra cadena")
                                                    recorrido_label.config(text="")
                                            else:
                                                resultado.config(text = "Cadena inválida, vuelve a ingresar otra cadena")
                                                recorrido_label.config(text="")
                                        elif(cadena[6] == "0"):
                                            recorrido.append("q19 ->")
                                            recorrido_label.config(text=recorrido)
                                            if (cadena[7] in q3):
                                                recorrido.append("q21 ->")
                                                recorrido_label.config(text=recorrido)
                                                if (cadena[8] in q21):
                                                    resultado.config(text="Cadena válida")
                                                    recorrido.append("q22 -> Estado de aceptación")
                                                    recorrido_label.config(text=recorrido)
                                                else:
                                                    resultado.config(text = "Cadena inválida, vuelve a ingresar otra cadena")
                                                    recorrido_label.config(text="")
                                            else:
                                                resultado.config(text = "Cadena inválida, vuelve a ingresar otra cadena")
                                                recorrido_label.config(text="")
                                        else:
                                            resultado.config(text = "Cadena inválida, vuelve a ingresar otra cadena")
                                            recorrido_label.config(text="")
                                    else:
                                        resultado.config(text = "Cadena inválida, vuelve a ingresar otra cadena")
                                        recorrido_label.config(text="")
                                elif (cadena[4] == "0"):
                                    recorrido.append("q15 ->")
                                    recorrido_label.config(text=recorrido)
                                    if (cadena[5] == "0"):
                                        recorrido.append("q16 ->")
                                        recorrido_label.config(text=recorrido)
                                        if(cadena[6] == "0"):
                                            recorrido.append("q17 ->")
                                            recorrido_label.config(text=recorrido)
                                            if (cadena[7] in q3):
                                                recorrido.append("q21 ->")
                                                recorrido_label.config(text=recorrido)
                                                if (cadena[8] in q21):
                                                    resultado.config(text="Cadena válida")
                                                    recorrido.append("q22 -> Estado de aceptación")
                                                    recorrido_label.config(text=recorrido)
                                                else:
                                                    resultado.config(text = "Cadena inválida, vuelve a ingresar otra cadena")
                                                    recorrido_label.config(text="")
                                            else:
                                                resultado.config(text = "Cadena inválida, vuelve a ingresar otra cadena")
                                                recorrido_label.config(text="")
                                        elif(cadena[6] in digitos0):
                                            recorrido.append("q19 ->")
                                            recorrido_label.config(text=recorrido)
                                            if (cadena[7] in q3):
                                                recorrido.append("q21 ->")
                                                recorrido_label.config(text=recorrido)
                                                if (cadena[8] in q21):
                                                    resultado.config(text="Cadena válida")
                                                    recorrido.append("q22 -> Estado de aceptación")
                                                    recorrido_label.config(text=recorrido)
                                                else:
                                                    resultado.config(text = "Cadena inválida, vuelve a ingresar otra cadena")
                                                    recorrido_label.config(text="")
                                            else:
                                                resultado.config(text = "Cadena inválida, vuelve a ingresar otra cadena")
                                                recorrido_label.config(text="")
                                        else:
                                            resultado.config(text = "Cadena inválida, vuelve a ingresar otra cadena")
                                            recorrido_label.config(text="")
                                    elif (cadena[5] in digitos0):
                                        recorrido.append("q18 ->")
                                        recorrido_label.config(text=recorrido)
                                        if (cadena[6] == "0"):
                                            recorrido.append("q19 ->")
                                            recorrido_label.config(text=recorrido)
                                            if (cadena[7] in q3):
                                                recorrido.append("q21 ->")
                                                recorrido_label.config(text=recorrido)
                                                if (cadena[8] in q21):
                                                    resultado.config(text="Cadena válida")
                                                    recorrido.append("q22 -> Estado de aceptación")
                                                    recorrido_label.config(text=recorrido)
                                                else:
                                                    resultado.config(text = "Cadena inválida, vuelve a ingresar otra cadena")
                                                    recorrido_label.config(text="")
                                            else:
                                                resultado.config(text = "Cadena inválida, vuelve a ingresar otra cadena")
                                                recorrido_label.config(text="")
                                        elif(cadena[6] in digitos0):
                                            recorrido.append("q20 ->")
                                            recorrido_label.config(text=recorrido)
                                            if (cadena[7] in q3):
                                                recorrido.append("q21 ->")
                                                recorrido_label.config(text=recorrido)
                                                if (cadena[8] in q21):
                                                    resultado.config(text="Cadena válida")
                                                    recorrido.append("q22 -> Estado de aceptación")
                                                    recorrido_label.config(text=recorrido)
                                                else:
                                                    resultado.config(text = "Cadena inválida, vuelve a ingresar otra cadena")
                                                    recorrido_label.config(text="")
                                            else:
                                                resultado.config(text = "Cadena inválida, vuelve a ingresar otra cadena")
                                                recorrido_label.config(text="")
                                        else:
                                            resultado.config(text = "Cadena inválida, vuelve a ingresar otra cadena")
                                            recorrido_label.config(text="")
                                    else:
                                        resultado.config(text = "Cadena inválida, vuelve a ingresar otra cadena")
                                        recorrido_label.config(text="")
                                else:
                                    resultado.config(text = "Cadena inválida, vuelve a ingresar otra cadena")
                                    recorrido_label.config(text="")
                            else:
                                resultado.config(text = "Cadena inválida, vuelve a ingresar otra cadena")
                                recorrido_label.config(text="")
                        else:
                            resultado.config(text = "Cadena inválida, vuelve a ingresar otra cadena")
                            recorrido_label.config(text="")
                    else:
                        resultado.config(text = "Cadena inválida, vuelve a ingresar otra cadena")
                        recorrido_label.config(text="")
                else:
                    resultado.config(text = "Cadena inválida, vuelve a ingresar otra cadena")
                    recorrido_label.config(text="")
        else:
            resultado.config(text = "Cadena inválida, vuelve a ingresar otra cadena")
            recorrido_label.config(text="")
    else:
            resultado.config(text = "Cadena inválida, vuelve a ingresar otra cadenaNADA")
            recorrido_label.config(text="")
    

ventana = tk.Tk()
ventana.title("Autómata finito")

ventana.geometry("700x200")

texto_label = tk.Label(ventana, text="Ingrese una cadena:")
texto_label.pack()

texto_label = tk.Label(ventana, text="Rangos: MT-0001-A  hasta  NT-9999-Z")
texto_label.pack()

entrada = tk.Entry(ventana, width=20)
entrada.pack()

boton_validar = tk.Button(ventana, text="Validar", command = validar_Cadena)
boton_validar.pack()

resultado = tk.Label(ventana, text="")
resultado.pack()

recorrido_label = tk.Label(ventana, text="")
recorrido_label.pack()

ventana.mainloop()



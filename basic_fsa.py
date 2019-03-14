
# Ambas dos funciones son sin estado, eso quiere decir
# que son puras, serian algo asi como funciones matematicas

def transicion(estado, cadena):
    caracter = cadena[0]
    resto = cadena[1:]

    if estado == 'q0' and caracter == "0":
        return ('q1', resto, False)

    if estado == 'q1' and caracter == "0":
        return ('q2', resto, False)

    if estado == 'q1' and caracter == "1":
        # final
        return ('q3', resto, True)

    if estado == 'q2' and caracter == "1":
        # final
        return ('q3', resto, True)


    return ('t', "", False)


def evaluar_cadena(cadena):
    ci = ("q0", cadena, False)
    while True:
        print ci
        (estado, cadena, aceptada) = ci
        if aceptada:
            break

        if len(cadena) == 0:
            break

        ci = transicion(estado, cadena)

    return ci[2]


aceptada = evaluar_cadena("001")
if aceptada:
    print "cadena aceptada"
else:
    print "cadena rechazada"

aceptada = evaluar_cadena("111")
if aceptada:
    print "cadena aceptada"
else:
    print "cadena rechazada"


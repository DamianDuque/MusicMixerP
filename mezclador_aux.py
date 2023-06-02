from datetime import datetime

def generarId():
    now = datetime.now()
    dia = format(now.day)
    mes = format(now.month)
    anio = format(now.year)
    hora = format(now.hour)
    minuto = format(now.minute)
    segundo = format(now.second)

    if int(dia) < 10:
        dia = "0" + dia
    if int(mes) < 10:
        mes = "0" + mes
    anio = anio[2:]
    if int(hora) < 10:
        hora = "0" + hora
    if int(minuto) < 10:
        minuto = "0" + minuto
    if int(segundo) < 10:
        segundo = "0" + segundo

    id = dia + mes + anio + hora + minuto + segundo

    return id    
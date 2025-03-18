h = int(input('Ingrese la hora: '))
m = int(input('Ingrese el minuto: '))
duración_minutos = int(input('Ingrese la duración en minutos: '))

hora_en_minutos = h * 60 + m + duración_minutos
hora_evento = (hora_en_minutos // 60) % 24
minutos_evento = hora_en_minutos % 60

print('El evento culmina a las', hora_evento, ':' , minutos_evento)


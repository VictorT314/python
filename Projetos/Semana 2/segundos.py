segundos = input("Por favor, entre com o número de segundos que deseja converter: ")

segundos = int(segundos)
dias = segundos // 86400
segRestante = segundos % 86400
horas = segRestante // 3600
segRestante = segRestante % 3600
minutos = segRestante // 60
segRestante = segRestante % 60
segundos = segRestante

print(dias,"dias,", horas,"horas,", minutos,"minutos e",segundos,"segundos.")

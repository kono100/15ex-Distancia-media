''' Escreva um programa que leia uma distância percorrida (km) e um tempo (horas). Retorne a 
velocidade média (km/h). '''

dist = float(input('Quantos kilometros você correu? '))
tempo = float(input('Quantas horas você correu? '))
media = dist/tempo
print(f'A velocidade média foi de {media:.2f}km/h')

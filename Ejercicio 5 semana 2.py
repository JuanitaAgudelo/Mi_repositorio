#Las reglas para representar un número en el sistema romano son las siguientes:
# Los símbolos I, X, C y M se pueden repetir hasta tres veces.
# Los símbolos V, L y D no pueden repetirse.
# Los símbolos I, X y C se suman si están a la derecha de otro mayor o igual.
# Los símbolos I, X y C se restan si están a la izquierda de otro mayor y solamente pueden anteponerse a los dos símbolos que le siguen en la sucesión:
# I se resta de V y X
# X se resta de L y C
# C se resta de D y M
# Los símbolos V, L y D no pueden colocarse a la izquierda de otro mayor.
# Una raya escrita sobre un grupo de símbolos aumenta su valor en mil veces.
# Dos rayas escritas sobre un grupo de símbolos aumentan su valor en un millón de veces.
#Las equivalencias de los símbollos son:
#I = 1 V = 5 X = 10 L = 50
#C = 100 D = 500 M = 1000
#Dado un número decimal, realizar la respectiva conversión a números romanos

print('Programa para convertir a numeros romanos ')

num=int(input('Ingrese el numero que desea convertir '))

if num>=0 and num<4000:
    r=''   #como r va a contener letras, se inicializa en cero, equivalente en letras, a la cadena vacía.
    
    while num>0:
        if num>=1000:
            num-=1000
            r+='M'
        elif num>=900:
            num-=900
            r+='CM'
        elif num>=500:
            num-=500
            r+='D'
        elif num>=400:
            num-=400
            r+='CD'
        elif num>=100:
            num-=100
            r+='C'
        elif num>=90:
            num-=90
            r+='XC'
        elif num>=50:
            num-=50
            r+='L'
        elif num>=40:
            num-=40
            r+='XL'
        elif num>=10:
            num-=10
            r+='X'
        elif num>=9:
            num-=9
            r+='IX'
        elif num>=5:
            num-=5
            r+='V'
        elif num>=4:
            num-=4
            r+='IV'
        else :
            num-=1
            r+='I'
    print('El numero romano es ', r)
else:
    print('datos no validos (Numeros enteros y menor de 4000')

#terminar el probelma con las rayas encima ajja     

    

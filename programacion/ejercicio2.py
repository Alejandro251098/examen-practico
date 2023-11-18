# ejercicio 2 : funcion para tabla de multiplicar




def tabla_multi( numeros):
   
    for multiplos in range(1, 11):
         
         print(numeros, '*', multiplos, '=', numeros*multiplos) 



numeros = int(input('Ingrese un numero'))


tabla_multi(numeros)
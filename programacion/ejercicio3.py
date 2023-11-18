# ejercicio 3: funcion para numeros primos


def verificar_primos(numero):
    contador = 0
    if numero < 1 :
      return print("ingrese un numero mayor a 1")
    for i in range(1, numero +1 ):
     if (numero % i) == 0: 
        contador+=1
        
    
        
numero=int(input("ingrese un numero"))

verificar_primos(numero)
print("es un numero primo")

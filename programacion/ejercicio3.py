# ejercicio 3: funcion para numeros primos


def verificar_primos(numero):


    if numero <= 1 :
         print("por favor escribir un numero entero positivo mayor a uno :")
    else :
       contador = 0  
    for  i in range(1 , numero+ 1):
          if numero % (i *0.5) == 0 :
              contador += 1      
                
          else:
              print("no es primo")
        
numero=int(input("ingrese un numero"))

verificar_primos(numero)
print(f"{numero} es un numero primo")

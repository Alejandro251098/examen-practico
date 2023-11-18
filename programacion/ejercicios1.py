# ejercicio 1 : funcion calculadora de descuetos

def calculadora_descnt(edad ,precio):


   if edad < 18  :
    print(precio*0.9)
 
   elif edad >= 65:
    print(precio * 0.85)
    
   if edad >=18 and edad < 65 :
    print(precio) 


precio = int(input("ingrese el valor del producto"))
edad = int(input("ingrese su edad"))

calculadora_descnt(edad,precio)






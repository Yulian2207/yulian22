#ciclo while

#while condicion:
       #Bloque de codigo a repetir

#Definir una variale que lleve el control del ciclo
# numero = 1

# while numero <= 5: #Condición para iterar numero de veces
#     print (numero)
#     numero += 1



#Contaremos hacia atras
# numero = 10

# while numero >1:
#         print(numero)
#         numero -= 1


#Crear un programa que sume los números ingresados por el usuario hasta que el usuario ingrese 0.
        
# suma = 0

# numero = int(input("Ingrese un número o pulsa 0 para salir: "))

# while numero != 0:
#         suma += numero
#         numero = int(input("Ingrese un número o pulsa 0 para salir: "))

# print (f"La suma total es: {suma}")


#Condicones dinamicas: 
#Son aleatorias, y pueden cambiar con la ejecución del código.

#Simulación basada emn una condición externa.
#Simularemos el crecimiento de una población hasta que alcance un limite.

# poblacion = 1000
# limite = 5000
# tasa_crecimiento = 1.1

# while poblacion < limite: 
#     print (f"Población actual: {poblacion}")
#     poblacion = (int(poblacion * tasa_crecimiento))


# print(f"Población final alcanzada: {poblacion}")

# poblacion = 1000
# limite = 5000
# tasa_crecimiento = 1.1
# anio = 1

# while poblacion < limite: 
#     print (f"En el año {anio}, la población actual es de: {poblacion}")
#     poblacion = (int(poblacion * tasa_crecimiento))
#     anio += 1


# print(f"Población final alcanzada: {poblacion}")


#Lecturas de un sensor...
#Simular la lectura de un sensor que medirá los valores aleatorios hasta que alcance un valor objetivo.


import random 

sensor = random.randint(0,50)
objetivo = 40
contador = 1

while sensor < objetivo:
    print (f"en la lectura numero {contador}, el valor del sensor es: {sensor}")
    sensor += random.randint (1,10)
    contador += 1

print (f"La lectura final alcanzada fue: {sensor}")
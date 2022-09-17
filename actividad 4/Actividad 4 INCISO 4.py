import time
#{} []
print ("---------------------")
print (" Carlos Ortiz Serrano")
print (" Carnet 200917231")
print (" Lic. en Informatica")
print (" ---------------------" )
print ("ACTIVIDAD No.4  ")
print ("I N C I S O -4-\n ")
print("Como funciona la herencia en Python\n")
print("La herencia es un mecanismo de la programación")
print("orientada a objetos que sirve para crear clases")
print("nuevas a partir de clases preexistentes.")
print ("E J E M P L O\n ")
#
#Creamos la clase padre
class ESTUDIANTE(object):
    # Definimos los parámetros edad y nombre
    def __init__(self, edad, nombre):
        #Declaramos que el atributo edad es igual al argumento edad
        self.edad = edad
        #Declaramos que el atributo nombre es igual al argumento nombre
        self.nombre = nombre 
class instituto(object):
    def presentar_instituto(self):
        print("""Estudio en el Instituto Publico""")
        
#Entre paréntesis indicamos la clase padre o principal ESTUDIANTE
#Lo que la convierte a computacion en una clase hija o secundaria
class computacion (ESTUDIANTE, instituto):
                                
    #Creamos el método presentarse
    def presentarse(self):
        #Se presenta llamando los atributos
       print (f"Soy {self.nombre} tengo {self.edad} años y estudio compu") 
       
#Indicamos argumentos edad y nombre
Carlos = computacion(37, "Carlos Ortiz") 
# Llamamos al método y carlos se presenta
Carlos.presentarse() 
Carlos.presentar_instituto()

#generar pausa en ejecucion
duracion = 2
time.sleep(duracion)
exit()

import time
#{} []
print ("---------------------")
print (" Carlos Ortiz Serrano")
print (" Carnet 200917231")
print (" Lic. en Informatica")
print (" ---------------------" )
print ("ACTIVIDAD No.4  ")
print ("I N C I S O -1-  ")

print ("\n1-: Solicitar 3 Elementos:")
class SOLICITUD:
#atributos
   # lista = []
    texto_1=str()
    texto_2=str()
    texto_3=str()
#metodos
    def asignar_texto_1(self, T1):
        self.texto_1=T1
        
    def asignar_texto_2(self, T2):
        self.texto_2=T2
        
    def asignar_texto_3(self, T3):
        self.texto_3=T3
    
    def longitud(self):
        suma=0
        suma=((len(self.texto_1)+(len(self.texto_2)+(len(self.texto_3))))/3)
        print("\nEl promedio de las longitudes es:\n",suma)
        
    def concatenar(self):
        concatenar=0
        concatenar=(self.texto_1+self.texto_2+self.texto_3)
        print ("\nConcatenado resultante es:",concatenar)
        if len(concatenar)>15:
            print ("EL TEXTO ES LARGO")
        if len(concatenar)==15:
            print ("Texto contiene 15 Caracteres")
        if len(concatenar)<15:
            print("El Texto es Corto")

                    
    def comparar_textos(self):
        comparar=0
        #print (len(self.texto_1))
        #print (len(self.texto_2))
        #print (len(self.texto_3))
        if (len(self.texto_1)>(len(self.texto_2)and(len(self.texto_3)))):
            print ("\nTexto con mas Caracteres es:\n",self.texto_1)
        if (len(self.texto_2)>(len(self.texto_3)and(len(self.texto_2)))):
            print ("\nTexto con mas Caracteres es:\n",self.texto_2)
        if (len(self.texto_3)>(len(self.texto_2)and(len(self.texto_1)))):
            print ("\nTexto con mas Caracteres es:\n",self.texto_3)


    def contar_numeros(self):
        concatenar2=0
        concatenar2=(self.texto_1+self.texto_2+self.texto_3)
        
        #texto="111 lampara 22"
        acumulado=0
        for inicio in range(len(concatenar2)):
            if (concatenar2[inicio]=="2") or (concatenar2[inicio]=="1")or(concatenar2[inicio]=="3") or (concatenar2[inicio]=="4")or(concatenar2[inicio]=="5") or (concatenar2[inicio]=="6")or(concatenar2[inicio]=="7") or (concatenar2[inicio]=="8")or (concatenar2[inicio]=="9") or (concatenar2[inicio]=="0")   :   
                acumulado+=1
        print ("La cantidad de numeros en los Textos es:\n",acumulado)
        #print (concatenar2)
                    
    
objeto=SOLICITUD()
objeto.asignar_texto_1(str(input("ingrese Texto No.1: ")))
objeto.asignar_texto_2(str(input("ingrese Texto No.2: ")))
objeto.asignar_texto_3(str(input("ingrese Texto No.3: ")))
objeto.longitud()
objeto.concatenar()
objeto.comparar_textos()
objeto.contar_numeros()


         
#generar pausa en ejecucion
duracion = 2
time.sleep(duracion)
exit()


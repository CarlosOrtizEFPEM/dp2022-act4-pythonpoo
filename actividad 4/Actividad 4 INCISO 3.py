import time
#{} []
print ("---------------------")
print (" Carlos Ortiz Serrano")
print (" Carnet 200917231")
print (" Lic. en Informatica")
print (" ---------------------" )
print ("ACTIVIDAD No.4  ")
print ("I N C I S O -3-\n ")

print ("Ingrese un numero")

class SOLICITUD_NUMERO:
#atributos
    numero=0
               
#metodos
    def asignar_numero(self,an):
        self.numero=an

    def numero_primo(self):        
        valor= range(2,self.numero)
        contador = 0
        for n in valor:
          if self.numero % n == 0:
            contador +=1
        if contador > 0 :
          print("El numero NO es primo" )
        else:
          print("El numero SI es primo")
   
    def factorial(self):
        factorial=1
        numero2=self.numero
        if numero2>0:
            while (numero2>1):
                factorial= (factorial * numero2)
                numero2 = numero2 - 1
            print ("El Factorial del numero es :",factorial)
            
    def perfecto(self):
        nuevo_numero=self.numero
        i=1
        contador=0
        while(i<nuevo_numero):
            if nuevo_numero%i==0:
                contador=contador+i
            i=i+1

        if contador ==nuevo_numero:
            print("El numero Si es perfecto")
        else:
            print ("El numero NO es perfecto")
            
    
    def a_binario(self):        
        if self.numero<=0:
            return "0"
        binario=""
        while self.numero>0:
            residuo=int(self.numero%2)
            self.numero=int(self.numero/2)
            binario=str(residuo)+binario                    
        print ("El Codigo binario es:",binario)                        
        return binario
                        
#metodo a llamar
objeto=SOLICITUD_NUMERO()
objeto.asignar_numero(int(input("Numero ingresado es ")))
objeto.factorial()
objeto.numero_primo()
objeto.perfecto()
objeto.a_binario()


#generar pausa en ejecucion
duracion = 2
time.sleep(duracion)
exit()

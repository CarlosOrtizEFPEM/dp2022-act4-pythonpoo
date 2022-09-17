import time
#{} []
print ("---------------------")
print (" Carlos Ortiz Serrano")
print (" Carnet 200917231")
print (" Lic. en Informatica")
print (" ---------------------" )
print ("ACTIVIDAD No.4  ")
print ("I N C I S O -2- \n  ")

print ("Solicita DATOS ")

class SOLICITUD_DATOS:
#aributos
    sueldo_base=0
    total_ventas=0
    comision=0
    igss=0
    total_ganado=0
    ahorro=0
    bonificacion=250
#metodos
    def asignar_sueldo(self,s1):
        self.sueldo_base=s1
        
    def asignar_ventas(self,t1):
        self.total_ventas=t1
        
    def calculos(self):        
        self.comision=self.total_ventas*0.10
        print ("\nIngresos del mes")
        print("Comision sobre ventas es:", self.comision)

        print("Bonificacion Ley 250")
        
        self.total_ganado=self.sueldo_base + self.comision + self.bonificacion
        print("Total Ganado es:",self.total_ganado)
        print("\nEgresos del Mes")
        

        self.ahorro=self.total_ganado*0.07
        print("El ahorro es :",self.ahorro)
                        
        self.igss=self.sueldo_base*0.0483
        print("IGSS es :",self.igss)

        self.total_descuentos=self.ahorro+self.igss
        print("Suma de descuentos:",self.total_descuentos)

        self.liquido=self.total_ganado -  self.total_descuentos
        print ("\nSUELDO LIQUIDO ES:",self.liquido)
        

#se manda a llamar
objeto=SOLICITUD_DATOS()
objeto.asignar_sueldo(int(input("Ingrese el suelgo base: ")))
objeto.asignar_ventas(int(input("Ingrese el total de Ventas del mes: ")))
objeto.calculos()

         
#generar pausa en ejecucion
duracion = 2
time.sleep(duracion)
exit()

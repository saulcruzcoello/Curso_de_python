
#Ejercicios basicos

#(tulpa = (1,2,3,4) 
#list = [10, 4.13, "Hola"] 
#z= True)

#Ejercicios operadores

#point_1=(0,1)
#point_2=(1,1)
#x= point_1[0]-point_2[0]
#y= point_1[1]-point_2[1]
#modulo= ((x**2)+(y**2))**0.5
#print(modulo)

#Ejemplos for y while 

#for i in range(5)
 #   print(i)

#i=0
#while i <5
 #   print(i)
  #  i+=1

#for i in range: (0,100)
 #   print(i)
  #  i=i+i


def validar_edad(age=10):
  if age<0:
    raise ValueError("Error catastrófico")
  print(age)


try:
    validar_edad()
except ValueError as e:
  print(e)

'''
students = ["Pedro", "María", "Juan", "Ana"]
grades = [3, 10, 8, 5]
for i, student in enumerate(students):
    
        print(f"Grades {grades[i]}: {student}")
'''
'''
f= open ("output_exercice.txt","w")
f.write("Esta es la primera linea \n")
f.write("Esta es la segunda linea \n")
f.close()
f= open ("output_exercice.txt","r")
contenido=f.read()
f.close()
print(contenido)

with open("output_exercice.txt", 'a') as f:
        f.write("Esta es la tercera")
with open("output_exercice.txt", 'r') as f:
        contenido=f.read()
print(contenido)
'''

'''
list_1 = [1, 2, 3, 4, 5]
list_2 = [1, 2, 3, 4, 5.0]
list_3 = [1, 2, 3, 4, 'a']

import numpy as np
a = np.array(list_1)
print(a)
print(a.dtype)

import numpy as np
a = np.array(list_2)
print(a)
print(a.dtype)

import numpy as np
a = np.array(list_3)
print(a)
print(a.dtype)
'''
'''
import numpy as np

a = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]],dtype=np.int16)
print(a)

'''
'''
print(np.diag([1, 2, 3], 1))
print(np.eye(3))
print(np.eye(3, 5))
print(np.diag([1, 2, 3]))

'''

'''
import matplotlib.pyplot as plt
import numpy as np
x_cord = np.array([1, 2, 3, 4, 5])
y_cord = np.array([1, 4, 9, 16, 25])
plt.scatter(x_cord, y_cord)
plt.plot(x_cord, y_cord)
plt.show()
'''
#pip install matplotlib
#ctr+c matar un proceso
'''
import matplotlib.pyplot as plt
import numpy as np
x=np.arange(0, 2*np.pi, 0.1)
plt.plot(x, np.sin(x))
plt.show()
'''

'''
from scipy import misc
import matplotlib.pyplot as plt

img = misc.face() # Imagen para pruebas que ofrece SciPy
print("Tipo de dato:", type(img)) # Tipo de dato: <class 'numpy.ndarray'>
print("Número de dimensiones:", img.ndim) # Número de dimensiones: 3
print("Tamaño de la imagen:", img.shape) # Tamaño de la imagen: (768, 1024, 3)

plt.imshow(img)

plt.show()
'''
#pip install scipy

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from random import randrange

# Valores x e y originales:

x_values = np.arange(0, 20)
y_values = [randrange(0, 10) for x in x_values]  # Randomly generated y values.

# Función de interpolación:

interpolation_function = interp1d(x_values, y_values)

# Nuevos valores x (más precisos) y valores e interpolados:

x_values_interp = np.arange(0, 19, .25)
y_values_interp = interpolation_function(x_values_interp)

plt.plot(x_values_interp, y_values_interp, '.-', color="darkorange", label="Datos interpolados")
plt.plot(x_values, y_values, '.', color="red", label="Raw data")

plt.title("Datos interpolados vs Datos originales")
plt.legend()
plt.grid(True)
plt.show()
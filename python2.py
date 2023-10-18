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
#ctr+c matar un proceso
'''
import matplotlib.pyplot as plt
import numpy as np
x=np.arange(0, 2*np.pi, 0.1)
plt.plot(x, np.sin(x))
plt.show()
'''
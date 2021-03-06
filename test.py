# Estudiante: Diana Carolina Quintero Bedoya
# Correo: diana.quintero01@correo.usa.edu.co
# Carrera: Ciencias de la computación e Inteligencia Artificial
# Fecha: 29 abril 2021
# Ultima Modificación: 5 mayo 2021 
# Docente: John Corredor Pdh
# Materia: Computación paralela y distrribuida
# Universidad Sergio Arboleda
# 
######### Rendimiento Cython/Python ##########
#

import functionE
import CyfunctionE 
import numpy as np
import time

def execute(D, N, X, beta, tetha):
        initial = time.time()
        functionE.rbf_network(X, beta, tetha)
        tiempoPy = time.time() - initial

        initial = time.time()
        CyfunctionE.rbf_network(X, beta, tetha)
        tiempoCy = time.time() - initial

        SpeedUp = round(tiempoPy/tiempoCy, 3)

        print("tiempo Py: {}\n".format(tiempoPy))
        print("tiempo Cy: {}\n".format(tiempoCy))
        print("SpeedUp: {}\n".format(SpeedUp))

N = 1500
beta = np.random.rand(N)
tetha = 10

D = 6
X = np.array([np.random.rand(N) for d in range(D)]).T
execute(D, N, X, beta, tetha)

D = 60
X = np.array([np.random.rand(N) for d in range(D)]).T
execute(D, N, X, beta, tetha)

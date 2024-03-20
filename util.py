import pandas as pd
import numpy as np


class tabla_misiones:
    def __init__(self, tabla_misiones):
        self.misiones = tabla_misiones
    def nueva_mision(self, nombre,valor):
        numero = self.misiones.shape[0] + 1
        new = pd.DataFrame({'Numero': [numero], 'Mision': [nombre], 'Valor': [valor]})
        self.misiones = pd.concat([self.misiones,new], ignore_index=True)
        self.misiones = self.misiones.reset_index(drop=True)
        return self.misiones
    

def barra_de_carga(porcentaje):
    valor = porcentaje/100
    barra = '[:-------------------------]'
    rango = int(21*valor)
    barra = f"[{'X' * rango}{'-' * (20 - rango)}]"
    if(valor == 1):
        return 'Fondos para la misión completados!'
    return barra

    
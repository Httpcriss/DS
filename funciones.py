#!/usr/bin/env python
# coding: utf-8

# In[1]:


def promedio(datos):
    
    x=[]
    for i in datos:
        if i==i:
            x.append(i)
    
    suma = sum(x)
    promedio = suma / len(x)
    
    return promedio


# In[2]:


def varianza(datos):
    n = len(datos)
    
    promedio = sum(datos) / n
    suma_cuadrados = sum((x - promedio) ** 2 for x in datos)
    
    varianza = suma_cuadrados / (n - 1)
    
    return varianza


# In[3]:


import math

def desviacion_estandar(datos):
    z=[]
    for i in datos:
        if i==i:
            z.append(i)
    
    n = len(z)
    
    promedio = (sum(z) / n)
    suma_cuadrados = sum((x - promedio) ** 2 for x in z)
    
    varianza = suma_cuadrados / (n - 1)
    
    desviacion_estandar = math.sqrt(varianza)
    
    return desviacion_estandar


# In[4]:


def mediana(datos):
    x=[]
    for i in datos:
        if i==i:
            x.append(i)
    
    datos_ordenados = sorted(x)
    n = len(datos_ordenados)

    if n % 2 == 0:
        medio1 = datos_ordenados[n // 2 - 1]
        medio2 = datos_ordenados[n // 2]
        mediana = (medio1 + medio2) / 2
    else:
        
        mediana = datos_ordenados[n // 2]

    return mediana


# In[5]:


def moda(datos):

    frecuencia = {}
    x=[]
    for i in datos:
        if i==i:
            x.append(i)
    for valor in datos:
        frecuencia[valor] = frecuencia.get(valor, 0) + 1

    # Encontramos el valor con la frecuencia más alta.
    moda = None
    frecuencia_maxima = 0
    for valor, count in frecuencia.items():
        if count > frecuencia_maxima:
            moda = valor
            frecuencia_maxima = count

    return moda


# In[ ]:


def cuartiles(y,z):
    p=[]
    for i in y:
        if i==i:
            p.append(i)
    p=sorted(p)
    cuartil=(z/4)*(len(p)-1)
    ponderacion=cuartil-int(cuartil)
    if ponderacion==0:
        return p[int(cuartil)]
    else:
        return p[int(cuartil)]*(1-ponderacion)+p[int(cuartil)+1]*ponderacion
    

def rango_intercuartil(datos):
    """
    Calcula el rango intercuartil (IQR) de un conjunto de datos.

    :param datos: Una lista o arreglo de datos.
    :return: El valor del rango intercuartil.
    """
    q3=cuartiles(datos,3)
    q1=cuartiles(datos,1)
    

    iqr = q3 - q1
    return iqr
    
def rango(y):
    """
    Calcula el rango de un conjunto de datos.

    :param datos: Una lista o arreglo de datos.
    :return: El valor del rango.
    """

    x=[]
    for i in y:
        if i==i:
            x.append(i)
    
    rango = max(x) - min(x)
    return rango


def percentiles(y,z):
    """
    Calcula los percentiles especificados de un conjunto de datos sin utilizar NumPy.

    :param datos: Una lista o arreglo de datos.
    :param percentiles: Una lista de los percentiles que deseas calcular (por ejemplo, [25, 50, 75] para cuartiles).
    :return: Un diccionario que contiene los valores de los percentiles calculados.
    """
    p=[]
    for i in y:
        if i==i:
            p.append(i)
    p=sorted(p)
    percentil=(z/100)*(len(p)-1)
    ponderacion=percentil-int(percentil)
    if ponderacion==0:
        return p[int(percentil)]
    else:
        return p[int(percentil)]*(1-ponderacion)+p[int(percentil)+1]*ponderacion

def mad(datos):
    x=[]
    for i in datos:
        if i==i:
            x.append(i)
    x=sorted(x)
    mediana_=mediana(x)
    desv=[]
    for i in x:
        desv.append(abs(i-mediana_))
    desv=sorted(desv)
    if len(desv)%2==0:
        mad=(desv[int(len(desv)/2)]+ desv[int((len(desv)/2)-1)])/2
        return mad
    else:
        mad=desv[int((len(desv)/2))] 
        return mad
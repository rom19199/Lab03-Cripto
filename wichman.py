import random
import struct
import math
import numpy as np
import matplotlib.pyplot as plt
import re
from skimage.data import camera
from PIL import Image


def xor(a, b):
    m = len(a)
    n = len(b)
    maxx = max(m,n)
    if (m < n):
        a = a + (n-m)*'0'
    if (n < m):
        b = b + (m-n)*'0'
        
    c = ''
    for i in range(0, maxx):
        c = c + str(int(a[i]) ^ int(b[i]))
    return c

def img2bits(I):
    ''' Convierte una imagen en escala de grises a cadena de bits.
        Input:  I = imagen, como numpy array de shape (m,n).
        Output: s = string de bits, donde se concatenan cada pixel de I.
    '''
    m, n = I.shape
    s = ''
    for i in range(0, m):
        for j in range(0, n):
            s = s + '{0:08b}'.format(I[i,j])
    return s

def funcion(f, n):
    return math.floor(f * 10 ** n) / 10 ** n
def Bits(num):
    return ''.join('{:0>8b}'.format(c) for c in struct.pack('!f', num))



def bits2img(x, shape):
    ''' Convierte una cadena de bits a una imagen en escala de grises.
        Input:  s = string de bits, donde se concatenan cada pixel de I.
                shape = dimensiones (m,n) de la imagen de salida I.
        Output: I = imagen, como numpy array de shape (m,n).
    '''

    m, n = shape
    I = np.zeros(m*n).astype(np.uint8)
    bts = re.findall('........', x)
    for i in range(0, len(bts)-1):
        I[i] = int(bts[i], 2)
    I = I.reshape(m,n)
    return I
    
#se importa la imagen
I = camera()
J = Image.fromarray(I)
J = J.resize((J.size[0]//2, J.size[1]//2), Image.LANCZOS)
I = np.array(J)
I.shape
k = 1

# Wichman-Hill generator
#Implementar un generador pseudo-aleatorio de Wichman-Hill
def WichmanHill(a,b):
    seed1 = a[0]
    seed2 = a[1]
    seed3 = a[2]
    resp = []
    lista = []
    
    for i in range (int(b)):
        seed1 = (171 * seed1) % 30269
        seed2 = (172 * seed2) % 30307
        seed3 = (170 * seed3) % 30323
        resp.append((float(seed1)/30269.0 + float(seed2)/30307.0 + float(seed3)/30323.0) % 1.0)
    for x in resp:
        binario = Bits(funcion(x,10))
        lista.append(binario)
    z = ''.join(map(str, lista))
    print(z[0:int(b)])
    return(z[0:int(b)])    

a = [random.randint(1, 30000),random.randint(1, 30000),random.randint(1, 30000)]

#cadena de la imagen original y las cadena aleatoria
cad1 = img2bits(I)
cad2 = WichmanHill(a, len(cad1))
cad3_xor = xor(cad1, cad2)

c1 = bits2img(cad2, I.shape)
c2 = bits2img(cad3_xor, I.shape)

plt.figure(figsize=(15,8))
plt.subplot(1,2,1)
plt.imshow(c1, cmap='gray')
plt.subplot(1,2,2)
plt.imshow(c2, cmap='gray')
plt.show()

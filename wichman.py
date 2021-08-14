import numpy as np
import matplotlib.pyplot as plt
import re
from skimage.data import manzana  # estas librerías solo se usan para
from PIL import Image               # llamar al ejemplo de cameraman.png
from random import randint
import random


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

def compare():
    imagen = img = io.imread('manzana.png',as_gray=True)
    J = Image.fromarray(imgen)
    J = J.resize((J.size[0]//2, J.size[1]//2), Image.LANCZOS)
    I = np.array(J) * 255
    I = I.astype(int)
    
    plt.figure()
    plt.imshow(I, cmap='gray')
    plt.show()


# Wichman-Hill generator
#Implementar un generador pseudo-aleatorio de Wichman-Hill
def WichmanHill(a,b):
    seed1 = randint(1, 30000)
    seed2 = randint(1, 30000)
    seed3 = randint(1, 30000)
    
    l = ''
    
    for i in range(b):
        seed1 = (171 * seed1) % 30269
        seed2 = (172 * seed2) % 30307
        seed3 = (170 * seed3) % 30323
        
        resp = ((float(seed1)/30269 + float(seed2)/30307 + float(seed3)/30323) % 1)
        l += str(round(resp))
        
    return (l)

def lfsr(semillas, taps, k):
    res = semillas
    sr, xor = semillas, 0
    while len(res) < k:
        for x in taps:
            xor += int(sr[x-1])
        xor = 0 if xor %2 == 0.0 else 1
        sr, xor = str(xor) + sr[:-1], 0
        res += sr
    return res

#cadena de la imagen original y las cadena aleatoria
cad1 = img2bits(I)
cad2 = WichmanHill(len(cad1))
cad3_xor = xor(cad1, cad2)

c1 = bits2img(cad2, I.shape)
c2 = bits2img(cad3_xor, I.shape)

plt.figure(figsize=(15,8))
plt.subplot(1,2,1)
plt.imshow(c1, cmap='gray')
plt.subplot(1,2,2)
plt.imshow(c2, cmap='gray')
plt.show()

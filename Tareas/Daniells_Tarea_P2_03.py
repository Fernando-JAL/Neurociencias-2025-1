import numpy as np
import matplotlib.pyplot as plt

# Ejercicio 1. Genera un arreglo 1D, llamado freq, de 4 elementos de números aleatorios enteros en el intervalo [1, 8]
freq = np.random.randint(1, 9, 4)
print("Frecuencia:", freq)

# Ejercicio 2. Genera un arreglo 1D, llamado amplitud, de 4 elementos de números aleatorios con distribución uniforme
# en el intervalo [3, 6]
amplitud = np.random.uniform(3, 6, 4)
print("Amplitud:", amplitud)

# Ejercicio 3. Use el metodo arange para generar un arreglo, llamado t, de 2000 números en el intervalo [0, 1]
t = np.arange(0, 1, 1/2000)
print("Arreglo t:", t)

# Ejercicio 4. Genere 4 ondas sinusoidales con cada frecuencia y amplitud.
# La ecuación de la onda sinusoidal es y(t) = A*sin(2*pi*B*t)
ondas = [amplitud[i] * np.sin(2 * np.pi * freq[i] * t) for i in range(4)]

# Ejercicio 5. Cree un arreglo llamado x, que sea la suma de las 4 ondas sinusoidales
x = sum(ondas)
print("Suma de ondas sinusoidales (x):", x)

#Transformada de Fourier
X = np.fft.fft(x)

# Ejercicio 6. Cree un arreglo, llamado frequence, de los enteros en el intervalo [0, 1999]
frequence = np.arange(2000)
print("Frecuencia en el dominio de Fourier:", frequence)

# Ejercicio 7. Calcular el valor absoluto a todos los elementos del arreglo X
absX = np.abs(X)
print("Valor absoluto de X:", absX)

# Ejercicio 8. De los primeros 10 elementos del arreglo del ejercicio anterior, determine los 4 elementos máximos y en qué índices se localizan
primeros_10_absX = absX[:10]
maximos_4 = np.sort(primeros_10_absX)[-4:]
indices_maximos_4 = np.argsort(primeros_10_absX)[-4:]
print("4 máximos valores:", maximos_4)
print("Índices de los 4 máximos valores:", indices_maximos_4)

#frecuencia y la amplitud Fourier
plt.stem(frequence, absX)
plt.show()

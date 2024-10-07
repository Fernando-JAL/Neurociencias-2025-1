import numpy as np
import matplotlib.pyplot as plt

# Ejercicio 1. Genera un arreglo 1D, llamado freq, de 4 elementos de números aleatorios enteros en el intervalo [1, 8]
freq = [1, 5, 7, 2]
#freq = np.random.randint(1, 8, size = [4])

# Ejercicio 2. Genera un arreglo 1D, llamado amplitud, de 4 elementos de números aleatorios con distribución uniforme
# en el intervalo [3, 6]
# amplitud = np.random.uniform(3, 6, size= 4)
amplitud = [4.5, 3.3, 5.1, 6]

# Ejercicio 3. Use el metodo arange para generar un arreglo, llamado t, de 2000 números en el intervalo [0, 1]

t = np.arange(0, 1, 1/2000)

# Ejercicio 4. Genere 4 ondas sinusoidales con cada frecuencia y amplitud.
# Hint: recuerde que la ecuación de la onda sinusoidal es y(t) = A*sin(2*piB*t) donde A es la amplitud y B es la
# frecuencia. Para usar pi en numpy, use np.pi
# Sugerencia: para visualizar las ondas sinusoidales puede usar las líneas de código
idx = 0
y = amplitud[idx] * np.sin(2 * np.pi * freq[idx] * t)
# print(amplitud[idx], freq[idx])
plt.plot(t, y)
idx = 1
y = amplitud[idx] * np.sin(2 * np.pi * freq[idx] * t)
print(amplitud[idx], freq[idx])
plt.plot(t, y)
idx = 2
y = amplitud[idx] * np.sin(2 * np.pi * freq[idx] * t)
print(amplitud[idx], freq[idx])
plt.plot(t, y)
idx = 3
y = amplitud[idx] * np.sin(2 * np.pi * freq[idx] * t)
print(amplitud[idx], freq[idx])
plt.plot(t, y)
plt.show()

# Ejercicio 5. Cree un arreglo llamado x, que sea la suma de las 4 ondas sinusoidales
for idx in range(1, 4):
    y += amplitud[idx] * np.sin(2 * np.pi * freq[idx] * t)
plt.plot(t, y)
plt.show()

# Numpy también permite aplicar operadores tales como la transormada de fourier a un arreglo de datos con
# el paquete np.fft, en particular la función np.fft.fft(x) aplica la transformada discreta de fourier al arreglo x
X = np.fft.fft(y)

# Ejercicio 6. Cree un arreglo, llamado frequence, de los enteros en el intervalo [0, 1999]
frequence = range(2000)

# Ejercicio 7. Calcular el valor absoluto a todos los elementos del arreglo X
absX = np.abs(X)

# Ejercicio 8. De los primeros 10 elementos del arreglo del ejercicio anterior, determine los 4 elementos máximos y en
# qué índices se localizan
print(absX[:10])


# Para mostrar la frecuencia y la amplitud en el dominio de Fourier use las siguientes líneas de código
plt.stem(frequence[:10], absX[:10])
plt.show()
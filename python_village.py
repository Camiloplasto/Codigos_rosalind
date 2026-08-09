# %%
#Rosalind #!: INI2 (Variables y algo de aritmetica)
a = 913
b = 918

resultado = (a ** 2) + (b ** 2)
# c^2 = a^2 + b^2 (cuadro de la hipotenusa)

print("Resultado del cuadrado de la hipotenusa", resultado)

# %%
#Cadenas y listas (Slicing)

texto = "szvXGQim2fj7PGK5czgxAPW1SAmeivaofiwZtfDCIaefNowPzalpestriss8gVEFQ2y8W0BKnufwofu7P7j7auYL4SLJTxLa4tYMD8LiC14ZCILnNwOzIsr0XX2gpkLWt1pLSMNTI28B8JTsibuMrcPqrNIWbmXFdTS"

a = 25
b = 30
c = 49
d = 57

palabra_1 = texto[a :b + 1]

palabra_2 = texto[c : d + 1]

print( f"{palabra_1} {palabra_2}")

# %%
#Condiciones (filtrar) y bucles (recorrer datos)

#Se definen los limites del Sample Dataset
a = 100
b = 8778

suma_impares = 0

for numero in range(a,b):
    if numero % 2==1:
        suma_impares = suma_impares + numero


print(suma_impares)

# %%
#Readin an Writing

#Se busca eliminar las lineas impares y dejar las pares

#Paso 1: Abrimos el archivo en modo lectura ("r" de read)
with open ("c:/Users/Camilo A. Marin Cast/Downloads/rosalind_ini5.txt", "r") as archivo:
    lineas = archivo.readlines()

#Paso 2: Filtrado para obtener las líneas pares
lineas_pares = lineas[1::2]

#Paso 3: Imprimir las líneas pares
print("Resultado:\n")
for linea in lineas_pares:
    print(linea.strip())

# %%
#Dictiornies
#un diccionario es una estructura de datos que permite almacenar pares de clave-valor.
# los k-mers son secuencias de ADN de longitud k. Se pueden usar diccionarios para contar la frecuencia de cada k-mer en una secuencia de ADN.

#Se separa el exto en palabras y se almacenan en una lista

# %%

texto = "When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be"

# Paso 2: Separamos el texto en palabras usando los espacios
palabras = texto.split(" ")

# Paso 3: Creamos un diccionario vacío para ir guardando el conteo
conteo = {}

# Paso 4: Contamos la frecuencia de cada palabra
for palabra in palabras:
    if palabra in conteo:
        conteo[palabra] = conteo[palabra] + 1  # Si ya la habíamos visto, sumamos 1
    else:
        conteo[palabra] = 1                     # Si es nueva, la registramos con 1

# Paso 5: Imprimimos la palabra y su valor usando .items()
for clave, valor in conteo.items():
    print(f"{clave} {valor}")

#with open("c:/Users/Camilo A. Marin Cast/Downloads/rosalind_ini6_output.txt", "w") as archivo_salida:
    for clave, valor in conteo.items():
        archivo_salida.write(f"{clave} {valor}\n")

# %%
#with open("c:/Users/Camilo A. Marin Cast/Downloads/rosalind_ini6_output.txt", "r") as archivo_salida:
#    palabras_conteo = archivo_salida.readlines()

#conteo = {}

# Paso 4: Contamos la frecuencia de cada palabra
#for lista in palabras_conteo:
#    if lista in conteo:
#        conteo[lista] = conteo[lista] + 1  # Si ya la habíamos visto, sumamos 1
#    else:
#        conteo[lista] = 1                     # Si es nueva, la registramos con 1

# Paso 5: Imprimimos la palabra y su valor usando .items()
#or clave, valor in conteo.items():
#    print(f"{clave} {valor}")

#with open("c:/Users/Camilo A. Marin Cast/Downloads/rosalind_ini6_output.txt", "w") as archivo_salida:
#    for clave, valor in conteo.items():
#        archivo_salida.write(f"{clave} {valor}\n")

#print(f"Total de palabras : {len(palabras_conteo)}")
#print(f"Primeras 5 palabras de la lista: {palabras_conteo[:5]}")

# %%
with open("c:/Users/Camilo A. Marin Cast/Downloads/rosalind_ini6 (1).txt", "r") as archivo_salida:
    palabras_conteo = archivo_salida.read().split()

#print(f"Total de palabras : {len(palabras_conteo)}")
#print(f"Primeras 5 palabras de la lista: {palabras_conteo[:5]}")

conteo = {}

# Paso 4: Contamos la frecuencia de cada palabra
for lista in palabras_conteo:
    if lista in conteo:
        conteo[lista] = conteo[lista] + 1  # Si ya la habíamos visto, sumamos 1
    else:
        conteo[lista] = 1                     # Si es nueva, la registramos con 1

# Paso 5: Imprimimos la palabra y su valor usando .items()
for clave, valor in conteo.items():
    print(f"{clave} {valor}")

with open("c:/Users/Camilo A. Marin Cast/Downloads/rosalind_ini6_output.txt", "w") as archivo_salida:
    for clave, valor in conteo.items():
        archivo_salida.write(f"{clave} {valor}\n")
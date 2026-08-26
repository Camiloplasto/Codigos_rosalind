# %%
#Counting Point Mutations (Contando Mutaciones Puntuales)

archivo_entrada = "C:/Users/Camilo A. Marin Cast/Downloads/Codigos_rosalind/counting_point_mutations/rosalind_hamm.txt"
archivo_salida = "C:/Users/Camilo A. Marin Cast/Downloads/Codigos_rosalind/counting_point_mutations/rosalind_hamm_result.txt"

with open (archivo_entrada, "r") as archivo:
    secuencia = archivo.read().splitlines()

adn_principal = secuencia[0]
adn_mutaciones = secuencia[1]

distancia = 0
len_adn_principal = len(adn_principal)
len_adn_mutaciones = len(adn_mutaciones)

for i in range(len(adn_principal)):
    if adn_principal[i] != adn_mutaciones[i]:
        distancia += 1

with open (archivo_salida, "w") as archivo_salida:
    archivo_salida.write(str(distancia))

print(f"ADN principal: {len_adn_principal}")
print(f"ADN mutaciones: {len_adn_mutaciones}")
print(f"Número de mutaciones: {distancia}")

#Se hace un codigo que toma el archivo dado por Rosalind, se pasa con .splitlines para que se creen las dos filas
#luego se defienen las dos filas con una variable las cuales luego se comparan en un ciclo por el cual anota cada una
#de las diferencias en la variable distanciapara luego escribirla en un .txt que es importado a Rosalind

# %%
#searching through the haystack
ruta_entrada = "C:/Users/Camilo A. Marin Cast/Downloads/Codigos_rosalind/searching_through_the_haystack/rosalind_hamm.txt"
ruta_salida = "C:/Users/Camilo A. Marin Cast/Downloads/Codigos_rosalind/searching_through_the_haystack/rosalind_hamm_result.txt"

secuencias = []
secuencia_filtrada = ""

with open (ruta_entrada, "r") as archivo_entrada:
    for linea in archivo_entrada:
        linea = linea.strip()

        if linea.startswith(">"):
            if secuencia_filtrada:
                secuencias.append(secuencia_filtrada)
                secuencia_filtrada = ""
        else:
            secuencia_filtrada += linea

    if secuencia_filtrada:
        secuencias.append(secuencia_filtrada)

secuencia_referencia = secuencias [0]
resto_secuencias = secuencias [1:]
#-------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------
#print(f"Secuencia filtrada unicamente con la secuencia principal: {secuencia_referencia }")
#print(f"Secuencia con todas las variables: {resto_secuencias}")
#-------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------
#Se generan todas las cadenas de referencia
subcadenas = []
for i in range(len(secuencia_referencia)):
    for j in range(i + 1, len(secuencia_referencia) + 1):
        subcadenas.append(secuencia_referencia[i:j])

#Las ordenamos de mayor a menor para encontrar la más larga primero
subcadenas.sort(key = len, reverse = True)

#Evaluar cuál es la primera subcadena que está en todas las demas
motivo_mas_largo = ""

for sub in subcadenas:
    #"all" verifica si "sub" está presente en cada una de las cadenas de resto_secuencias
    if all(sub in adn for adn in resto_secuencias):
        motivo_mas_largo = sub
        break #Como están ordenadas de mayor a menor, la primera que cumpla es la respuesta

with open (ruta_salida, "w") as archivo_salida:
    archivo_salida.write(motivo_mas_largo)

print(f"Motivo más largo encontrado: {motivo_mas_largo}")
print(f"Longitud de la secuencia de referencia {len(secuencia_referencia)}")
print(f"Longitud de la subsecadena más larga en comun: {len(motivo_mas_largo)}")

#Se realizo un proceso donde se toman dos varaibles iniciales las cuales son secuencias y secuencia_filtrada
#donde se leyo el archivo con un with y luego con un ciclo for se hizo una unión de cada una de las lineas del .txt
#donde el punto base o el comienzo de cada linea era el indicativo o la presencia de un ">", cada una de las lineas creadas
#pasa a la variable de "secucencia_filtrada" y hasta cuando vuelve a encontrar otro ">" esta se sigue guardando, luego al encontrar
#un nuevo indicador de linea esta se envia a la otra variable creada la cual es "secuencias". Luego se definieron las variables de "secuencia_referencia"
#y "resto_secuencias", para luego crear las subcadenas (variable), se hace solo con la variable de "secuencia_referencia" en la cual el ciclo for de range toma
#cada posición establecida en "i" y va haciendo recortes encontrando todas las dispocisiones que puede a tener esa linea, es decir crea todas las subcadenas que pueden existir
#de la cadena de referencia, luego ya guardadas en la lista "subcadenas", con sort se ponen de mayor a menor, debido a que el punto del ejercicio es encontrar la subcadena más
#larga, luego se define la variable "motivo_mas_largo", donde con un ciclo for se le indica que con cada una de las subcadenas en la lista "subcadenas" vaya comparando hasta encontrar
#la que la subcadena que esta en todas las demas, es decir la secuencia en comun entre todas las cadenas, lograndose con las funciones "all" y "break"

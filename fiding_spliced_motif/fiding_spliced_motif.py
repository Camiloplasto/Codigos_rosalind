# %%
#Fiding a Spliced Motif (encontrando un motivo empalmado)

archivo_entrada = "C:/Users/Camilo A. Marin Cast/Downloads/Codigos_rosalind/fiding_spliced_motif/rosalind_sseq.txt"
archivo_salida = "C:/Users/Camilo A. Marin Cast/Downloads/Codigos_rosalind/fiding_spliced_motif/rosalind_sseq_result.txt"

secuencias = []
secuencias_conjunto = ""

with open(archivo_entrada, "r") as archivo:
    for linea in archivo:
        linea = linea.strip()

        if linea.startswith(">"):
            if secuencias_conjunto:
                secuencias.append(secuencias_conjunto)
                secuencias_conjunto = ""

        else:
            secuencias_conjunto += linea

    if secuencias_conjunto:
        secuencias.append(secuencias_conjunto)

#se definen las variables para la secuencia principal y las subsecuencias
secuencia_principal = secuencias[0]
subsecuencias = secuencias[1]

indices = []
posicion_s = 0

for base in subsecuencias:
    posicion = secuencia_principal.find(base, posicion_s)
    indices.append(str(posicion + 1))
    #Se guarda como un string para que sea más facil unirlo después con espacios
    posicion_s = posicion + 1

resultado = " ".join(indices)

with open(archivo_salida, "w") as archivo:
    archivo.write(resultado)

print(f"Secuencia principal: {secuencia_principal}")
print(f"Subsecuencia: {subsecuencias}")
print(f"Índices: {resultado}")

#Implementación en Python para encontrar los índices de aparición de una subsecuencia (motivo no contiguo) en una cadena de ADN:

#- Lectura y parsing FASTA del archivo de entrada para procesar la cadena principal (s) y el motivo (t).
#- Búsqueda voraz (greedy) carácter por carácter utilizando 'find()' a partir del último índice encontrado (posicion_s).
#- Conversión de posiciones a base 1 (1-based indexing) ajustando con '+1' para el formato requerido por Rosalind.
#- Actualización de 'posicion_s = posicion + 1' en cada iteración para garantizar el orden de aparición sin retroceder.
#- Formateo del resultado final unido por espacios mediante 'join()' y guardado en archivo de salida.
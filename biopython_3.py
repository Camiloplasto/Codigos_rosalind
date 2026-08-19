# %%

#Buscando en un pajar

ruta_entrada = "C:/Users/Camilo A. Marin Cast/Downloads/Codigos_rosalind/rosalind_subs.txt"
ruta_salida = "C:/Users/Camilo A. Marin Cast/Downloads/Codigos_rosalind/rosalind_subs_result.txt"

with open (ruta_entrada, "r") as archivo_entrada:
    secuencia_adn = archivo_entrada.read().strip().splitlines()

s = secuencia_adn[0]  # Asumiendo que la secuencia de ADN está en la primera línea del archivo (de hecho, es la secuencia principal)
t = secuencia_adn[1]  # Asumiendo que la subsecuencia que queremos buscar está en la segunda línea del archivo

posiciones = []
len_s = len(s)
len_t = len(t)

# busqueda de motivos (recorriendo la secuencia principal y comparando con la subsecuencia)
for i in range(len_s - len_t + 1):
    if s[i : i + len_t] == t:
        posiciones.append(str(i + 1))  # Agregamos la posición (1-indexed)

# formatear resultado como una cadena de texto
resultado = " ".join(posiciones)

with open (ruta_salida, "w") as archivo_salida:
    archivo_salida.write(resultado)

print(f"Longitud de la secuencia principal: {len_s}")
print(f"Posiciones de la subsecuencia en la secuencia principal: {resultado}")

####################################################################################
####################################################################################

####################################################################################
####################################################################################
# %%
#Transcripción de RNA a proteína

ruta_entrada = "C:/Users/Camilo A. Marin Cast/Downloads/Codigos_rosalind/Transcripcion_ARN_PROTEINA/rosalind_prot.txt"
ruta_salida = "C:/Users/Camilo A. Marin Cast/Downloads/Codigos_rosalind/Transcripcion_ARN_PROTEINA/rosalind_prot_result.txt"

with open (ruta_entrada, "r") as archivo_entrada:
    secuencia_arn = archivo_entrada.read().strip()

codigo_genetico = {
    # Fenilalanina y Leucina
    'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
    'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
    # Isoleucina y Metionina (Codón de Inicio)
    'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',
    # Valina
    'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
    # Serina
    'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
    'AGU': 'S', 'AGC': 'S',
    # Prolina
    'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    # Treonina
    'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
    # Alanina
    'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    # Tirosina y Codones de Parada (Stop)
    'UAU': 'Y', 'UAC': 'Y', 'UAA': 'Stop', 'UAG': 'Stop',
    # Histidina y Glutamina
    'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
    # Asparagina y Lisina
    'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
    # Ácido Aspártico y Ácido Glutámico
    'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
    # Cisteína, Codón de Parada (Stop) y Triptófano
    'UGU': 'C', 'UGC': 'C', 'UGA': 'Stop', 'UGG': 'W',
    # Arginina
    'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
    'AGA': 'R', 'AGG': 'R',
    # Glicina
    'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
}

proteina = ""

for i in range(0, len(secuencia_arn), 3):
    codon = secuencia_arn[i:i + 3]
    aminoacido = codigo_genetico.get(codon)

    if aminoacido == "Stop" or aminoacido is None:
        break

    proteina += aminoacido

with open (ruta_salida, "w") as archivo_salida:
    archivo_salida.write(proteina)

# %%
#RNA splicing

ruta_entrada = "C:/Users/Camilo A. Marin Cast/Downloads/Codigos_rosalind/rna_splicing/rosalind_splc.txt"
ruta_salida = "C:/Users/Camilo A. Marin Cast/Downloads/Codigos_rosalind/rna_splicing/rosalind_splc_result.txt"

secuencias = []
secuencia_actual = ""

with open (ruta_entrada, "r") as archivo_entrada:
    for linea in archivo_entrada:
        linea = linea.strip()

        if linea.startswith(">"):
            #si se encuenta con un ">", se guarda la secuencia acumulada anterior
            if secuencia_actual:
                secuencias.append(secuencia_actual)
                secuencia_actual = ""
        else:
            #si es texto de ADN, se va pegando
            secuencia_actual += linea

    if secuencia_actual:
        secuencias.append(secuencia_actual)

#Se definen las variables para la secuencia principal y los intrones
adn_principal = secuencias[0]  # La primera secuencia es la secuencia principal
intrones = secuencias[1:]  # Las secuencias restantes son los intrones

#print(f"intrones: {intrones}")
#print(f"adn_principal: {adn_principal}")

#Se eliminan los intrones de la secuencia principal
cadena_limpia = adn_principal
for intron in intrones:
    cadena_limpia = cadena_limpia.replace(intron, "")

#se hace la transcripción reemplazando las T por U
secuencia_arn = cadena_limpia.replace("T", "U")

#Se define el código genético para traducir los codones a aminoácidos
codigo_genetico = {
    # Fenilalanina y Leucina
    'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
    'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
    # Isoleucina y Metionina (Codón de Inicio)
    'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',
    # Valina
    'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
    # Serina
    'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
    'AGU': 'S', 'AGC': 'S',
    # Prolina
    'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    # Treonina
    'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
    # Alanina
    'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    # Tirosina y Codones de Parada (Stop)
    'UAU': 'Y', 'UAC': 'Y', 'UAA': 'Stop', 'UAG': 'Stop',
    # Histidina y Glutamina
    'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
    # Asparagina y Lisina
    'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
    # Ácido Aspártico y Ácido Glutámico
    'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
    # Cisteína, Codón de Parada (Stop) y Triptófano
    'UGU': 'C', 'UGC': 'C', 'UGA': 'Stop', 'UGG': 'W',
    # Arginina
    'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
    'AGA': 'R', 'AGG': 'R',
    # Glicina
    'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
}

#Cumple la función de iniciar una variable vacía para almacenar la proteína traducida
proteina: str = ""

#Se traducen los codones a aminoácidos
for i in range(0, len(secuencia_arn), 3):
    codon = secuencia_arn[i:i + 3]
    aminoacido = codigo_genetico.get(codon)

    if aminoacido == "Stop" or aminoacido is None:
        break

    proteina += aminoacido

with open (ruta_salida, "w") as archivo_salida:
    archivo_salida.write(proteina)

#print(f"Secuencia de ARN transcrita: {secuencia_arn}")
#print(f"Total de nucleótidos en la secuencia de ARN: {len(secuencia_arn)}")
#print(f"Total de nucleótidos en la secuencia de ADN: {len(adn_principal)}")
#print(f"Secuencia de proteína traducida: {proteina}")
#print(f"Total de aminoácidos en la proteína traducida: {len(proteina)}")
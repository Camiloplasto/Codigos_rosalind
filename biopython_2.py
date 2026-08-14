# %%

#conteo de bases nitrogenadas en una secuencia de ADN
with open ("c:/Users/Camilo A. Marin Cast/Downloads/rosalind_dna.txt", "r") as secuencia_cruda:
    secuencia_leida = secuencia_cruda.read().strip()

conteo_nucleotidos = {}

for nucleotido in secuencia_leida:
    if nucleotido in conteo_nucleotidos:
        conteo_nucleotidos[nucleotido] += 1
    else:
        conteo_nucleotidos[nucleotido] = 1

#Sacamos los conteos asegurando el ordén (usando get para evitar errores si alguna base no está presente)
a = conteo_nucleotidos.get("A", 0)
c = conteo_nucleotidos.get("C", 0)
g = conteo_nucleotidos.get("G", 0)
t = conteo_nucleotidos.get("T", 0)

resultado = f"{a} {c} {g} {t}"

with open("c:/Users/Camilo A. Marin Cast/Downloads/rosalind_dna_output.txt", "w") as archivo_salida:
    archivo_salida.write(resultado)

print("Resultado:", resultado)


# %%
#Solción de la IA

#opción 1

# %% [ROSALIND: DNA - Desde Cero (Opción 1)]

ruta_in = "c:/Users/Camilo A. Marin Cast/Downloads/rosalind_dna.txt"
ruta_out = "c:/Users/Camilo A. Marin Cast/Downloads/rosalind_dna_output.txt"

with open(ruta_in, "r") as archivo:
    dna = archivo.read().strip()

# Usamos una lista por comprensión que cuenta en el orden exacto 'ACGT'
# y luego unimos todo con un espacio usando ' '.join()
conteo = [str(dna.count(base)) for base in "ACGT"]
resultado = " ".join(conteo)

with open(ruta_out, "w") as salida:
    salida.write(resultado)

print("Resultado:", resultado)

# %%
# Opción 2

# %% [ROSALIND: DNA - Desde Cero (Opción 2)]
from collections import Counter

ruta_in = "c:/Users/Camilo A. Marin Cast/Downloads/rosalind_dna.txt"
ruta_out = "c:/Users/Camilo A. Marin Cast/Downloads/rosalind_dna_output.txt"

with open(ruta_in, "r") as archivo:
    dna = archivo.read().strip()

# Counter cuenta la frecuencia de cada carácter automáticamente
frecuencias = Counter(dna)

# Construimos la respuesta consultando A, C, G y T en orden
resultado = f"{frecuencias['A']} {frecuencias['C']} {frecuencias['G']} {frecuencias['T']}"

with open(ruta_out, "w") as salida:
    salida.write(resultado)

print("Resultado:", resultado)


############################################################################################################
############################################################################################################
#------------------------------------------------------------------------------------------------------------
############################################################################################################
############################################################################################################

# %%

#Transcripción de ADN a ARN

input_path = "c:/Users/Camilo A. Marin Cast/Downloads/Rosalind_txt/rosalind_rna.txt"
output_path = "c:/Users/Camilo A. Marin Cast/Downloads/Rosalind_txt/rosalind_rna_output.txt"

with open (input_path, "r") as archivo_entrada:
    secuencia_adn = archivo_entrada.read().strip()

#Se hace la transcripción reemplazando las T por U
secuencia_arn = secuencia_adn.replace("T", "U")

with open (output_path, "w") as archivo_salida:
    archivo_salida.write(secuencia_arn)

print(f"Secuencia de ARN transcrita: {secuencia_arn}")
print(f"Total de nucleótidos en la secuencia de ARN: {len(secuencia_arn)}")
print(f"Total de nucleótidos en la secuencia de ADN: {len(secuencia_adn)}")

############################################################################################################
############################################################################################################
#------------------------------------------------------------------------------------------------------------
############################################################################################################
############################################################################################################
# %%
#Realizar la hebra complementaria de ADN

input_path = "c:/Users/Camilo A. Marin Cast/Downloads/Rosalind_txt/rosalind_revc.txt"
output_path = "c:/Users/Camilo A. Marin Cast/Downloads/Rosalind_txt/rosalind_revc_output.txt"

with open(input_path, "r") as archivo_entrada:
    secuencia_adn = archivo_entrada.read().strip()

#se invierte la secuencia
secuencia_adn_invertida = secuencia_adn[::-1]

#se mapean los complementos de cada base nitrogenada
tabla_complemento = str.maketrans("ACGT", "TGCA")
secuencia_complementaria = secuencia_adn_invertida.translate(tabla_complemento)

with open(output_path, "w") as archivo_salida:
    archivo_salida.write(secuencia_complementaria)

print(f"Secuencia complementaria: {len(secuencia_complementaria)} nucleótidos")
print("Primeros 10 nucleótidos de la secuencia complementaria:", secuencia_complementaria[:10])
print("Ultimos 10 nucleótidos de la secuencia complementaria:", secuencia_complementaria[-10:])
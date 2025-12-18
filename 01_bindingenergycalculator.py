# LECCIÓN 2: Automatizando con bucles. Curva de estabilidad

# En la lección anterior estudiamos una calculadora que servía para un isótopo concreto. En la vida real, ~
# se trabajan con cientos y cientos de isótopos a la vez, por lo que hemos de dar un paso adelante.

# Introducimos conceptos nuevos:
# Lista ([...]). Es como un vector, en lugr de una variable para cada cosa, guardamos muchas cosas juntas entre corchetes.
# Bucle "for". Es una orden que dice: "para cada elemento de esta lista, repite estas instrucciones".
# Indentación (Sangría). En Python, lo que está dentro del bucle tiene que estar desplazado a la derecha (4 espacios o directamente
# con el tabulador). Si lo pegas al margen izquierdo, Python cree que está fuera del bucle.

# Definimos las constantes (en unidades de masa atómica—u)
masa_proton = 1.007276
masa_neutron = 1.008665
u_a_MeV = 931.5

# Nuestra base de datos (una lista de listas).
# Formato: [Nombre, Z (protones), N (neutrones), Masa_Real (u)]
datos_nucleares = ["Deuterio", 1, 1, 2.014102], ["Tritio", 1, 2, 3.016049], ["Helio-4", 2, 2, 4.002602], ["Oxígeno-16", 8, 8, 15.994915], ["Hierro-56", 26, 30, 55.934937], ["Uranio-235", 92, 143, 235.0439299]

# Encabecero del resultado
print(f"{'ISÓTOPO':<12} | {'E. ENLACE (Total)':<20} | {'E. POR NUCLEÓN (B/A)'}")
print("-" * 65)

# Comienza el bucle.
for nucleo in datos_nucleares:
    # Extraemos los datos de la lista (desempaqueto, por así decirlo)
    nombre = nucleo[0]
    Z = nucleo[1]
    N = nucleo[2]
    masa_real = nucleo[3]
    # Número másico
    A = N + Z
    # Cálculo numérico (misma física que antes)
    masa_teorica = (Z*masa_proton) + (N*masa_neutron)
    defecto = masa_teorica - masa_real
    energia_total = defecto*u_a_MeV

    # IMPORTANTE. Energía por nucleón, para comparar estabilidad
    energia_por_nucleon = energia_total / A

    # Imprimo una línea por cada vuelta del bucle
    print(f"{nombre:<12} | {energia_total:10.2f} MeV       | {energia_por_nucleon:.4f} MeV/u")

# A la vista de los resultados, vemos que el Deuterio tiene muy poca energía de enlace por nucleón, es decir, es "blandito", poco estable.
# El Hierro-56, sin embargo, es el pico de la curva de estabilidad. Es el núcleo más fuertemente unido del universo, y es por ello que 
# las estrellas mueren cuando empiezan a producir hierro: ya no pueden sacar energía fusionándolo.
# El Uranio-235 baja a unos 7.5 MeV, tiene menos energía de enlace por nucleón que el hierro o productos intermedios. Si lo rompemos (fisión)
# para ir hacia el centro de la tabla, liberas energía.


# También podemos dibujar la gráfica con el número másico (A) en el eje X y la energía por nucleón en el eje Y.
# Cargamos la librería matplotlib con el apodo plt
import matplotlib.pyplot as plt

# Vamos a renombrar los datos y añadir un par más para que se vea más bonito
datos_nucleares = ["H-2", 1, 1, 2.014102], ["H-3", 1, 2, 3.016049], ["He-4", 2, 2, 4.002602], ["Li-7", 3, 4, 7.016003], ["C-12", 6, 6, 12.000000], ["O-16", 8, 8, 15.994915], ["Fe-56", 26, 30, 55.934937], ["Kr-89", 36, 53, 88.91763], ["U-235", 92, 143, 235.0439299]

# Pasamos con las listas vacías que llenaremos dentro del bucle para graficar
eje_x_masa = []
eje_y_energia = []
nombres = []

# Comienza el bucle
for nucleo in datos_nucleares:
    nombre = nucleo[0]
    Z = nucleo[1]
    N = nucleo[2]
    masa_real = nucleo[3]
    # El número másico:
    A = Z + N
    # Cálculos físicos
    masa_teorica = (Z*masa_proton) + (N*masa_neutron)
    defecto = masa_teorica - masa_real
    energia_total = defecto*u_a_MeV
    energia_por_nucleon = energia_total / A
    # Guardamos los datos en las listas
    eje_x_masa.append(A)
    eje_y_energia.append(energia_por_nucleon)
    nombres.append(nombre)
# Graficamos
plt.figure(figsize=(10,6))
plt.plot(eje_x_masa, eje_y_energia, color='blue', alpha=0.3)
plt.scatter(eje_x_masa, eje_y_energia, color='red', s=100)
# Nombres a cada punto
for i in range(len(nombres)):
    plt.text(eje_x_masa[i], eje_y_energia[i] + 0.1, nombres[i], fontsize=12)
# Decoración
plt.title("Curva de energía de enlace nuclear. Binding Energy", fontsize=16)
plt.xlabel("Número másico (A) — Tamaño del núcleo", fontsize=12)
plt.ylabel("Energía de enlace por nucleón (MeV/u)", fontsize=12)
plt.grid(True, linestyle='--')
plt.show()
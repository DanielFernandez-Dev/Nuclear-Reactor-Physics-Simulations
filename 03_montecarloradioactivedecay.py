# LECCIÓN 4: Simulación Monte Carlo
# La física nuclear es probabilística. No se sabe cuándo se va a desintegrar un átomo, solo sabemos la probabilidad de que ocurra.
# Los códigos profesionales como MCNP (Monte Carlo N-Particle) que se usan en el CERN, por ejemplo, se basan en tirar dados millones 
# de veces.
# Vamos a crear ahora un Simulador de Desintegración Radiactiva usando números aleatorios. El reto es el siguiente: 
# Tenemos 1000 átomos de un isótopo radiactivo inestable. En cada segundo, cada átomo tira un dado. Si saca un "1", 
# se desintegra (desaparece); si no, sobrevive. Queremos ver cómo esa población baja hasta cero y si se cumple la famosa 
# Ley Exponencial estudiada, 
#   N=N0e^{-lambda t}.

import matplotlib.pyplot as plt
import random # Librería para tirar dados

# 1. CONFIGURACIÓN DEL EXPERIMENTO
atomos_iniciales = 1000
probabilidad_desintegracion = 0.1 # 10% de probabilidad cada segundo, lambda
tiempo_maximo = 100
# Listas
historial_tiempo = []
historial_atomos = []
atomos_actuales = atomos_iniciales
print(f"--- INICIO MONTE CARLO: {atomos_actuales} ÁTOMOS ---")

# 2. BUCLE TEMPORAL
for t in range(tiempo_maximo):
    historial_tiempo.append(t)
    historial_atomos.append(atomos_actuales)
    # 3. EL CORAZÓN DE MONTE CARLO
    # Recorremos cada átomo que queda vivo uno a uno. Puede tardar si ponemos millones de átomos
    desintegrados_en_este_seg = 0
    for i in range(atomos_actuales):
        # Tiramos un dado entre 0.0 y 1.0
        tiro = random.random()
        # Si el número es menor que la probabilidad (0.1), se muere
        if tiro < probabilidad_desintegracion:
            desintegrados_en_este_seg += 1
    # Restamos las bajas a la población actual
    atomos_actuales -= desintegrados_en_este_seg
    # Si no quedan átomos, paramos
    if atomos_actuales <= 0:
        print(f"Todos los átomos se han desintegrado en t={t} s.")
        break
# 4. RESULTADO VISUAL
plt.figure(figsize=(10,6))
# Puntos azules -> simulación real con ruido
plt.scatter(historial_tiempo, historial_atomos, s=10, color='blue', label="Simulación Monte Carlo")
# Curva teórica
# N(t) = N0 * (1-p)^t
# Esto se debe a que nuestro paso de tiempo, p=0.1, es muy pequeño. La aproximación por serie de Taylor permite el 
# paso del sistema continuo al discreto, de forma que e^(-p) = 1-p y (1-p)^t = e^(-p*t)
curva_teorica = []
for t in historial_tiempo:
    val = atomos_iniciales * ((1-probabilidad_desintegracion)**t)
    curva_teorica.append(val)
plt.plot(historial_tiempo, curva_teorica, color='red', linewidth=2, label='Ley Teórica (Exponencial)')
plt.title(f"Simulación Monte Carlo de Desintegración ({atomos_iniciales} átomos)")
plt.xlabel("Tiempo (s)")
plt.ylabel("Átomos restantes")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
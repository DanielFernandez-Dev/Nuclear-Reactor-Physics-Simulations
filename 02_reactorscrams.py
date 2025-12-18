# LECCIÓN 3: El cerebro del reactor

# Hasta ahora hemos operado con cálculos, siendo nuestro ordenador una calculadora glorificada. Un Operador Nuclear no solo calcula;
# toma decisiones basadas en datos que varían con el tiempo. Vamos a programar una versión simple del sistema de protección del reactor.
    # Concepto físico: transitorios. Las cosas cambian de segundo a segundo.
    # Concepto Python: Condicionales (if/else) y bucles de tiempo (while)
# Vamos a simular un reactor que se está calentando peligrosamente. El código será el Sistema Automático de Protección.
    # 1. El reactor empieza estable.
    # 2. Introduciremos una perturbación (subida de potencia).
    # 3. El código debe vigilar la temperatura.
    # 4. Si pasa de 310°C -> alarma
    # 5. Si pasa de 320°C -> SCRAM (Disparo Automático / Caída de barras).

import matplotlib.pyplot as plt
# Para simular el paso del tiempo real
import time
print(f"---INICIANDO SIMULACIÓN DE REACTOR PWR---")

# 1. Condiciones iniciales
temperatura = 300.0 # Grados Celcius
tiempo = 0
scram = False # Al principio no ha saltado el disparo, está estable.
# Listas para guardar el historial y luego graficar
historial_tiempo = []
historial_temp = []

# 2. BUCLE DEL TIEMPO. GAME LOOP
# "Mientras el tiempo sea menor a 50 segundos..."
while tiempo < 50:
    # Guardamos los datos actuales para la gráfica
    historial_tiempo.append(tiempo)
    historial_temp.append(temperatura)
    # FÍSICA DEL REACTOR SIMULADA
    if not scram:
        # Si NO hay scram, el reactor está ganando potencia. Accidente.
        # Ahora sube 2 grados por segundo, muchísimo para nuestra tarea.
        temperatura = temperatura + 2.0
    else:
        # Si sí hubo scram, las barras han caído y enfrían el núcleo. La temperatura baja 5 grados.
        temperatura = temperatura - 5.0
    # SISTEMA DE PROTECCIÓN
    if temperatura > 320 and not scram:
        print(f"[ALERTA] T={tiempo}s: ¡TEMP {temperatura} °C CRÍTICA -> SCRAM ACTIVADO.")
        scram = True
    elif temperatura > 310 and not scram:
        print(f"[ALERTA] T={tiempo}s: Temp {temperatura} °C alta. Monitorizando...")
    # Avanzamos el tiempo
    tiempo = tiempo + 1
    # Truco para que no acabe instantáneo en la consola.
    time.sleep(0.2)

# 3. ANÁLISIS POST-ACCIDENTE (GRÁFICA)
plt.figure(figsize=(10,6))
plt.plot(historial_tiempo, historial_temp, label="Temp. Refrigerante", linewidth=3)
# Línea roja de peligro
plt.axhline(y=320, color='r', linestyle="--", label="Límite SCRAM (320°C)")
plt.title('Simulación de Transitorio y Disparo Automático (SCRAM)')
plt.xlabel('Tiempo (segundos)')
plt.ylabel('Temperatura (°C)')
plt.legend()
plt.grid(True)
plt.show()
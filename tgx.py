import math
# La función implementa la fórmula de la distancia euclidiana en 3D:
# √[(x₂-x₁)² + (y₂-y₁)² + (z₂-z₁)²]
def distancia_3d(punto1, punto2):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(punto1, punto2)))

def calcular_ruta_cable(dimensiones_transportador,
                        posicion_motor,                       
                        longitud_total_cable,                        
                        posicion_mural,
                        factor_curvatura=1.07):
    
    altura = dimensiones_transportador[2]
    
    # posiciones originales de las patas
    patas = [
        ("P1", (-487, -467.5, 1000)),
        ("P4", (487, -467.5, 1000)),
        ("P3", (487, 467.5, 1000)),
        ("P2", (-487, 467.5, 1000))
    ]
    
    # calcula la distancia entre las coordenadas de la pata y la posición del mural.
    pata_cercana = min(patas, key=lambda p: distancia_3d(p[1], posicion_mural)) #Aquí, key=lambda compara los puntos basándose en su distancia al origen.
    # y min() elige la pata con la menor distancia.
    
    # Calcular la distancia del motor a la pata más cercana
    distancia_motor_pata = distancia_3d(posicion_motor, pata_cercana[1])

    # Calcular longitud fija del cable
    centro_transportador = (0, 0, altura)
    distancia_motor_centro = distancia_3d(posicion_motor, centro_transportador)
    longitud_fija = 2 * distancia_motor_centro + distancia_motor_pata
    
    # Calcular longitud del cable hasta el mural
    distancia_pata_mural = distancia_3d(pata_cercana[1], posicion_mural)
    
    longitud_cable = (longitud_fija + distancia_pata_mural) * factor_curvatura
    
    cable_restante = longitud_total_cable - longitud_cable
    
    return pata_cercana[0], longitud_cable, cable_restante, distancia_pata_mural, distancia_motor_pata

# Ejemplo de uso
dimensiones_transportador = (1850, 1850, 1100)  # ancho, profundidad, altura NO CONFUNDIR CON COORDENADAS
posicion_motor = (-788, 37, 900)  # Posición real del motor
longitud_total_cable = 6000
factor_curvatura = 1.07 # Este es para los cables.

# Posición del mural (en 3D, incluyendo la altura)
posicion_mural = (955, 1154, 300)  # x, y, z (donde z es la altura del mural)

pata_cercana, longitud_cable, cable_restante, distancia_pata_mural, distancia_motor_pata = calcular_ruta_cable(
    dimensiones_transportador,
    posicion_motor,
    longitud_total_cable,
    posicion_mural,
    factor_curvatura
)

print(f"Pata más cercana al mural: {pata_cercana}")
print(f"Longitud total del cable hasta el tope del mural: {longitud_cable:.2f} mm")
print(f"Cable restante: {cable_restante:.2f} mm")
print(f"Distancia de la pata al mural: {distancia_pata_mural:.2f} mm")
print(f"Distancia motor a pata: {distancia_motor_pata:.2f} mm")
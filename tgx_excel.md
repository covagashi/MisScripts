## Fórmulas de Excel para cálculo de ruta de cable

1. **Distancia 3D entre dos puntos:**
   ```
   =RAIZ((X2-X1)^2 + (Y2-Y1)^2 + (Z2-Z1)^2)
   ```

2. **Distancia motor a cada pata:**
   ```
   =RAIZ((Xmotor-Xpata)^2 + (Ymotor-Ypata)^2 + (Zmotor-Zpata)^2)
   ```

3. **Distancia de cada pata al mural:**
   ```
   =RAIZ((Xpata-Xmural)^2 + (Ypata-Ymural)^2 + (Zpata-Zmural)^2)
   ```

4. **Encontrar la pata más cercana al mural:**
   ```
   =INDICE(NombresPatas, COINCIDIR(MIN(DistanciasPatasAlMural), DistanciasPatasAlMural, 0))
   ```

5. **Longitud fija del cable:**
   ```
   =2 * RAIZ((Xmotor-0)^2 + (Ymotor-0)^2 + (Zmotor-AlturaCentro)^2) + DistanciaMotorPataMinima
   ```

6. **Longitud total del cable hasta el mural:**
   ```
   =(LongitudFija + DistanciaPataMinimaMural) * FactorCurvatura
   ```

7. **Cable restante:**
   ```
   =LongitudTotalCable - LongitudCableHastaMural
   ```

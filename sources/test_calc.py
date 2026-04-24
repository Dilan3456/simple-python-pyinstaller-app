class RubikCube2x2:
    """
    Representación y manipulación de un cubo Rubik 2x2x2

    Estructura del arreglo de 24 posiciones:
    - Posiciones 0-3: Cara Roja (R)
    - Posiciones 4-7: Cara Azul (A)
    - Posiciones 8-11: Cara Morada (M)
    - Posiciones 12-15: Cara Verde (V)
    - Posiciones 16-19: Cara Naranja (N)
    - Posiciones 20-23: Cara Amarilla (L)

    Estructura de cada cara (4 posiciones):
    0 1
    2 3
    """

    def __init__(self):
        """Inicializa el cubo en su estado resuelto"""
        # Estado inicial: cada cara con su color
        self.cube = list("RRRRAAAAMMMMVVVVNNNNLLLL")

        # Índices de las caras: U(Azul), D(Verde), L(Rojo), R(Naranja), F(Amarilla), B(Morada)
        self.FACES = {
            'U': (4, 5, 6, 7),      # Azul - Arriba
            'D': (12, 13, 14, 15),  # Verde - Abajo
            'L': (0, 1, 2, 3),      # Rojo - Izquierda
            'R': (16, 17, 18, 19),  # Naranja - Derecha
            'F': (20, 21, 22, 23),  # Amarilla - Frente
            'B': (8, 9, 10, 11)     # Morada - Atrás
        }

        # Mapeo de abreviaturas españolas a movimientos
        self.MOVIMIENTOS = {
            'sup-der': ('U', True),   # Superior derecha
            'sup-izq': ('U', False),  # Superior izquierda
            'inf-der': ('D', True),   # Inferior derecha
            'inf-izq': ('D', False),  # Inferior izquierda
            'lde-der': ('R', True),   # Lateral derecha - derecha
            'lde-izq': ('R', False),  # Lateral derecha - izquierda
            'liz-der': ('L', True),   # Lateral izquierda - derecha
            'liz-izq': ('L', False),  # Lateral izquierda - izquierda
            'fro-der': ('F', True),   # Frontal - derecha
            'fro-izq': ('F', False),  # Frontal - izquierda
            'pos-der': ('B', True),   # Posterior - derecha
            'pos-izq': ('B', False)   # Posterior - izquierda
        }

    def ejecutar_movimiento(self, abreviatura):
        """
        Ejecuta un movimiento usando su abreviatura en español

        Movimientos válidos:
        - sup-der: giro a derecha de cara superior
        - sup-izq: giro a izquierda de cara superior
        - inf-der: giro a derecha de cara inferior
        - inf-izq: giro a izquierda de cara inferior
        - lde-der: giro a derecha de cara lateral derecha
        - lde-izq: giro a izquierda de cara lateral derecha
        - liz-der: giro a derecha de cara lateral izquierda
        - liz-izq: giro a izquierda de cara lateral izquierda
        - fro-der: giro a derecha de cara frontal
        - fro-izq: giro a izquierda de cara frontal
        - pos-der: giro a derecha de cara posterior
        - pos-izq: giro a izquierda de cara posterior
        """
        if abreviatura not in self.MOVIMIENTOS:
            print(f"Error: Movimiento '{abreviatura}' no reconocido")
            print("Movimientos válidos:", list(self.MOVIMIENTOS.keys()))
            return False

        cara, sentido_derecha = self.MOVIMIENTOS[abreviatura]

        if cara == 'U':
            self.move_U(clockwise=sentido_derecha)
        elif cara == 'D':
            self.move_D(clockwise=sentido_derecha)
        elif cara == 'L':
            self.move_L(clockwise=sentido_derecha)
        elif cara == 'R':
            self.move_R(clockwise=sentido_derecha)
        elif cara == 'F':
            self.move_F(clockwise=sentido_derecha)
        elif cara == 'B':
            self.move_B(clockwise=sentido_derecha)

        return True

    def display(self):
        """Muestra el estado actual del cubo"""
        print("\nEstado del cubo:")
        print("Arreglo completo:", "".join(self.cube))
        print("\nVista desenvuelta:")
        print(f"  Azul (U):     {self.cube[4]}{self.cube[5]}")
        print(f"                {self.cube[6]}{self.cube[7]}")
        print(f"\n  Rojo (L):     {self.cube[0]}{self.cube[1]}  "
              f"Morada (B):  {self.cube[8]}{self.cube[9]}  "
              f"Naranja (R): {self.cube[16]}{self.cube[17]}  "
              f"Amarilla (F): {self.cube[20]}{self.cube[21]}")
        print(f"                {self.cube[2]}{self.cube[3]}  "
              f"              {self.cube[10]}{self.cube[11]}  "
              f"              {self.cube[18]}{self.cube[19]}  "
              f"               {self.cube[22]}{self.cube[23]}")
        print(f"\n  Verde (D):    {self.cube[12]}{self.cube[13]}")
        print(f"                {self.cube[14]}{self.cube[15]}")

    def rotate_face_cw(self, face_indices):
        """Rota una cara 90° en sentido de las manecillas del reloj"""
        i0, i1, i2, i3 = face_indices
        # Permuta los elementos: (i0 i1 i2 i3) -> (i2 i0 i3 i1)
        self.cube[i0], self.cube[i1], self.cube[i2], self.cube[i3] = \
            self.cube[i2], self.cube[i0], self.cube[i3], self.cube[i1]

    def rotate_face_ccw(self, face_indices):
        """Rota una cara 90° en sentido contrario a las manecillas del reloj"""
        i0, i1, i2, i3 = face_indices
        # Permuta los elementos: (i0 i1 i2 i3) -> (i1 i3 i0 i2)
        self.cube[i0], self.cube[i1], self.cube[i2], self.cube[i3] = \
            self.cube[i1], self.cube[i3], self.cube[i0], self.cube[i2]

    def move_U(self, clockwise=True):
        """Mueve la cara Azul (Up)"""
        if clockwise:
            self.rotate_face_cw(self.FACES['U'])
        else:
            self.rotate_face_ccw(self.FACES['U'])
        self._rotate_adjacent_U(clockwise)

    def move_D(self, clockwise=True):
        """Mueve la cara Verde (Down)"""
        if clockwise:
            self.rotate_face_cw(self.FACES['D'])
        else:
            self.rotate_face_ccw(self.FACES['D'])
        self._rotate_adjacent_D(clockwise)

    def move_L(self, clockwise=True):
        """Mueve la cara Roja (Left)"""
        if clockwise:
            self.rotate_face_cw(self.FACES['L'])
        else:
            self.rotate_face_ccw(self.FACES['L'])
        self._rotate_adjacent_L(clockwise)

    def move_R(self, clockwise=True):
        """Mueve la cara Naranja (Right)"""
        if clockwise:
            self.rotate_face_cw(self.FACES['R'])
        else:
            self.rotate_face_ccw(self.FACES['R'])
        self._rotate_adjacent_R(clockwise)

    def move_F(self, clockwise=True):
        """Mueve la cara Amarilla (Front)"""
        if clockwise:
            self.rotate_face_cw(self.FACES['F'])
        else:
            self.rotate_face_ccw(self.FACES['F'])
        self._rotate_adjacent_F(clockwise)

    def move_B(self, clockwise=True):
        """Mueve la cara Morada (Back)"""
        if clockwise:
            self.rotate_face_cw(self.FACES['B'])
        else:
            self.rotate_face_ccw(self.FACES['B'])
        self._rotate_adjacent_B(clockwise)

    def _rotate_adjacent_U(self, clockwise):
        """Rota los bordes adyacentes al movimiento U"""
        # Ciclo para sup-der (clockwise): L(0,1) <- R(2,3) <- F(0,1) <- B(0,1) <- L(0,1)
        if clockwise:
            temp = [self.cube[0], self.cube[1]]
            self.cube[0], self.cube[1] = self.cube[16], self.cube[17]
            self.cube[16], self.cube[17] = self.cube[20], self.cube[21]
            self.cube[20], self.cube[21] = self.cube[8], self.cube[9]
            self.cube[8], self.cube[9] = temp
        else:
            temp = [self.cube[0], self.cube[1]]
            self.cube[0], self.cube[1] = self.cube[8], self.cube[9]
            self.cube[8], self.cube[9] = self.cube[20], self.cube[21]
            self.cube[20], self.cube[21] = self.cube[16], self.cube[17]
            self.cube[16], self.cube[17] = temp

    def _rotate_adjacent_D(self, clockwise):
        """Rota los bordes adyacentes al movimiento D"""
        # Ciclo para inf-der (clockwise): F(2,3) -> L(2,3) -> B(2,3) -> R(2,3) -> F(2,3)
        if clockwise:
            temp = [self.cube[20], self.cube[21]]
            self.cube[20], self.cube[21] = self.cube[16], self.cube[17]
            self.cube[16], self.cube[17] = self.cube[8], self.cube[9]
            self.cube[8], self.cube[9] = self.cube[0], self.cube[1]
            self.cube[0], self.cube[1] = temp
        else:
            temp = [self.cube[20], self.cube[21]]
            self.cube[20], self.cube[21] = self.cube[0], self.cube[1]
            self.cube[0], self.cube[1] = self.cube[8], self.cube[9]
            self.cube[8], self.cube[9] = self.cube[16], self.cube[17]
            self.cube[16], self.cube[17] = temp

    def _rotate_adjacent_L(self, clockwise):
        """Rota los bordes adyacentes al movimiento L"""
        # Ciclo: U(4,6) <- B(11,9) <- D(14,12) <- F(22,20) <- U(4,6)
        if clockwise:
            temp = [self.cube[4], self.cube[6]]
            self.cube[4], self.cube[6] = self.cube[20], self.cube[22]
            self.cube[20], self.cube[22] = self.cube[12], self.cube[14]
            self.cube[12], self.cube[14] = self.cube[11], self.cube[9]
            self.cube[11], self.cube[9] = temp
        else:
            temp = [self.cube[4], self.cube[6]]
            self.cube[4], self.cube[6] = self.cube[9], self.cube[11]
            self.cube[9], self.cube[11] = self.cube[12], self.cube[14]
            self.cube[12], self.cube[14] = self.cube[20], self.cube[22]
            self.cube[20], self.cube[22] = temp

    def _rotate_adjacent_R(self, clockwise):
        """Rota los bordes adyacentes al movimiento R"""
        # Ciclo: U(5,7) <- F(23,21) <- D(13,15) <- B(8,10) <- U(5,7)
        if clockwise:
            temp = [self.cube[5], self.cube[7]]
            self.cube[5], self.cube[7] = self.cube[8], self.cube[10]
            self.cube[8], self.cube[10] = self.cube[13], self.cube[15]
            self.cube[13], self.cube[15] = self.cube[21], self.cube[23]
            self.cube[21], self.cube[23] = temp
        else:
            temp = [self.cube[5], self.cube[7]]
            self.cube[5], self.cube[7] = self.cube[21], self.cube[23]
            self.cube[21], self.cube[23] = self.cube[13], self.cube[15]
            self.cube[13], self.cube[15] = self.cube[8], self.cube[10]
            self.cube[8], self.cube[10] = temp

    def _rotate_adjacent_F(self, clockwise):
        """Rota los bordes adyacentes al movimiento F"""
        # Ciclo: U(6,7) <- L(3,1) <- D(12,13) <- R(18,16) <- U(6,7)
        if clockwise:
            temp = [self.cube[6], self.cube[7]]
            self.cube[6], self.cube[7] = self.cube[2], self.cube[0]
            self.cube[2], self.cube[0] = self.cube[13], self.cube[12]
            self.cube[13], self.cube[12] = self.cube[19], self.cube[17]
            self.cube[19], self.cube[17] = temp
        else:
            temp = [self.cube[6], self.cube[7]]
            self.cube[6], self.cube[7] = self.cube[17], self.cube[19]
            self.cube[17], self.cube[19] = self.cube[12], self.cube[13]
            self.cube[12], self.cube[13] = self.cube[0], self.cube[2]
            self.cube[0], self.cube[2] = temp

    def _rotate_adjacent_B(self, clockwise):
        """Rota los bordes adyacentes al movimiento B"""
        # Ciclo: U(4,5) <- R(16,18) <- D(15,14) <- L(1,3) <- U(4,5)
        if clockwise:
            temp = [self.cube[4], self.cube[5]]
            self.cube[4], self.cube[5] = self.cube[18], self.cube[16]
            self.cube[18], self.cube[16] = self.cube[15], self.cube[14]
            self.cube[15], self.cube[14] = self.cube[1], self.cube[3]
            self.cube[1], self.cube[3] = temp
        else:
            temp = [self.cube[4], self.cube[5]]
            self.cube[4], self.cube[5] = self.cube[1], self.cube[3]
            self.cube[1], self.cube[3] = self.cube[14], self.cube[15]
            self.cube[14], self.cube[15] = self.cube[16], self.cube[18]
            self.cube[16], self.cube[18] = temp


# Ejemplo de uso
if __name__ == "__main__":
    cubo = RubikCube2x2()

    print("=== CUBO RUBIK 2x2x2 ===")
    cubo.display()



    print("\n--- Movimiento: sup-izq (cara superior a izquierda) ---")
    cubo.ejecutar_movimiento('sup-izq')
    cubo.display()

    # print("\n--- Secuencia de movimientos ---")
    # secuencia = ['inf-der', 'liz-izq', 'pos-der', 'fro-izq']
    # for mov in secuencia:
    #     print(f"Ejecutando: {mov}")
    #     cubo.ejecutar_movimiento(mov)

    print("\nEstado final:")
    cubo.display()

    print("\n--- Movimientos válidos disponibles ---")
    movimientos = list(cubo.MOVIMIENTOS.keys())
    for i, mov in enumerate(movimientos, 1):
        print(f"{i:2d}. {mov}")


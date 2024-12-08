import math  
# Clase Point (Punto) que representa un punto en el plano cartesiano.
class Point:
    def __init__(self, x=0, y=0) -> None:
        """
        Inicializa un punto con las coordenadas x e y. Si no se especifican, 
        se asignan valores por defecto (0,0).
        """

        self.x = x
        self.y = y

    def __str__(self) -> str:
        """Devuelve una cadena que describe el objeto 'Point'."""
        return "Se ha creado el objeto punto"

    def move(self, new_x, new_y):
        """Permite mover el punto a nuevas coordenadas (new_x, new_y)."""
        self.x = new_x
        self.y = new_y

    def reset(self):
        """Reinicia las coordenadas del punto a (0, 0)."""
        self.x = 0
        self.y = 0

    def compute_distance(self, point: "Point") -> float:
        """
        Calcula la distancia entre el punto actual y otro punto utilizando
        la fórmula de distancia euclidiana.
        """
        return (((self.x - point.x) ** 2) + ((self.y - point.y) ** 2)) ** 0.5

    # Descripción de la clase como una definición general
    definition: str = "Entidad geométrica abstracta que representa" \
                "una ubicación en un espacio."


# Clase Line (Línea) que representa una línea definida por dos puntos.
class Line:
    def __init__(self, point_start: 'Point', point_end: 'Point') -> None:
        """Inicializa una línea con dos puntos de inicio y fin."""
        self.point_start = point_start
        self.point_end = point_end
        self.length = point_start.compute_distance(point_end)  # Calcula la longitud de la línea
        self.dx = point_end.x - point_start.x  # Diferencia en el eje x
        self.dy = point_end.y - point_start.y  # Diferencia en el eje y
        self.slope = (self.dy) / (self.dx) if self.dx != 0 else None  # Calcula la pendiente (si no es vertical)
        self.slope_radians = round(math.atan2(self.dy, self.dx), 2)  # Calcula la pendiente en radianes
        self.slope_degrees = f"{math.degrees(self.slope_radians):.2f}°"  # Convierte la pendiente a grados
        self.discretize_line_matrix: list = []  # Lista para almacenar puntos discretizados de la línea

    def calculate_length(self) -> float:
        """Devuelve la longitud de la línea."""
        return self.length

    def calculate_slope(self) -> float:
        """Devuelve la pendiente de la línea."""
        return self.slope

    # Método para determinar si la línea cruza el eje X
    def calculate_horizontal_cross(self) -> bool:
        return True if (self.point_end.y * self.point_start.y) < 0 else False

    # Método para determinar si la línea cruza el eje Y
    def calculate_vertical_cross(self) -> bool:
        return True if (self.point_end.x * self.point_start.x) < 0 else False

    # Discretiza la línea en varios puntos y los guarda en una lista
    def discretize_line(self, number_of_points: int) -> list:
        self.discretize_line_matrix = []
        increment_x = self.dx / (number_of_points - 1)  # Incremento en el eje X
        increment_y = self.dy / (number_of_points - 1)  # Incremento en el eje Y
        for i in range(number_of_points):
            self.discretize_line_matrix.append(
                Point(self.point_start.x + increment_x * i,
                      self.point_start.y + increment_y * i)
            )
        return self.discretize_line_matrix


# Clase Rectangle (Rectángulo) que representa un rectángulo con diferentes métodos de inicialización.
class Rectangle:
    def __init__(self, method: int = 1, *args) -> None:
        """Inicializa un rectángulo según el método seleccionado."""
        match method:
            case 1:  # Método 1: Esquina inferior-izquierda, ancho y altura
                self.bottom_left_corner = args[0]
                self.width: Point = args[1]
                self.height = args[2]
                self.center = Point(
                    self.bottom_left_corner.x + self.width / 2,
                    self.bottom_left_corner.y + self.height / 2,
                )
            case 2:  # Método 2: Centro, ancho y altura
                self.center: Point = args[0]
                self.width = args[1]
                self.height = args[2]
            case 3:  # Método 3: Esquinas inferior-izquierda y superior-derecha
                self.bottom_left_corner: Point = args[0]
                self.upper_right_corner: Point = args[1]
                self.width = (
                    self.upper_right_corner.x - self.bottom_left_corner.x
                    )
                self.height = (
                    self.upper_right_corner.y - self.bottom_left_corner.y
                    )
                self.center = Point(
                    self.bottom_left_corner.x + self.width / 2,
                    self.bottom_left_corner.y + self.height / 2,
                )
            case 4:  # Método 4: Líneas como lados del rectángulo
                self.bottom: Line = args[0]
                self.left: Line = args[1]
                self.upper: Line = args[2]
                self.right: Line = args[3]
                if not (
                    self.bottom.point_start.x == self.left.point_start.x
                    and self.left.point_end.y == self.upper.point_start.y
                    and self.upper.point_end.x == self.right.point_start.x
                    and self.right.point_start.y == self.bottom.point_start.y
                ):
                    print(
                        "Los puntos no coinciden, por lo tanto no se puede"
                        " crear un rectángulo"
                    )
                    return None
                self.width = self.right.length
                self.height = self.upper.length
                self.center = Point(
                    self.left.point_start.x + self.width / 2,
                    self.bottom.point_start.y + self.height / 2,
                )
            case _:  # Método por defecto
                print("No se ha seleccionado un método válido")

    def compute_area(self) -> float:
        """Calcula y devuelve el área del rectángulo."""
        return self.height * self.width

    def compute_perimeter(self) -> float:
        """Calcula y devuelve el perímetro del rectángulo."""
        return 2 * (self.height + self.width)

    def calculate_interference_point(self, point: 'Point') -> bool:
        """Determina si un punto está dentro del rectángulo."""
        return (
            (self.center.x - self.width / 2 <= point.x
            <= self.center.x + self.width / 2) and
            (self.center.y - self.height / 2 <= point.y
            <= self.center.y + self.height / 2)
        )

    def calculate_interference_line(self, line: 'Line') -> bool:
        """Determina si una línea cruza el rectángulo."""
        start_interference = self.calculate_interference_point(line.point_start)
        end_interference = self.calculate_interference_point(line.point_end)
        return start_interference != end_interference


# Clase Square (Cuadrado) que hereda de Rectangle, representando un cuadrado.
class Square(Rectangle):
    def __init__(self, method: int = 0, *args) -> None:
        """Inicializa un cuadrado y valida que sus lados sean iguales."""
        super().__init__(method, *args)
        if self.width != self.height:
            print(
                "El ancho y el alto no son iguales, por lo tanto"
                " no se puede crear un cuadrado",
                self.width,
                self.height
            )


# Creación de puntos y líneas de prueba.
point1 = Point(x=1, y=0)
point2 = Point(x=4, y=2)
point3 = Point(x=2.5, y=1)
point4 = Point(x=-3, y=0)
point5 = Point(x=2, y=1)
point6 = Point(x=2, y=4)
point7 = Point(x=4, y=0)
point8 = Point(x=1, y=2)
point9 = Point(x=1, y=3)
point10 = Point(x=4, y=3)

# Creación de líneas de prueba.
line1 = Line(point4, point5)
line2 = Line(point4, point6)
line3 = Line(point1, point7)
line4 = Line(point1, point8)
line5 = Line(point8, point2)
line6 = Line(point7, point2)
line7 = Line(point1, point9)
line8 = Line(point9, point10)
line9 = Line(point7, point10)

# Pruebas de los métodos de Line
print(line2.slope_radians)  # Muestra la pendiente en radianes
print(line2.slope_degrees)  # Muestra la pendiente en grados
line2.discretize_line(5)  # Discretiza la línea en 5 puntos
for idx, point in enumerate(line2.discretize_line_matrix, start=1):
    print(f"[[Punto {idx}], [{point.x:.2f}], [{point.y:.2f}]]")

# Creación de rectángulos y cuadrados usando diferentes métodos
# Metodo 1: Esquina inferior-izquierda, ancho y altura
rectangle1 = Rectangle(1, point1, 3, 2)
square1 = Square(1, point1, 3, 3)

# Metodo 2: Centro, ancho y altura
rectangle2 = Rectangle(2, point1, 3, 2)
square2 = Square(2, point1, 3, 3)

# Metodo 3: Esquinas inferior-izquierda y superior-derecha
rectangle3 = Rectangle(3, point1, point2)
square3 = Square(3, point1, point2)

#Metodo 4: Líneas como lados del rectángulo y cuadrado
rectangle3 = Rectangle(4, line3, line4, line5, line6)
square3 = Square(4, line3, line7, line8, line9)

# Pruebas de los métodos de Rectangle
print(rectangle3.compute_area())  # Calcula el área del rectángulo
print(rectangle3.compute_perimeter())  # Calcula el perímetro del rectángulo
# Verifica si un punto está dentro del rectángulo
print(rectangle3.calculate_interference_point(point=point3)) 
print(rectangle3.calculate_interference_point(point=point4)) 
# Verifica si una línea cruza el rectángulo
print(rectangle3.calculate_interference_line(line1))  
print(rectangle3.calculate_interference_line(line2))  
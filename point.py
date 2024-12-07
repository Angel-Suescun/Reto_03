import math

class Point:

    def __init__(self, x=0, y=0) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return "Se ha creado el objeto punto"

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def reset(self):
        self.x = 0
        self.y = 0

    def compute_distance(self, point: "Point") -> float:
        return (((self.x - point.x) ** 2) + ((self.y - point.y) ** 2)) ** 0.5

    definition: str = "Entidad geometrica abstracta que representa una ubicación en un espacio."
    


class Line:
    def __init__(self, point_start: 'Point', point_end: 'Point') -> None:
        self.point_start = point_start
        self.point_end = point_end
        self.length = point_start.compute_distance(point_end)
        self.dx = point_end.x - point_start.x
        self.dy = point_end.y - point_start.y
        self.slope = (self.dy) / (self.dx) if self.dx != 0 else None
        self.slope_radians = round(math.atan2(self.dy, self.dx), 2)
        self.slope_degrees =f"{math.degrees(self.slope_radians):.2f}°"
        self.discretize_line_matriz: list = []

    def calculate_length(self) -> float:
        return self.length

    def calculate_slope(self) -> float:
        return self.slope
    
    # Se calcula si la linea cruza el eje x por medio de la multiplicacion de
    # los puntos en y, si el resultado es negativo, la linea cruza el eje x
    def calculate_horizontal_croos(self) -> bool:  
        return True if (self.point_end * self.point_start) < 0 else False
    
    # Se calcula si la linea cruza el eje y por medio de la multiplicacion de
    # los puntos en x, si el resultado es negativo, la linea cruza el eje y
    def calculate_vertical_cross(self) -> bool:
        return True if (self.point_end * self.point_start) < 0 else False
    
    def discretize_line(self, number_of_points: int)-> list:
        self.discretize_line_matriz = []
        increment_x = self.dx / (number_of_points - 1)
        increment_y = self.dy / (number_of_points - 1)
        for i in range(number_of_points):
            self.discretize_line_matriz.append(
                Point(self.point_start.x + increment_x * i,
                 self.point_start.y + increment_y * i)
                )
        return self.discretize_line_matriz
    


class Rectangle:
    def __init__(self, method: int = 1, *args) -> None:
        match method:
            case 1:  # Bottom-left corner (Point), width, and height
                self.bottom_left_corner = args[0]
                self.width: Point = args[1]
                self.height = args[2]
                self.center = Point(
                    self.bottom_left_corner.x + self.width / 2,
                    self.bottom_left_corner.y + self.height / 2,
                )
            case 2:  # Center (Point), width, and height
                self.center: Point = args[0]
                self.width = args[1]
                self.height = args[2]
            case 3:  # Bottom-left and upper-right corners (Points)
                self.bottom_left_corner: Point = args[0]
                self.upper_right_corner: Point = args[1]
                self.width =( 
                    self.upper_right_corner.x - self.bottom_left_corner.x
                )
                self.height = (
                    self.upper_right_corner.y - self.bottom_left_corner.y
                )
                self.center = Point(
                    self.bottom_left_corner.x + self.width / 2,
                    self.bottom_left_corner.y + self.height / 2,
                )
            case 4:  # bottom, left, upper, and right (line)
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
                    print("Los puntos no coinciden, por lo tanto no se puede crear un rectangulo")
                    return None
                self.width = self.right.length
                self.height = self.upper.length
                self.center = Point(
                    self.left.point_start.x + self.width / 2,
                    self.bottom.point_start.y + self.height / 2,
                )
            case _:  # Default
                print("No se ha seleccionado un metodo valido")

    def compute_area(self) -> float:
        return self.height * self.width

    def compute_perimeter(self) -> float:
        return 2 * (self.height + self.width)

    def calculate_interference_point(self, point: 'Point') -> bool:
        return (
            (self.center.x - self.width / 2 <= point.x <= self.center.x + 
            self.width / 2) and 
            (self.center.y - self.height / 2 <= point.y <= self.center.y +
            self.height / 2)
        )

    def calculate_interference_line(self, line: 'Line') -> bool:
        start_interference = self.calculate_interference_point(line.point_start)
        end_interference = self.calculate_interference_point(line.point_end)
        return start_interference != end_interference


class Square(Rectangle):
    def __init__(self, method: int = 0, *args) -> None:
        super().__init__(method, *args)
        if self.width != self.height:
            print(
                "El ancho y el alto no son iguales, no se puede crear un cuadrado."
                , self.width,
                self.height
                )


# Asignacion Puntos
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



# Asignacion Linea
line1 = Line(point4, point5)
line2 = Line(point4, point6)
line3 = Line(point1, point7)
line4 = Line(point1, point8)
line5 = Line(point8, point2)
line6 = Line(point7, point2)
line7 = Line(point1, point9)
line8 = Line(point9, point10)
line9 = Line(point7, point10)



# Pruebas de metodos
print(line2.slope_radians)
print(line2.slope_degrees)
line2.discretize_line(5)
for idx, point in enumerate(line2.discretize_line_matriz, start=1):
    print(f"[[Point {idx}], [{point.x:.2f}], [{point.y:.2f}]]")


# # Asignacion Rectangulo y Cuadrado

# #Metodo 1
# rectangle1 = Rectangle(1, point1, 3, 2)
# square1= Square(1, point1, 3, 3)

# #Metodo 2
# rectangle2 = Rectangle(2, point1, 3, 2)
# square2= Square(2, point1, 3, 3)

# #Metodo 3
# rectangle3 = Rectangle(3, point1, point2)
# # Se usa para probar el error de que no se puede crear un cuadrado
# square3= Square(3, point1, point2) 

#Metodo 3
rectangle3 = Rectangle(4, line3, line4, line5, line6)
square3= Square(4, line3, line7, line8, line9)
print(square3.compute_perimeter())


# # Pruebas de metodos
# print(rectangle3.compute_area())
# print(rectangle3.compute_perimeter())
# print(rectangle3.calculate_interference_point(point=point3))
# print(rectangle3.calculate_interference_point(point=point4))
# print(rectangle3.calculate_interference_line(line1))
# print(rectangle3.calculate_interference_line(line2))


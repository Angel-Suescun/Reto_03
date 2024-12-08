import random


class MenuItem:
    """Representa un artículo del menú con un nombre y un precio."""

    def __init__(self, name: str, price: int) -> None:
        """Inicializa el artículo del menú con nombre y precio."""
        self.name = name
        self.price = price

    def calculate_total(self, order: 'Order') -> float:
        """Calcula el total de una orden aplicando descuento."""
        total = sum(order.items.values())
        total -= total * order.discount_percentage
        return total

    def print_order(self, order: 'Order') -> None:
        """Imprime los detalles de la orden y el total con descuento."""
        for item, price in order.items.items():
            print(f"{item.name} - {price}")
        print(f"Descuento: {order.discount_percentage * 100}%")
        print(f"Total: ${order.calculate_total():,} pesos")


class Order:
    """Representa una orden realizada por un cliente."""

    def __init__(self, student: bool = False) -> None:
        """Inicializa la orden con un descuento y una lista de artículos."""
        self.items: dict = {}  # Diccionario de artículos con cantidades
        self.discount_percentage: float = 0  # Descuento inicial
        self.student = student  # Flag para indicar si es estudiante

    def add_item(self, item: MenuItem, quantity: int) -> None:
        """Añade un artículo a la orden multiplicado por la cantidad."""
        self.items[item] = quantity * item.price

    def calculate_total(self) -> float:
        """Calcula el total de la orden aplicando el descuento."""
        total = sum(self.items.values())
        total -= total * self.discount_percentage  # Aplica descuento
        return total

    def promos(self) -> None:
        """Aplica promociones y descuentos según reglas predefinidas."""
        self.discount_percentage = 0  # Restablece el descuento

        # Descuento por cantidad de artículos
        if len(self.items) >= 6:  # 6 platos o más 10% de descuento
            self.discount_percentage += 0.1

        # Descuento adicional para estudiantes
        if self.student:  # Descuento del 20% para estudiantes
            self.discount_percentage += 0.2

        # Descuento aleatorio del 100%
        if random.random() < 0.1:  # 10% de probabilidad
            self.discount_percentage = 1

    def print_order(self) -> None:
        """Imprime la orden y el total con descuento aplicado."""
        for item, price in self.items.items():
            print(f"{item.name} - {price}")
        print(f"Descuento: {self.discount_percentage * 100}%")
        print(f"Total: ${self.calculate_total():,} pesos")


class Drink(MenuItem):
    """Clase para representar una bebida del menú."""

    def __init__(self, name: str, price: int, unit: int) -> None:
        """
        Inicializa una bebida con su nombre, precio y unidad de medida(ml).
        """
        super().__init__(name, price)
        self.unit = unit


class MainDishes(MenuItem):
    """Clase para representar un plato principal del menú."""

    def __init__(self, name: str, price: int, ingredients: list) -> None:
        """
        Inicializa un plato principal con su nombre, precio e ingredientes.
        """
        super().__init__(name, price)
        self.ingredients: list = ingredients


class Dessert(MenuItem):
    """Clase para representar un postre del menú."""

    def __init__(self, name: str, price: int, size: int) -> None:
        """Inicializa un postre con su nombre, precio y tamaño."""
        super().__init__(name, price)
        self.size = size


class Salads(MenuItem):
    """Clase para representar una ensalada del menú."""

    def __init__(self, name: str, price: int, container: str) -> None:
        """
        Inicializa una ensalada con su nombre, precio y tipo de recipiente.
        """
        super().__init__(name, price)
        self.container = container


class Soups(MenuItem):
    """Clase para representar una sopa del menú."""

    def __init__(self, name: str, price: int, temperature: int) -> None:
        """Inicializa una sopa con su nombre, precio y temperatura."""
        super().__init__(name, price)
        self.temperature = temperature  # 1: caliente, 2: frío


class Breakfast(MenuItem):
    """Clase para representar un desayuno del menú."""

    def __init__(self, name: str, price: int, quantity: int) -> None:
        """Inicializa un desayuno con su nombre, precio y cantidad."""
        super().__init__(name, price)
        self.quantity = quantity


# Bebidas
cafe = Drink("Café", 2000, 200)  # 200 ml
jugo_lulo = Drink("Jugo de Lulo", 2500, 250)  # 250 ml
agua_panela = Drink("Agua de panela", 1500, 300)  # 300 ml

# Platos principales
arepas = MainDishes("Arepa con queso", 8000, ["arepa", "queso"])
bandeja_paisa = MainDishes(
    "Bandeja Paisa",
    25000,
    ["arroz", "frijoles", "huevo", "carne", "chicharrón", "aguacate"],
)
sancocho = MainDishes(
    "Sancocho de gallina", 15000, ["gallina", "yuca", "papas", "plátano"]
)
ajiaco = MainDishes("Ajiaco", 18000, ["pollo", "papas", "mazorca", "guasca"])
empanadas = MainDishes("Empanadas", 3500, ["harina de maíz", "carne", "papas"])
bandeja_pescado = MainDishes(
    "Bandeja De Pescado",
    22000,
    ["arroz", "pescado frito", "patacones", "ensalada", "aguacate"],
)
tamal = MainDishes(
    "Tamales", 7000, ["masa de maíz", "carne", "pollo", "papa", "zanahoria"]
)

# Postres
arroz_con_leche = Dessert("Arroz con Leche", 3500, 200)  # 200 g
tres_leches = Dessert("Pastel Tres Leches", 5000, 180)  # 180 g
torta_de_guanabana = Dessert("Torta de Guanábana", 4500, 150)  # 150 g

# Ensaladas
ensalada_mixta = Salads("Ensalada Mixta", 4000, "tazón")
ensalada_de_pasta = Salads("Ensalada de Pasta", 5000, "plato")

# Sopas
sopa_de_lentejas = Soups("Sopa de Lentejas", 6000, 1)  # Caliente
sopa_de_carne = Soups("Sopa de Carne", 8000, 1)  # Caliente
sopa_de_vegetales = Soups("Sopa de Vegetales", 7000, 1)  # Caliente

# Desayunos
arepas_con_huevo = Breakfast("Arepas con Huevo", 5000, 2)  # 2 unidades
calentado = Breakfast("Calentado", 7000, 1)  # 1 porción
empanadas_con_aji = Breakfast("Empanadas con Aji", 4500, 3)  # 3 unidades


# Funcionamiento de las órdenes
print("---Orden 1---")
cliente = Order(student=True)
cliente.add_item(arepas, 2)
cliente.add_item(cafe, 1)
cliente.add_item(bandeja_paisa, 1)
cliente.add_item(arroz_con_leche, 1)

cliente.promos()
cliente.print_order()

print("\n\n---Orden 2---")
cliente2 = Order()
cliente2.add_item(ajiaco, 1)
cliente2.add_item(jugo_lulo, 1)
cliente2.add_item(sancocho, 1)
cliente2.add_item(tres_leches, 1)
cliente2.add_item(arepas_con_huevo, 5)
cliente2.add_item(empanadas, 2)
cliente2.add_item(torta_de_guanabana, 1)
cliente2.add_item(agua_panela, 1)

cliente2.promos()
cliente2.print_order()

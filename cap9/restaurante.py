class Restaurante:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Informação 1 {self.restaurant_name}, informação 2 {self.cuisine_type}")


    def open_restaurant(self):
        print("Aberto")

favorito = Restaurante("Sucessos bar", "a bo")

favorito.describe_restaurant()
favorito.open_restaurant()

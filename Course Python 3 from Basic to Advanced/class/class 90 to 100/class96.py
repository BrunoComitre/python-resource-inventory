class Product:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price
        
    def sale_off(self, percent):
        self.price = self.price - (self.price * (percent / 100))
        
    # Getter
    @property
    def price(self):
        return self._price
    
    # Setter
    @price.setter
    def price(self, value):
        if isinstance(value, str):
            value = float(value.replace("R$", ""))
        self._price = value
        

    # Getter
    @property
    def name(self):
        return self._name
    
    # Setter
    @name.setter
    def name(self, value):
        self._name = value.title()
        
product1 = Product("Jeans", 100)
product1.sale_off(10)
print(product1.price)

product2 = Product("Shirt", 50)
product2.sale_off(50)
print(product2.price)

product3 = Product("T-SHIRT", 80.0)
product3.sale_off(90)
print(product3.price)
print(product3.name)

product4 = Product("SHORTS", "R$20")
product4.sale_off(20)
print(product4.price)
print(product4.name)

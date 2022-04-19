class Productos:
    nombre: str
    precio: int
    cantidad: int
    marca: str

    def __init__(self, nombre, precio, cantidad, marca):
        self._nombre = nombre
        self._precio = precio
        self._cantidad = cantidad
        self._marca = marca

    def get_nombre(self):
        return self._nombre

    def get_precio(self):
        return self._precio

    def get_cantidad(self):
        return self._cantidad

    def get_marca(self):
        return self._marca

    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_precio(self, precio):
        self._precio = precio

    def set_cantidad(self, cantidad):
        self._cantidad = cantidad

    def set_marca(self, marca):
        self._marca = marca

    def mostrar(self):
        print(
            "\n".join(
                [
                    f"\n"
                    f"Producto: {self.get_nombre()}",
                    f"Precio: {self.get_precio()}",
                    f"Cantidad: {self.get_cantidad()}",
                    f"Marca: {self.get_marca()}",                 
                ]
            )
        )

    def porcentaje (self):
        cantidad = int(input("Ingrese la cantidad de productos a comprar: \n"))
        cantidadreal = self.get_cantidad()
        cantidadnew = cantidadreal - cantidad
        if cantidadnew < 0:
            print("No hay suficientes productos en stock")
        else:
            self.set_cantidad(cantidadnew)
            if cantidad >= 100:
                porcentaje = (self.get_precio() * 20) / 100
                precio = self.get_precio() - porcentaje
                totalpagar = cantidad * precio
                print(f"El precio a pagar por los productos es: {totalpagar}")
                    
            else:
                precio = self.get_precio() 
                totalpagar = cantidad * precio
                print(f"El precio a pagar por los productos es: {totalpagar}")

class Tienda:
    def comprar(self):
        shampo = Productos("Shampoo", 10, 10, "Pantene")
        acondicionador = Productos("Acondicionador", 50, 150, "Tresemmé")
        cremaCapilar = Productos("Crema Capilar", 60, 180, "Pantene")
        gel = Productos("Gel", 30, 200, "Ego")
        fijador = Productos("Fijador Capilar", 80, 10, "Tresemmé")

        bandera = True
        print("Bienvenido al supermercado!")
        while bandera:
            print(
                "\nQue le gustaria hacer? \n1. Comprar productos. \n2. Ver productos. \n3. Salir"
            )
            opcion = int(input("Ingrese una opcion: "))
            if opcion == 1:
                pros = input("Ingrese el nombre del producto: ")
                
                if pros.lower() == shampo.get_nombre().lower():
                    shampo.porcentaje()
                elif pros.lower() == acondicionador.get_nombre().lower():
                    acondicionador.porcentaje()
                
                elif pros.lower() == cremaCapilar.get_nombre().lower():
                    cremaCapilar.porcentaje()
                
                elif pros.lower() == gel.get_nombre().lower():
                    gel.porcentaje()

                elif pros.lower() == fijador.get_nombre().lower():
                    fijador.porcentaje()
            
            if opcion == 2:
                shampo.mostrar()
                acondicionador.mostrar()
                cremaCapilar.mostrar()
                gel.mostrar()
                fijador.mostrar()

            if opcion == 3:
                print("Gracias por su compra!")
                print("Hasta luego!")
                break

            if opcion < 1 or opcion > 3:
                print("Opcion no valida")
                x = Tienda()
                x.comprar()
    
    

program = Tienda()
program.comprar()
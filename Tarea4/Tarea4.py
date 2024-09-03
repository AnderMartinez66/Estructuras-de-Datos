class Smartphone:
    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio

    def __str__(self):
        return f"{self.marca} {self.modelo} - ${self.precio}"
    
    def actualizar(self, nueva_marca=None, nuevo_modelo=None, nuevo_precio=None):
        if nueva_marca:
            self.marca = nueva_marca
        if nuevo_modelo:
            self.modelo = nuevo_modelo
        if nuevo_precio:
            self.precio = nuevo_precio

class Nodo:
    def __init__(self, smartphone=None):
        self.smartphone = smartphone
        self.siguiente = None
        
class ListaLigada:
    def __init__(self):
        self.head = None

    def esta_vacia(self):
        return self.head is None
    
    def get_tamanio(self):
        tamanio = 0
        nodo_actual = self.head
        while nodo_actual:
            tamanio += 1
            nodo_actual = nodo_actual.siguiente
        return tamanio
    
    def agregar_al_final(self, smartphone):
        nuevo_nodo = Nodo(smartphone)
        if self.esta_vacia():
            self.head = nuevo_nodo
            return
        nodo_actual = self.head
        while nodo_actual.siguiente:
            nodo_actual = nodo_actual.siguiente
        nodo_actual.siguiente = nuevo_nodo
    
    def agregar_al_inicio(self, smartphone):
        nuevo_nodo = Nodo(smartphone)
        nuevo_nodo.siguiente = self.head
        self.head = nuevo_nodo

    def agregar_despues_de(self, modelo, smartphone_nuevo):
        nodo_actual = self.head
        while nodo_actual:
            if nodo_actual.smartphone.modelo == modelo:
                nuevo_nodo = Nodo(smartphone_nuevo)
                nuevo_nodo.siguiente = nodo_actual.siguiente
                nodo_actual.siguiente = nuevo_nodo
                return
            nodo_actual = nodo_actual.siguiente
        print(f"No se encontró un smartphone con el modelo {modelo}.")    
    
    def eliminar_por_posicion(self, posicion):
        if self.esta_vacia():
            print("La lista está vacía.")
            return
        if posicion == 0:
            self.head = self.head.siguiente
            return
        
        nodo_actual = self.head
        nodo_anterior = None
        contador = 0

        while nodo_actual and contador < posicion:
            nodo_anterior = nodo_actual
            nodo_actual = nodo_actual.siguiente
            contador += 1

        if nodo_actual is None:
            print("Posición fuera de rango.")
            return

        nodo_anterior.siguiente = nodo_actual.siguiente
    
    def eliminar_primero(self):
        if self.esta_vacia():
            print("La lista está vacía.")
            return

        self.head = self.head.siguiente
    
    def eliminar_final(self):
        if self.esta_vacia():
            print("La lista está vacía.")
            return

        # Si solo hay un nodo en la lista
        if self.head.siguiente is None:
            self.head = None
            return

        nodo_actual = self.head
        nodo_anterior = None

        # Recorrer la lista hasta el penúltimo nodo
        while nodo_actual.siguiente:
            nodo_anterior = nodo_actual
            nodo_actual = nodo_actual.siguiente

        # Eliminar la referencia al último nodo
        nodo_anterior.siguiente = None

    def buscar_posicion(self, modelo):
        nodo_actual = self.head
        posicion = 0
        while nodo_actual:
            if nodo_actual.smartphone.modelo == modelo:
                return posicion
            nodo_actual = nodo_actual.siguiente
            posicion += 1
        return -1  # Si no se encuentra el modelo
    
    def actualizar(self, modelo, nueva_marca=None, nuevo_modelo=None, nuevo_precio=None):
        nodo_actual = self.head
        while nodo_actual:
            if nodo_actual.smartphone.modelo == modelo:
                nodo_actual.smartphone.actualizar(nueva_marca, nuevo_modelo, nuevo_precio)
                return
            nodo_actual = nodo_actual.siguiente
        print(f"No se encontró un smartphone con el modelo {modelo} para actualizar.")
    
    def transversal(self):
        nodo_actual = self.head
        while nodo_actual:
            print(nodo_actual.smartphone)
            nodo_actual = nodo_actual.siguiente

def main():
    smartphone1 = Smartphone("Apple", "iPhone 13", 19899)
    smartphone2 = Smartphone("Samsung", "Galaxy S21", 15998)
    smartphone3 = Smartphone("Google", "Pixel 6", 11899)
    smartphone4 = Smartphone("OnePlus", "9 Pro", 13899)
    smartphone5 = Smartphone("Xiaomi", "Redmi Note 13 Pro", 8499)
    smartphone6 = Smartphone("Huawei", "Pura 70 Ultra", 22998)
    smartphone7 = Smartphone("Motorola", "Edge 40 Pro", 25999)

    lista = ListaLigada()

    lista.agregar_al_inicio(smartphone1)
    lista.agregar_al_final(smartphone2)
    lista.agregar_despues_de("Galaxy S21", smartphone3)
    lista.agregar_al_final(smartphone4)
    lista.agregar_al_final(smartphone5)
        
    lista.transversal()

    lista.eliminar_por_posicion(1)

    print(" ")
    print("Eliminando el smartphone de la posición 2:")
    lista.transversal()

    print(" ")
    print("Actualizando el segundo elemento:")
    lista.actualizar("Pixel 6", nuevo_precio=10899)
    lista.transversal()

    print(" ")
    print("Agregando otro elemento al inicio:")
    lista.agregar_al_inicio(smartphone6)
    lista.transversal()

    print(" ")
    print("Agregando otro elemento al final:")
    lista.agregar_al_final(smartphone7)
    lista.transversal()
    
if __name__ == "__main__":
    main()
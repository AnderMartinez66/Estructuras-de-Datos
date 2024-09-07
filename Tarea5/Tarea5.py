class Numero:
    def __init__(self, valor):
        self.valor = valor
    
    def __repr__(self):
        return str(self.valor)
    
    def actualizar(self, nuevo_numero=None, ):
        if nuevo_numero:
            self.valor = nuevo_numero

class Nodo:
    def __init__(self, valor=None):
        self.valor = valor
        self.anterior = None
        self.siguiente = None

class DoubleLinkedList:
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

    def agregar_al_inicio(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.esta_vacia():
            self.head = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.head
            self.head.anterior = nuevo_nodo
            self.head = nuevo_nodo
    
    def agregar_al_final(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.esta_vacia():
            self.head = nuevo_nodo
        else:
            actual = self.head
            while actual.siguiente:  # Recorremos hasta el último nodo
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
            nuevo_nodo.anterior = actual

    def agregar_después_de(self, referencia, valor):
        nuevo_nodo = Nodo(valor)
        actual = self.head
        while actual is not None:
            if actual == referencia:  # Encontramos el nodo de referencia
                nuevo_nodo.siguiente = actual.siguiente
                nuevo_nodo.anterior = actual
                if actual.siguiente:  # Si hay un nodo siguiente
                    actual.siguiente.anterior = nuevo_nodo
                actual.siguiente = nuevo_nodo
                return  # Terminamos una vez insertado
            actual = actual.siguiente

    def buscar(self, valor):
        actual = self.head
        indice = 0

        # Recorremos la lista buscando el valor
        while actual is not None:
            if actual.valor == valor:
                return indice
            actual = actual.siguiente
            indice += 1

        # Si el valor no se encuentra en la lista, devolvemos -1
        return -1
    
    def eliminar_el_primero(self):
        if not self.esta_vacia():
            if self.head.siguiente is None:  # Solo hay un nodo
                self.head = None  # La lista queda vacía
            else:
                self.head = self.head.siguiente  # Mover la cabeza al segundo nodo
                self.head.anterior = None  # Eliminar la referencia al nodo anterior

    def eliminar_el_final(self):
        if not self.esta_vacia():
            if self.head.siguiente is None:  # Solo hay un nodo
                self.head = None  # La lista queda vacía
            else:
                actual = self.head
                while actual.siguiente:
                    actual = actual.siguiente
                actual.anterior.siguiente = None
                     

    def eliminar_por_posicion(self, posicion):
        if self.esta_vacia():
            return  # Si la lista está vacía, no hay nada que eliminar

        actual = self.head
        indice = 0

        # Si queremos eliminar el primer nodo
        if posicion == 0:
            self.eliminar_el_primero()
            return

        # Recorremos hasta la posición deseada
        while actual is not None and indice < posicion:
            actual = actual.siguiente
            indice += 1

        # Si hemos llegado al final sin encontrar la posición, no hacemos nada
        if actual is None:
            return

        # Si el nodo a eliminar es el último
        if actual.siguiente is None:
            self.eliminar_el_final()
            return

        # Para eliminar un nodo intermedio
        if actual.anterior:
            actual.anterior.siguiente = actual.siguiente
        if actual.siguiente:
            actual.siguiente.anterior = actual.anterior
    
    def actualizar(self, posicion, nuevo_valor):
        if self.esta_vacia():
            print("La lista está vacía.")
            return

        actual = self.head
        indice = 0

        # Recorremos hasta la posición deseada
        while actual is not None and indice < posicion:
            actual = actual.siguiente
            indice += 1

        # Si hemos llegado al final sin encontrar la posición, no hacemos nada
        if actual is None:
            print("Posición fuera de rango.")
            return

        # Actualizamos el valor del nodo en la posición encontrada
        actual.valor = nuevo_valor

    def transversal(self):
        actual = self.head
        while actual is not None:
            print(actual.valor, end=" ")
            actual = actual.siguiente
        print()  # Para un salto de línea al final

def main():
    lista = DoubleLinkedList()

    lista.agregar_al_inicio(50)
    lista.agregar_al_final(60)
    lista.agregar_al_final(65)
    lista.agregar_al_final(70)
    lista.agregar_al_final(80)
    lista.agregar_al_final(90)

    lista.transversal()

    print("Eliminando el de la posición 2")
    lista.eliminar_por_posicion(1)
    lista.transversal()

    print("Actualizando la posición 4 a 88")
    lista.actualizar(3, 88)
    lista.transversal()

    print("Buscando el valor 80 en la lista")
    indice = lista.buscar(Numero(80))

    if indice != -1:
        print(f"El valor 80 está en la posición {indice}.")
    else:
        print("No se encontró el valor 80 en la lista.")
           
if __name__ == "__main__":
    main()
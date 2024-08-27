class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

nodo1 = Nodo(100)
nodo2 = Nodo(200)
nodo3 = Nodo(300)
nodo4 = Nodo(400)
nodo5 = Nodo(600)

nodo1.siguiente = nodo2
nodo2.siguiente = nodo3
nodo3.siguiente = nodo4
nodo4.siguiente = nodo5

actual = nodo1
while actual is not None:
    print(actual.valor)
    actual = actual.siguiente

actual = nodo1
while actual is not None:
    if actual.valor == 300:
        actual.valor = 333
        break
    actual = actual.siguiente

print("\nValores después de cambiar el nodo 3 a 333:")
actual = nodo1
while actual is not None:
    print(actual.valor)
    actual = actual.siguiente

nuevo_nodo = Nodo(700)
actual = nodo1
while actual.siguiente is not None:
    actual = actual.siguiente
actual.siguiente = nuevo_nodo

print("\nValores después de agregar el nuevo nodo con valor 700:")
actual = nodo1
while actual is not None:
    print(actual.valor)
    actual = actual.siguiente

nuevo_nodo_inicio = Nodo(50)
nuevo_nodo_inicio.siguiente = nodo1
nodo1 = nuevo_nodo_inicio

print("\nValores después de agregar el nuevo nodo con valor 50 al inicio:")
actual = nodo1
while actual is not None:
    print(actual.valor)
    actual = actual.siguiente
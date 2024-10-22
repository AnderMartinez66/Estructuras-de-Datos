class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.esta_vacia():
            return self.items.pop()
        return None

    def tamanio(self):
        return len(self.items)

    def ver_pila(self):
        return self.items

def eliminar_medio(pila, tamanio_medio):
    if tamanio_medio == 1:
        pila.pop()
        return

    elemento_superior = pila.pop()
    eliminar_medio(pila, tamanio_medio - 1)

    pila.push(elemento_superior)

def remover_elemento_medio(pila):
    if pila.esta_vacia():
        return
    tamanio = pila.tamanio()
    tamanio_medio = (tamanio // 2) + 1
    eliminar_medio(pila, tamanio_medio)

def potencia(a, b):
    if b == 0:
        return 1
    if b < 0:
        return 1 / potencia(a, -b)
    return a * potencia(a, b - 1)


base = 6
exponente = 5
resultado = potencia(base, exponente)
print(f"{base} elevado a la {exponente} es: {resultado}")

pila = Pila()
for i in range(1, 8):
    pila.push(i)

print("Pila original:", pila.ver_pila())
remover_elemento_medio(pila)
print("Pila después de remover el elemento del medio:", pila.ver_pila())

class ClienteBanco:
    def __init__(self, nombre, perfil, saldo):
        self.nombre = nombre
        self.perfil = perfil 
        self.saldo = saldo

    def retirar(self, monto):
        if self.saldo >= monto:
            self.saldo -= monto
            print(f"{self.nombre} retiró la cantidad de ${monto}. Saldo actual: ${self.saldo}")
        else:
            print(f"{self.nombre} no tiene suficiente saldo para retirar ${monto}. Saldo actual: ${self.saldo}")

    def __str__(self):
        return f"Cliente: {self.nombre}, Perfil: {self.perfil}, Saldo: ${self.saldo}"


class ColaConPrioridadAcotada:
    def __init__(self, niveles_prioridad):
        self.subcolas = [[] for _ in range(niveles_prioridad)]

    def insertar(self, cliente, prioridad):
        if 0 <= prioridad < len(self.subcolas):
            self.subcolas[prioridad].append(cliente)
        else:
            raise ValueError("Prioridad fuera de rango")

    def atender(self):
        for subcola in self.subcolas:
            if subcola:
                return subcola.pop(0) 
        raise Exception("No hay clientes en la cola")

    def mostrar(self):
        for i, subcola in enumerate(self.subcolas):
            print(f"Prioridad {i}: {[str(cliente) for cliente in subcola]}")

    def atender_todos(self):
        while any(self.subcolas):
            cliente = self.atender()
            print(f"Atendiendo a: {cliente}")


def obtener_prioridad(perfil):
    prioridades = {
        "no es cliente": 5,
        "cliente nuevo": 4,
        "cliente frecuente": 3,
        "cliente premium": 2,
        "celebridad": 1
    }
    return prioridades.get(perfil, 5)


def main():
    cola = ColaConPrioridadAcotada(6)  # Niveles de prioridad: 0 a 5

    # Llegan 2 clientes nuevos
    cliente1 = ClienteBanco("Cliente 1", "cliente nuevo", 20000)
    cliente2 = ClienteBanco("Cliente 2", "cliente nuevo", 13000)
    cola.insertar(cliente1, obtener_prioridad(cliente1.perfil))
    cola.insertar(cliente2, obtener_prioridad(cliente2.perfil))

    cliente3 = ClienteBanco("Cliente 3", "no es cliente", 0)
    cliente4 = ClienteBanco("Cliente 4", "no es cliente", 0)
    cliente5 = ClienteBanco("Cliente 5", "no es cliente", 0)
    cola.insertar(cliente3, obtener_prioridad(cliente3.perfil))
    cola.insertar(cliente4, obtener_prioridad(cliente4.perfil))
    cola.insertar(cliente5, obtener_prioridad(cliente5.perfil))

    celebridad = ClienteBanco("Celebridad", "celebridad", 2000000)
    cola.insertar(celebridad, obtener_prioridad(celebridad.perfil))

    print("\nEstado de la cola:")
    cola.mostrar()

    siguiente = cola.atender()
    print(f"\nAtendiendo a: {siguiente}")
    siguiente.retirar(10000)

    # Llegan dos clientes más: uno frecuente y uno premium
    cliente6 = ClienteBanco("Cliente 6", "cliente frecuente", 25000)
    cliente7 = ClienteBanco("Cliente 7", "cliente premium", 50000)
    cola.insertar(cliente6, obtener_prioridad(cliente6.perfil))
    cola.insertar(cliente7, obtener_prioridad(cliente7.perfil))

    # Atender al siguiente cliente
    siguiente = cola.atender()
    print(f"\nAtendiendo a: {siguiente}")

    # Imprimir el estado de la cola
    print("\nEstado de la cola:")
    cola.mostrar()

    # Atender todos los clientes restantes
    print("\nAtendiendo a todos los clientes restantes:")
    cola.atender_todos()

    # Imprimir el estado final de la cola
    print("\nEstado final de la cola:")
    cola.mostrar()


if __name__ == "__main__":
    main()

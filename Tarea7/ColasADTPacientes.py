class Paciente:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return f"Paciente: {self.nombre}"

class ColaADT:
    def __init__(self):
        self.cola = []

    def registrar(self, paciente):
        self.cola.append(paciente)
        print(f"{paciente} registrado en la cola.")

    def atender(self):
        if self.esta_vacia():
            print("No hay pacientes en espera.")
        else:
            paciente_atendido = self.cola.pop(0)
            print(f"Atendiendo a {paciente_atendido}.")

    def mostrar_cola(self):
        if self.esta_vacia():
            print("No hay pacientes en la cola.")
        else:
            print("Pacientes en la cola:")
            for paciente in self.cola:
                print(f"- {paciente}")

    def siguiente(self):
        if self.esta_vacia():
            print("No hay pacientes en espera.")
        else:
            print(f"El siguiente paciente es: {self.cola[0]}")

    def esta_vacia(self):
        return len(self.cola) == 0

def main():
    cola_pacientes = ColaADT()

    cola_pacientes.registrar(Paciente("Elizabeth"))
    cola_pacientes.registrar(Paciente("Ander"))
    cola_pacientes.registrar(Paciente("Paulo"))

    cola_pacientes.mostrar_cola()

    cola_pacientes.siguiente()

    cola_pacientes.atender()

    cola_pacientes.mostrar_cola()

    cola_pacientes.registrar(Paciente("Erick"))
    cola_pacientes.registrar(Paciente("Amy"))

    cola_pacientes.atender()

    cola_pacientes.mostrar_cola()

if __name__ == "__main__":
    main()

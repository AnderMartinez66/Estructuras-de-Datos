class NodoArbol:
    def __init__(self, value, left=None, right=None):
        self.data = value 
        self.left = left
        self.right = right

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def _imprimir_arbol(self, nodo, nivel=0, prefijo="Raíz: "):
        if nodo is not None:
            resultado = " " * (nivel * 4) + prefijo + str(nodo.data) + "\n"
            if nodo.left is not None or nodo.right is not None:
                resultado += self._imprimir_arbol(nodo.left, nivel + 1, "Izq: ")
                resultado += self._imprimir_arbol(nodo.right, nivel + 1, "Der: ")
            return resultado
        else:
            return " " * (nivel * 4) + prefijo + "None\n"

arbol = ArbolBinario()
arbol.raiz = NodoArbol(10,NodoArbol(5,NodoArbol(1)),NodoArbol(15,None,NodoArbol(25))) 

print("\nRepresentación Visual del Árbol:")
print(arbol._imprimir_arbol(arbol.raiz))

arbol1 = ArbolBinario()
arbol1.raiz = NodoArbol("Diego", NodoArbol("Pedro", NodoArbol("Susan"), NodoArbol("Diana")), NodoArbol("Mario"))

print("\nRepresentación Visual del Árbol:")
print(arbol1._imprimir_arbol(arbol1.raiz))

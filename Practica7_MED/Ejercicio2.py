class NodoExpr:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

def es_operador(tok):
    return tok in {"+", "-", "*", "/", "^"}

# Construye árbol a partir de una lista de tokens en POSTFIX
def construir_desde_postfix(tokens):
    stack = []
    for tok in tokens:
        if es_operador(tok):
            # operador: pop dos operandos (derecho, izquierdo)
            right = stack.pop()
            left = stack.pop()
            nodo = NodoExpr(tok)
            nodo.izquierdo = left
            nodo.derecho = right
            stack.append(nodo)
        else:
            # operando (número). Convertir a float/int según corresponda
            try:
                if "." in tok:
                    val = float(tok)
                else:
                    val = int(tok)
            except:
                val = tok  # podría ser variable (dejar como string)
            stack.append(NodoExpr(val))
    return stack[0] if stack else None

# Evaluar el árbol (si los operandos son numéricos)
def evaluar(nodo):
    if nodo is None:
        return 0
    if not es_operador(str(nodo.valor)):
        return nodo.valor  # número o variable (para variables habría que mapear)
    a = evaluar(nodo.izquierdo)
    b = evaluar(nodo.derecho)
    op = nodo.valor
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    if op == "/":
        return a / b
    if op == "^":
        return a ** b
    raise ValueError("Operador desconocido: " + str(op))

# Recorridos: Preorden, Inorden (con paréntesis), Postorden
def preorder(nodo):
    if nodo is None: 
        return []
    return [str(nodo.valor)] + preorder(nodo.izquierdo) + preorder(nodo.derecho)

def inorder(nodo):
    if nodo is None:
        return []
    if es_operador(str(nodo.valor)):
        return ["("] + inorder(nodo.izquierdo) + [str(nodo.valor)] + inorder(nodo.derecho) + [")"]
    else:
        return [str(nodo.valor)]

def postorder(nodo):
    if nodo is None:
        return []
    return postorder(nodo.izquierdo) + postorder(nodo.derecho) + [str(nodo.valor)]

# --- Ejemplo de uso ---
if __name__ == "__main__":
    # Expresión: (3 + 4) * (5 - 2) ^ 2
    # Postfix equivalente: 3 4 + 5 2 - 2 ^ *
    postfix_tokens = ["3", "4", "+", "5", "2", "-", "2", "^", "*"]

    raiz = construir_desde_postfix(postfix_tokens)

    print("Preorden  (prefija):", " ".join(preorder(raiz)))
    print("Inorden   (infija) :", " ".join(inorder(raiz)))
    print("Postorden (posfija) :", " ".join(postorder(raiz)))
    print("Evaluación:", evaluar(raiz))  # Resultado numérico
import tkinter as tk
from tkinter import simpledialog, scrolledtext, messagebox
from collections import defaultdict

class Grammar:
    def __init__(self, variables, terminals, start_variable, productions):
        self.variables = variables
        self.terminals = terminals
        self.start_variable = start_variable
        self.productions = productions

    def to_gnf(self):
        new_productions = []
        for left, right in self.productions:
            if len(right) == 1:
                if right[0] in self.variables:
                    new_productions.append((left, right))
                elif right[0] in self.terminals:
                    new_productions.append((left, ('ε', right[0])) if right[0] != 'ε' else (left, right))
            elif len(right) > 1:
                new_variable = f"{left}_{len(new_productions)}"
                for i in range(len(right) - 1):
                    new_productions.append((new_variable, (right[i],)))
                new_productions.append((left, (new_variable, right[-1])))

        self.variables.update({new_variable for left, right in new_productions if len(right) == 1})
        self.productions = new_productions
        return self

    def remove_unit_rules(self):
        new_productions = []
        unit_productions = [(left, right) for left, right in self.productions if len(right) == 1 and right[0] in self.variables]

        new_productions.extend((left, right) for left, right in self.productions if (left, right) not in unit_productions)
        for left, unit in unit_productions:
            for prod in self.productions:
                if prod[0] == unit[0] and prod not in unit_productions:
                    new_productions.append((left, prod[1]))

        self.productions = list(set(new_productions))
        return self

    def remove_self_loops(self):
        self.productions = [(left, right) for left, right in self.productions if not (len(right) == 1 and right[0] == left)]
        return self

    def __str__(self):
        grouped_productions = defaultdict(list)
        for left, right in self.productions:
            grouped_productions[left].append(' '.join(right))
        return '\n'.join(f"{left} -> {' | '.join(rights)}" for left, rights in grouped_productions.items())

def is_in_cnf(grammar):
    if grammar is None:
        return False, "No se ha definido ninguna gramática."
    
    has_epsilon = any(right == ('ε',) for left, right in grammar.productions if left == grammar.start_variable)
    
    for left, right in grammar.productions:
        if len(right) == 1 and right[0] == 'ε':
            if left != grammar.start_variable:
                return False, "No está en CNF. Solo el símbolo de inicio puede tener una producción epsilon."
        elif len(right) == 1:
            if right[0] not in grammar.terminals:
                return False, "No está en CNF. Los símbolos individuales a la derecha deben ser terminales."
        elif len(right) == 2:
            if any(symbol not in grammar.variables for symbol in right):
                return False, "No está en CNF. Ambos símbolos a la derecha de una producción binaria deben ser variables."
            if grammar.start_variable in right and has_epsilon:
                return False, "No está en CNF. El símbolo de inicio no puede aparecer a la derecha de las producciones si tiene una producción epsilon."
        else:
            return False, "No está en CNF. Las producciones deben tener uno o dos símbolos a la derecha."
    
    return True, "La gramática está en Forma Normal de Chomsky."

def check_cnf():
    is_cnf, message = is_in_cnf(grammar)
    messagebox.showinfo("Verificación de CNF", message)

def input_grammar():
    try:
        variables = set(simpledialog.askstring("Input", "Ingrese las variables (separadas por comas):").split(","))
        terminals = set(simpledialog.askstring("Input", "Ingrese los terminales (separados por comas):").split(","))
        start_variable = simpledialog.askstring("Input", "Ingrese la variable de inicio:")
        num_productions = simpledialog.askinteger("Input", "¿Cuántas producciones desea ingresar?")
        productions = []
        for _ in range(num_productions):
            left = simpledialog.askstring("Input", "Ingrese el lado izquierdo de la producción:")
            right_tuple = tuple(simpledialog.askstring("Input", "Ingrese el lado derecho de la producción (separado por espacios para múltiples):").split())
            productions.append((left, right_tuple))
        global grammar
        grammar = Grammar(variables, terminals, start_variable, productions)
        display_grammar()
    except Exception as e:
        messagebox.showerror("Error", f"Se ha producido un error: {e}")
        grammar = None  # Reset grammar if input fails

def display_grammar():
    grammar_text.config(state=tk.NORMAL)
    grammar_text.delete('1.0', tk.END)
    if grammar is not None:
        grammar_text.insert(tk.END, str(grammar))
    else:
        initial_message = "Bienvenido, escribe tu gramática\n\n"
        grammar_text.insert(tk.END, initial_message)
    grammar_text.config(state=tk.DISABLED)
def convert_to_gnf():
    global grammar
    if grammar is not None:
        grammar = grammar.to_gnf()
        display_grammar()
    else:
        messagebox.showinfo("Info", "Aún no se ha ingresado ninguna gramática.")

def remove_unit_rules():
    global grammar
    if grammar is not None:
        grammar = grammar.remove_unit_rules()
        display_grammar()
    else:
        messagebox.showinfo("Info", "Aún no se ha ingresado ninguna gramática.")

def remove_self_loops():
    global grammar
    if grammar is not None:
        grammar = grammar.remove_self_loops()
        display_grammar()
    else:
        messagebox.showinfo("Info", "Aún no se ha ingresado ninguna gramática.")

app = tk.Tk()
app.title("Conversor de Gramáticas")

btn_input = tk.Button(app, text="Ingresar Gramática", command=input_grammar)
btn_input.pack()

grammar_text = scrolledtext.ScrolledText(app, width=80, height=20)
grammar_text.pack()

btn_convert = tk.Button(app, text="Convertir a GNF", command=convert_to_gnf)
btn_convert.pack()

btn_remove_unit = tk.Button(app, text="Eliminar Reglas Unitarias", command=remove_unit_rules)
btn_remove_unit.pack()

btn_remove_loops = tk.Button(app, text="Eliminar Bucles Propios", command=remove_self_loops)
btn_remove_loops.pack()

btn_check_cnf = tk.Button(app, text="Verificar si está en FNC", command=check_cnf)
btn_check_cnf.pack()

app.mainloop()
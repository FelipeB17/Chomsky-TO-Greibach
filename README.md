# Proyecto: Conversor de Gramáticas FNC a FNG  
Autores:  
- **Andrés Felipe Beltrán Assaf** - 1152262  
- **Josué Daniel Pérez Guerrero** - 1152273  

## Descripción del Proyecto

Esta aplicación en Python permite verificar, analizar y convertir gramáticas en **Forma Normal de Chomsky (FNC)** a **Forma Normal de Greibach (FNG)**. Diseñada con una interfaz gráfica amigable utilizando **Tkinter**, facilita la interacción del usuario con gramáticas formales a través de botones funcionales y un área de visualización de resultados.

---

## Requisitos

- Python 3.x instalado
- Módulo `tkinter` habilitado (incluido por defecto en la mayoría de distribuciones de Python)

---

## Manual de Usuario

### 1. Inicio de la Aplicación

- Ejecuta el archivo principal de la aplicación (por ejemplo, `main.py`)
- Se abrirá una ventana con varios botones y un área de texto para mostrar gramáticas y resultados

### 2. Interfaz de Usuario

La interfaz gráfica incluye:

- **Botón "Ingresar Gramática"**  
  Permite al usuario introducir variables, terminales, símbolo inicial y producciones.

- **Área de Texto Central**  
  Muestra la gramática ingresada y los resultados de las conversiones y verificaciones.

- **Botón "Convertir a GNF"**  
  Realiza la conversión de la gramática visible a la **Forma Normal de Greibach (FNG)**.

- **Botón "Eliminar Reglas Unitarias"**  
  Elimina reglas del tipo A → B, donde ambas son variables.

- **Botón "Eliminar Bucles Propios"**  
  Elimina reglas como A → A.

- **Botón "Verificar si está en FNC"**  
  Verifica si la gramática cumple con los requisitos de la FNC.

### 3. Ejemplos de Uso

#### Ejemplo 1: Gramática en FNC

- **Variables:** S, A, B  
- **Terminales:** a, b  
- **Inicio:** S  
- **Producciones:**


S → AB | a
A → BA | b
B → a | b


**Pasos:**
1. Clic en **"Ingresar Gramática"** e introduce los datos.
2. Verifica si está en FNC usando el botón correspondiente.
3. Convierte la gramática a FNG haciendo clic en **"Convertir a GNF"**.

#### Ejemplo 2: Gramática NO en FNC

- **Variables:** S, A, B, C  
- **Terminales:** a, b, c  
- **Inicio:** S  
- **Producciones:**

S → Aa | B
A → BC
B → b
C → cS | c


**Pasos:**
1. Ingresa la gramática como en el ejemplo anterior.
2. Verifica si está en FNC. Se mostrará que **no cumple** por la producción `S → Aa`.
3. Aun así, intenta convertirla a FNG con el botón correspondiente y observa cómo el programa gestiona la transformación.

---

### 4. Cerrar la Aplicación

- Puedes cerrar la ventana directamente o interrumpir el proceso desde la terminal (Ctrl+C).

---

## Observaciones

Esta herramienta está diseñada como apoyo educativo para entender y transformar gramáticas formales. Su interfaz gráfica busca simplificar el manejo de estructuras propias de la teoría de lenguajes y autómatas.

---



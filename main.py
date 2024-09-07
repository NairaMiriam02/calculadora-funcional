import customtkinter as ctk
import math

# === Configurando tema ===
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

# === Funções de cálculo ===

# ---- Operações Aritméticas ----
def adicao():
    entrada = entry1.get()
    try:
        lista = list(map(float, entrada.split('+')))
        if len(lista) > 0:
            resultado = sum(lista)
            label_resultado.configure(text=f"Resultado: {resultado}")
    except ValueError:
        label_resultado.configure(text='Entrada inválida. Por favor, insira "+" ou um número válido.')

def subtracao():
    try:
        entrada = entry1.get()
        lista = list(map(float,entrada.split('-')))
        if len(lista) > 0:
            sub = lista[0]
            for n in lista[1:]:
                sub-=n
            label_resultado.configure(text=f"Resultado: {sub}")
    except ValueError:
        label_resultado.configure(text='Entrada inválida. Por favor, insira "-" ou um número válido.')

def multiplicacao():
    entrada = entry1.get()
    try:
        lista = list(map(float, entrada.split('x')))
        if len(lista) > 0:
            mult = 1
            for n in lista:
                mult *= n
            label_resultado.configure(text=f"Resultado da multiplicação: {mult}")
    except ValueError:
        label_resultado.configure(text='Entrada inválida. Por favor, insira "x" ou um número válido.')

def divisao():
    entrada = entry1.get()
    try:
        lista = list(map(float, entrada.split('/')))
        if len(lista) > 1:  
            resultado = lista[0]
            for n in lista[1:]:
                if n != 0:
                    resultado /= n
                else:
                    label_resultado.configure(text="Divisão por zero não é permitida.")
                    return
            label_resultado.configure(text=f"Resultado da divisão: {resultado}")
        else:
            label_resultado.configure(text="Por favor, insira mais de um valor para a divisão.")
    except ValueError:
        label_resultado.configure(text='Entrada inválida. Por favor, insira "/" ou números válidos.')

def radiciacao():
    try:
        num = float(entry1.get())
        raiz = math.sqrt(num)
        label_resultado.configure(text=f"Resultado: {raiz}")
    except ValueError:
        label_resultado.configure(text="Entrada inválida. Por favor, insira um número válido.")

def potenciacao():
    entrada = entry1.get()
    try:
        lista=list(map(float,entrada.split('^')))
        if len(lista) > 0:
            pot=lista[0]
            for n in lista[1:]:
                pot**=n
            label_resultado.configure(text=f"Resultado: {pot}")
    except ValueError:
        label_resultado.configure(text='Entrada inválida. Por favor, insira o "^" ou um número válido.')

# ----- Áreas e Perímetros ----
def area_perimetro_quad():
    entrada = entry1.get()
    try:
        lado = float(entrada)
        area = lado ** 2
        perimetro = 4 * lado
        label_resultado.configure(text=f"Área do quadrado: {area:.2f} - Perímetro do quadrado: {perimetro:.2f}")
    except ValueError:
        label_resultado.configure(text="Entrada inválida. Por favor, insira um número válido.")

def area_perimetro_ret():
    entrada = entry1.get()
    try:
        lista = list(map(float, entrada.split()))
        if len(lista) == 2:
            largura, altura = lista
            area = largura * altura
            perimetro = 2 * (largura + altura)
            label_resultado.configure(text=f"Área do retângulo: {area:.2f} - Perímetro do retângulo: {perimetro:.2f}")
        else:
            label_resultado.configure(text="Por favor, insira dois valores (largura e altura).")
    except ValueError:
        label_resultado.configure(text="Entrada inválida. Por favor, insira números válidos.")

def area_perimetro_tri():
    entrada = entry1.get()
    try:
        lista = list(map(float, entrada.split()))
        if len(lista) == 2:
            base, altura = lista
            area = 0.5 * base * altura
            hipotenusa = math.sqrt(base**2 + altura**2)
            perimetro = base + altura + hipotenusa
            label_resultado.configure(text=f"Área do triângulo: {area:.2f} - Perímetro do triângulo: {perimetro:.2f}")
        else:
            label_resultado.configure(text="Por favor, insira base e altura separados por um espaço: ")
    except ValueError:
        label_resultado.configure(text="Entrada inválida. Por favor, insira números válidos.")

def area_perimetro_circ():
    entrada = entry1.get()
    try:
        raio = float(entrada)
        area = math.pi * raio ** 2
        perimetro = 2 * math.pi * raio
        label_resultado.configure(text=f"Área do círculo: {area:.2f} - Perímetro do círculo: {perimetro:.2f}")
    except ValueError:
        label_resultado.configure(text="Entrada inválida. Por favor, insira o raio do circulo ou um número válido.")

def area_perimetro_trap():
    entrada = entry1.get()
    try:
        lista = list(map(float, entrada.split()))
        if len(lista) == 3 and lista[0] > lista[1]:
            base_maior, base_menor, altura = lista
            area = 0.5 * (base_maior + base_menor) * altura
            lado_obliquo = math.sqrt(((base_maior - base_menor) / 2)**2 + altura**2)
            perimetro = base_maior + base_menor + 2 * lado_obliquo

            label_resultado.configure(text=f"Área do trapézio: {area:.2f} - Perímetro do trapézio: {perimetro:.2f}")
        else:
            label_resultado.configure(text="Insira a base maior, a menor e a altura, separados por um espaço: ")
    except ValueError:
        label_resultado.configure(text="Entrada inválida. Por favor, insira números válidos.")

# ---- Volumes de Sólidos ----
def volume_cilindro():
    entrada = entry1.get()
    try:
        lista = list(map(float, entrada.split()))
        if len(lista) == 2:
            raio, altura = lista
            volume = math.pi * raio ** 2 * altura
            label_resultado.configure(text=f"Volume do cilindro: {volume:.2f}")
        else:
            label_resultado.configure(text="Por favor, insira dois valores (raio e altura).")
    except ValueError:
        label_resultado.configure(text="Entrada inválida. Por favor, insira números válidos.")

def volume_cubo():
    entrada = entry1.get() 
    try:
        aresta = float(entrada)
        if aresta < 0:
            label_resultado.configure(text="A aresta deve ser um número não negativo.")
        else:
            volume = aresta ** 3
            label_resultado.configure(text=f"Volume do cubo: {volume}")
    except ValueError:
        label_resultado.configure(text="Entrada inválida. Por favor, insira um número válido.")

def volume_paralelepipedo():
    entrada = entry1.get()
    try:
        lista = list(map(float, entrada.split()))
        if len(lista) == 3:
            comprimento, largura, altura = lista
            volume = comprimento * largura * altura
            label_resultado.configure(text=f"Volume do paralelepípedo: {volume}")
        else:
            label_resultado.configure(text="Por favor, insira três valores (comprimento, largura e altura).")
    except ValueError:
        label_resultado.configure(text="Entrada inválida. Por favor, insira números válidos.")

def volume_esfera():
    entrada = entry1.get()
    try:
        raio = float(entrada)
        if raio < 0:
            label_resultado.configure(text="O raio deve ser um número não negativo.")
        else:
            volume = (4/3) * math.pi * raio ** 3
            label_resultado.configure(text=f"Volume da esfera: {volume}")
    except ValueError:
        label_resultado.configure(text="Entrada inválida. Por favor, insira um número válido.")

def volume_piramide():
    entrada = entry1.get()
    try:
        lista = list(map(float, entrada.split()))
        if len(lista) == 2:
            area_base, altura = lista
            volume = (1/3) * area_base * altura
            label_resultado.configure(text=f"Volume da pirâmide: {volume:.2f}")
        else:
            label_resultado.configure(text="Por favor, insira dois valores (área da base e altura).")
    except ValueError:
        label_resultado.configure(text="Entrada inválida. Por favor, insira números válidos.")

def volume_prisma():
    entrada = entry1.get()
    try:
        lista = list(map(float, entrada.split()))
        if len(lista) == 2:
            area_base, altura = lista
            volume = area_base * altura
            label_resultado.configure(text=f"Volume do prisma: {volume}")
        else:
            label_resultado.configure(text="Por favor, insira dois valores (área da base e altura).")
    except ValueError:
        label_resultado.configure(text="Entrada inválida. Por favor, insira números válidos.")



# ---- Equações ---- 

# ---- Conversão de Medidas ---- 

# ---- Conversão de Volumes ----
def litro_para_mililitros():
    entrada = entry1.get()
    try:
        litros = float(entrada)
        mililitros = litros * 1000
        label_resultado.configure(text= f"{litros:.2f} litros é igual a {mililitros:.2f} mililitros.")
    except ValueError:
        label_resultado.configure(text="Entrada inválida. Por favor, insira números válidos.")

# ---- Porcentagem ---- 

# ---- Estatística Básica ----


# === Escolha de categoria ===
def atualizar_opcoes(opcao_inicial):
    if opcao_inicial == "Selecionar Opção":
        menu_calculo2.configure(values=[], command=None)
        esconder_entradas()
    elif opcao_inicial == "Operações Aritméticas":
        menu_calculo2.configure(values=["Adição", "Subtração", "Multiplicação", "Divisão", "Radiciação", "Potenciação"], command=atualizar_calculo)
        menu_calculo2.set("Selecionar Opção")
        mostrar_entradas()
    elif opcao_inicial == "Área e Perímetro":
        menu_calculo2.configure(values=["Quadrado", "Retangulo", "Triangulo", "Circulo", "Trapézio"], command=atualizar_calculo)
        menu_calculo2.set("Selecionar Opção")
        mostrar_entradas()
    elif opcao_inicial == "Volumes de Sólidos":
        menu_calculo2.configure(values=["Cilindro", "Cubo", "Paralelepípedo", "Esfera", "Pirâmide", "Prisma"], command=atualizar_calculo)
        menu_calculo2.set("Selecionar Opção")
        mostrar_entradas()
    elif opcao_inicial == "Equações":
        menu_calculo2.configure(values=["Primeiro Grau", "Segundo Grau"], command=atualizar_calculo)
        menu_calculo2.set("Selecionar Opção")
        mostrar_entradas()
    elif opcao_inicial == "Conversão de Medidas":
        menu_calculo2.configure(values=[], command=atualizar_calculo)
        menu_calculo2.set("Selecionar Opção")
        mostrar_entradas()
    elif opcao_inicial == "Conversão de Volumes":
        menu_calculo2.configure(values=["Litros para Mililitros"], command=atualizar_calculo)
        menu_calculo2.set("Selecionar Opção")
        mostrar_entradas()
    elif opcao_inicial == "Porcentagem":
        menu_calculo2.configure(values=[], command=atualizar_calculo)
        menu_calculo2.set("Selecionar Opção")
        mostrar_entradas()
    elif opcao_inicial == "Estatística Básica":
        menu_calculo2.configure(values=[], command=atualizar_calculo)
        menu_calculo2.set("Selecionar Opção")
        mostrar_entradas()

# ----------------- ADICIONAR -----------------------

# === Calculo especifico de acordo com a categoria===
def atualizar_calculo(tipo_calculo):
    if tipo_calculo == "Adição":
        botao_calcular.configure(command=adicao)
        mostrar_entradas(tipo_calculo)
    elif tipo_calculo == "Subtração":
        botao_calcular.configure(command=subtracao)
        mostrar_entradas(tipo_calculo)
    elif tipo_calculo == "Multiplicação":
        botao_calcular.configure(command=multiplicacao)
        mostrar_entradas(tipo_calculo)
    elif tipo_calculo == "Divisão":
        botao_calcular.configure(command=divisao)
        mostrar_entradas(tipo_calculo)
    elif tipo_calculo == "Radiciação":
        botao_calcular.configure(command=radiciacao)
        mostrar_entradas(tipo_calculo)
    elif tipo_calculo == "Potenciação":
        botao_calcular.configure(command=potenciacao)
        mostrar_entradas(tipo_calculo)
# ----------
    elif tipo_calculo == "Quadrado":
        botao_calcular.configure(command=area_perimetro_quad)
        mostrar_entradas(tipo_calculo)
    elif tipo_calculo == "Retangulo":
        botao_calcular.configure(command=area_perimetro_ret)
        mostrar_entradas(tipo_calculo)
    elif tipo_calculo == "Triangulo":
        botao_calcular.configure(command=area_perimetro_tri)
        mostrar_entradas(tipo_calculo)
    elif tipo_calculo == "Circulo":
        botao_calcular.configure(command=area_perimetro_circ)
        mostrar_entradas(tipo_calculo)
    elif tipo_calculo == "Trapézio":
        botao_calcular.configure(command=area_perimetro_trap)
        mostrar_entradas(tipo_calculo)
# ----------
    elif tipo_calculo == "Cilindro":
        botao_calcular.configure(command=volume_cilindro)
        mostrar_entradas(tipo_calculo)
    elif tipo_calculo == "Cubo":
        botao_calcular.configure(command=volume_cubo)
        mostrar_entradas(tipo_calculo)
    elif tipo_calculo == "Paralelepípedo":
        botao_calcular.configure(command=volume_paralelepipedo)
        mostrar_entradas(tipo_calculo)
    elif tipo_calculo == "Esfera":
        botao_calcular.configure(command=volume_esfera)
        mostrar_entradas(tipo_calculo)
    elif tipo_calculo == "Pirâmide":
        botao_calcular.configure(command=volume_piramide)
        mostrar_entradas(tipo_calculo)
    elif tipo_calculo == "Prisma":
        botao_calcular.configure(command=volume_prisma)
        mostrar_entradas(tipo_calculo)

# ------
    elif tipo_calculo == "Litros para Mililitros":
        botao_calcular.configure(command=litro_para_mililitros)
        mostrar_entradas(tipo_calculo)


# ----------------- ADICIONAR -----------------------

# === Mostrar ou esconder entradas de acordo com a escolha de cálculo ===
def mostrar_entradas(tipo_calculo=None):
        entry1.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
def esconder_entradas():
    entry1.grid_forget()

# === Criando janela principal ===
app = ctk.CTk()
app.geometry("400x400")
app.title("Calculadora Multifuncional")

# === Configurando grid responsivo ===
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)

# Primeira escolha: categorias de cálculos
label1 = ctk.CTkLabel(app, text="Escolha uma categoria")
label1.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
menu_calculo1 = ctk.CTkOptionMenu(app, values=["Selecionar Opção", "Operações Aritméticas", "Área e Perímetro", "Volumes de Sólidos", 
"Equações", "Conversão de Medidas", "Conversão de Volumes", "Porcentagem", "Estatística Básica"], command=atualizar_opcoes) #---------- ADICIONAR CATEGORIA----------
menu_calculo1.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Segunda escolha: tipo de cálculo dentro da categoria
label2 = ctk.CTkLabel(app, text="Escolha o cálculo específico")
label2.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
menu_calculo2 = ctk.CTkOptionMenu(app, values=[])
menu_calculo2.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
# Definir o valor inicial "Escolha a categoria"
menu_calculo2.set("Selecionar Opção")
# Área de entrada de valores
entry1 = ctk.CTkEntry(app)
# Botão para calcular
botao_calcular = ctk.CTkButton(app, text="Calcular")
botao_calcular.grid(row=6, column=0, columnspan=2, padx=10, pady=10)
# Exibe o resultado
label_resultado = ctk.CTkLabel(app, text=None)
label_resultado.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

# Iniciar a aplicação
app.mainloop()
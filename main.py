import customtkinter as ctk
import math

# === Configurando tema ===
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

# === Funções de cálculo ===

# ---- Operações Aritméticas ----
def adicao():
    try:
        entrada = entry1.get()
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
    try:
        entrada = entry1.get()
        lista = list(map(float, entrada.split('x')))
        if len(lista) > 0:
            mult = 1
            for n in lista:
                mult *= n
            label_resultado.configure(text=f"Resultado da multiplicação: {mult}")
    except ValueError:
        label_resultado.configure(text='Entrada inválida. Por favor, insira "x" ou um número válido.')

def divisao():
    try:
        entrada = entry1.get()
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
    try:
        entrada = entry1.get()
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
    try:
        entrada = entry1.get()
        lado = float(entrada)
        area = lado ** 2
        perimetro = 4 * lado
        label_resultado.configure(text=f"Área do quadrado: {area} - Perímetro do quadrado: {perimetro}")
    except ValueError:
        label_resultado.configure(text="Entrada inválida. Por favor, insira um número válido.")

def area_perimetro_ret():
    try:
        entrada = entry1.get()
        lista = list(map(float, entrada.split()))
        if len(lista) == 2:
            largura, altura = lista
            area = largura * altura
            perimetro = 2 * (largura + altura)
            label_resultado.configure(text=f"Área do retângulo: {area} - Perímetro do retângulo: {perimetro}")
        else:
            label_resultado.configure(text="Por favor, insira dois valores (largura e altura).")
    except ValueError:
        label_resultado.configure(text="Entrada inválida. Por favor, insira números válidos.")

def area_perimetro_tri():
    try:
        entrada = entry1.get()
        lista = list(map(float, entrada.split()))
        if len(lista) == 2:
            base, altura = lista
            area = 0.5 * base * altura
            hipotenusa = math.sqrt(base**2 + altura**2)
            perimetro = base + altura + hipotenusa
            label_resultado.configure(text=f"Área do triângulo: {area} - Perímetro do triângulo: {perimetro}")
        else:
            label_resultado.configure(text="Por favor, insira base e altura separados por um espaço: ")
    except ValueError:
        label_resultado.configure(text="Entrada inválida. Por favor, insira números válidos.")

def area_perimetro_circ():
    try:
        entrada = entry1.get()
        raio = float(entrada)
        area = math.pi * raio ** 2
        perimetro = 2 * math.pi * raio
        label_resultado.configure(text=f"Área do círculo: {area} - Perímetro do círculo: {perimetro}")
    except ValueError:
        label_resultado.configure(text="Entrada inválida. Por favor, insira o raio do circulo ou um número válido.")

def area_perimetro_trap():
    try:
        entrada = entry1.get()
        lista = list(map(float, entrada.split()))
        if len(lista) == 3 and lista[0] > lista[1]:
            base_maior, base_menor, altura = lista
            area = 0.5 * (base_maior + base_menor) * altura
            lado_obliquo = math.sqrt(((base_maior - base_menor) / 2)**2 + altura**2)
            perimetro = base_maior + base_menor + 2 * lado_obliquo

            label_resultado.configure(text=f"Área do trapézio: {area} - Perímetro do trapézio: {perimetro}")
        else:
            label_resultado.configure(text="Insira a base maior, a menor e a altura, separados por um espaço: ")
    except ValueError:
        label_resultado.configure(text="Entrada inválida. Por favor, insira números válidos.")

# ---- Volumes de Sólidos ----
def volume_cilindro():
    try:
        entrada = entry1.get()
        lista = list(map(float, entrada.split()))
        if len(lista) == 2:
            raio, altura = lista
            volume = math.pi * raio ** 2 * altura
            label_resultado.configure(text=f"Volume do cilindro: {volume}")
        else:
            label_resultado.configure(text="Por favor, insira dois valores (raio e altura).")
    except ValueError:
        label_resultado.configure(text="Entrada inválida. Por favor, insira números válidos.")

def volume_cubo():
    try:
        entrada = entry1.get() 
        aresta = float(entrada)
        if aresta < 0:
            label_resultado.configure(text="A aresta deve ser um número não negativo.")
        else:
            volume = aresta ** 3
            label_resultado.configure(text=f"Volume do cubo: {volume}")
    except ValueError:
        label_resultado.configure(text="Entrada inválida. Por favor, insira um número válido.")

def volume_paralelepipedo():
    try:
        entrada = entry1.get()
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
    try:
        entrada = entry1.get()
        raio = float(entrada)
        if raio < 0:
            label_resultado.configure(text="O raio deve ser um número não negativo.")
        else:
            volume = (4/3) * math.pi * raio ** 3
            label_resultado.configure(text=f"Volume da esfera: {volume}")
    except ValueError:
        label_resultado.configure(text="Entrada inválida. Por favor, insira um número válido.")

def volume_piramide():
    try:
        entrada = entry1.get()
        lista = list(map(float, entrada.split()))
        if len(lista) == 2:
            area_base, altura = lista
            volume = (1/3) * area_base * altura
            label_resultado.configure(text=f"Volume da pirâmide: {volume}")
        else:
            label_resultado.configure(text="Por favor, insira dois valores (área da base e altura).")
    except ValueError:
        label_resultado.configure(text="Entrada inválida. Por favor, insira números válidos.")

def volume_prisma():
    try:
        entrada = entry1.get()
        lista = list(map(float, entrada.split()))
        if len(lista) == 2:
            area_base, altura = lista
            volume = area_base * altura
            label_resultado.configure(text=f"Volume do prisma: {volume}")
        else:
            label_resultado.configure(text="Por favor, insira dois valores (área da base e altura).")
    except ValueError:
        label_resultado.configure(text="Entrada inválida. Por favor, insira números válidos.")

def volume_cone():
    try:
        entrada = entry1.get()
        lista = list(map(float, entrada.split()))
        if len(lista) == 2:
            raio, altura = lista
            volume = (1/3) * math.pi * raio ** 2 * altura
            label_resultado.configure(text=f"Volume do cone: {volume}")
        else:
            label_resultado.configure(text="Por favor, insira dois valores (raio e altura).")
    except ValueError:
        label_resultado.configure(text="Entrada inválida. Por favor, insira números válidos.")

# ---- Equações ---- 
def primeira_equacao():
    try:
        entrada = entry1.get()
        lista = list(map(float, entrada.split()))
        if len(lista) == 2:
            a, b = lista
            if a != 0:
                x = -b / a
                label_resultado.configure(text=f"Resultado: x = {x}")
            else:
                label_resultado.configure(text="O coeficiente 'a' não pode ser zero.")
        else:
            label_resultado.configure(text="Por favor, insira dois valores (coeficiente a e coeficiente b).")
    except ValueError:
        label_resultado.configure(text="Entrada inválida. Por favor, insira números válidos.")

def segunda_equacao():
    try:
        entrada = entry1.get()
        lista = list(map(float, entrada.split()))
        if len(lista) == 3:
            a, b, c = lista
            delta = b**2 - 4*a*c
            
            if delta > 0:
                x1 = (-b + math.sqrt(delta)) / (2 * a)
                x2 = (-b - math.sqrt(delta)) / (2 * a)
                label_resultado.configure(text=f"Soluções da equação do 2º grau: x¹ = {x1}, x² = {x2}")
            elif delta == 0:
                x = -b / (2 * a)
                label_resultado.configure(text=f"Solução da equação do 2º grau: x = {x}")
            else:
                label_resultado.configure(text="A equação não possui raízes reais.")
        else:
            label_resultado.configure(text="Por favor, insira três valores (coeficientes a, b e c).")
    except ValueError:
        label_resultado.configure(text="Entrada inválida. Por favor, insira números válidos.")

# ---- Conversão de Medidas ---- 
def m_para_cm():
    try:
        entrada = entry1.get()
        metros = float(entrada)
        centimetros = metros * 100
        label_resultado.configure(text=f"{metros} m é igual a {centimetros} cm.")
    except ValueError:
        label_resultado.configure(text="Entrada inválida. Por favor, insira números válidos.")

def cm_para_m():
    try:
        entrada = entry1.get()
        centimetros = float(entrada)
        metros = centimetros / 100
        label_resultado.configure(text=f"{centimetros} cm é igual a {metros} m.")
    except ValueError:
        label_resultado.configure(text="Entrada inválida. Por favor, insira números válidos.")

def m_para_mm():
    try:
        entrada = entry1.get()
        metros = float(entrada)
        milimetros = metros * 1000
        label_resultado.configure(text=f"{metros} m é igual a {milimetros} mm.")
    except ValueError:
        label_resultado.configure(text="Entrada inválida. Por favor, insira números válidos.")

def mm_para_m():
    try:
        entrada = entry1.get()
        milimetros = float(entrada)
        metros = milimetros / 1000
        label_resultado.configure(text=f"{milimetros} mm é igual a {metros} m.")
    except ValueError:
        label_resultado.configure(text="Entrada inválida. Por favor, insira números válidos.")

def km_para_m():
    try:
        entrada = entry1.get()
        quilometros = float(entrada)
        metros = quilometros * 1000
        label_resultado.configure(text=f"{quilometros} km é igual a {metros} m.")
    except ValueError:
        label_resultado.configure(text="Entrada inválida. Por favor, insira números válidos.")

def m_para_km():
    try:
        entrada = entry1.get()
        metros = float(entrada)
        quilometros = metros / 1000
        label_resultado.configure(text=f"{metros} m é igual a {quilometros} km.")
    except ValueError:
        label_resultado.configure(text="Entrada inválida. Por favor, insira números válidos.")

# ---- Conversão de Volumes ----
def l_para_ml():
    try:
        entrada = entry1.get()
        litros = float(entrada)
        mililitros = litros * 1000
        label_resultado.configure(text= f"{litros} litros é igual a {mililitros} mililitros.")
    except ValueError:
        label_resultado.configure(text="Entrada inválida. Por favor, insira números válidos.")

def ml_para_l():
    try:
        entrada = entry1.get()
        mililitros = float(entrada)
        litros = mililitros / 1000
        label_resultado.configure(text=f"{mililitros} mililitros é igual a {litros} litros.")
    except ValueError:
        label_resultado.configure(text="Entrada inválida. Por favor, insira números válidos.")

def metros_cubicos_para_l():
    try:
        entrada = entry1.get()
        metros_cubicos = float(entrada)
        litros = metros_cubicos * 1000
        label_resultado.configure(text=f"{metros_cubicos} metros cúbicos é igual a {litros} litros.")
    except ValueError:
        label_resultado.configure(text="Entrada inválida. Por favor, insira números válidos.")

def l_para_metros_cubicos():
    try:
        entrada = entry1.get()
        litros = float(entrada)
        metros_cubicos = litros / 1000
        label_resultado.configure(text=f"{litros} litros é igual a {metros_cubicos} metros cúbicos.")
    except ValueError:
        label_resultado.configure(text="Entrada inválida. Por favor, insira números válidos.")

# ---- Porcentagem ---- 
def aumento():
    try:
        entrada = float(entry1.get())
        aumento = float(entry2.get())
        resultado = entrada * (1 + aumento / 100)
        label_resultado.configure(text=f"Valor com aumento: {resultado}")
    except ValueError:
        label_resultado.configure(text="Entrada inválida. Por favor, insira primeiro números válidos.")

def diminuição():
    try:
        entrada = float(entry1.get())
        diminuicao = float(entry2.get())
        diminuicao = float(entrada)
        resultado = entrada * (1 - diminuicao / 100)
        label_resultado.configure(text=f"Valor com diminuição: {resultado}")
    except ValueError:
        label_resultado.configure(text="Entrada inválida. Por favor, insira números válidos.")

def porcentagem():
    try:
        entrada = float(entry1.get())
        porcentagem = float(entry2.get())
        resultado = entrada * (porcentagem / 100)
        label_resultado.configure(text=f"O valor da porcentagem é: {resultado}")
    except ValueError:
        label_resultado.configure(text="Entrada inválida. Por favor, insira números válidos.")

# ---- Estatística Básica ----
def media():
    try:
        entrada = entry1.get()
        numeros = list(map(float, entrada.split()))
        media = sum(numeros) / len(numeros)
        label_resultado.configure(text=f"A média dos números é: {media}")
    except ValueError:
        label_resultado.configure(text="Entrada inválida. Por favor, insira números válidos.")

def mediana():
    try:
        entrada = entry1.get()
        numeros = list(map(float, entrada.split()))
        numeros.sort()
        meio = len(numeros) // 2
        if len(numeros) % 2 == 0:
            mediana = (numeros[meio - 1] + numeros[meio]) / 2
        else:
            mediana = numeros[meio]
        label_resultado.configure(text=f"A mediana dos números é: {mediana}")
    except ValueError:
        label_resultado.configure(text="Entrada inválida. Por favor, insira números válidos.")

def moda():
    try:
        entrada = entry1.get()
        numeros = list(map(float, entrada.split()))
        contagem = {num: numeros.count(num) for num in set(numeros)}
        moda = [num for num, count in contagem.items() if count == max(contagem.values())]
        if len(moda) == len(numeros):
            label_resultado.configure(text="Não há moda.")
        else:
            label_resultado.configure(text=f"A moda dos números é: {', '.join(map(str, moda))}")
    except ValueError:
        label_resultado.configure(text="Entrada inválida. Por favor, insira números válidos.")

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
        menu_calculo2.configure(values=["Cilindro", "Cubo", "Paralelepípedo", "Esfera", "Pirâmide", "Prisma", "Cone"], command=atualizar_calculo)
        menu_calculo2.set("Selecionar Opção")
        mostrar_entradas()
    elif opcao_inicial == "Equações":
        menu_calculo2.configure(values=["Primeiro Grau", "Segundo Grau"], command=atualizar_calculo)
        menu_calculo2.set("Selecionar Opção")
        mostrar_entradas()
    elif opcao_inicial == "Conversão de Medidas":
        menu_calculo2.configure(values=["Metros -> Centimetros", "Centimetros -> Metros", "Metros -> milimetros", 
"Milimetros -> Metros", "Quilometros -> Metros", "Metros -> Quilometros"], command=atualizar_calculo)
        menu_calculo2.set("Selecionar Opção")
        mostrar_entradas()
    elif opcao_inicial == "Conversão de Volumes":
        menu_calculo2.configure(values=["Litros -> Mililitros", "Mililitros -> Litros", "Metros Cubicos -> Litros", "Litros -> Metros Cubidos"], command=atualizar_calculo)
        menu_calculo2.set("Selecionar Opção")
        mostrar_entradas()
    elif opcao_inicial == "Porcentagem":
        menu_calculo2.configure(values=["Percentual de Aumento","Percentual de Redução", "Encontrar Porcentagem"], command=atualizar_calculo)
        menu_calculo2.set("Selecionar Opção")
        mostrar_entradas()
    elif opcao_inicial == "Estatística Básica":
        menu_calculo2.configure(values=["Média", "Mediana", "Moda"], command=atualizar_calculo)
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
    elif tipo_calculo == "Cone":
        botao_calcular.configure(command=volume_cone)
        mostrar_entradas(tipo_calculo)
# ----------
    elif tipo_calculo == "Primeiro Grau":
        botao_calcular.configure(command=primeira_equacao)
        mostrar_entradas(tipo_calculo)
    elif tipo_calculo == "Segundo Grau":
        botao_calcular.configure(command=segunda_equacao)
        mostrar_entradas(tipo_calculo)
# ----------
    elif tipo_calculo == "Metros -> Centimetros":
        botao_calcular.configure(command=m_para_cm)
        mostrar_entradas(tipo_calculo)
    elif tipo_calculo == "Centimetros -> Metros":
        botao_calcular.configure(command=cm_para_m)
        mostrar_entradas(tipo_calculo)
    elif tipo_calculo == "Metros -> milimetros":
        botao_calcular.configure(command=m_para_mm)
        mostrar_entradas(tipo_calculo)
    elif tipo_calculo == "Milimetros -> Metros":
        botao_calcular.configure(command=mm_para_m)
        mostrar_entradas(tipo_calculo)
    elif tipo_calculo == "Quilometros -> Metros":
        botao_calcular.configure(command=km_para_m)
        mostrar_entradas(tipo_calculo)
    elif tipo_calculo == "Metros -> Quilometros":
        botao_calcular.configure(command=m_para_km)
        mostrar_entradas(tipo_calculo)
# ----------
    elif tipo_calculo == "Litros para Mililitros":
        botao_calcular.configure(command=l_para_ml)
        mostrar_entradas(tipo_calculo)
    elif tipo_calculo == "Mililitros -> Litros":
        botao_calcular.configure(command=ml_para_l) # , 
        mostrar_entradas(tipo_calculo)
    elif tipo_calculo == "Metros Cubicos -> Litros":
        botao_calcular.configure(command=metros_cubicos_para_l)
        mostrar_entradas(tipo_calculo)
    elif tipo_calculo == "Litros -> Metros Cubidos":
        botao_calcular.configure(command=l_para_metros_cubicos)
        mostrar_entradas(tipo_calculo)
# ----------
    elif tipo_calculo == "Percentual de Aumento":
        botao_calcular.configure(command=aumento)
        mostrar_entradas(tipo_calculo)
    elif tipo_calculo == "Percentual de Redução":
        botao_calcular.configure(command=diminuição)
        mostrar_entradas(tipo_calculo)
    elif tipo_calculo == "Encontrar Porcentagem":
        botao_calcular.configure(command=porcentagem)
        mostrar_entradas(tipo_calculo)
# ----------
    elif tipo_calculo == "Média":
        botao_calcular.configure(command=media)
        mostrar_entradas(tipo_calculo)
    elif tipo_calculo == "Mediana":
        botao_calcular.configure(command=mediana)
        mostrar_entradas(tipo_calculo)
    elif tipo_calculo == "Moda":
        botao_calcular.configure(command=moda)
        mostrar_entradas(tipo_calculo)

# ----------------- ADICIONAR -----------------------

# === Mostrar ou esconder entradas de acordo com a escolha de cálculo ===
def mostrar_entradas(tipo_calculo=None):
    if tipo_calculo in ["Percentual de Aumento","Percentual de Redução","Encontrar Porcentagem"]:
        entry1.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
        entry2.grid(row=5, column=0, columnspan=2, padx=10, pady=10)
    else:
        entry1.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
        entry2.grid_forget()
def esconder_entradas():
    entry1.grid_forget()
    entry2.grid_forget()


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
entry2 = ctk.CTkEntry(app)
# Botão para calcular
botao_calcular = ctk.CTkButton(app, text="Calcular")
botao_calcular.grid(row=6, column=0, columnspan=2, padx=10, pady=10)
# Exibe o resultado
label_resultado = ctk.CTkLabel(app, text=None)
label_resultado.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

# Iniciar a aplicação
app.mainloop()
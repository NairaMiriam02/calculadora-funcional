#-----------------------------------------------------------
print('''     
============================
   Calculadora Matemática  
============================

> Qual funcionalidade deseja usar?

[1] Operações Matemáticas
[2] Áreas e Perímetros
[3] Volumes de Sólidos
[4] Equações
[5] Conversão de Medidas
[6] Conversão de Volumes
[7] Porcentagem
''')
escolha = int(input('''
Digite uma opção:
>>> '''))
#-------------------------------------------------------------
if escolha == 1:
    print('''
> Qual operação matemática irá usar?

[1] Adição
[2] Subtração
[3] Multiplicação
[4] Divisão
[5] Radiciação
[6] Potenciação
''')
#-----------------------------------------------------------------------
    escolha = int(input(">>> "))
    if escolha == 1:
        soma = 0
        while True:
            n = float(input('''
Digite o valor a ser somado ou [0] para Parar:
>>> '''))
            if n != 0:
                soma += n
            else:
                print(f"Soma total: {soma:.2f}")
                break
#-----------------------------------------------------------------------
    elif escolha == 2:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        print(f"Resultado da subtração: {num1 - num2:.2f}")
#-----------------------------------------------------------------------
    elif escolha == 3:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        print(f"Resultado da multiplicação: {num1 * num2:.2f}")
#-----------------------------------------------------------------------
    elif escolha == 4:
        num1 = float(input("Digite o dividendo: "))
        num2 = float(input("Digite o divisor: "))
#-----------------------------------------------------------------------
        if num2 != 0:
            print(f"Resultado da divisão: {num1 / num2:.2f}")
        else:
            print("Divisão por zero não é permitida.")
#-----------------------------------------------------------------------
    elif escolha == 5:
        import math
        num = float(input("Digite o número: "))
        raiz = math.sqrt(num)
        print(f"Raiz quadrada de {num}: {raiz:.2f}")
#-----------------------------------------------------------------------
    elif escolha == 6:
        base = float(input("Digite a base: "))
        expoente = float(input("Digite o expoente: "))
        resultado = base ** expoente
        print(f"{base} elevado a {expoente}: {resultado:.2f}")
    else:
        print("Opção inválida.")
#----------------------------------------------------------------
elif escolha == 2:
    print('''
> Qual polígono irá usar?

[1] Quadrado
[2] Retângulo
[3] Triângulo
[4] Círculo
[5] Trapézio
[6] Paralelogramo
''')
    escolha = int(input(">>> "))
#-----------------------------------------------------------------------
    if escolha == 1:
        lado = float(input("Digite o comprimento do lado: "))
        area = lado ** 2
        perimetro = 4 * lado
        print(f"Área do quadrado: {area:.2f}")
        print(f"Perímetro do quadrado: {perimetro:.2f}")
#-----------------------------------------------------------------------
    elif escolha == 2:
        largura = float(input("Digite a largura: "))
        altura = float(input("Digite a altura: "))
        area = largura * altura
        perimetro = 2 * (largura + altura)
        print(f"Área do retângulo: {area:.2f}")
        print(f"Perímetro do retângulo: {perimetro:.2f}")
#-----------------------------------------------------------------------
    elif escolha == 3:
        base = float(input("Digite a base: "))
        altura = float(input("Digite a altura: "))
        area = 0.5 * base * altura
        print(f"Área do triângulo: {area:.2f}")
#-----------------------------------------------------------------------
    elif escolha == 4:
        import math
        raio = float(input("Digite o raio: "))
        area = math.pi * raio ** 2
        perimetro = 2 * math.pi * raio
        print(f"Área do círculo: {area:.2f}")
        print(f"Perímetro do círculo: {perimetro:.2f}")
#-----------------------------------------------------------------------
    elif escolha == 5:
        base_maior = float(input("Digite a base maior: "))
        base_menor = float(input("Digite a base menor: "))
        altura = float(input("Digite a altura: "))
        area = 0.5 * (base_maior + base_menor) * altura
        print(f"Área do trapézio: {area:.2f}")
#-----------------------------------------------------------------------
    elif escolha == 6:
        base = float(input("Digite a base: "))
        altura = float(input("Digite a altura: "))
        area = base * altura
        print(f"Área do paralelogramo: {area:.2f}")
    else:
        print("Opção inválida.")
#--------------------------------------------------------------------
elif escolha == 3:
    print('''
> Qual sólido irá usar?

[1] Cilindro
[2] Cubo
[3] Paralelepípedo
[4] Esfera
[5] Pirâmide
[6] Prisma
[7] Cone
''')
    escolha = int(input(">>> "))
#-----------------------------------------------------------------------
    import math
    if escolha == 1:
        raio = float(input("Digite o raio: "))
        altura = float(input("Digite a altura: "))
        volume = math.pi * raio ** 2 * altura
        print(f"Volume do cilindro: {volume:.2f}")
#-----------------------------------------------------------------------
    elif escolha == 2:
        aresta = float(input("Digite a aresta: "))
        volume = aresta ** 3
        print(f"Volume do cubo: {volume:.2f}")
#-----------------------------------------------------------------------
    elif escolha == 3:
        comprimento = float(input("Digite o comprimento: "))
        largura = float(input("Digite a largura: "))
        altura = float(input("Digite a altura: "))
        volume = comprimento * largura * altura
        print(f"Volume do paralelepípedo: {volume:.2f}")
#-----------------------------------------------------------------------
    elif escolha == 4:
        raio = float(input("Digite o raio: "))
        volume = (4/3) * math.pi * raio ** 3
        print(f"Volume da esfera: {volume:.2f}")
#-----------------------------------------------------------------------
    elif escolha == 5:
        import math
        base_area = float(input("Digite a área da base: "))
        altura = float(input("Digite a altura: "))
        volume = (1/3) * base_area * altura
        print(f"Volume da pirâmide: {volume:.2f}")
#-----------------------------------------------------------------------
    elif escolha == 6:
        base_area = float(input("Digite a área da base: "))
        altura = float(input("Digite a altura: "))
        volume = base_area * altura
        print(f"Volume do prisma: {volume:.2f}")
#-----------------------------------------------------------------------
    elif escolha == 7:
        raio = float(input("Digite o raio da base: "))
        altura = float(input("Digite a altura: "))
        volume = (1/3) * math.pi * raio ** 2 * altura
        print(f"Volume do cone: {volume:.2f}")
    else:
        print("Opção inválida.")
#---------------------------------------------------------------------
elif escolha == 4:
    print('''
> Qual grau de equação deseja usar?
    
[1] Equação de 1º grau
[2] Equação de 2º grau
''')
    escolha = int(input(">>> "))
#-----------------------------------------------------------------------
    if escolha == 1:
        a = float(input("Digite o coeficiente a: "))
        b = float(input("Digite o coeficiente b: "))
        x = -b / a
        print(f"Solução da equação {a}x + {b} = 0: x = {x:.2f}")
#-----------------------------------------------------------------------
    elif escolha == 2:
        a = float(input("Digite o coeficiente a: "))
        b = float(input("Digite o coeficiente b: "))
        c = float(input("Digite o coeficiente c: "))
        delta = b ** 2 - 4 * a * c
        if delta > 0:
            x1 = (-b + math.sqrt(delta)) / (2 * a)
            x2 = (-b - math.sqrt(delta)) / (2 * a)
            print(f"Raízes da equação: x1 = {x1:.2f}, x2 = {x2:.2f}")
        elif delta == 0:
            x = -b / (2 * a)
            print(f"Raiz da equação: x = {x:.2f}")
        else:
            print("A equação não possui raízes reais.")
    else:
        print("Opção inválida.")
#----------------------------------------------------------------------
elif escolha == 5:
    print('''
> Qual medida deseja converter?

[1] Quilômetro (km) > > > Metro (m)
[2] Metro (m) > > > Quilômetro (km)
[3] Centímetro( cm) > > > Metro (m)
[4] Metro (m) > > > Centímetro (cm)
[5] Milímetro (mm) > > > Centímetro (cm)
[6] Centímetro (cm) > > > Milímetro (mm)
''')
    escolha = int(input(">>> "))
#-----------------------------------------------------------------------
    if escolha == 1:
        km = float(input("Digite a distância em quilômetros: "))
        metros = km * 1000
        print(f"{km} km é igual a {metros:.2f} m")
#-----------------------------------------------------------------------
    elif escolha == 2:
        metros = float(input("Digite a distância em metros: "))
        km = metros / 1000
        print(f"{metros} m é igual a {km:.2f} km")
#-----------------------------------------------------------------------
    elif escolha == 3:
        cm = float(input("Digite a medida em centímetros: "))
        metros = cm / 100
        print(f"{cm} cm é igual a {metros:.2f} m")
#-----------------------------------------------------------------------
    elif escolha == 4:
        metros = float(input("Digite a medida em metros: "))
        cm = metros * 100
        print(f"{metros} m é igual a {cm:.2f} cm")
#-----------------------------------------------------------------------
    elif escolha == 5:
        mm = float(input("Digite a medida em milímetros: "))
        cm = mm / 10
        print(f"{mm} mm é igual a {cm:.2f} cm")
#-----------------------------------------------------------------------
    elif escolha == 6:
        cm = float(input("Digite a medida em centímetros: "))
        mm = cm * 10
        print(f"{cm} cm é igual a {mm:.2f} mm")
    else:
        print("Opção inválida.")
#----------------------------------------------------------------------
elif escolha == 6:
    print('''
> Qual volume deseja converter?

[1] Quilômetro cúbico (km³) > > > Metro cúbico (m³)
[2] Metro cúbico (m³) > > > Quilômetro cúbico (km³)
[3] Centímetro cúbico (cm³) > > > Metro cúbico (m³)
[4] Metro cúbico (m³) > > > Centímetro cúbico (cm³)
[5] Milímetro cúbico (mm³) > > > Centímetro cúbico (cm³)
[6] Centímetro cúbico (cm³) > > > Milímetro cúbico (mm³)
''')
    escolha = int(input(">>> "))
#-----------------------------------------------------------------------
    if escolha == 1:
        km3 = float(input("Digite o volume em quilômetros cúbicos: "))
        m3 = km3 * 1e9
        print(f"{km3} km³ é igual a {m3:.2f} m³")
#-----------------------------------------------------------------------
    elif escolha == 2:
        m3 = float(input("Digite o volume em metros cúbicos: "))
        km3 = m3 / 1e9
        print(f"{m3} m³ é igual a {km3:.2f} km³")
#-----------------------------------------------------------------------
    elif escolha == 3:
        cm3 = float(input("Digite o volume em centímetros cúbicos: "))
        m3 = cm3 / 1e6
        print(f"{cm3} cm³ é igual a {m3:.2f} m³")
#-----------------------------------------------------------------------
    elif escolha == 4:
        m3 = float(input("Digite o volume em metros cúbicos: "))
        cm3 = m3 * 1e6
        print(f"{m3} m³ é igual a {cm3:.2f} cm³")
#-----------------------------------------------------------------------
    elif escolha == 5:
        mm3 = float(input("Digite o volume em milímetros cúbicos: "))
        cm3 = mm3 / 1000
        print(f"{mm3} mm³ é igual a {cm3:.2f} cm³")
#-----------------------------------------------------------------------
    elif escolha == 6:
        cm3 = float(input("Digite o volume em centímetros cúbicos: "))
        mm3 = cm3 * 1000
        print(f"{cm3} cm³ é igual a {mm3:.2f} mm³")
    else:
        print("Opção inválida.")
#------------------------------------------------------------------
elif escolha == 7:
    valor = float(input("Digite o valor total: "))
    porcentagem = float(input("Digite a porcentagem sobre o total: "))
    resultado = valor * (porcentagem / 100)
    print(f"O valor de {porcentagem}% de {valor} é {resultado:.2f}")
#---------------------------------------------------------------------------
else:
    print("Escolha não disponível, tente novamente.")
#---------------------------------------------------------------------------

import math  # Importa o módulo math para funções matemáticas avançadas, como raiz quadrada e pi

# Exibe o cabeçalho do programa
print('''
==================
 Calculadora Escolar
==================
''')

# Inicia o loop principal do programa
while True:
    # Loop para garantir que a escolha do usuário seja um número inteiro válido
    while True:
        try:
            escolha = int(input('''
> Qual funcionalidade deseja usar?
[1] Operações Aritméticas
[2] Áreas e Perímetros
[3] Volumes de Sólidos
[4] Equações
[5] Conversão de Medidas
[6] Conversão de Volumes
[7] Porcentagem
[8] Estatística Básica
[0] Sair do programa
Digite uma opção:
>>> '''))
            break  # Sai do loop se a entrada for um número inteiro válido
        except ValueError:
            # Trata entradas que não são números inteiros
            print("Entrada inválida. Por favor, insira um número inteiro.")

    # Opção para operações aritméticas
    if escolha == 1:
        while True:
            try:
                operacao = int(input('''
> Qual operação matemática irá usar?
[1] Adição
[2] Subtração
[3] Multiplicação
[4] Divisão
[5] Radiciação
[6] Potenciação
>>> '''))
                break  # Sai do loop se a entrada for um número inteiro válido
            except ValueError:
                # Trata entradas que não são números inteiros
                print("Entrada inválida. Por favor, insira um número inteiro.")

        # Adição
        if operacao == 1:
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                # Exibe o resultado da adição
                print(f"Resultado da subtração: {num1 + num2:.2f}")
            except ValueError:
                # Trata entradas que não são números válidos
                print("Entrada inválida. Por favor, insira um número válido.")

        # Subtração
        elif operacao == 2:
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                # Exibe o resultado da subtração
                print(f"Resultado da subtração: {num1 - num2:.2f}")
            except ValueError:
                # Trata entradas que não são números válidos
                print("Entrada inválida. Por favor, insira um número válido.")

        # Multiplicação
        elif operacao == 3:
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                # Exibe o resultado da multiplicação
                print(f"Resultado da multiplicação: {num1 * num2:.2f}")
            except ValueError:
                # Trata entradas que não são números válidos
                print("Entrada inválida. Por favor, insira um número válido.")

        # Divisão
        elif operacao == 4:
            try:
                num1 = float(input("Digite o dividendo: "))
                num2 = float(input("Digite o divisor: "))
                if num2 != 0:
                    # Exibe o resultado da divisão
                    print(f"Resultado da divisão: {num1 / num2:.2f}")
                else:
                    # Trata a divisão por zero
                    print("Divisão por zero não é permitida.")
            except ValueError:
                # Trata entradas que não são números válidos
                print("Entrada inválida. Por favor, insira um número válido.")

        # Radiciação (raiz quadrada)
        elif operacao == 5:
            try:
                num = float(input("Digite o número: "))
                raiz = math.sqrt(num)  # Calcula a raiz quadrada
                # Exibe o resultado da radiciação
                print(f"Raiz quadrada de {num}: {raiz:.2f}")
            except ValueError:
                # Trata entradas que não são números válidos
                print("Entrada inválida. Por favor, insira um número válido.")

        # Potenciação
        elif operacao == 6:
            try:
                base = float(input("Digite a base: "))
                expoente = float(input("Digite o expoente: "))
                resultado = base ** expoente  # Calcula a potenciação
                # Exibe o resultado da potenciação
                print(f"{base} elevado a {expoente}: {resultado:.2f}")
            except ValueError:
                # Trata entradas que não são números válidos
                print("Entrada inválida. Por favor, insira um número válido.")

        else:
            # Trata opções de operação inválidas
            print("Opção inválida.")

    # Opção para áreas e perímetros
    elif escolha == 2:
        while True:
            try:
                poligono = int(input('''
> Qual polígono irá usar?
[1] Quadrado
[2] Retângulo
[3] Triângulo
[4] Círculo
[5] Trapézio
[6] Paralelogramo
>>> '''))
                break  # Sai do loop se a entrada for um número inteiro válido
            except ValueError:
                # Trata entradas que não são números inteiros
                print("Entrada inválida. Por favor, insira um número inteiro.")

        # Quadrado
        if poligono == 1:
            try:
                lado = float(input("Digite o comprimento do lado: "))
                area = lado ** 2  # Calcula a área do quadrado
                perimetro = 4 * lado  # Calcula o perímetro do quadrado
                # Exibe os resultados
                print(f"Área do quadrado: {area:.2f}")
                print(f"Perímetro do quadrado: {perimetro:.2f}")
            except ValueError:
                # Trata entradas que não são números válidos
                print("Entrada inválida. Por favor, insira um número válido.")

        # Retângulo
        elif poligono == 2:
            try:
                largura = float(input("Digite a largura: "))
                altura = float(input("Digite a altura: "))
                area = largura * altura  # Calcula a área do retângulo
                perimetro = 2 * (largura + altura)  # Calcula o perímetro do retângulo
                # Exibe os resultados
                print(f"Área do retângulo: {area:.2f}")
                print(f"Perímetro do retângulo: {perimetro:.2f}")
            except ValueError:
                # Trata entradas que não são números válidos
                print("Entrada inválida. Por favor, insira um número válido.")

        # Triângulo
        elif poligono == 3:
            try:
                base = float(input("Digite a base: "))
                altura = float(input("Digite a altura: "))
                area = 0.5 * base * altura  # Calcula a área do triângulo
                # Exibe o resultado
                print(f"Área do triângulo: {area:.2f}")
            except ValueError:
                # Trata entradas que não são números válidos
                print("Entrada inválida. Por favor, insira um número válido.")

        # Círculo
        elif poligono == 4:
            try:
                raio = float(input("Digite o raio: "))
                area = math.pi * raio ** 2  # Calcula a área do círculo
                perimetro = 2 * math.pi * raio  # Calcula o perímetro do círculo
                # Exibe os resultados
                print(f"Área do círculo: {area:.2f}")
                print(f"Perímetro do círculo: {perimetro:.2f}")
            except ValueError:
                # Trata entradas que não são números válidos
                print("Entrada inválida. Por favor, insira um número válido.")

        # Trapézio
        elif poligono == 5:
            try:
                base_maior = float(input("Digite a base maior: "))
                base_menor = float(input("Digite a base menor: "))
                altura = float(input("Digite a altura: "))
                area = 0.5 * (base_maior + base_menor) * altura  # Calcula a área do trapézio
                # Exibe o resultado
                print(f"Área do trapézio: {area:.2f}")
            except ValueError:
                # Trata entradas que não são números válidos
                print("Entrada inválida. Por favor, insira um número válido.")

        # Paralelogramo
        elif poligono == 6:
            try:
                base = float(input("Digite a base: "))
                altura = float(input("Digite a altura: "))
                area = base * altura  # Calcula a área do paralelogramo
                # Exibe o resultado
                print(f"Área do paralelogramo: {area:.2f}")
            except ValueError:
                # Trata entradas
                print("Entrada inválida. Por favor, insira um número válido.")
    elif escolha == 0:
        break
print("Você saiu do programa, espero ter ajudado.")

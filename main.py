print('''     Calculadora Matemática
================================

Qual funcionalidade quer usar?

[1] Operações Matemáticas
[2] Áreas e Perímetros
[3] Volumes de Sólidos
[4] Equações
[5] Conversão de Medidas
[6] Conversão de Volumes 
''')
escolha = int(input("Digite uma opção: "))
if escolha == 1:
    print('''
Qual operação matemática irá usar?

[1] Adição
[2] Subtração
[3] Multiplicação
[4] Divisão
[5] Radiciação
[6] Potenciação
''')
elif escolha == 2:
    print('''
Qual polígono irá usar?

[1] Quadrado
[2] Retângulo
[3] Triângulo
[4] Círculo
[5] Trapézio
''')
elif escolha == 3:
    print('''
Qual sólido irá usar?

[1] Cilindro
[2] Cubo
[3] Paralelepípedo
[4] Esfera
[5] Piramide
[6] Prisma
[7] Cone
''')
elif escolha == 4:
    print('''Qual grau de equação irá usar?
[1] Primeiro
[2] Segundo
''')
elif escolha == 5:
    print('''
Qual será a sua conversão?

[1] km ---> m
[2]  m ---> cm
[3] cm ---> mm
[4] km ---> cm
[5]  m ---> mm
''')

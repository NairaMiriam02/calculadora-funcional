#-----------------------------------------------------------
print('''     Calculadora Matemática
================================

Qual funcionalidade quer usar?

[1] Operações Matemáticas
[2] Áreas e Perímetros
[3] Volumes de Sólidos
[4] Equações
[5] Conversão de Medidas
[6] Conversão de Volumes
[7] Porcentagem
''')
escolha = int(input("Digite uma opção: "))
#-------------------------------------------------------------
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
#----------------------------------------------------------------
elif escolha == 2:
    print('''
Qual polígono irá usar?

[1] Quadrado
[2] Retângulo
[3] Triângulo
[4] Círculo
[5] Trapézio
''')
#--------------------------------------------------------------------
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
#---------------------------------------------------------------------
elif escolha == 4:
    print('''Qual grau de equação deseja usar?
[1] Equação de 1º grau
[2] Equação de 2º grau
''')
#----------------------------------------------------------------------
elif escolha == 5:
    print('''
Qual medida deseja converter?

[1] Quilômetro(km) >>> Metro(m)
[2] Metro(m) >>> Quilômetro(km)
[3] Centímetro(cm) >>> Metro(m)
[4] Metro(m) >>> Centímetro(cm)
[5] Milímetro(mm) >>> Centímetro(cm)
[6] Centímetro(cm) >>> Milímetro(mm)
''')
#----------------------------------------------------------------------
elif escolha == 6:
    print('''
Qual volume deseja converter?

[1]
[2]
[3]
[4]
[5]
''')
#------------------------------------------------------------------
elif escolha == 7:
    valor = float(input("Digite o valor total: "))
    percentagem = float(input("Digite a porcentagem sobre o total:

                        








                        

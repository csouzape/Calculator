numero1 = float(input("Digite o seu primeiro numero: "))
numero2 = float(input("Digite o seu segundo numero:"))
operacao = input("Qual operacao voce quer?: +, -, *, /):")

if operacao == "+":
    print("Soma:", numero1 + numero2) 
elif operacao == "-":
    print("Subtração:", numero1 - numero2)
elif operacao == "*":
    print("Multiplicação:", numero1 * numero2) 
elif operacao == "/":
    print("Divisão", numero1 / numero2)
else:
    print("Operação Invalida")
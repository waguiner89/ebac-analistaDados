continuar = "S"

while continuar.upper() == "S":
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    print("Digite o número da operação deseja realizar")
    op = int(input("1-Adição / 2-Subtração / 3-Multiplicação / 4-Divisão: "))

    if op == 1:
        resultado = num1 + num2
        print(f"A soma de {num1}+{num2} = {resultado}")
        continuar = input("Digite S para realizar nova operação ou N para finalizar: ")
    elif op == 2:
        resultado = num1 - num2
        print(f"A subtração de {num1}-{num2} = {resultado}")
        continuar = input("Digite S para realizar nova operação ou N para finalizar: ")
    elif op == 3:
        resultado = num1 * num2
        print(f"A multiplicação de {num1}x{num2} = {resultado}")
        continuar = input("Digite S para realizar nova operação ou N para finalizar: ")
    elif op == 4:
        if num1 == 0 or num2 == 0:
            print("Numerador ou denominador não podem ser zero!")
            continuar = input("Digite S para realizar nova operação ou N para finalizar: ")
        else:
            resultado = num1 / num2
            print(f"A divisão de {num1}/{num2} = {resultado}")
            continuar = input("Digite S para realizar nova operação ou N para finalizar: ")
    else:
        print|("Escolha entre 1 a 4!")
        continuar = input("Digite S para realizar nova operação ou N para finalizar: ")

print("Finalizando...")

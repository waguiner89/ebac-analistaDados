#!/bin/bash

echo "Digite o primeiro numero: "
read num1
echo "Digite o segundo numero: "
read num2

echo "Escolha uma operacao: (1-Adicao - 2-Subtracao - 3-Multiplicacao - 4-Divisao): "
read operacao

case $operacao in
	1) resultado=$(echo "$num1 + $num2" | bc);;
	2) resultado=$(echo "$num1 - $num2" | bc);;
	3) resultado=$(echo "$num1 * $num2" | bc);;
	4) resultado=$(echo "scale=2; $num1 / $num2" | bc);;
esac

echo "Resultado: $resultado"

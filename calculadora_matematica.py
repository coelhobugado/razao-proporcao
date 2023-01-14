# -*- coding: utf-8 -*-

import re

def ratio_proportion(a, b, c):
    ratio = a / b
    proportion = c / (a + b)
    return ratio, proportion

def harmonic_mean(a, b):
    harmonic_mean = 2/((1/a)+(1/b))
    return harmonic_mean

while True:
    print("Digite 1 para calcular Razão e Proporção, 2 para calcular Média Harmônica ou 3 para sair:")
    opcao = input()

    if opcao == "1":
        print("Digite a pergunta:")
        pergunta = input()
        valores = re.findall(r'\d+', pergunta) # extrai os números da pergunta
        a, b, c = int(valores[0]), int(valores[1]), int(valores[2])
        ratio, proportion = ratio_proportion(a, b, c)
        print("Razão entre a e b: ", ratio)
        print("Proporção de c: ", proportion)
    elif opcao == "2":
        print("Digite a pergunta:")
        pergunta = input()
        valores = re.findall(r'\d+', pergunta) # extrai os números da pergunta
        a, b = int(valores[0]), int(valores[1])
        harmonic_mean = harmonic_mean(a, b)
        print("Média harmônica de a e b: ", harmonic_mean)
    elif opcao == "3":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")

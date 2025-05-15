from typing import List, Tuple

def troco_guloso(moedas: List[int], valor: int) -> Tuple[List[int], int]:

    moedas = sorted(moedas, reverse=True)
    resultado = []
    iteracoes = 0
    for moeda in moedas:
        qtd = valor // moeda
        resultado.append(qtd)
        valor -= qtd * moeda
        iteracoes += 1
    return resultado, iteracoes

if __name__ == "__main__":
    moedas = [100, 25, 10, 5, 1]
    valor = 289
    resultado, iteracoes = troco_guloso(moedas, valor)
    print(f"Troco para {valor} centavos com moedas {moedas}: {resultado} (iterações: {iteracoes})") 
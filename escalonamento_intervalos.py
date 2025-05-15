from typing import List, Tuple

def escalonamento_guloso(s: List[int], f: List[int]) -> Tuple[List[int], int]:

    n = len(s)
    # Ordena os intervalos pelo término
    intervalos = sorted([(s[i], f[i], i) for i in range(n)], key=lambda x: x[1])
    resultado = []
    ultimo_fim = -float('inf')
    iteracoes = 0
    for inicio, fim, idx in intervalos:
        iteracoes += 1
        if inicio > ultimo_fim:
            resultado.append(idx)
            ultimo_fim = fim
    return resultado, iteracoes

if __name__ == "__main__":
    s = [1, 3, 0, 5, 8, 5]
    f = [2, 4, 6, 7, 9, 9]
    resultado, iteracoes = escalonamento_guloso(s, f)
    print(f"Índices dos intervalos escolhidos: {resultado} (iterações: {iteracoes})") 
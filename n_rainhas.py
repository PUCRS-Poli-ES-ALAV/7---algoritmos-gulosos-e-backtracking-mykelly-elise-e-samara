from typing import List, Tuple

def n_rainhas_uma_solucao(n: int) -> Tuple[List[List[int]], int]:

    tabuleiro = [[0]*n for _ in range(n)]
    iteracoes = [0]
    solucao = []

    def seguro(linha, coluna):
        for i in range(linha):
            if tabuleiro[i][coluna]:
                return False
            if coluna - (linha - i) >= 0 and tabuleiro[i][coluna - (linha - i)]:
                return False
            if coluna + (linha - i) < n and tabuleiro[i][coluna + (linha - i)]:
                return False
        return True

    def resolver(linha):
        iteracoes[0] += 1
        if linha == n:
            for i in range(n):
                solucao.append(tabuleiro[i][:])
            return True
        for coluna in range(n):
            if seguro(linha, coluna):
                tabuleiro[linha][coluna] = 1
                if resolver(linha + 1):
                    return True
                tabuleiro[linha][coluna] = 0
        return False

    resolver(0)
    return solucao, iteracoes[0]

def n_rainhas_todas_solucoes(n: int) -> Tuple[List[List[List[int]]], int]:

    tabuleiro = [[0]*n for _ in range(n)]
    todas = []
    iteracoes = [0]

    def seguro(linha, coluna):
        for i in range(linha):
            if tabuleiro[i][coluna]:
                return False
            if coluna - (linha - i) >= 0 and tabuleiro[i][coluna - (linha - i)]:
                return False
            if coluna + (linha - i) < n and tabuleiro[i][coluna + (linha - i)]:
                return False
        return True

    def resolver(linha):
        iteracoes[0] += 1
        if linha == n:
            todas.append([row[:] for row in tabuleiro])
            return
        for coluna in range(n):
            if seguro(linha, coluna):
                tabuleiro[linha][coluna] = 1
                resolver(linha + 1)
                tabuleiro[linha][coluna] = 0

    resolver(0)
    return todas, iteracoes[0]

if __name__ == "__main__":
    n = 4
    solucao, iteracoes = n_rainhas_uma_solucao(n)
    print(f"Solução para {n}-rainhas (uma):")
    for linha in solucao:
        print(linha)
    print(f"Iterações: {iteracoes}\n")

    todas, iteracoes = n_rainhas_todas_solucoes(n)
    print(f"Total de soluções para {n}-rainhas: {len(todas)} (iterações: {iteracoes})")
    for sol in todas:
        for linha in sol:
            print(linha)
        print("---") 
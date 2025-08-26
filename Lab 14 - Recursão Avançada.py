m = int(input())
n = int(input())
def matriz(n):
    global lista
    lista = []
    for k in range(m):
        k = []
        lista.append(k)
        for i in range(n):
            linha = input().split()
            linha = list(map(int, linha))
            k.append(linha)
    return lista

def criando_submatriz(matriz, linhas, colunas):
    submatriz = []
    for i in range(len(matriz) - 1):
        linha = []
        for j in range(len(matriz) - 1):
            linha.append(0)
        submatriz.append(linha)
    linha_i = 0 
    for i in range(len(matriz)):
        coluna_j = 0
        for j in range(len(matriz)):
            if j != colunas:
                submatriz[linha_i][coluna_j] = matriz[i][j]
                coluna_j = coluna_j + 1
        if i != linhas:
            linha_i = linha_i + 1
    return submatriz

def determinante(matriz):
    det = 0
    if len(matriz) == 2:
        det = (matriz[0][0])*(matriz[1][1])-(matriz[1][0]*matriz[0][1])
        return det
    elif len(matriz) > 2:
        for j in range(len(matriz)):
            det = det + ((-1) ** (j)) * (matriz[0][j]) * determinante(criando_submatriz(matriz, 0, j))
        return det

def multiplicacao(lista):
    resultado = 1
    for x in range(len(lista)):
        resultado = resultado * determinante(lista[x])
    return resultado

matriz(n)
print(f"Após as {m} transformações, o objeto {n}-dimensional teve o volume multiplicado no valor {multiplicacao(lista)}.")
m = i

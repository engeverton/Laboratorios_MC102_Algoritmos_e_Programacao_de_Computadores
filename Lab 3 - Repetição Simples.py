q = int(input())
T = float(input())
C = int(input())
n = int(input())
 
i = 1
soma = 0
atual = (T * i + T * C)
while i <= q: 
    Vi = T * i + T * C
    print(i, end='')
    print(" " + "%.2f" %(Vi), end='') 
    soma = soma + atual 
    atual = (T * (i + 1) + T * C) 
    print(" " + "%.2f" %(soma)) 
    if i == q:
        print ("%.2f" %(soma))
    i = i + 1
 
i = 1
soma1 = 0
atual = n 
while soma1 <= (soma - n):
    soma1 = soma1 + atual 
    atual = n
    print(soma1)
    i = i + 1
print(i - 1)
print("BATERIA DE TESTES TERMINADA")
 

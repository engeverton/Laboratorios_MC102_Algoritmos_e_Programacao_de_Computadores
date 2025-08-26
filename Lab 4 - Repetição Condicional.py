G = "+ 1 2"
(operador,a,b)= G.split()
G = G.split()
i = 0
while operador != 0: 
    G = input()
    (operador,a,b)= G.split()
    G = G.split()
    if operador == "+":
        print(int(a) + int(b))
    elif operador == "-":
        print(int(a)- int(b))
    elif operador == "/":
        print((int(a)//int(b)), end=' ')
        print((int(a)%int(b)))
    elif operador == "*":
        print(int(a) * int(b))
    elif operador == ";":
        if a == b:
            print(0)
        elif (int(a)- int(b)) < 0: 
            for i in range(1, (((int(a)- int(b)))*(-1))): 
                if (int(a)- int(b)) % i == 0: 
                    print(i, end= "") 
                    print(" ", end="") 
            print((((int(a)- int(b)))*(-1))) 
        else: 
            for i in range(1, (int(a)- int(b))): 
                if (int(a)- int(b)) % i == 0: 
                    print(i, end= "") 
                    print(" ", end="") 
            print(int(a)- int(b)) 
    i = i + 1

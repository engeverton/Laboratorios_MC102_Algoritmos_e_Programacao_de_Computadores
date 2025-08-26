v_s, a_s, d_s) = input().split()
(v_c, a_c, d_c) = input().split()
v_s = int(v_s) 
a_s = int(a_s) 
d_s = int(d_s) 
v_c = int(v_c) 
a_c = int(a_c) 
d_c = int(d_c) 
t = 0 
turno = 1
x = int(input())
 
def aleatorios(n):
    global lista
    lista = []
    for i in range(1, n + 1):
        global x
        xn = ((7*x + 111) % 1024)
        lista.append(xn)
        x = xn
    if len(lista) == 1:
        return f"MENSAGEM DEBUG - número gerado: {lista[0]}"
    elif len(lista) == 2:
        return f"MENSAGEM DEBUG - número gerado: {lista[0]}\nMENSAGEM DEBUG - número gerado: {lista[1]}"
 
def soco():
    global v_c, v_s, d
    if turno % 2 != 0:
        a = aleatorios(1)
        m = (lista[0] % 3)
        d = m*(a_s - d_c)
        if d < 0:
            return f"{a}\nO clone sofreu {0} pontos de dano!"
        else:
            v_c=v_c-d
            return f"{a}\nO clone sofreu {d} pontos de dano!"
    else:
        c = aleatorios(1)
        m = lista[0] % 3
        d = m*(a_c - d_s)
        if d < 0:
            return f"{c}\nSarah sofreu {0} pontos de dano!"
        else:
            v_s=v_s-d
            return f"{c}\nSarah sofreu {d} pontos de dano!"
 
def arremesso_de_facas():
    global v_c, v_s
    if turno % 2 != 0:
        a = aleatorios(1)
        n = (lista[0] % 6)
        d = 0
        for i in range(1, n + 1):
            d = d + (a_s // 3**i)
        v_c=v_c-d
        return f"{a}\nO clone sofreu {d} pontos de dano!"
    else:
        c = aleatorios(1)
        n = (lista[0] % 6)
        d = 0
        for i in range(1, n + 1):
            d = d + (a_c // 3**i)
        v_s=v_s-d
        return f"{c}\nSarah sofreu {d} pontos de dano!"
 
def invocacao_de_fada():
    global v_c, v_s, a_s, a_c, d_c, d_s, t
    t=0
    if turno % 2 != 0:
        b = aleatorios(2)
        p = (lista[0] % 100)
        q = (lista[1] % 1024)
        if q < 100 and q % 2 != 0:
            v_s=v_s+p
            a_s = a_s + q
            return f"{b}\nSarah ganhou {p} pontos de vida!\nSarah ganhou {q} pontos de ataque!"
        elif q < 100 and q % 2 == 0:
            v_s=v_s+p
            d_s = d_s + q
            return f"{b}\nSarah ganhou {p} pontos de vida!\nSarah ganhou {q} pontos de defesa!"
        elif q >= 1019:
            t=1
            return f"{b}\nSarah ganhou {p} pontos de vida!\nO quê? A fada trouxe um monstro gigante com ela!\nO Clone e o castelo foram destruídos,\ne Sarah agora tem um novo pet.\nFINAL SECRETO - PARABENS???"
        else:
            v_s=v_s+p
            return f"{b}\nSarah ganhou {p} pontos de vida!"
    else:
        c = aleatorios(2)
        p = (lista[0] % 100)
        q = (lista[1] % 1024)
        if q < 100 and q % 2 != 0:
            v_c=v_c+p
            a_c = a_c + q
            return f"{c}\nO clone ganhou {p} pontos de vida!\nO clone ganhou {q} pontos de ataque!"
        elif q < 100 and q % 2 == 0:
            v_c=v_c+p
            d_c = d_c + q
            return f"{c}\nO clone ganhou {p} pontos de vida!\nO clone ganhou {q} pontos de defesa!"
        elif q >= 1019:
            t = 1
            return f"{c}\nO clone ganhou {p} pontos de vida!\nO quê? A fada trouxe um monstro gigante com ela!\nSarah foi derrotada..."
        else:
            v_c=v_c+p
            return f"{c}\nO clone ganhou {p} pontos de vida!"
 
def derrotado():
    global v_s, v_c
    if(v_s<=0):
        print("Sarah foi derrotada...")
        exit()
    if(v_c<=0):
        print("O clone foi derrotado! Sarah venceu!\nFIM - PARABENS")
        exit()
 
while turno <= 10000: 
    habilidade = input()
    if habilidade == "soco":        
        print(soco())
    elif habilidade == "facas":
        print(arremesso_de_facas())
    else:
        if habilidade == "fada":
            print(invocacao_de_fada())
            if(t==1):
                exit()
            t=0
    derrotado()
    turno = turno + 1
 

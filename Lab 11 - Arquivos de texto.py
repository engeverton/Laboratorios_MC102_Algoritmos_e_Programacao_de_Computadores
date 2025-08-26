n = int(input()) 
titulos = [] 
leitores = [] 
leitores_finais = [] 
cliques = [] 
tempos = [] 
noticias = [] 
for i in range(n): 
    arquivo = input() 
    with open(f"{arquivo}", "r") as f: 
        identificador = f.readline().split(": ") 
        identificador = int(identificador[1]) 
        titulo, nome_do_titulo = f.readline().rstrip().split("titulo: ") 
        qtd, quantidade_de_leitores = f.readline().split(": ") 
        qtd_final, quantidade_final = f.readline().split(": ") 
        qtd_cliques, quantidade_de_cliques = f.readline().split(": ") 
        tempo, quantidade_de_tempo = f.readline().split(": ") 
        noticia = f.read().split("\n") 
        del noticia[-1] 
        titulos.append(nome_do_titulo) 
        leitores.append(quantidade_de_leitores) 
        leitores_finais.append(quantidade_final) 
        cliques.append(quantidade_de_cliques) 
        tempos.append(quantidade_de_tempo) 
        noticias.append(noticia) 
        with open("relatorio_" + f"{identificador}" + ".txt", "w+") as x: 
            f.seek(0, 0) 
            x.write(f.readline()) 
            f.readline() 
            x.write(f.readline()) 
            x.write(f.readline()) 
            x.write(f.readline()) 
            x.write(f.readline()) 
with open("relatorio_final.txt", "w+") as g: 
    leitores = list(map(int, leitores)) 
    leitores_finais = list(map(int, leitores_finais)) 
    cliques = list(map(int, cliques)) 
    tempos = list(map(int, tempos)) 
    titulo_qtd = dict(zip(leitores, titulos)) 
    titulo_qtdfinal = dict(zip(leitores_finais, titulos)) 
    #Letras A, B, C, D, E, F foram colocadas conforme mostrado na lista 2 do enunciado do lab. 
    l = 0 
    for i in leitores: 
        l += i 
    A = l//(len(leitores)) 
    g.write(f"{A}\n") 
    B = max(leitores) 
    g.write(f"\"{titulo_qtd[B]}\" {B}\n") 
    C = max(leitores_finais) 
    g.write(f"\"{titulo_qtdfinal[C]}\" {C}\n") 
    l1 = 0 
    for j in cliques: 
        l1 += j 
    D = l1//(len(cliques)) 
    g.write(f"{D}\n") 
    E = max(tempos) 
    g.write(f"{E}\n") 
    soma = 0 
    for k in range(n): 
        soma += len(noticias[k]) 
    F = soma//n 
    g.write(f"{F}") 

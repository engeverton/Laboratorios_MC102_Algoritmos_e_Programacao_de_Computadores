if __name__=="__main__": 
    lista_de_strings = input().split(", ") 
    final = (lista_de_strings[len(lista_de_strings)-1:][0]).split("/ ") 
    arquivos = lista_de_strings + final 
    del arquivos[-3] 
  
    def fotos(arquivos): 
        global elementos_unicos  
        elementos_unicos = [] 
        for i in arquivos[:len(arquivos)-1]: 
            if i not in elementos_unicos: 
                elementos_unicos.append(i) 
        return len(elementos_unicos) 
  
    def consecutivos(arquivos): 
        contadores = [] 
        iguais = [] 
        contador = 0 
        for i in range(len(arquivos)): 
            if arquivos[i] == arquivos[i - 1]: 
                contador += 1 
                contadores.append(contador) 
                iguais.append(arquivos[i]) 
            else: 
                contador = 0 
        maior = max(contadores) 
        j = contadores.index(max(contadores)) 
        return f"{iguais[j]} {maior+1}" 
  
    def organizando(arquivos): 
        global removendo 
        x = arquivos[-1] 
        removendo = [] 
        for i in arquivos: 
            if i not in removendo: 
                removendo.append(i) 
        removendo.remove(x)  
        for i in range(len(removendo)): 
            removendo[i] = removendo[i][:3].upper() + removendo[i][3:].lower() 
            removendo[i] = removendo[i].replace(" ", "-") 
        return removendo 
  
    def listas(removendo): 
        HA = [] 
        CR = [] 
        CC = [] 
        for i in range(len(removendo)): 
            if removendo[i][:2] == "HA": 
                HA.append(removendo[i]) 
            elif removendo[i][:2] == "CR": 
                CR.append(removendo[i]) 
            elif removendo[i][:2] == "CC": 
                CC.append(removendo[i]) 
        return f"{HA}\n{CR}\n{CC}" 
  
print(consecutivos(arquivos)) 
print(fotos(arquivos)) 
organizando(arquivos) 
print(listas(removendo)) 

 = int(input())
print("*Que página de meme do Instagram você é?*\nQual a sua idade?")
print(i)
if 0 <= i <= 125:
    if i < 25:
        print("Quantos segundos são necessários para saber se um vídeo é bom?")
        s = int(input())
        print(s)
        if s >= 0:
            print("RESULTADO")
            if s <= 5:
                print("Você deveria estar no TikTok")
            else:
                print("Sua página de memes é: @meltmemes")
        else:
            print("Erro: entrada inválida")
    elif 25 <= i <= 40:
        print("Qual banda você gosta mais?")
        b = str(input())
        if b == "A":
            print("A) Matanza\nRESULTADO\nSua página de memes é: @badrockistamemes")
        elif b == "B":
            print("B) Iron Maiden\nRESULTADO\nSua página de memes é: @badrockistamemes")
        else:
            if b == "C":
                print("C) Imagine Dragons\nSão as capivaras os melhores animais da Terra?")
            elif b == "D":
                print("D) BlackPink\nSão as capivaras os melhores animais da Terra?")
            c = (input())
            if (c == "Sim" or c == "Não"):
                if c == "Sim":
                    print("Sim\nRESULTADO\nSua página de memes é: @genteboamemes")
                elif c == "Não":
                    print("Não\nRESULTADO\nSua página de memes é: @wrongchoicememes")
            else:
                print(c)
                print("Erro: entrada inválida")
    elif i > 40:
        print("Que imagem de bom dia você manda no grupo da família?")
        d = (input())
        if(d == "A" or d=="B" or d=="C"):
            if d == "A":
                print("A) Bebê em roupa de flor\nRESULTADO\nSua página de memes é: @bomdiabebe")
            elif d == "B":
                print("B) Gato\nRESULTADO\nSua página de memes é: @kittykatmsgs") 
            elif d == "C":
                print("C) Coração e rosas\nRESULTADO\nSua página de memes é: @bomdiaflordodia")
        else:
            print(d)
            print("Erro: entrada inválida")
else:
    print("Erro: entrada inválida") 

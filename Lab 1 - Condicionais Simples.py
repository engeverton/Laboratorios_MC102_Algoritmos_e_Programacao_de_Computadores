dia_do_mes = int(input())
dia_da_semana = str(input()) 
valor_da_compra = float(input())
if dia_do_mes % 7 == 0:
    print("%.2f" %(valor_da_compra * 0.5))
else:
    if dia_da_semana == "sexta-feira":
        print("%.2f" %(valor_da_compra * 0.75))
    else:
        if valor_da_compra < dia_do_mes:
            print("%.2f" %(0))
        else:
            print("%.2f" %(valor_da_compra - dia_do_mes))
if dia_da_semana == "terça-feira" or dia_da_semana == "quarta-feira" or dia_da_semana == "quinta-feira" or dia_da_semana == "sexta-feira":
    print("Agradecemos a preferência, tenha uma ótima" + " " + dia_da_semana + "!")    
else:
    if dia_da_semana == "sábado" or dia_da_semana == "domingo":
        print("Agradecemos a preferência, tenha um ótimo fim de semana!")
if dia_da_semana == "segunda-feira":
    print("É um dia terrível, você não devia ter saído da cama.")

'''Autor: Gabriel Passos Mota
Componente Curricular: Algoritmos I
Concluido em: 08/09/2025
Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.'''
AMARELO= "\033[33;1m"
NEUTRO ="\033[m"

loop = (input("Digite um número diferente de 0 para adentrar o programa: "))
while not loop.isdigit():
    loop = (input("Digite um número: "))
        
verificação = 0 #variável para entrar no loop de verificação de entrada do usuário no float
 
#variáveis da Mega Sena
arrecadação_MS = 0
premio_bruto_MS = 0
Concursos_MS = 0    #Contador dos concursos Mega Sena
Acumulador_F_05 = 0 #  acúmulo feito para os concursos que terminam em 0 ou 5 
Acumulador_M_virada = 0 
acumulador_sena = 0
acumulador_quina = 0
acumulador_quadra = 0
Seguridade_social_MS = 0
fnc_MS = 0
Comite_Olimpico_Paralimpico_MS = 0
funpen_MS = 0
fnsp_MS = 0
Custos_Operacionais_MS = 0
imposto_MS = 0
media_MS = 0
Arrecadação_total_MS = 0
Mega_da_Virada = 0

#VARIÁVEIS DA QUINA
arrecadação_Q = 0
Acumulador_São_João = 0 
acumulador_F_5 =0
Acumulo_P_concurso = 0 
Concursos_Q = 0
Seguridade_social_Q = 0
fnc_Q = 0
Comite_Olimpico_Paralimpico_Q = 0
funpen_Q = 0
fnsp_Q =0
Custos_Operacionais_Q = 0
imposto_Q = 0
acumulador_quina_Q = 0
acumulador_quadra_Q = 0
acumulador_terno = 0
media_Q = 0
Arrecadação_total_Q = 0
Quina_São_João = 0

#Variáveis da Lotofácil
arrecadação_LF = 0
Lotofácil_Independência = 0
Acumulador_L_independência = 0     
Acumulador_F_0 = 0  #acumulador para concursos de final 0
Concursos_LF = 0
Seguridade_social_LF = 0
fnc_LF = 0
Comite_Olimpico_Paralimpico_LF = 0
funpen_LF = 0
fnsp_LF =0
Custos_Operacionais_LF = 0
imposto_LF = 0
acumulador_principal = 0
acumulador_fixo = 0
media_LF = 0
Arrecadação_total_LF = 0
Premio_Fixo = 0
Premio_principal = 0



while int(loop)   != 0:
    print(f"{AMARELO} ---MENU PRINCIPAL---{NEUTRO} \n")
    menu_inicial= (input("1-Mega-Sena\n2-Quina\n3-Lotofácil\n4-Estatísticas Gerais\n0-Sair\n"))
    
    #Atribuição das variáveis para os Sub-Menus
    loop_MS = menu_inicial
    loop_Q = menu_inicial
    loop_LF = menu_inicial
    loop = menu_inicial

    while not menu_inicial.isdigit() or int(menu_inicial) == 1 | 2 | 3 | 4 | 0:
        print(f"{AMARELO} ---MENU PRINCIPAL---{NEUTRO} \n")
        menu_inicial = (input("1-Mega-Sena\n2-Quina\n3-Lotofácil\n4-Estatísticas Gerais\n0-Sair\n")) 

        loop_MS = menu_inicial
        loop_Q = menu_inicial
        loop_LF = menu_inicial
        loop = menu_inicial
    
    match int(menu_inicial):



        case 1:
            
            while int(loop_MS) == 1:
                print(f"{AMARELO}-----Menu da Mega Sena-----{NEUTRO}")
                menu_mega_sena = (input("""1-Mega-Sena \n2-Mega da Virada\n3-Tabela de distribuição\n4-Voltar
5-Estatísticas Individuais do último jogo\n"""))

                while not menu_mega_sena.isdigit() :
                    print(f"{AMARELO}-----Menu da Mega Sena-----{NEUTRO}")
                    menu_mega_sena = (input("""1-Mega-Sena \n2-Mega da Virada\n3-Tabela de distribuição\n4-Voltar
5-Estatísticas Individuais do último jogo\n"""))
                
                if int(menu_mega_sena) == 4:
                    loop_MS = 4
                if int(menu_mega_sena) == 3:
                    print("--MEGA-SENA--")
                    print(f"""Destinação:{AMARELO}
Prêmio Bruto Total = 46%%
Sena(6 acertos) = 35%% do prêmio bruto
Quina(5 acertos) = 19%% do prêmio bruto 
Quadra(quatro acertos) = 19%% do prêmio bruto 
Acumula para concursos finais 0 ou 5 = 22%% do prêmio bruto 
Mega da Virada = 5%% do prêmio bruto 
Seguridade Social = 17,32%% 
Fundo Nacional de Cultura(FNC) = 3%% 
Comitê Olímpico e Paralímpico = 1,7%% 
Fundo Penitenciário Nacional(FUNPEN) = 3,14%% 
Fundo Nacional de Segurança Pública (FNSP) = 9,26%% 
Custos Operacionais (CAIXA) = 9,57%% 
Outros encargos e taxas legais = 10,01%%{NEUTRO}\n""")                    

                if int(menu_mega_sena) == 1:
                    
                    print("\nSubstitua a (,) por (.) para digitar o valor da aposta")
                    Concursos_MS += 1
                    '''Utiliza o .replace() para identificar se tem um ponto e o subistitui
                       por um espaço vazio, verificando após isso se todos os caracteres são
                       números utilizando o . isdigit()'''
                    while verificação ==0:  
                        valor_aposta_MS = input("Informe o valor de uma aposta na Mega Sena:")
                                
                        if valor_aposta_MS.replace('.','',1).isdigit():
                            valor_aposta_MS = float(valor_aposta_MS)
                            if int(valor_aposta_MS) > 0:
                                verificação = 1
                        
                    verificação = 0 
                    while verificação == 0:
                        quantidade_apostas = (input(" Digite quantas apostas foram realizadas: "))
                        while not quantidade_apostas.isdigit():
      
                            quantidade_apostas = (input(" Digite quantas apostas foram realizadas: "))
                        if int(quantidade_apostas) > 0:
                            verificação = 1
                    verificação = 0
                    
                    while not quantidade_apostas.isdigit():

                        quantidade_apostas = (input(" Digite quantas apostas foram realizadas: "))
                    
                    #Cálculo do valor total arrecadado e do prêmio Bruto
                    arrecadação_MS = valor_aposta_MS * float(quantidade_apostas)
                    Arrecadação_total_MS = arrecadação_MS
                    premio_bruto_MS = arrecadação_MS * (46/100)
                    arrecadação_MS -= premio_bruto_MS

                    #Aplicação dos prêmios que não tiveram ganhadores
                    if acumulador_sena > 0:
                        premio_bruto_MS += acumulador_sena
                        acumulador_sena = 0
                    if acumulador_quina > 0:
                        premio_bruto_MS += acumulador_quina
                        acumulador_quina = 0
                    if acumulador_quadra > 0:
                        premio_bruto_MS += acumulador_quadra
                        acumulador_quadra = 0

                    #Aplicação do acumulador para prêmios terminados em 5 ou 0
                    if Concursos_MS % 5 == 0:               
                        premio_bruto_MS += Acumulador_F_05
                        Acumulador_F_05 = 0

                    #Distribuição do prêmio bruto
                    premio_sena = premio_bruto_MS * (35/100)
                    premio_quina = premio_bruto_MS * (19/100)
                    premio_quadra = premio_bruto_MS * (19/100)

                    Premio_final_0ou5 = premio_bruto_MS * (22/100)
                    Acumulador_F_05 += Premio_final_0ou5

                    Mega_da_Virada = premio_bruto_MS * (5/100) 
                    Acumulador_M_virada += Mega_da_Virada

                    #Distribuição para os fundos
                    Seguridade_social_MS = arrecadação_MS * (17.32/100)   
                    fnc_MS = arrecadação_MS * (3/100)
                    Comite_Olimpico_Paralimpico_MS = arrecadação_MS * (1.7/100)
                    funpen_MS = arrecadação_MS * (3.14/100)
                    fnsp_MS = arrecadação_MS * (9.26/100)
                    Custos_Operacionais_MS = arrecadação_MS * (9.57/100)
                    imposto_MS = arrecadação_MS* (10.01/100)

                    
                    ganhadores = 1 
                    

                    while ganhadores > 0:
                        quant_ganhadores = 3
                        print("\nSempre existirá um ganhador!\n")
                        
                        sena = (input("Digite a quantidade de ganhadores do prêmio por Sena:"))
                        while not sena.isdigit():
                            
                            sena = (input("Digite a quantidade de ganhadores do prêmio por Sena:"))
                        if int(sena) == 0:
                            acumulador_sena += premio_sena
                            quant_ganhadores -=1

                        quina = (input("Digite a quantidade de ganhadores do prêmio por Quina: "))
                        while not quina.isdigit():
                            quina = (input("Digite a quantidade de ganhadores do prêmio por Quina: "))
                        if int(quina) == 0:
                                acumulador_quina += premio_quina
                                quant_ganhadores-=1                               
                       
                        quadra = (input("Digite a quantidade de ganhadores do prêmio por Quadra: "))
                        while not quadra.isdigit():
                            
                            quadra = (input("Digite a quantidade de ganhadores do prêmio por Quadra: "))
                        if int(quadra) == 0:
                                acumulador_quadra += premio_quadra
                                quant_ganhadores-=1
                    

                        if quant_ganhadores >0:
                             
                            ganhadores = 0

                    divisão_Sena = 0
                    divisão_Quina = 0
                    divisão_Quadra = 0

                    if int(sena) != 0:     
                        divisão_Sena = premio_sena/int(sena)
                    if int(quina) != 0:
                        divisão_Quina = premio_quina/int(quina)
                    if int(quadra) != 0:
                        divisão_Quadra = premio_quadra/int(quadra)   
                    

                    print(f"\nPremio Bruto = {premio_bruto_MS:.2f}")

                    print(f"\nCada ganhador da Sena irá receber {divisão_Sena:.2f} Reais")
                    print(f"Cada ganhador da Quina irá receber {divisão_Quina:.2f} Reais")
                    print(f"Cada ganhador da Quadra vai receber {divisão_Quadra:.2f} Reais\n")

                    media_MS = int(premio_sena + premio_quina + premio_quadra)/(int(sena + quina + quadra) )

                #Estatísticas individuais dos jogos da Mega Sena    
                if int(menu_mega_sena) == 5:
                    loop_MS = 3
                if int(loop_MS) == 3:
                    print(f"A arrecadação total do último jogo foi: {Arrecadação_total_MS}\n")
                            
                    print(f"A média dos prêmios é: {media_MS:.2f}")

                    print("Distribuição do dinheiro arrecadado para os fundos:\n")
                    print(f" Mega da virada {Mega_da_Virada:.2f} Reais")
                    print(f" Seguridade Social {Seguridade_social_MS:.2f} Reais")
                    print(f" Fundo Nacional de Cultura {fnc_MS:.2f} Reais")
                    print(f" Comite Olímpico e Paralímpico: {Comite_Olimpico_Paralimpico_MS:.2f} Reais")
                    print(f" Fundo Penintenciário Nacioal: {funpen_MS:.2f} Reais")
                    print(f" Fundo Nacional De Segurança Pública: {fnsp_MS:.2f} Reais")
                    print(f" Custos Operacionais: {Custos_Operacionais_MS:.2f} Reais")
                    print(f" Impostos: {imposto_MS:.2f} Reais")
                    loop_MS = 1  
                            
                        

                if int(menu_mega_sena) == 2:
                    Concursos_MS += 1
                    print("Substitua a (,) por (.) para digitar o valor da aposta")

                    while verificação == 0: 
                        valor_aposta_MS = input("Informe o valor de uma aposta na Mega Sena da virada:")        
                        if valor_aposta_MS.replace('.','',1).isdigit():
                            valor_aposta_MS = float(valor_aposta_MS)
                            if int(valor_aposta_MS) > 0:
                                verificação = 1 
                    verificação = 0

                    quantidade_apostas = (input(" Digite quantas apostas foram realizadas: ")) 
                    while not quantidade_apostas.isdigit():
                        print("Digite certo agora")
                        quantidade_apostas = (input(" Digite quantas apostas foram realizadas: ")) 
                    
        
                     #Distribuição do Dinheiro arrecadado
                    arrecadação_MS_MS = valor_aposta_MS * float(quantidade_apostas)
                    Arrecadação_total_MS = arrecadação_MS_MS
                    premio_bruto_MS = arrecadação_MS_MS * (46/100)
                    arrecadação_MS -= premio_bruto_MS
                    
                    premio_bruto_MS += Acumulador_M_virada

                    premio_sena = premio_bruto_MS * (35/100)
                    premio_quina = premio_bruto_MS * (19/100)
                    premio_quadra = premio_bruto_MS * (19/100)

                    Premio_final_0ou5 = premio_bruto_MS * (22/100) 
                    Acumulador_F_05 += Premio_final_0ou5            #acumulador para finais 0 ou 5 

                    if Concursos_MS % 5 == 0:               #Condicional para caso seja um concurso de número terminado em 5 ou 0.
                        premio_bruto_MS += Acumulador_F_05

                    Mega_da_Virada = premio_bruto_MS * (5/100)

                    Seguridade_social_MS = arrecadação_MS * (17.32/100)   
                    fnc_MS = arrecadação_MS * (3/100)
                    Comite_Olimpico_Paralimpico_MS = arrecadação_MS* (1.7/100)
                    funpen_MS = arrecadação_MS * (3.14/100)
                    fnsp_MS = arrecadação_MS * (9.26/100)
                    Custos_Operacionais_MS = arrecadação_MS * (9.57/100)
                    imposto_MS = arrecadação_MS * (10.01/100)

                    ganhadores = 1 
                    while ganhadores > 0:
                        quant_ganhadores = 3
                        print("\nSempre existirá um ganhador!\n")
                        
                        sena = (input("Digite a quantidade de ganhadores do prêmio por Sena:"))
                        
                        while not sena.isdigit():
                            print("Digite NÚMEROS")
                            sena = (input("Digite a quantidade de ganhadores do prêmio por Sena:"))
                            
                        if int(sena) == 0:
                            quant_ganhadores -=1
                                    
                        quina = (input("Digite a quantidade de ganhadores do prêmio por Quina: "))

                        while not quina.isdigit():
                            quina = (input("Digite a quantidade de ganhadores do prêmio por Quina: "))

                        if int(quina) == 0:
                                quant_ganhadores-=1                               
                       
                        quadra = (input("Digite a quantidade de ganhadores do prêmio por Quadra: "))
                        
                        while not quadra.isdigit():
                            print("Você tem que digitar um número!!!")
                            quadra = (input("Digite a quantidade de ganhadores do prêmio por Quadra: "))
                        if int(quadra) == 0:
                                quant_ganhadores-=1
                    
                        if quant_ganhadores >0:
                            print("funcionou") 
                            ganhadores = 0                   

                    if int(sena) == 0:
                        premio_quina += premio_sena
                        

                    if int(quina) == 0:
                        premio_quadra += premio_quina
                        

                    if int(quadra) == 0:
                        premio_sena += premio_quadra

                    if int(sena) and int(quadra) == 0:
                        premio_quina += (premio_quadra + premio_sena)    
                    
                    divisão_Sena = 0
                    divisão_Quina = 0
                    divisão_Quadra = 0
                    
                    if int(sena) != 0:     
                        divisão_Sena = int(premio_sena)/int(sena)
                    if int(quina) != 0:
                        divisão_Quina = int(premio_quina)/int(quina)
                    if int(quadra) != 0:
                        divisão_Quadra = int(premio_quadra)/int(quadra)  

                    media_MS = int(premio_sena + premio_quina + premio_quadra)/(int(sena + quina + quadra))
                    

                    print(f"\nPremio Bruto = {premio_bruto_MS:.2f}")

                    print(f"\nCada ganhador da Sena irá receber {divisão_Sena:.2f} Reais")
                    print(f"Cada ganhador da Quina irá receber {divisão_Quina:.2f} Reais")
                    print(f"Cada ganhador da Quadra vai receber {divisão_Quadra:.2f} Reais\n")




        case 2:

            while int(loop_Q) == 2:
                print(f"{AMARELO}------MENU da Quina------{NEUTRO}")
                menu_Quina = (input("""1-Quina \n2-Quina De São João\n3-distribuição\n4-Voltar
5-Estatísticas Individuais do último jogo\n"""))

                while not menu_Quina.isdigit():
                    print(f"{AMARELO}------MENU da Quina------{NEUTRO}")
                    menu_Quina = (input("""1-Mega-Sena \n2-Mega da Virada\n3- Tabela de distribuição\n4-Voltar
5-Estatísticas individuais do último Jogo\n"""))
                menu_Quina = int(menu_Quina)
                if menu_Quina == 4:
                    loop_Q = 4
                if int(menu_Quina) == 3:
                    print("--QUINA--")
                    print(f"""Destinação:{AMARELO}
Prêmio Bruto Total = 50%%
Quina(5 acertos) = 35%% do prêmio bruto
Quadra(4 acertos) = 15%% do prêmio bruto 
Terno(3 acertos) = 10%% do prêmio bruto 
Quina de São João = 15%% do prêmio bruto 
Acúmulo quando ninguém acerta Quina = 15%% do prêmio bruto
Acúmulo para o próximo concurso = 10%% do prêmio bruto                   
Seguridade Social = 17,32%% 
Fundo Nacional de Cultura(FNC) = 3%% 
Comitê Olímpico e Paralímpico = 1,7%% 
Fundo Penitenciário Nacional(FUNPEN) = 3,14%% 
Fundo Nacional de Segurança Pública (FNSP) = 9,26%% 
Custos Operacionais (CAIXA) = 9,57%% 
Outros encargos e taxas legais = 6,01%%{NEUTRO}\n""")
                if menu_Quina == 1:
                    Concursos_Q +=1
                    while verificação ==0:  
                        valor_aposta_Q = input("Informe o valor de uma aposta na Quina:")        
                        if valor_aposta_Q.replace('.','',1).isdigit():
                            valor_aposta_Q = float(valor_aposta_Q)
                            if valor_aposta_Q > 0:
                                verificação = 1
                    verificação = 0
                    while verificação == 0: 
                        quantidade_apostas = (input(" Digite quantas apostas foram realizadas: "))  
                        while not quantidade_apostas.isdigit():
                            print("Digita a parada certa ai abençoado(a)")
                            quantidade_apostas = (input(" Digite quantas apostas foram realizadas: "))
                        if int(quantidade_apostas) > 0:
                            verificação = 1
                    verificação = 0

                    arrecadação_Q = valor_aposta_Q * int(quantidade_apostas)
                    Arrecadação_total_Q = arrecadação_Q
                    Premio_bruto_Q = arrecadação_Q * (50/100)
                    arrecadação_Q -= Premio_bruto_Q
                    Premio_bruto_Q += Acumulo_P_concurso
                    
                    #aplicação dos acumuladores do jogo passado
                    if acumulador_quina_Q > 0:
                        Premio_bruto_Q += acumulador_quina_Q
                        acumulador_quina_Q = 0
                    if acumulador_quadra_Q > 0:
                        Premio_bruto_Q += acumulador_quadra_Q
                        acumulador_quadra_Q = 0
                    if acumulador_terno > 0:
                        Premio_bruto_Q += acumulador_terno
                        acumulador_terno = 0

                    if Concursos_Q % 10 == 5:
                        Premio_bruto_Q += acumulador_F_5
                    

                    premio_quina = Premio_bruto_Q * (35/100)
                    premio_quadra = Premio_bruto_Q * (15/100)
                    premio_terno = Premio_bruto_Q * (10/100)

                    Quina_São_João = Premio_bruto_Q * (15/100)
                    Acumulador_São_João += Quina_São_João
                    Concursos_Final_5 = Premio_bruto_Q * (15/100)  
                    acumulador_F_5 += Concursos_Final_5
                    Acumulo_P_concurso = Premio_bruto_Q * (10/100) #Acumulo do prêmio para o próximo concurso

                    Seguridade_social_Q = arrecadação_Q * (17.32/100)
                    fnc_Q = arrecadação_Q * (3/100)
                    Comite_Olimpico_Paralimpico_Q = arrecadação_Q * (1.7/100)
                    funpen_Q = arrecadação_Q * (3.14/100)
                    fnsp_Q = arrecadação_Q * (9.26/100)
                    Custos_Operacionais_Q = arrecadação_Q * (9.57/100)
                    imposto_Q = arrecadação_Q * (6.01/100)

                    ganhadores = 1 
                    while ganhadores > 0:
                        quant_ganhadores = 3
                        print("\nSempre existirá um ganhador!\n")
                        
                        quina = (input("Digite a quantidade de ganhadores do prêmio por Quina:"))                        
                        while not quina.isdigit():
                            print("Digite NÚMEROS")
                            quina = (input("Digite a quantidade de ganhadores do prêmio por Quina:"))
                        if int(quina) == 0:
                            acumulador_quina_Q += premio_quina
                            quant_ganhadores -=1
                                    
                        quadra = (input("Digite a quantidade de ganhadores do prêmio por Quadra: "))
                        while not quadra.isdigit():
                            quadra = (input("Digite a quantidade de ganhadores do prêmio por Quadra: "))
                        if int(quadra) == 0:
                                acumulador_quadra_Q += premio_quadra
                                quant_ganhadores-=1                               
                       
                        terno = (input("Digite a quantidade de ganhadores do prêmio por Terno: "))
                        while not terno.isdigit():
                            print("Você tem que digitar um número!!!")
                            terno = (input("Digite a quantidade de ganhadores do prêmio por Terno: "))
                        if int(terno) == 0:
                                acumulador_terno += premio_terno
                                quant_ganhadores-=1

                        if quant_ganhadores >0:
                            print("funcionou") 
                            ganhadores = 0

                    divisão_Quina = 0
                    divisão_Quadra = 0
                    divisão_Terno = 0
                    if int(quina) > 0:        
                        divisão_Quina = premio_quina/int(quina)
                    if int(quadra) > 0:
                        divisão_Quadra = premio_quadra/int(quadra)
                    if int(terno) > 0:
                        divisão_Terno = premio_terno/int(terno)
                    media_Q = float(premio_quina + premio_quadra + premio_terno)/(int(quina + quadra + terno))

                    print(f"\nPremio Bruto = {Premio_bruto_Q:.2f}")

                    print(f"\nCada ganhador da Quina irá receber {divisão_Quina:.2f} Reais")
                    print(f"Cada ganhador da Quadra irá receber {divisão_Quadra:.2f} Reais")
                    print(f"Cada ganhador do Terno vai receber {divisão_Terno:.2f} Reais\n")

                if int(menu_Quina) == 5:
                    loop_Q = 3                    
                if int(loop_Q) == 3:
                    print(f"A arrecadação total do último jogo foi: {Arrecadação_total_Q}\n") 
                    print(f"A média dos prêmios é: {media_Q:.2f}") 

                    print("Distribuição do dinheiro arrecadado:\n")
                    print(f" Quina de São João {Quina_São_João:.2f} Reais")
                    print(f" Seguridade Social {Seguridade_social_Q:.2f} Reais")
                    print(f" Fundo Nacional de Cultura {fnc_Q:.2f} Reais")
                    print(f" Comite Olímpico e Paralímpico: {Comite_Olimpico_Paralimpico_Q:.2f} Reais")
                    print(f" Fundo Penintenciário Nacioal: {funpen_Q:.2f} Reais")
                    print(f" Fundo Nacional De Segurança Pública: {fnsp_Q:.2f} Reais")
                    print(f" Custos Operacionais: {Custos_Operacionais_Q:.2f} Reais")
                    print(f" Impostos: {imposto_Q:.2f} Reais")
                    loop_Q = 2


                if menu_Quina == 2:
                    Concursos_Q +=1

                    while verificação ==0:  
                        valor_aposta_Q = input("Informe o valor de uma aposta na Quina de São João:")        
                        if valor_aposta_Q.replace('.','',1).isdigit():
                            valor_aposta_Q = float(valor_aposta_Q)
                            if valor_aposta_Q > 0:
                                verificação = 1
                    verificação = 0   
 
                    while verificação == 0:
                        quantidade_apostas = (input(" Digite quantas apostas foram realizadas: "))
                        while not quantidade_apostas.isdigit():
                            print("Digita a parada certa ai abençoado(a)")
                            quantidade_apostas = (input(" Digite quantas apostas foram realizadas: "))
                        if int(quantidade_apostas) > 0:
                            verificação = 1
                    arrecadação_Q = valor_aposta_Q * int(quantidade_apostas)
                    Arrecadação_total = arrecadação_Q
                    Premio_bruto_Q = arrecadação_Q * (50/100)
                    arrecadação_Q -= Premio_bruto_Q
                    Premio_bruto_Q += Acumulo_P_concurso
                    if Concursos_Q % 10 == 5:
                        Premio_bruto_Q += acumulador_F_5
                    

                    #distribuição do prêmio bruto para as premiações
                    premio_quina = Premio_bruto_Q * (35/100)
                    premio_quadra = Premio_bruto_Q * (15/100)
                    premio_terno = Premio_bruto_Q * (10/100)

                    Premio_bruto_Q += Acumulador_São_João   #aplicação do acumulador da quina de São João 
                    Quina_São_João = Premio_bruto_Q * (15/100)
                    Acumulador_São_João += Quina_São_João
                    Concursos_Final_5 = Premio_bruto_Q * (15/100)
                    acumulador_F_5 += Concursos_Final_5  

                    Acumulo_P_concurso = Premio_bruto_Q * (10/100) #Acumulo do prêmio para o próximo concurso

                    Seguridade_social_Q = arrecadação_Q * (17.32/100)
                    fnc_Q = arrecadação_Q * (3/100)
                    Comite_Olimpico_Paralimpico_Q = arrecadação_Q * (1.7/100)
                    funpen_Q = arrecadação_Q * (3.14/100)
                    fnsp_Q = arrecadação_Q * (9.26/100)
                    Custos_Operacionais_Q = arrecadação_Q * (9.57/100)
                    imposto_Q = arrecadação_Q * (6.01/100)

                    ganhadores = 1 
                    while ganhadores > 0:
                        quant_ganhadores = 3
                        print("\nSempre existirá um ganhador!\n")
                        
                        quina = (input("Digite a quantidade de ganhadores do prêmio por Quina:"))                        
                        while not quina.isdigit():
                            print("Digite NÚMEROS")
                            quina = (input("Digite a quantidade de ganhadores do prêmio por Quina:"))
                        if int(quina) == 0:
                            quant_ganhadores -=1
                                    
                        quadra = (input("Digite a quantidade de ganhadores do prêmio por Quadra: "))
                        while not quadra.isdigit():
                            quadra = (input("Digite a quantidade de ganhadores do prêmio por Quadra: "))
                        if int(quadra) == 0:
                                quant_ganhadores-=1                               
                       
                        terno = (input("Digite a quantidade de ganhadores do prêmio por Terno: "))
                        while not terno.isdigit():
                            print("Você tem que digitar um número!!!")
                            terno = (input("Digite a quantidade de ganhadores do prêmio por Terno: "))
                        if int(terno) == 0:    
                                quant_ganhadores-=1

                        if quant_ganhadores >0:
                            print("funcionou") 
                            ganhadores = 0

                    if int(quina) == 0:
                        premio_quadra += premio_quina
                        

                    if int(quadra) == 0:
                        premio_terno += premio_quadra
                        

                    if int(terno) == 0:
                        premio_quina += premio_terno

                    if int(quina) and int(terno) == 0:
                        premio_quina += (premio_quadra + premio_sena)

                    divisão_Quina = 0
                    divisão_Quadra = 0
                    divisão_Terno = 0        
                    if int(quina) > 0:        
                        divisão_Quina = premio_quina/int(quina)
                    if int(quadra) > 0:
                        divisão_Quadra = premio_quadra/int(quadra)
                    if int(terno) > 0:
                        divisão_Terno = premio_terno/int(terno)
                    media_Q = float(premio_quina + premio_quadra + premio_terno)/(int(quina + quadra + terno))
                    
                    print(f"\nPremio Bruto = {Premio_bruto_Q:.2f}")

                    print(f"\nCada ganhador da Quina irá receber {divisão_Quina:.2f} Reais")
                    print(f"Cada ganhador da Quadra irá receber {divisão_Quadra:.2f} Reais")
                    print(f"Cada ganhador do Terno vai receber {divisão_Terno:.2f} Reais\n")



        
        case 3:
            
            while int(loop_LF) == 3:
                print(f"{AMARELO}-----Menu da Lotofácil-----{NEUTRO}")
                menu_lotofácil = (input("""1-lotofácil \n2-lotofácil da independência\n3-Tabela de distribuição\n4-Voltar
5-Estatítiscas Individuais\n"""))
                while not menu_lotofácil.isdigit():
                    menu_lotofácil = (input("""1-lotofácil \n2-lotofácil da independência\n3-Tabela de distribuição\n4-Voltar
5-Estatítiscas Individuais\n"""))
                menu_lotofácil = int(menu_lotofácil)
                if int(menu_lotofácil) == 4:
                    loop_LF = 4
                if menu_lotofácil == 3:
                    print("-----LOTOFÁCIL-----")
                    print(f"""Destinação:{AMARELO}
Prêmio Bruto Total = 43,35%%
prêmios princiaps:(15 e 14 acertos) = 35%% do prêmio bruto
Lotofácil da independência(acumulo anual) = 13%% do prêmio bruto 
Acúmulo para final 0 = 10%% do prêmio bruto 
premiação fixa(11,12,13 acertos)= 15%% do prêmio bruto  
Seguridade Social = 17,32%% 
Fundo Nacional de Cultura(FNC) = 3%% 
Comitê Olímpico e Paralímpico = 1,7%% 
Fundo Penitenciário Nacional(FUNPEN) = 3,14%% 
Fundo Nacional de Segurança Pública (FNSP) = 9,26%% 
Custos Operacionais (CAIXA) = 9,57%% 
Outros encargos e taxas legais = 12,66%%{NEUTRO}\n""")
                if menu_lotofácil == 1:
                    Concursos_LF += 1
                    verificação = 0
                    while verificação == 0:  
                        Valor_aposta_LF = input("Informe o valor de uma aposta na Lotofácil:")        
                        if Valor_aposta_LF.replace('.','',1).isdigit():
                            Valor_aposta_LF= float(Valor_aposta_LF)
                            if Valor_aposta_LF > 0:
                                verificação = 1


                    verificação = 0
                    while verificação == 0:
                        quantidade_apostas = (input(" Digite quantas apostas foram realizadas: "))
                        while not quantidade_apostas.isdigit():
                            print("Digita a parada certa ai abençoado(a)")
                            quantidade_apostas = (input(" Digite quantas apostas foram realizadas: "))
                        if int(quantidade_apostas) > 0:
                            verificação = 1
                    #Distribuição do Dinheiro arrecadado para o prêmio bruto
                    arrecadação_LF = Valor_aposta_LF * int(quantidade_apostas)
                    Arrecadação_total_LF = arrecadação_LF
                    Premio_bruto_LF = arrecadação_LF * (43.35/100)
                    arrecadação_LF -= Premio_bruto_LF

                    Premio_principal = Premio_bruto_LF * (62/100)
                    Premio_Fixo = Premio_bruto_LF * (15/100)
                    
                    Premio_final_0 = Premio_bruto_LF * (10/100)
                    Acumulador_F_0 += Premio_final_0

                    if Concursos_LF % 5 == 0 and Concursos_LF % 2 == 0:               #Condicional para caso seja um concurso de número terminado em   0
                        Premio_principal += Acumulador_F_0
                        Acumulador_F_0 = 0

                    Lotofácil_Independência = Premio_bruto_LF * (13/100) #Acumulador da lotofácil da independência
                    Acumulador_L_independência += Lotofácil_Independência

                    #distribuição para o resto do dinheiro arrecadado
                    Seguridade_social_LF = arrecadação_LF * (17.32/100)   
                    fnc_LF = arrecadação_LF * (3/100)
                    Comite_Olimpico_Paralimpico_LF = arrecadação_LF * (1.7/100)
                    funpen_LF = arrecadação_LF * (3.14/100)
                    fnsp_LF = arrecadação_LF * (9.26/100)
                    Custos_Operacionais_LF = arrecadação_LF * (9.57/100)
                    imposto_LF = arrecadação_LF * (12.66/100)
                    
                    ganhadores = 1
                    while ganhadores > 0:
                        quant_ganhadores = 2
                        ganhadores_principal = (input("Digite a quantidade de ganhadores do prêmio princial:"))
                        while not ganhadores_principal.isdigit():
                            print("Digite NÚMEROS")
                            ganhadores_principal = (input("Digite a quantidade de ganhadores do prêmio principal:"))
                        if int(ganhadores_principal) == 0:
                            acumulador_principal += Premio_principal
                            quant_ganhadores -=1
                        
                        ganhadores_Fixo = (input("Digite a quantidade de ganhadores do prêmio Fixo: "))
                        while not ganhadores_Fixo.isdigit():
                            ganhadores_Fixo = (input("Digite a quantidade de ganhadores do prêmio fixo "))
                        if int(ganhadores_Fixo) == 0:
                            acumulador_fixo += Premio_Fixo
                            quant_ganhadores-=1
                        
                        if quant_ganhadores > 0:
                            ganhadores = 0
                    
                    Divisão_Princial = 0
                    Divisão_Fixo = 0
                    if int(ganhadores_principal) > 0:
                        Divisão_Princial = Premio_principal/int(ganhadores_principal)
                    if int(ganhadores_Fixo) > 0:
                        Divisão_Fixo = Premio_Fixo/int(ganhadores_Fixo)                     

                    print(f"\nPremio Bruto = {Premio_bruto_LF:.2f}")

                    print(f"\nCada ganhador do prêmio principal levará {Divisão_Princial:.2f} Reais")
                    print(f"Cada ganhador do prêmio fixo levará  {Divisão_Fixo:.2f} Reais") 

                    media_LF = (Premio_Fixo + Premio_principal)/(int(ganhadores_principal + ganhadores_Fixo))
                if int(menu_lotofácil) == 5:
                    loop_LF = 5
                if int(loop_LF) == 5:
                    print(f"Valor total arrecadado: {Arrecadação_total_LF}")
                    print(f"A média dos prêmios é {media_LF}")
                    print("\nDistribuição do dinheiro arrecadado:")
                    print(f" Lotofácil da independência {Lotofácil_Independência:.2f} Reais")
                    print(f" Seguridade Social {Seguridade_social_LF:.2f} Reais")
                    print(f" Fundo Nacional de Cultura {fnc_LF:.2f} Reais")
                    print(f" Comite Olímpico e Paralímpico: {Comite_Olimpico_Paralimpico_LF:.2f} Reais")
                    print(f" Fundo Penintenciário Nacioal: {funpen_LF:.2f} Reais")
                    print(f" Fundo Nacional De Segurança Pública: {fnsp_LF:.2f} Reais")
                    print(f" Custos Operacionais: {Custos_Operacionais_LF:.2f} Reais")
                    print(f" Impostos: {imposto_LF:.2f} Reais")
                    loop_LF = 3


                if menu_lotofácil == 2:
                    Concursos_LF += 1
                    verificação = 0
                    while verificação ==0:  
                        Valor_aposta_LF = input("Informe o valor de uma aposta na Lotofácil:")        
                        if Valor_aposta_LF.replace('.','',1).isdigit():
                            Valor_aposta_LF= float(Valor_aposta_LF)
                            if Valor_aposta_LF > 0:
                                verificação = 1
                      
                    verificação = 0
                    while verificação == 0:
                        quantidade_apostas = (input(" Digite quantas apostas foram realizadas: "))
                        while not quantidade_apostas.isdigit():
                            print("Digita a parada certa ai abençoado(a)")
                            quantidade_apostas = (input(" Digite quantas apostas foram realizadas: "))
                        if int(quantidade_apostas) > 0:
                            verificação = 1 

                    #Distribuição do Dinheiro arrecadado para o prêmio bruto
                    arrecadação_LF = Valor_aposta_LF * int(quantidade_apostas)
                    Premio_bruto_LF = arrecadação_LF * (43.35/100)
                    Premio_bruto_LF += Acumulador_L_independência
                    arrecadação_LF -= Premio_bruto_LF

                    Premio_principal = Premio_bruto_LF * (62/100)
                    Premio_Fixo = Premio_bruto_LF * (15/100)
                    
                    Premio_final_0 = Premio_bruto_LF * (10/100)
                    Acumulador_F_0 += Premio_final_0

                    if Concursos_LF % 5 == 0 and Concursos_LF % 2 == 0:               #Condicional para caso seja um concurso de número terminado em   0
                        Premio_principal += Acumulador_F_0
                        Acumulador_F_0 = 0

                    Lotofácil_Independência = Premio_bruto_LF * (13/100) #Acumulador da lotofácil da independência
                    Acumulador_L_independência += Lotofácil_Independência

                    #distribuição para o resto do dinheiro arrecadado
                    Seguridade_social_LF = arrecadação_LF * (17.32/100)   
                    fnc_LF = arrecadação_LF * (3/100)
                    Comite_Olimpico_Paralimpico_LF = arrecadação_LF * (1.7/100)
                    funpen_LF = arrecadação_LF * (3.14/100)
                    fnsp_LF = arrecadação_LF * (9.26/100)
                    Custos_Operacionais_LF = arrecadação_LF * (9.57/100)
                    imposto_LF = arrecadação_LF * (12.66/100)
                    
                    ganhadores = 1
                    while ganhadores > 0:
                        quant_ganhadores = 2
                        ganhadores_principal = (input("Digite a quantidade de ganhadores do prêmio princial:"))
                        while not ganhadores_principal.isdigit():
                            print("Digite NÚMEROS")
                            ganhadores_principal = (input("Digite a quantidade de ganhadores do prêmio principal:"))
                        if int(ganhadores_principal) == 0:  
                            quant_ganhadores -=1
                        
                        ganhadores_Fixo = (input("Digite a quantidade de ganhadores do prêmio Fixo: "))
                        while not ganhadores_Fixo.isdigit():
                            ganhadores_Fixo = (input("Digite a quantidade de ganhadores do prêmio fixo "))
                        if int(ganhadores_Fixo) == 0:
                            quant_ganhadores-=1
                        
                        if quant_ganhadores > 0:
                            ganhadores = 0
                        
                        if ganhadores_principal == 0:
                            Premio_Fixo += Premio_principal
                            Premio_principal = 0
                        if ganhadores_Fixo == 0:
                            Premio_principal += Premio_Fixo
                            Premio_Fixo = 0
                    
                    Divisão_Princial = 0
                    Divisão_Fixo = 0
                    if int(ganhadores_principal) > 0:
                        Divisão_Princial = Premio_principal/int(ganhadores_principal)
                    if int(ganhadores_Fixo) > 0:
                        Divisão_Fixo = Premio_Fixo/int(ganhadores_Fixo)
                    

                    print(f"\nPremio Bruto = {Premio_bruto_LF:.2f}")

                    print(f"\nCada ganhador do prêmio principal levará {Divisão_Princial:.2f} Reais")
                    print(f"Cada ganhador do prêmio fixo levará  {Divisão_Fixo:.2f} Reais")
                    media_LF = (Premio_Fixo + Premio_principal)/(int(ganhadores_principal + ganhadores_Fixo))
    
        case 4:
            verificação = 0
            while verificação == 0:
                print(f"{AMARELO}---Menu das Estatísticas Gerais---{NEUTRO}")
                menu_estatísticas = (input("1-Rentabilidade\n2-Estatísticas individuais\n3-voltar\n"))
                while not menu_estatísticas.isdigit():
                    print(f"{AMARELO}---Menu das Estatísticas Gerais---{NEUTRO}")
                    menu_estatísticas = (input("1-Rentabilidade\n2-Estatísticas individuais\n3-voltar\n"))
                if int(menu_estatísticas) == 1 or int(menu_estatísticas) == 2 or int(menu_estatísticas) == 3:
                    verificação = 1
            verificação = 0

            if int(menu_estatísticas) == 1:
                #Rentabilidade para os jogadores
                if media_MS > media_Q and media_MS > media_LF:
                    print("A loteria mais rentável para os jogadores é a Mega Sena ")
                if media_Q > media_MS and media_Q > media_LF:
                    print("A loteria mais rentável para os jogadores é a Quina")
                if media_LF > media_MS and media_LF > media_Q:
                    print("A loteria mais rentável para os jogadores é a Lotofácil")
                if media_MS == media_Q == media_LF:
                    print("As três são igualmente rentáveis para os jogadores")
                #Rentabilidade para a Caixa
                if Arrecadação_total_MS > Arrecadação_total_Q and Arrecadação_total_MS > Arrecadação_total_LF:
                    print("A loteria mais rentável para caixa é a Mega Sena")
                if Arrecadação_total_Q > Arrecadação_total_MS and Arrecadação_total_Q > Arrecadação_total_LF:
                    print("A loteria mais rentável para caixa é a Quina")
                if Arrecadação_total_LF > Arrecadação_total_MS and Arrecadação_total_LF > Arrecadação_total_Q:
                    print("A loteria mais rentável apra a caixa é a Lotofácil")
                if Arrecadação_total_MS == Arrecadação_total_Q == Arrecadação_total_LF:
                    print("As loterias foram igualmente rentáveis para a Caixa")
                #Rentabilidade para os fundos
                if  Seguridade_social_MS > Seguridade_social_Q and Seguridade_social_MS > Seguridade_social_LF:
                    print("A loteria mais rentável para o fundo de seguridade social é a Mega Sena")
                elif Seguridade_social_Q > Seguridade_social_LF and Seguridade_social_Q > Seguridade_social_MS:
                    print("A loteria mais rentável para o fundod de Seguridade Social é a Quina")
                elif Seguridade_social_LF > Seguridade_social_MS and Seguridade_social_LF > Seguridade_social_Q:
                    print("A loteria mais rentável para o fundo de Seguridade social é a Lotofácil")

                if fnc_MS > fnc_Q and fnc_MS > fnc_LF:
                    print("A loteria mais rentável para o fundo nacional de cultura é a Mega Sena")
                elif fnc_Q > fnc_MS and fnc_Q> fnc_LF:
                    print("A loteria mais rentável para o fundo nacional de cultura é a Quina")
                elif fnc_LF > fnc_Q and fnc_LF> fnc_MS:
                    print("A loteria mais rentável para o fundo nacional de cultura é a Lotofácil")

                if Comite_Olimpico_Paralimpico_MS > Comite_Olimpico_Paralimpico_Q and Comite_Olimpico_Paralimpico_MS > Comite_Olimpico_Paralimpico_LF:
                    print("A loteria mais rentável para o Comite olímpico e paralímpico é a Mega Sena")
                elif Comite_Olimpico_Paralimpico_Q > Comite_Olimpico_Paralimpico_MS and Comite_Olimpico_Paralimpico_Q > Comite_Olimpico_Paralimpico_LF:
                    print("A loteria mais rentável para o Comite olímpico e paralímpico é a Quina")
                elif Comite_Olimpico_Paralimpico_LF > Comite_Olimpico_Paralimpico_Q and Comite_Olimpico_Paralimpico_LF > Comite_Olimpico_Paralimpico_MS:
                    print("A loteria mais rentável para o Comite olímpico e paralímpico é a Lotofácil")

                if funpen_MS > funpen_Q and funpen_MS > funpen_LF:
                    print("A loteria mais rentável para o fundo nacional penintenciário é a Mega Sena")
                elif funpen_Q > funpen_MS and funpen_Q > funpen_LF:
                    print("A loteria mais rentável para o fundo nacional penintenciário é a Quina")
                elif funpen_LF > funpen_Q and funpen_LF > funpen_MS:
                    print("A loteria mais rentável para o fundo nacional penintenciário é a Lotofácil")

                if fnsp_MS > fnsp_Q  and fnsp_MS> fnsp_LF:
                    print("A loteria mais rentável para o fundo nacional de segurança pública é a Mega Sena ")
                elif fnsp_Q > fnsp_MS and fnsp_Q > fnsp_LF:
                    print("A loteria mais rentável para o fundo nacional de segurança pública é a Quina")
                elif fnsp_LF > fnsp_Q and fnsp_LF > fnsp_MS:
                    print("A loteria mais rentável para o fundo nacional de segurança pública é a Lotofácil")

                if Custos_Operacionais_MS > Custos_Operacionais_Q and Custos_Operacionais_MS > Custos_Operacionais_LF:
                    print("A loteria mais rentável para os custos operacionais é a Mega Sena")
                elif Custos_Operacionais_Q > Custos_Operacionais_MS and Custos_Operacionais_Q > Custos_Operacionais_LF:
                    print("A loteria mais rentável para os custos operacionais é a Quina")
                elif Custos_Operacionais_LF > Custos_Operacionais_Q and Custos_Operacionais_LF > Custos_Operacionais_MS:
                    print("A loteria mais rentável para os custos operacionais é a Lotofácil")

                if imposto_MS > imposto_Q and imposto_MS> imposto_LF:
                    print("A loteria mais rentável para a arrecadação de impostos é a Mega Sena")
                elif imposto_Q > imposto_MS and imposto_Q > imposto_LF:
                    print("A loteria mais rentável para a arrecadação de impostos é a Quina")
                elif imposto_LF > imposto_Q and imposto_LF> imposto_MS:
                    print("A loteria mais rentável para a arrecadação de impostos é a Lotofácil")
            
            if int( menu_estatísticas) == 2:
                print("--Estatítisticas da Mega Sena--")

                print(f"A arrecadação total do último jogo foi: {Arrecadação_total_MS}\n")         
                print(f"A média dos prêmios é: {media_MS:.2f}")

                print("Distribuição do dinheiro arrecadado para os fundos:\n")
                print(f" Mega da virada {Mega_da_Virada:.2f} Reais")
                print(f" Seguridade Social {Seguridade_social_MS:.2f} Reais")
                print(f" Fundo Nacional de Cultura {fnc_MS:.2f} Reais")
                print(f" Comite Olímpico e Paralímpico: {Comite_Olimpico_Paralimpico_MS:.2f} Reais")
                print(f" Fundo Penintenciário Nacioal: {funpen_MS:.2f} Reais")
                print(f" Fundo Nacional De Segurança Pública: {fnsp_MS:.2f} Reais")
                print(f" Custos Operacionais: {Custos_Operacionais_MS:.2f} Reais")
                print(f" Impostos: {imposto_MS:.2f} Reais\n")

                print("---Estatísticas da Quina---")

                print(f"A arrecadação total do último jogo foi: {Arrecadação_total_Q}\n") 
                print(f"A média dos prêmios é: {media_Q:.2f}") 

                print("Distribuição do dinheiro arrecadado para os fundos:\n")
                print(f" Quina de São João {Quina_São_João:.2f} Reais")
                print(f" Seguridade Social {Seguridade_social_Q:.2f} Reais")
                print(f" Fundo Nacional de Cultura {fnc_Q:.2f} Reais")
                print(f" Comite Olímpico e Paralímpico: {Comite_Olimpico_Paralimpico_Q:.2f} Reais")
                print(f" Fundo Penintenciário Nacioal: {funpen_Q:.2f} Reais")
                print(f" Fundo Nacional De Segurança Pública: {fnsp_Q:.2f} Reais")
                print(f" Custos Operacionais: {Custos_Operacionais_Q:.2f} Reais")
                print(f" Impostos: {imposto_Q:.2f} Reais\n")

                print("----Estatísticas da Lotofácil----")

                print(f"Valor total arrecadado: {Arrecadação_total_LF}")
                print(f"a média dos prêmios é de: {media_LF}")

                print("\nDistribuição do dinheiro arrecadado para os fundos:")
                print(f" Lotofácil da independência {Lotofácil_Independência:.2f} Reais")
                print(f" Seguridade Social {Seguridade_social_LF:.2f} Reais")
                print(f" Fundo Nacional de Cultura {fnc_LF:.2f} Reais")
                print(f" Comite Olímpico e Paralímpico: {Comite_Olimpico_Paralimpico_LF:.2f} Reais")
                print(f" Fundo Penintenciário Nacioal: {funpen_LF:.2f} Reais")
                print(f" Fundo Nacional De Segurança Pública: {fnsp_LF:.2f} Reais")
                print(f" Custos Operacionais: {Custos_Operacionais_LF:.2f} Reais")
                print(f" Impostos: {imposto_LF:.2f} Reais\n")

if int(loop) == 0:
    print("Saindo do Programa...")

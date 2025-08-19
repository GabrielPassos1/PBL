loop = int(input("Digite qualquer número diferente de 0 caso deseje adentrar o programa "))
Mega_da_Virada = 0
Premio_bruto_MS = 0
while loop != 0:
    print("---MENU---\n")
    menu_inicial= int(input("1-Mega-Sena\n2-Quina\n3-Lotofácil\n4-Estatísticas Gerais\n0-Sair\n"))
    loop_MS = menu_inicial
    loop_Q = menu_inicial
    match menu_inicial:
        case 1:
            print("--MEGA-SENA--")
            print("""Destinação:
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
Outros encargos e taxas legais = 10,01%%\n""")
            while loop_MS < 2:
                menu_mega_sena = int(input("""1-Mega-Sena \n2-Mega da Virada\n"""))
                if menu_mega_sena == 1:
                    
                    Valor_aposta_MS = float(input("Informe o valor de uma aposta na Mega Sena:")) #Registro do valor de uma aposta na mega cena normal.
                    Quantidade_apostas = int(input(" Digite quantas apostas foram realizadas: ")) #Quantidade de apostas registradas.
                    Arrecadação = Valor_aposta_MS * Quantidade_apostas
                    Premio_bruto_MS = Arrecadação * (46/100)
                    Premio_bruto_MS += Mega_da_Virada
                    Premio_sena = Premio_bruto_MS * (35/100)
                    Premio_quina = Premio_bruto_MS * (19/100)
                    Premio_quadra = Premio_bruto_MS * (19/100)
                    Premio_final_0ou5 = Premio_bruto_MS * (22/100)
                    Mega_da_Virada = Premio_bruto_MS * (5/100)
                    Seguridade_social = Arrecadação * (17.32/100)
                    fnc = Arrecadação * (3/100)
                    Comite_Olimpico_Paralimpico = Arrecadação * (1.7/100)
                    funpen = Arrecadação * (3.14/100)
                    fnsp = Arrecadação * (9.26/100)
                    Custos_Operacionais = Arrecadação * (9.57/100)
                    Imposto = Arrecadação * (10.01/100)
                    
                    for premiação in range(1,5,+1):                                               # Estrutura de repetição para registrar a quantidade de ganhadores.
                        if premiação == 1:
                            Sena = int(input("Digite a quantidade de ganhadores do prêmio por Sena:"))
                        elif premiação == 2:
                            Quina = int(input("Digite a quantidade de ganhadores do prêmio por Quina: "))
                        elif premiação == 3:
                            Quadra = int(input("Digite a quantidade de ganhadores do prêmio por Quadra: "))
                        elif premiação == 4:
                            Finais_0_5 = int(input("Digite a quantidade de ganhadores do prêmio com números terminados em 0 e 5: ")) 

                    Divisão_Sena = Premio_sena/Sena
                    Divisão_Quina = Premio_quina/Quina
                    Divisão_Quadra = Premio_quadra/Quadra
                    Divisão_Final_0ou5 = Premio_final_0ou5/Finais_0_5

                    print(f"\nPremio Bruto = {Premio_bruto_MS:.2f}")

                    print(f"\nCada ganhador da Sena irá receber {Divisão_Sena:.2f} Reais")
                    print(f"Cada ganhador da Quina irá receber {Divisão_Quina:.2f} Reais")
                    print(f"Cada ganhador da Quadra vai receber {Divisão_Quadra:.2f} Reais\n")

                    print(f"Acumulou para concursos {Divisão_Final_0ou5:.2f} Reais")
                    print(f"Acumulou para a Mega da virada {Mega_da_Virada:.2f} Reais")
                    print(f"Foi distribuído para Seguridade Social {Seguridade_social:.2f} Reais")
                    print(f"Foi distribuído para o Fundo Nacional de Cultura {fnc:.2f} Reais")
                    print(f"Foi distribuído para o Comite Olímpico e Paralímpico: {Comite_Olimpico_Paralimpico:.2f} Reais")
                    print(f"Foi distribuído para o Fundo Penintenciário Nacioal: {funpen:.2f} Reais")
                    print(f"Foi distribuído para o Fundo Nacional De Segurança Pública: {fnsp:.2f} Reais")
                    print(f"Foi distribuído para Custos Operacionais: {Custos_Operacionais:.2f} Reais")
                    print(f"Foi distribuído para os Impostos: {Imposto:.2f} Reais")
                    
                    

                loop_MS = int(input("\nDeseja Recalcula alguma Mega Sena ?\n1-(Sim)  2-(Voltar ao Menu principal)"))

                if menu_mega_sena == 2:
                    print
        case 2:
            print("--QUINA--")
            print("""Destinação:
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
Outros encargos e taxas legais = 6,01%%\n""")
            while loop_Q < 2:
                menu_mega_sena = int(input("""1-Quina \n2-Quina De São João\n"""))
                if menu_mega_sena == 1:
                    Valor_aposta_MS = float(input("Informe o valor de uma aposta na Mega Sena:")) #Registro do valor de uma aposta na mega cena normal.
                    Quantidade_apostas = int(input(" Digite quantas apostas foram realizadas: ")) #Quantidade de apostas registradas.
                    Arrecadação = Valor_aposta_MS * Quantidade_apostas
                    Premio_bruto_Q = Arrecadação * (50/100)
                    Premio_quina = Premio_bruto_Q * (35/100)
                    Premio_quadra = Premio_bruto_Q * (15/100)
                    Premio_terno = Premio_bruto_Q * (10/100)
                    Quina_São_João = Premio_bruto_Q * (15/100)
                    Q_Sem_acertos = Premio_bruto_Q * (15/100) #Premiação para quando ninguém acertou Quina
                    Acumulo_P_concurso = Premio_bruto_Q * (10/100) #Acumulo do prêmio para o próximo concurso
                    Seguridade_social = Arrecadação * (17.32/100)
                    fnc = Arrecadação * (3/100)
                    Comite_Olimpico_Paralimpico = Arrecadação * (1.7/100)
                    funpen = Arrecadação * (3.14/100)
                    fnsp = Arrecadação * (9.26/100)
                    Custos_Operacionais = Arrecadação * (9.57/100)
                    Imposto = Arrecadação * (10.01/100)

                    for premiação in range(1,5,+1):                                               # Estrutura de repetição para registrar a quantidade de ganhadores.
                        if premiação == 1:
                            Sena = int(input("Digite a quantidade de ganhadores do prêmio por Sena:"))
                        elif premiação == 2:
                            Quina = int(input("Digite a quantidade de ganhadores do prêmio por Quina: "))
                        elif premiação == 3:
                            Quadra = int(input("Digite a quantidade de ganhadores do prêmio por Quadra: "))
                        elif premiação == 4:
                            Finais_0_5 = int(input("Digite a quantidade de ganhadores do prêmio com números terminados em 0 e 5: \n")) 

    
    loop = menu_inicial
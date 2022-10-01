def conjuntoTrabalho(paginas, quadros):
    # contador de faltas de paginas
    falta = 0
    # numero de referencias feitas
    referencias = 0
    # tempo decorrido
    tempo = 0
    # limiar
    limiar = int(quadros/2)+1

    # lista de memorias, inicia com nenhum elemento, 
    # sem nenhuma referencia e sem um ultimo instante de referencia
    memoria = []
    for _ in range(quadros):
        memoria.append([None, 0, 0])
    
    # for com range do tamanho da quantidade de paginas
    for i in range(len(paginas)):
        # a cada iteração soma-se 1 ao instante de tempo decorrido
        tempo+=1
        # verifica se houve sucesso na substituicao
        sucesso = False
        # for com range igual ao valor de quadros (4)
        for j in range(quadros):
            # se houver espaco livre na memoria
            if memoria[j][0] == None:
                # adiciona a pagina naquele espaco de memoria
                memoria[j][0] = paginas[i]
                # seta o bit de referencia para 1
                memoria[j][1] = 1
                # adiciona o instante de tempo atual
                memoria[j][2] = tempo
                # incrementa o contador de faltas de paginas
                falta+=1
                # seta sucesso como True, pois a substituicao obteve sucesso
                sucesso=True
                break
            # se a pagina ja estiver na memoria
            if memoria[j][0] == paginas[i]:
                # seta o bit de referencia para 1
                memoria[j][1] = 1
                # atualiza o instante de tempo com o tempo atual
                memoria[j][2] = tempo
                # seta sucesso como True
                sucesso = True
                break
        # se nao houver espaco, tampouco a pagina estiver na memoria
        if not sucesso:
            # variavel que guarda indice da pagina que sera substituida
            subst = 0
            # for com range igual ao valor de quadros (4)
            for j in range(quadros):
                # se o bit de referencia estiver 0
                if memoria[j][1]==0:
                    # idade da pagina é a subtracao do instante atual com o ultimo instante em que foi referenciada
                    idade = tempo - memoria[j][2]
                    # se a idade for maior q o limiar
                    if idade > limiar:
                        # a pagina no indice j sera substituida
                        subst = j
                        break
                    # se a idade for maior que o ultimo instante de referencia da pagina no indice subst
                    if idade > (tempo-memoria[subst][2]):
                        # atualiza o subst com o indice da pagina mais velha
                        subst = j
            
            # adiciona a pagina na posicao que deve substituir
            memoria[subst][0] = paginas[i]
            # seta o bit de referencia como 1
            memoria[subst][1] = 1
            # atualiza o ultimo instante de uso
            memoria[subst][2] = tempo

            # incrementa o contador de faltas
            falta+=1

        referencias+=1
        # se o contador for igual a 4 (o limite de referencias)
        if referencias == 4:
            # zera as referencias
            referencias = 0
            # seta todos os bits de referencia na memoria como 0
            for j in range(quadros):
                memoria[j][1] = 0

    return "CT "+str(falta)
from collections import deque

def segundaChance(paginas, quadros):
    # contador de faltas de paginas
    falta = 0
    # contador de quantidade de referencias (deve ser no maximo 4)
    referencia = 0
    # lista de memorias, inicia com nenhum elemento e sem nenhuma referencia
    memoria = []
    for _ in range(quadros):
        memoria.append([None, 0])
    # fila circular
    filaCircular = deque()

    # For com range do tamanho da lista de paginas
    for i in range(len(paginas)):
        # variavel para verificar se houve sucesso na substituicao
        sucesso = False
        # range do tamanho da lista de quadros (4)
        for j in range(quadros):
            # se houver alguma posicao na lista de quadros vazia (=None)
            if memoria[j][0] == None:
                # adiciona a pagina na posicao i naquele espaco de memoria
                memoria[j][0] = paginas[i]
                # seta o bit de referencia daquele espaco de memoria com 1
                memoria[j][1] = 1
                # adiciona aquele indice na lista circular
                filaCircular.append(j)
                # incrementa o contador de faltas de paginas
                falta+=1
                # seta sucesso como True pois houve sucesso na substituicao
                sucesso=True
                break
            
            # se a pagina estiver na memoria
            if memoria[j][0] == paginas[i]:
                # seta seu bit de referencia como 1
                memoria[j][1] = 1
                # indica sucesso
                sucesso = True
                break

        # se nao houve sucesso, ou seja, 
        # a pagina nao estava na memoria nem havia espaco para ela 
        if not sucesso:
            # usa-se o primeiro valor da fila circular com indices das paginas referenciadas
            indice = filaCircular[0]

            # varre a lista de memorias procurando por uma referencia diferente de 0
            while memoria[indice][1] != 0:
                # move a lista para a esquerda em 1 posicao
                filaCircular.rotate(-1)
                # atualiza o indice da lista na busca do while
                indice = filaCircular[0]
            
            # realiza mais uma rotacao na lista, para que o elemento encontrado vá para o final
            filaCircular.rotate(-1)

            # adiciona a pagina na posicao i no espaco de memoria encontrado
            memoria[indice][0] = paginas[i]
            # atualiza o bit daquela pagina como 1
            memoria[indice][1] = 1
            # incrementa o contador de faltas
            falta+=1

        # incrementa o contador de referencias
        referencia+=1
        # se o contador for igual a 4 (o limite de referencias)
        if referencia == 4:
            # zera as referencias
            referencia = 0
            # seta todos os bits de referencia na memoria como 0
            for j in range(quadros):
                memoria[j][1] = 0
    
    return "SC "+str(falta)
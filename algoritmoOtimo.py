def algoritmoOtimo(paginas, quadros):
    # memoria ocupada
    memoria = []
    # numero de faltas de paginas
    falta = 0
    
    # for com range do tamanho das paginas
    for i in range(len(paginas)):
        # se a pagina na posicao i nao estiver na memoria
        if paginas[i] not in memoria:
            # se o tamanho da lista com a memoria ocupada ainda for menor que o tamanho maximo de quadros
            if len(memoria) < quadros:
                # adiciona a nova pagina na memoria
                memoria.append(paginas[i])
            # caso contrario, se a pagina nao estiver na memoria 
            # mas a lista estiver cheia
            else:
                # for com range do tamanho da memoria
                for j in range(len(memoria)):
                    # se a memoria na posicao j nao estiver na lista de paginas restantes (paginas[i+1:])
                    # ou seja, nao sera referenciada
                    if memoria[j] not in paginas[i+1:]:
                        # a memoria na posicao j é alocada para a pagina na posicao i
                        memoria[j] = paginas[i]
                        break
            # incrementa contador de faltas
            falta+=1
    return "OTM "+str(falta)

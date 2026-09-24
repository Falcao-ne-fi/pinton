def registrarTentativas():
  tentativas = []
  i = 0
  while i < 10:
        valor = int(input(f"Insira o {i + 1}° valor: "))
        if valor > 3 or valor < 0:
            print("valor invalido fi")
            continue
        else:
            tentativas.append(valor)
            i += 1

  return tentativas

def calcularPontuacao(tentativas):
    pontuacaoTotal = 0
    for pontos in tentativas:
        pontuacaoTotal += pontos
        
    return pontuacaoTotal

def calcularAproveitamento(tentativas):
    pontosConvertidos = 0
    pontosNaoConvertidos = 0
    for arremesso in tentativas:
        if arremesso == 0:
            pontosNaoConvertidos += 1
        else:
            arremessosConvertidos += 1
            pontosConvertidos += arremesso
            
    print(f"Arremessos convertidos: {arremessosConvertidos}")
    print(f"Pontos Não convertidos: {pontosNaoConvertidos}")
    taxaDeAproveitamento = (arremessosConvertidos/10) * 100
    
    print(f"Taxa de aproveitamento: {taxaDeAproveitamento}%")

def encontrarCestaMaisFrequente(tentativas):
    contagem = [0,0,0,0]
    tempMaior = 0
    maior = 0
    for arremessos in tentativas:
        contagem[arremessos] += 1
    for i in range(4):
        if contagem[i] > tempMaior:
            tempMaior = contagem[i]
            maior = i

    print(f"Tipo de arremesso mais frequente: {maior} pontos")



    
arremessos=registrarTentativas()

print(calcularPontuacao(arremessos))
encontrarCestaMaisFrequente(arremessos)
3
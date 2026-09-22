Jogadores = ["Henrique", "Juca", "Carlos", "Pedro", "Maria"]
Gols = [2,3,4,2,3]

def calcularTotalGols():
    sum = 0
    for gol in Gols:
        sum = sum + gol
    return(sum)

def calcularMediaGols():
  media = (calcularTotalGols()/len(Jogadores))
  return(media)

def encontrarArtilheiros(Gols,Jogadores):
   maiorTemp = 0
   indice=0
   indiceTemp=0
   for gol in Gols:
      if gol > maiorTemp:
         maiorTemp= gol
         indiceTemp = indice
      indice =+ 1

   return(maiorTemp, indiceTemp)

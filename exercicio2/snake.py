from typing import List

def find_snake_on_grid(grid: List[str]) -> List[List[int]]:

  snake = []
  coluna=0
  linha =0

  for y_coluna in grid: #percorri a coluna
    linha =  grid[coluna].find("h") #procurei o h e salvei (-1 = não encontrado)
     
    if linha >= 0: #segui  o codigo verificando se ja encontrei o h. se for true  
        #print(posicao)
        
        snake.append([linha,coluna]) # adiciono o valor a variavel snake | posição da linha (string)
        break # nao preciso mais procurar, entao saio da estrutura
    coluna+=1 # incrementei o contador (coluna)
      ###############################################################
  achei = True

  while achei: # permanescer lendo valores até que "achei" se torne falso 
      achei = False    

      if linha + 1 < len(grid[coluna]) and grid[coluna][linha + 1] == "<": #para controlar as bordas
          linha += 1 #ando coom a variavel para posição correta
          snake.append([linha, coluna]) # atualizo linha e coluna (x e y) a variavel snake
          achei = True   #atualizo "achei"

          # repito o processo para os 3 casos
      elif linha - 1 >= 0 and grid[coluna][linha - 1] == ">":
          linha -= 1
          snake.append([linha, coluna])
          achei = True

      elif coluna - 1 >= 0 and grid[coluna - 1][linha] == "v":
          coluna -= 1
          snake.append([linha, coluna])
          achei = True

      elif coluna + 1 < len(grid) and grid[coluna + 1][linha] == "^":
          coluna += 1
          snake.append([linha, coluna])
          achei = True
          # se chegou aqui e não se tornou "true" significa que não tem mais para onde ir 

  return snake
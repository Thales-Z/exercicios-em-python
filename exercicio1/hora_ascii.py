def seven_segmentify(time_: str) -> str:
  
  #ASCII primeira versão (não funcionou)
  #as_cii = [" _\n| |\n|_| \n","|\n| "," _\n _|\n|_ ","_\n_|\n_| ","|_|\n  |"," _\n|_\n _|"," _\n|_\n|_| "," _\n  |\n  | "," _\n|_|\n|_| "," _\n|_|\n _| "," ", " .\n . "]

  as_cii = [ " _ \n| |\n|_|","   \n  |\n  |"," _ \n _|\n|_ "," _ \n _|\n _|","   \n|_|\n  |"," _ \n|_ \n _|"," _ \n|_ \n|_|"," _ \n  |\n  |"," _ \n|_|\n|_|"," _ \n|_|\n _|","   \n   \n   ","   \n . \n . "]
  
  as_cii_2 = []
  cont=0
  cont_2=0
      #separar as letras e retirar o " : "
  for item in time_: 
      if item != ":":
          numero= int(item)  
         # print(numero) teste
          
          # tratando do "0 a esquerda"
          if numero==0 and cont==0:
              desenho = as_cii[10]
              as_cii_2.append(desenho)
              #print(numero)
              cont+=1 #contador para verificar se o primeiro numero é 0 
              cont_2+=1 #contador para saber quando colocar os " : "

          else:
              desenho = as_cii[numero]
              as_cii_2.append(desenho)
              cont_2+=1
              cont+=1
              #print(cont_2) teste

          if cont_2 == 2:
              desenho = as_cii[11] # colocando os " : "
              as_cii_2.append(desenho)
              #print(desenho) teste
          
  # separando os "desenhos" em 3 partes, uma variavel pra cada parte            
  inicio = ""
  meio = ""
  fim = ""
  # agrupando na mesma linha cada parte da hora
  for bloco in as_cii_2:
    partes = bloco.split('\n')
    inicio += partes[0]
    meio += partes[1]
    fim += partes[2]
    
  return inicio + "\n" + meio + "\n" + fim 

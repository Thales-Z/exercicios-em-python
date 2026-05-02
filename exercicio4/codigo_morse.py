from typing import List

def possibilities(word: str) -> List[str]:
  # Crie um dicionario para traduzir os codigos para letras reais
  dicionario = {
      ".": "E", "-": "T",
      ".-": "A", "..": "I", "--": "M", "-.": "N",
      "-..": "B", "-.-.": "C", "-..": "D", "..-.": "F",
      "--.": "G", "....": "H", ".---": "J", "-.-": "K",
      ".-..": "L", "---": "O", ".--.": "P", "--.-": "Q",
      ".-.": "R", "...": "S", "..-": "U", "...-": "V",
      ".--": "W", "-..-": "X", "-.--": "Y", "--..": "Z"
  }

  # Lista inicial que começa apenas com a palavra original (que tem as interrogações)
  lista = []
  lista.append(word)

  # variável de controle para manter o loop rodando enquanto tiver "?" para buscar
  aux = True

  while aux:
      aux = False #Variavel se torna falsa para parar o loop se não achar "?".
      nova_lista = [] 


      for item in lista:
          # se eu encontrar um "?" na palavra atual
          if "?" in item:
              aux = True 

              #crio duas versões da palavra.
              ponto = item.replace("?", ".", 1) 
              traco = item.replace("?", "-", 1) 

              # atualizo a "nova lista"
              nova_lista.append(ponto)
              nova_lista.append(traco)
          else:
              # Se não tem "?", a nova lista recebe o item
              nova_lista.append(item)

          # Se houve alguma alteração (aux é True), atualizo a lista principal com as novas versões
          if aux:
              lista = nova_lista


      resposta = []

      # Varro a lista final para traduzir os códigos para letras
      for codigo in lista:
          # Existe esse codigo no dicionario?
          if codigo in dicionario:
              letra = dicionario[codigo] #letra recebe o codigo
              resposta.append(letra) #acrescento a resposta

  return resposta
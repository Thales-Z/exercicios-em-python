linha vem primeiro
X = linha 
Y = coluna

grid = [
            "   ",        #indice 0  "Y" = coluna
            " h<",      #indice 1  "Y" = coluna
            "   ",        #indice 2  "Y" = coluna
        ]
        prcurar h na linha 0 da coluna 0 (achou, conta quantas casas precisou andar e guarda o valor da linha e coluna)
        não achou, vai pra  coluna 1 e procura na linha, a partir  0, se o h esta la, se estiver, guarda o valor da X e Y.
        nao achou: repita o processo.
        apos achar a cabeça, preciso encontrar quem aponta pra ela (ex: h<) e quem aponta para quem esta apontando para a cabeça... e assim ate que o ultimo não tenha ninguem apontando pra ele.
 
 como saber quem esta apontando pra quem? 
 visualmente consigo dizer, mas como transformar isso  em codigo?
 
para que alguem aponte para a cabeça em qualquer lugar, os simbolos precisam ser "> ou <", sendo uma cobra valida, só terá 1 que apontara para cabeça, então se cobra estiver em x =0, procurar por "<" em x, se achar, salvar na variavel snake com append, senão. verificar em y = 0 na posição x=0 se existe um "v", se positivo, salvar essa posição, se não, verificar em y =2 por um "^" em x=0, algum desses sera verdadeiro.

---------------------


 
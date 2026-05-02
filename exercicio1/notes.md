1. decidi converter o valor da variavel "time_" para int para ficar mais facil
2. precisei retirar os " : "
3. fiz um vetor ("numero") com os numeros obtidos 
4. decidi fazer um dicionario em um vetor (" as_cii") e manipular esse vetor atribuindo o seu valor na variavel as_cii_2
5. usei uma variavel auxiliar ("desenho") para salva as posições do vetor
6. para solucionar o "zero a esquerda", criei um contador, verificando se o primeio valor de "numero" é igual a 0 e se o contador se encontra zerado, sendo verdadeiro, ao inves de receber "0 (no formato ASCII)", recebe um espaço e itera o contador. se for  falso, pega o valor de "as_cii" no indice [numero] e guarda em "desenho", depois preenche o vetor "as_cii_2"  com o valor de desenho, depois aumenta o contador
7. crie outro contador para controlar o momento de usar os " : " se for igual a 2, separe as horas dos minutos com " : "
----------------------

no primeiro momento estava tendo dificuldade em como enviar o horario em formato ASCII, eles estavam indo de maneira vertical, notei que percisava ser na horizontal e que todos deveriam ter o mesmo numero de caracter então reescrevi o dicionário para poder ficar no padrão.
- criei  3 variaveis vazias para enviar as horas de maneira horizontal
- preenchi as variaveis com o conteudo de "as_cii_2" e usei a  função split para cortar e deixar tudo num mesma linha
- resolvi o quebra cabeça concatenando nas variaveis criada, acessando o indice [0] para o toop, [1] para o meio e [2] para o final.

rescunhos 

     #pegar o valor da variavel horario indice da variavel ascii 
     # for item in as_cii:
       #as_cii_2 = as_cii[cont]
       #cont+=1
       #print(as_cii_2)


    #print(hora)
      #for testar in as_cii:
        #print(testar)
        
        # ir na posição "item" e substituir o item pelo mesmo  valor da posiçao ascii


      #criar um alfabeto para converter o horario em ASCII
      #if horario[0] =="0":
         #as_cii [0] ="thale "
         #print(as_cii)

    #for hora in as_cii:
     #if horario[hora]==1:
        #as_cii [0] = "|\n|"
        #print(ascii)
         #percorrer o vetor horario, quando ele encontrar um numero
         #percorrer o vetor as_c11 e atribuir a esse numero um codigo ascii
         #vetor ascii [9] {" ", |}
    #guardar cada numero em uma tradução 





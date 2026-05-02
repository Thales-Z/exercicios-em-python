Ler "List".
identificar quantos caracaters contem

- se for 1 caracter, cessar vet1
vetor com 1 [E, T] 
- se for 2 caracter, cessar vet2
vetor com 2 [A, I, M, N]
- se for 3 caracter, cessar vet3
vetor com 3 ou mais [B,C,D,F,G,H,J,K,L,O,P,Q,R,S,U,V,W,X,Y,Z]

se "List" for = a ?
return vet 1 
se não: ve for 

-------------------------------------------

Mudei a forma de pensar quando percebi que estava indo para um caminho muito longo. Ao invés de procurar por quantidade de caracters, fiz um dicionário uníco para todos os casos.
busquei em um loop for, primeiro se existe "?" na palavra recebida, se houver, troco esse "?" por " . " e "-" e armazeno essas substituições em variáveis temporárias "ponto e traco" e as adiciono em uma nova lista.
Se não tiver "?", assumo que o código pode ser traduzido direto e atribuo a nova lista o item da lista. se cair nesse "else", aux é falso e a lista recebe a nova lista.
Mantive essa busca dentro de um "while", se aux terminar falso, não precisa mais rodar o loop while.

Agora arrumo a resposta 

Procuro através de um for, se na "lista" existe algum "codigo" em meu dicionário, se sim, crio uma variável "letra" e atribuo a ela código que consta na lista  e adiciono a resposta o valor dessa variável "letra".

Basicamente vou na tentativa e erro, se ao substituir "?" por " . " e " - " encontrar uma letra em meu dicionario, adiciono essa letra a minha resposta, se não encontrar, não adiciono.
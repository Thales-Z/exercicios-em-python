Neste desafio, você receberá uma grade 2D na forma de um array de strings:

[
  " >>h   ",
  " ^   v ",
  " ^<<<< ",
]
Esta grade representa uma cobra. A cabeça da cobra é representada pelo caractere h no par de coordenadas x, y [3, 0]. À esquerda da cabeça há um caractere > em [2, 0] que representa o próximo segmento da cobra após a cabeça. O caractere > em [1, 0] é o próximo segmento na cauda da cobra após [2, 0], e assim por diante, com cada caractere "seta" apontando para o segmento anterior.

Seu algoritmo deve retornar um array 2D representando os pares de coordenadas x, y da cabeça da cobra até a cauda. O retorno para a entrada acima deve ser:

[
  [3, 0],
  [2, 0],
  [1, 0],
  [1, 1],
  [1, 2],
  [2, 2],
  [3, 2],
  [4, 2],
  [5, 2],
  [5, 1]
]
A entrada da grade sempre será bem formatada e é garantido que contenha uma única cobra. Os únicos caracteres serão do conjunto "<>v^h" para representar ponteiros para a esquerda, direita, para baixo, para cima e a cabeça, respectivamente.
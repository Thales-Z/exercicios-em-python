Neste desafio, sua missão é criar um relógio que mostre horas simulando relógio digital, para isso será preciso converter uma string de tempo no formato "11:03" em uma representação ASCII de um display de 7 segmentos.

Por exemplo, o tempo "13:24" deve ser convertido pela sua função para

    _     _    
  | _| .  _||_|
  | _| . |_   |
Especificamente, existem três linhas (a linha superior é principalmente em branco, com ocasionais caracteres '_' para ajudar a formar a parte superior de alguns dígitos). Quatro caracteres são usados no total: ' ' (espaço), '|' (pipe), '_' (sublinhado) e '.' (ponto).

Veja os casos de teste para os arranjos de todas as possíveis grades de caracteres grandes.

Note que todas as entradas seguirão estritamente o formato de tempo /^\d\d:\d\d$/. Além disso, todas as entradas serão horários válidos, então /^([01]\d|2[0-3]):([0-5]\d)$/ é uma regex mais precisa que define a entrada (o ^ e $ significam o começo e o fim da string, respectivamente, e [0-5] é um único dígito definido pelo intervalo). Você não precisa verificar a validade.

O único caso especial a ser tratado é um zero à esquerda no campo hora. Isso deve ser convertido em um espaço vazio, como mostrado nos testes de amostra.

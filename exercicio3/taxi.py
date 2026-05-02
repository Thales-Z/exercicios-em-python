def escolhe_taxi(tf1,vqr1,tf2,vqr2):
  #taxa fixa 
  #valor do km da empresa
  #calcular os valores 
  tf1 = float(tf1)
  vqr1 = float (vqr1)
  tf2 = float (tf2)
  vqr2 = float (vqr2)
  
  
  #calcular os valores
  if vqr1==vqr2 and tf1==tf2:
    return "Tanto faz"
  if tf1<= tf2 and vqr1<= vqr2:
    return "Empresa 1"
  if tf2 <=tf1 and vqr2<=vqr1:
     return "Empresa 2"
  #preciso encontrar a distancia que o valor "tanto faz"
  n = (tf1 - tf2) / (vqr1 - vqr2)
  if n<0:
    n=n*(-1)
  n = round (n,2)

    #comparo quem tem a menor taxa fixa
  if tf1 < tf2:
      melhor = "Empresa 1"
      melhor_2 = "Empresa 2"
  else:
    melhor = "Empresa 2"
    melhor_2 = "Empresa 1"
  return f"{melhor} quando a distância < {n}, Tanto faz quando a distância = {n}, {melhor_2} quando a distância > {n}"
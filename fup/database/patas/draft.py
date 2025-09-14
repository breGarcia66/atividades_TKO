chico = int(input());
cebolinha = int(input());
totAnimais = int(input());
listaAnimais = [];
contador = 0;
contadorPatas = 0;

while contador < totAnimais:
  listaAnimais.append(input());
  contador += 1;

for i in listaAnimais:
  if i == 'c' or i == 'v':
    contadorPatas += 4;
  else:
    contadorPatas += 2;

print(contadorPatas);

def conferirDiferença (valorA, valorB):
  if valorA > valorB:
    return valorA - valorB;
  elif valorB > valorA:
    return valorB - valorA;
  else :
    return 0
  
difChico = conferirDiferença(chico, contadorPatas);
difCebolinha = conferirDiferença(cebolinha, contadorPatas);

if (difChico < difCebolinha):
  print('Chico Bento');
elif difCebolinha < difChico:
  print('Cebolinha');
else :
  print('empate');
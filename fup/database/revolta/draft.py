exercito =  int(input());
listaExercito = [];
contador = 0;
while contador < exercito:
  listaExercito.append(int(input()));
  contador += 1;

listaPares = list(filter(lambda i: i % 2 == 0, listaExercito));
listaImpares =  list(filter(lambda i: i % 2 != 0, listaExercito));

somaPar = sum(listaPares);
somaImpar = sum(listaImpares);

if somaPar > somaImpar:
  print('rebeldes');
elif somaImpar > somaPar:
  print('soldados');
else:
  print('empate');
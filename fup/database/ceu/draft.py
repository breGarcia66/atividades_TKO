pedra = int(input());
contador = 0;
retorno = '[';
while contador <= 9:
  if contador != pedra:
    casa = str(contador);
    retorno += ' ' + casa;

  contador += 1;

if pedra != 10:
  retorno += ' ceu ]';
else:
  retorno += ' ]';

print(retorno);
contador = int(input());
fim = int(input());

while contador <= fim:
  if contador % 3 == 0 and contador % 5 != 0:
    print('zig');
  elif contador % 5 == 0 and contador % 3 != 0:
    print('zag');
  elif contador % 3 == 0 and contador % 5 == 0:
    print('zigzag');
  else:
    print(contador);
  contador += 1;
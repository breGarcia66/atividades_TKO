jogador_1 = input();
jogador_2 = input();

if (jogador_1 == 'P' and jogador_2 == 'R') or \
   (jogador_1 == 'R' and jogador_2 == 'S') or \
   (jogador_1 == 'S' and jogador_2 == 'P'):
   print('jog1');

elif jogador_1 == jogador_2:
   print('empate');

else:
   print('jog2');
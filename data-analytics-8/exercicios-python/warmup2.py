animais = ['Gato', 'Cachorro', 'Leão', 'Elefante', 'Girafa', 'Tigre', 'Leopardo', 'Coelho', 'Rato', 'Esquilo', 'Cavalo', 'Vaca', 'Ovelha', 'Macaco', 'Panda', 'Urso', 'Lobo', 'Zebra', 'Canguru', 'Golfinho']

animais.sort()

[print(animal) for animal in animais]

with open('animais.txt', 'w') as txt:

    [txt.write(f'{animal}\n') for animal in animais]
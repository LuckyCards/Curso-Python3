from pygame import mixer
print(f'\033[33m{"—"*30:^30}\033[m')
print(f'\033[36m{"EXERCÍCIO Nº 21":^30}\033[m')
print(f'\033[33m{"—"*30:^30}\033[m')
mixer.init()
mixer.music.load('Desafios\\only.mp3')
mixer.music.play()
print(f'\033[32m{"—"*31:^31}\033[m')
print(f'\033[36m{"EXERCÍCIO Nº 73":^31}\033[m')
print(f'\033[32m{"—"*31:^31}\033[m')

times = ('\033[36mCruzeiro eSports\033[m', '\033[36mFlamengo eSports\033[m', '\033[36mFURIA Esports\033[m', '\033[36mINTZ\033[m', '\033[36mKaBuM! e-Sports\033[m', '\033[36mLOUD\033[m', '\033[36mpaiN Gaming\033[m', '\033[36mRED Canids\033[m', '\033[36mRensga eSports\033[m', '\033[36mVorax\033[m')
print(f'Os 2 times finalistas são: {times[:2]}')
print(f'Os 3 piores times nesta temporada são: {times[:-4:-1]}')
for pos, x in enumerate(sorted(times)):
    print(f'\n{x} terminou em {pos+1}º lugar na temporada.')
import random
koin_asli = 1
koin_palsu = 0

def mengacak_koin(n):  
    global koin 
    koin = [koin_asli] * (n - 1) + [koin_palsu] * (1)
    random.shuffle(koin)
    print(koin)
    return koin
def mengetes_yang_palsu(n):
    for i in range(1,n):
        if koin[0]==koin[i]:
            pass
        elif koin[0]<koin[i]:
            return print("koin ke",1,"adalah koin yang palsu")
        else:
            return print("koin ke",i+1,"adalah koin yang palsu")
n=int(input("Masukkan Jumlah Koin:"))
mengacak_koin(n)
mengetes_yang_palsu(n)
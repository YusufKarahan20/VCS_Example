sayi = int(input("Kaç tane sayı girmek istersin:"))        
asal_sayi = 0                                            #kaç tane asal sayı olduğunu belirlemek için değişken atıyorum
asal_sayi_toplam = 0
    sayac = 0                            #sayı asal mı değil mi belirlemek için sayaç tutuyorum
    for i in range(2, x+1):
        if x % i == 0:
            sayac += 1
    if sayac == 1:
        print(x, "asal sayıdır")           
        asal_sayi += 1
        asal_sayi_toplam += x              #sayı asal ise değerini bu değişkende tutuyorum

sayi=int(input("hangi sayının faktöriyelini hesaplamak istiyorsunuz: "))


if sayi==0:
    deger=1

list=[]
while sayi != 0:
    list.append(sayi)
    sayi=sayi-1

baslangıc_indexi=0
deger=1
while len(list)> baslangıc_indexi:
    deger=list[baslangıc_indexi]*deger
    baslangıc_indexi=baslangıc_indexi+1
print(deger)

while True:

    while True:
        soru=input("tekrardan oynamak ister misiniz? (E/H): ")
    #while içerisine while yapmamız gerekiyor benim kısmımda eksik olan orasıydı.
        if "E"==soru.upper():
            sayi=int(input("hangi sayının faktöriyelini hesaplamak istiyorsunuz: "))
            if sayi==0:
                deger=1

            list=[]
            while sayi != 0:
                list.append(sayi)
                sayi=sayi-1

            baslangıc_indexi=0
            deger=1
            while len(list)> baslangıc_indexi:
                deger=list[baslangıc_indexi]*deger
                baslangıc_indexi=baslangıc_indexi+1
            print(deger)

        elif (soru.upper()) and ("H"!=soru.upper()):
            print("girdiğiniz karakter yanlıştır... tekrardan deneyiniz")

        elif "H"==soru.upper():
            print("faktöriyel alma işleminden çıkışa yönlendiriliyorsnuz...")
            exit() #exit komutu ile komuttan tamamen çıkmamızı sağlar while komutu ise döngünün altındaki while döngüsünden kurtulmasını sağlamaktadır.



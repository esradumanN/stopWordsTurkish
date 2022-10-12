import string
metin_ad=input("Türkçe bir metin giriniz: ").lower()
yeni_metin= ""
for i in metin_ad:
    if i not in string.punctuation: #noktalama isaretlerini sildim
        yeni_metin += i

f = open("stop_words_turkish", "r") #dosya okuttum
words_list=[]

for word in f: #textteki kelimeleri okuyup listeye atadik
    word = word[:-1] #/n sildik
    words_list.append(word)

kalan_metin = ""

yeni_metin2 = yeni_metin.split(" ")
for word in yeni_metin2:
    if word not in words_list:
        if kalan_metin == "":
            kalan_metin+= word
        else:
            kalan_metin = kalan_metin + " " + word #stop_wordsleri sildik

def print_edit():
    print("Noktalama işaretleri ve gereksiz kelimeler çıkarıldıktan sonra küçük harflerle kalan metin: ")
    print(kalan_metin)

    print("Kalan metindeki kelimeler ve tekrar sayıları: ")
    print("Kelime\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tTekrar Say")
    print("---------------------------------------------------------------------\t\t----------")

print_edit()

def tekrar(): #kac kez tekrar ettigini bulan fonk
    kelime_say = {}
    for word in kalan_metin.split():
        if word not in kelime_say:
            kelime_say[word] = 1
        else:
            kelime_say[word] += 1
    for key in kelime_say.keys():
        print("%s\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t %s " % (key, kelime_say[key]))

tekrar()

kalan_kelimeler = kalan_metin.split(" ")
kelime_uzunluk = []
kelime_sayi = []

for kelime in kalan_kelimeler: #uzunluklarini bulduk
    uzunluk = len(kelime)
    if uzunluk not in kelime_uzunluk: #listede yoksa listeye ekledik
        kelime_uzunluk.append(uzunluk)
        kelime_sayi.append(1)
    else: #listede varsa sayisini arttirdik
        index = kelime_uzunluk.index(uzunluk)
        kelime_sayi[index] +=1

total_list = [] #iki listeyi birlestirdik
for i in range(len(kelime_sayi)):
    temp_list = [kelime_uzunluk[i], kelime_sayi[i]]
    total_list.append(temp_list)
total_list.sort() #kücükten büyüge siraladik

def print_edit2():
    print("Kalan metindeki her uzunluktaki kelime sayıları: ")
    print("Uzunluk\tKelime Say")
    print("-------\t----------")

print_edit2()

for x in range(len(total_list)): #listedeki elemanlarinin sayilarini ve uzunluklarini yazdirdik
    print(total_list[x][0], "\t\t\t", total_list[x][1])






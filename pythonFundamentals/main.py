# Temel Veri Tipleri
print("Integer (int): ", type(1))
print("Float (float): ", type(1.5))
print("String (str): ", type("1"))
print("Boolean (bool): ", type(True))

# Integer (int):  <class 'int'>
# Float (float):  <class 'float'>
# String (str):  <class 'str'>
# Boolean (bool):  <class 'bool'>

# Bunlar, çoğunlukla Python'da sıklıkla karşılaşacağımız temel veri türleridir.

# Integer (int) veri tipi tam sayılardır.
# Float (float) veri tipi ondalıklı (virgüllü) sayılardır.
# String (str) veri tipi metin verileridir. İçerisinde sayı barındırabilir, ancak bu sayılar gerçek sayılar değildir.
# Boolean (bool) veri tipi True/False (Doğru/Yanlış) ifadeleridir.

print(3*2)
# 6

print("2" * "3")
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# Input In [3], in <cell line: 1>()
# ----> 1 "2" * "3"

# TypeError: can't multiply sequence by non-int of type 'str'

print("2" + "3")
# '23'

print("2" * 3)
# '222'

print(2 + 3)
# 5




# Listeler (Lists)
# Listeler süper esnektir, farklı veri tiplerinin birleşimden oluşabilirler ve üzerilerinde değişiklik yapmamıza izin verirler.

#     Önemli Not: Listelerin köşeli parantezler ile gösterildiğine dikkat edin!

example_list = [1,[2,3,4],3,4,5,6,7,8]
print(example_list)
# [1, [2, 3, 4], 3, 4, 5, 6, 7, 8]

print(type(example_list))
# list

print(len(example_list))
# 8

# Artık bir tuple veri yapısına sahip olduğumuza göre, ondan tek bir parça almak istersek ne yapmamız gerek?

# Tuple veri tipi içerisinde bir çok değer barındırdığı için onların içerisinden istediğimiz kısmı alabilmemiz için Python index yapısını kullanmamız gerekir.

print(example_list[1]) # Unutmayalım, Python'da index yapıları 0'dan başlayarak devam eder!
print(example_list[2])
# [2, 3, 4]
# 3


# Peki ya birden fazla elemanı almak istersem?

#     İşte o zaman verinin o kısmını ayırmam lazım.
# Python Slicing:

# # Slicing Yapısı
# ayrılacak_değişkenin_ismi[başlangıç_index : bitiş_index : atlama_sayısı]
#     Önemli Not: İndex sayıları belirtilirken başlangıç_index olarak belirttiğimiz index dahil edilirken, bitiş_index dahil edilmez!

# Sadece 3 adet index aldığımızı unutmayın; 1, 2, 3 numaralı indexler
print(example_list[1:4])
# [[2, 3, 4], 3, 4]

# Peki ya sondan 1, 2 index değeri almak istersem?

print(example_list[-2:])
print(example_list[-1])
# [7, 8]
# 8

print(example_list[0])
# 1

example_list[0] = 'DIFFERENT NOW'
print(example_list)
# ['DIFFERENT NOW', [2, 3, 4], 3, 4, 5, 6, 7, 8]
# Listelerin içerisindeki verileri değiştirebildiğimiz gibi istediğimiz parçaları çıkarabilir veya dışarıdan veri ekleyebiliriz.

# Listemize ekleme yapalım
example_list.append(2)
print(example_list)
# ['DIFFERENT NOW', [2, 3, 4], 3, 4, 5, 6, 7, 8, 2]

# Listede istenilen indexe ekleme yapalım
example_list.insert(1, "New Data")
print(example_list)
# ['DIFFERENT NOW', 'New Data', [2, 3, 4], 3, 4, 5, 6, 7, 8, 2]

# Listemizden 2 elemanını çıkaralım
example_list.remove(2)
print(example_list)
# ['DIFFERENT NOW', 'New Data', [2, 3, 4], 3, 4, 5, 6, 7, 8]

# Listeden istenilen indexteki elemanı çıkaralım
example_list.pop(2)
print(example_list)
# ['DIFFERENT NOW', 'New Data', 3, 4, 5, 6, 7, 8]

# Sözlükler (Dictionaries)
# Şu anda işlememiz gereken son ana veri tipimiz sözlüklerdir. Sözlükler şu ana kadar öğrendiğimiz veri tiplerinden farklı olarak "gruplara" sahip olmamızı sağlar, ancak indexe göre çalışmak yerine Key/Value (Anahtar/Değer) çiftlerini kullanılırlar. Bunun bazı önemli faydaları var, ancak öncesinde nasıl çalıştığını görelim.

#     Önemli Not: Sözlükler de küme parantezleriyle gösterilir, ancak bir set olarak algılanmamaları için Key ve Value değerlerinden oluşması gerekir.

new_dictionary = {'key_for_this_thing': 8}
print(new_dictionary['key_for_this_thing'])
# 8
# Sözlükler, her bir key değerinin içerisinde birden fazla farklı veri tipi bulundurabilir.

new_dictionary = {'key_for_a_list': [0,1,2,3,4], 'key_for_another_dictionary': {'bob': 1}}
print(new_dictionary['key_for_a_list'])
# [0, 1, 2, 3, 4]

print(new_dictionary['key_for_another_dictionary'])
print(new_dictionary['key_for_another_dictionary']['bob'])
# {'bob': 1}
# 1

career_stats = {'babe_ruth': {1914: ["Red Sox", 5, 10, 0], 1915:['Red Sox', 43, 104, 4]},
                'gavvy_cravath': {1914: ['Phillies',149,604,14]}}

print(career_stats['babe_ruth'])
print(career_stats['babe_ruth'][1914])
# {1914: ['Red Sox', 5, 10, 0], 1915: ['Red Sox', 43, 104, 4]}
# ['Red Sox', 5, 10, 0]

# Ek olarak sadece key ve value değerine de ulaşılabilir.
print(career_stats.keys())
print(career_stats.values())
# dict_keys(['babe_ruth', 'gavvy_cravath'])
# dict_values([{1914: ['Red Sox', 5, 10, 0], 1915: ['Red Sox', 43, 104, 4]}, {1914: ['Phillies', 149, 604, 14]}])
# Sözlükleri sevmemizin nedeni, veri almada gerçekten hızlı olmaları ve içermek istediğimiz her değere bir anahtar atamamıza izin vermeleridir.

# Değişken İsimleri
# Değişken isimleriyle ilgili bir kaç kuraldan da bahsetmesek olmaz. Genel olarak, şu kurala bağlı kalmak mantıklıdır,

    # Sarhoş halim bu değişkenin isminden ne için kullanıldığını anlayabilir mi? Anlayamıyorsanız, değiştirin!

# Bu kuralı biraz daha detaylandıracak olursak,

    # Değişken isimleriniz anlamlı ifadelerden oluşmalı. Örneğin, x anlamlı bir ifade değildir.
    # Uzun değişken isimleri anlamsız değişken isimlerine göre bile tercih edilir. Kısa, ancak anlamlı isimler her zaman daha iyidir.
    # Boşlukları temsil etmek için _ kullanın. (Bu genel bir Python kuralıdır)
    # Büyük harfli içeren yazımlardan kaçının.
    # Python uluslararası alanda oldukça popüler olan bir programlama dilidir, ilerleyen aşamalarda araştırma yaparken bile İngilizce bilgisi bizi her zaman öne taşıyacak. Bu sebeple, mümkünse kodlarımızı İngilizce olarak yazmak her zaman daha iyidir.

# Bazı örnek değişken isimleri:

    # customer_order_value, ordered_document_list, mlb_batting_statistics_1887_1990

# İçeriğini görmeden bile, bu değişkenlerin içinde ne tarz bilgiler barındırdığını tahmin edebiliyorum. İşte bu bizim istediğimiz stil!


# Koşullu İfadeler (If / Elif / Else)

# Gerçek hayatta, genellikle etrafımızdaki bilgileri değerlendirmeli ve ardından gözlemlediklerimize göre bir hareket tarzı seçmeliyiz.

    # Hava güzelse dışarı çıkacağım. (Hava güzel değilse dışarı çıkmayacağım anlamına gelir.)

# Python'da if yapısı bu tür karar verme seçeneklerini yönetmek için kullanılırız. Belirtilen durumun gerçekleşmesi durumunda bu yöntemi izle, gerçekleşmediği durumlarda ise şu yöntemi izle mantığı vardır.

if 3 > 4:
    print("3 is bigger")
print("3 is not bigger")
# 3 is not bigger


number = 10
if number < 5:
    print(number, 'is smaller than 5')
if number < 12:
    print(number, 'is smaller than 12')
if number < 25:
    print(number, 'is smaller than 25')
# 10 is smaller than 12
# 10 is smaller than 25


number = 10
if number < 5:
    print(number, 'is smaller than 5')
elif number < 12:
    print(number, 'is smaller than 12')
elif number < 25:
    print(number, 'is smaller than 25')
# 10 is smaller than 12
# 2'den fazla koşul belirtmek de mümkündür


a = 30
b = 20 
c = 10
if a < b or b > c:
    print("a is bigger than b AND b is bigger than c")
elif a < b or b < c:
    print("a is smaller than b AND b is smaller than c")
else:
    print("These conditions did not hold")
# a is bigger than b AND b is bigger than c


number_list = [10,20,30,40,50]
if 60 in number_list:
    print("Yes!")

# Peki ya liste içerisinde tüm elemanları belirli bir işleme tabi tutmak istersem?

# Döngüler (For / While)
# Döngü, aynı kod bloğunun potansiyel olarak birçok kez tekrar tekrar yürütülmesi anlamına gelir. Python'da döngü kurabileceğimiz 2 temel yapı vardır:

    # For & While Döngüleri.
# Ancak veri biliminde yapılan çalışmalarda genellikle for döngüleri çok daha yaygın bir şekilde kullanılırlar.

for number in number_list:
    new_number = number * 5 / 3
    print(new_number)
# 16.666666666666668
# 33.333333333333336
# 50.0
# 66.66666666666667
# 83.33333333333333

x = 0
while x < 10:
    print(x)
    x += 1
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9


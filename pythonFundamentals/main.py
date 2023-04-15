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

# Fonksiyonlar - Yazılanları Sürekli Tekrar Etmeme Sanatı
# Eğer bir gün kendini önceden yazdıklarını kopyala-yapıştır yaparken yakalarsan, hayır bunu yapma...

# Önceden yazdığımız kodlar hiç bir zaman kopyala-yapıştır yapılmamalı. Peki ben önceden yaptığım bir işlemi, şu anda çalıştığım satıra nasıl taşıyacağım?

    # İşte bunun çözümü fonksiyonlar oluşturmak.

# Diyelim ki satış kaydından bir kullanıcınin verilerini almak ve o tabloda bir kullanıcıyı kaç kez gördüğümü takip etmek istediğim bir grup veriyi işliyorum.

table1 = [['Sam', 36, 85.95],
 ['Carol', 75, 53.65],
 ['Sam', 90, 95.37],
 ['Doug', 61, 19.8],
 ['Sam', 41, 45.22],
 ['Doug', 29, 42.98],
 ['Oliver', 61, 95.74],
 ['Carol', 32, 17.12],
 ['Tari', 27, 68.83],
 ['Tari', 81, 62.47]]

name_counter = {}
for row in table1:
    name = row[0]
    if name in name_counter.keys():
        name_counter[name] += 1
    else:
        name_counter[name] = 1
print(name_counter)
# {'Sam': 3, 'Carol': 2, 'Doug': 2, 'Oliver': 1, 'Tari': 2}

# Peki elime yeni bir tablo daha geldi ve tekrardan aynı işlemi yapmam gerekiyor.

# Elimde 2 seçeneğim var,

    # Ya üstte yazdığım ifadeyi kopyala-yapıştır yapıcam?
    # Ya da üstte yazdığım ifadeyi bir fonksiyona dönüştürücem?

# Hadi bu sefer fonksiyona dönüştürmeyi deneyelim,

def count_names_in_tables(table_to_count):
    """
    İlk sütunu kullanıcının adından oluşacak şekilde, bir tablo verisi alır
    ve her bir kullanıcının tabloda kaç defa geçtiğini bulur.
    ---
    Girdi: Tablo (bir çok listeden oluşan bir liste)
    Çıktı: Sözlük (İsimler key değerleri, kaç defa geçtikleri value değerleri)
    """
    name_counter = {}
    for row in table_to_count:
        name = row[0]
        if name in name_counter.keys():
            name_counter[name] += 1
        else:
            name_counter[name] = 1
    return name_counter
print(count_names_in_tables(table1))
# {'Sam': 3, 'Carol': 2, 'Doug': 2, 'Oliver': 1, 'Tari': 2}

table2 = [['Oliver', 12, 49.95],
 ['Tari', 76, 30.71],
 ['Carol', 98, 25.07],
 ['Carol', 24, 11.85],
 ['Carol', 34, 13.36],
 ['Kelly', 14, 34.31],
 ['Tari', 6, 86.11],
 ['Tari', 90, 29.08],
 ['Carol', 55, 45.61],
 ['Sam', 88, 97.47]]

print(count_names_in_tables(table2))
# {'Oliver': 1, 'Tari': 3, 'Carol': 4, 'Kelly': 1, 'Sam': 1}

# Belge Dizini Yapıları
# Belge dizileri, o şeyin işlevini tanımlamaya yardımcı olan ve özellikle fonksiyon yapılarından sonra gelen üç tırnaklı dizelerdir.

def multiply_by_two(number):
    """
    Bu fonksiyon girdi olarak girilen değeri 2'yle çarpar
    ---
    Girdi: Sayısal
    Çıktı: Sayısal
    """
    return 2*number
multiply_by_two(4)
# 8

multiply_by_two("4")
# '44'

# Enumerate
# Bazı durumlarda elemanlarımızın index numaralarına erişme ve onlarla çalışma ihtiyacı duyarız. Bu amaç doğrultusunda eğer satırın index numaralarına ihtiyacım varsa bu konuda enumerate fonksiyonundan yararlanabiliriz.

for ix, row in enumerate(table1):
    print(ix, row, table1[ix])
# 0 ['Sam', 36, 85.95] ['Sam', 36, 85.95]
# 1 ['Carol', 75, 53.65] ['Carol', 75, 53.65]
# 2 ['Sam', 90, 95.37] ['Sam', 90, 95.37]
# 3 ['Doug', 61, 19.8] ['Doug', 61, 19.8]
# 4 ['Sam', 41, 45.22] ['Sam', 41, 45.22]
# 5 ['Doug', 29, 42.98] ['Doug', 29, 42.98]
# 6 ['Oliver', 61, 95.74] ['Oliver', 61, 95.74]
# 7 ['Carol', 32, 17.12] ['Carol', 32, 17.12]
# 8 ['Tari', 27, 68.83] ['Tari', 27, 68.83]
# 9 ['Tari', 81, 62.47] ['Tari', 81, 62.47]

# List Comprehensions
# List Comprehensions, mevcut listelere dayalı listeler tanımlamanın ve oluşturmanın oldukça etkili bir yoludur. Liste oluşturmak için normal fonksiyonlardan ve döngülerden genellikle daha kompakt ve daha hızlıdır. Ancak, kodun kullanıcı dostu olmasını sağlamak için çok uzun List Compherensions'ları tek bir satıra yazmaktan kaçınmalıyız.

a_list_of_numbers = [1,2,3,4,5,7]

new_list_of_numbers = [x + 1 for x in a_list_of_numbers if x > 2]
print(new_list_of_numbers)
[4, 5, 6, 8]
new_list = []
for number in a_list_of_numbers:
    if number > 2:
        new_list.append(number + 1)
new_list
# [4, 5, 6, 8]

# Lambda Fonksiyonu ve Sıralama İşlemleri
# Python'da sıralama işlemleri yapabilmek için elimizde 2 farklı yolumuz vardır. Şimdi bunları aşağıdaki örneklerle görelim ve aralarındaki farkı anlamaya çalışalım.

# Sütunlar = (İsim, Yaş, Maaş)
alumni = [('bob',32,72000),
          ('alice',29,115000),
          ('charlie',25,95000)]

print(sorted(alumni)) # Sıralama işlemleri için kullanılan fonksiyon
print(alumni)
# [('alice', 29, 115000), ('bob', 32, 72000), ('charlie', 25, 95000)]
# [('bob', 32, 72000), ('alice', 29, 115000), ('charlie', 25, 95000)]

# Sorun ne? Aslında sorted fonksiyonunu çalıştırdığımızda istediğimiz sonucu vermişti? Ama orijinal verimizi değiştirmemiş...

# Bir de bu yazım şekliyle deneyelim.

alumni.sort() # sort fonksiyonu sıralamayı orijinal veri üzerinde gerçekleştirdi
print(alumni)
# [('alice', 29, 115000), ('bob', 32, 72000), ('charlie', 25, 95000)]

# Şimdi oldu! Çünkü sorted(alumni) fonksiyonunu çalıştırdığımda verinin orijinal halini değiştirmek yerine, aslında bana değerlerimizin sıralı halini yeni bir liste olarak tanımlamış oldu.

# Genellikle sorted fonksiyonunu kullanmak .sort fonksiyonuna nazaran daha güvenli bir işlemdir, çünkü yanlışlıkla .sort fonksiyonunu kullanırsanız, orijinal verinizi komple değiştirmiş olursunuz.

# Ama sıralama işlemlerimizi şu ana kadar hep ilk sütundaki (isim) alfabetik sıraya göre yaptık. Şimdi de değerleri biraz tersten sıralamayı biraz da maaş sütununa göre sıralamayı inceleyelim.

print(sorted(alumni, reverse=True))
# [('charlie', 25, 95000), ('bob', 32, 72000), ('alice', 29, 115000)]

# İlk sütun dışında bir değere göre sıralama yapmak için Python'a nasıl sıralanacağını söylememiz gerekir. Bu iş, bir lambda fonksiyonu için harika bir kullanımdır. Lambda fonksiyonları, kaydetmek istemediğimiz fonksiyon tanımlamalarıdır. İşlevlerini sadece bir satırda tamamlamalarını ve sonra hafıza alanını çalmamalarını isteriz.

print(sorted(alumni, key=lambda row: row[2]))
# [('bob', 32, 72000), ('charlie', 25, 95000), ('alice', 29, 115000)]

alumni.sort(key=lambda row: row[2], reverse=True)
print(alumni)
# [('alice', 29, 115000), ('charlie', 25, 95000), ('bob', 32, 72000)]

# sorted fonksiyonu için key parametresi, her bir verinin hangi parçasına göre sıralamak istediğimizi tanımlayan bir fonksiyon alır. Burada ikinci indexteki (maaş) bilgilerine göre sıralama yapmasını söyledik. İşlevin kendisi çok ilginç değil, bu çizginin ötesinde yaşamasını istemiyoruz.

# Bu ifadeyi sonrasında tekrardan kullanabilmek için bir fonksiyon yapısına dönüştürecek olursak ise...

def get_second_column_of_row(row):
    """
    Satırda bulunan 2. indexe ait değerleri döndürür.
    """
    return row[2]

print(sorted(alumni, key=get_second_column_of_row))
# [('bob', 32, 72000), ('charlie', 25, 95000), ('alice', 29, 115000)]

# Ama gerçekçi olmak gerekirse, bu fonksiyonu isim alanıma kaydetmek istemiyorum, bir daha da asla istemeyeceğim. Bunun yerine, tüm kodumu tek kullanımlık fonksiyonlarla kirletmeden davranışı tanımlamak için lambda fonksiyonu kullanıyoruz. Lambda fonksiyonu, özellikle map veya filter fonksiyonlarını kullanmak gibi işler yaparken, python dilinin ortak bir parçasıdır. Ama bunlar şimdilik başka bir zamanın tartışma konusu.

# Hata Mesajları
# Python'da yazdığımız kod bloğu içerisinde beklenmedik durumlarla karşılaşıldığında, hata mesajları vermeye başlar ve o hatanın sebebini çözene kadar yapmak istediğimiz işlemi bizim için askıya alır.

# Ancak bazı durumlarda yazdığımız kodların doğru şekilde kullanılmasını sağlamak için kendimiz hata mesajları tanımlama ihtiyacı hissederiz.

class_list = [1,2,3]
if len(class_list) % 2 != 0:
    raise ValueError("List should have an even number of elements!") # Tanımladığımız hata mesajı
# ---------------------------------------------------------------------------
# ValueError                                Traceback (most recent call last)
# Input In [49], in <cell line: 2>()
#       1 class_list = [1,2,3]
#       2 if len(class_list) % 2 != 0:
# ----> 3     raise ValueError("List should have an even number of elements!")

# ValueError: List should have an even number of elements!

# İstenmeyen durumlarla başa çıkmak için assert fonksiyonunu da kullanabiliriz.

def sum_up_a_list(list_to_sum):
    """
    Girdi olarak bir sayı listesi alır ve liste
    içerisindeki sayıların toplamını hesaplar.
    """
    # Girdi olarak verilen değerler list yapısında olsun istiyorum
    assert type(list_to_sum) == list, "Input must be a list!"
    return sum(list_to_sum)

print(sum_up_a_list(3))
# ---------------------------------------------------------------------------
# AssertionError                            Traceback (most recent call last)
# Input In [50], in <cell line: 10>()
#       7     assert type(list_to_sum) == list, "Input must be a list!"
#       8     return sum(list_to_sum)
# ---> 10 print(sum_up_a_list(3))

# Input In [50], in sum_up_a_list(list_to_sum)
#       2 """
#       3 Girdi olarak bir sayı listesi alır ve liste
#       4 içerisindeki sayıların toplamını hesaplar.
#       5 """
#       6 # Girdi olarak verilen değerler list yapısında olsun istiyorum
# ----> 7 assert type(list_to_sum) == list, "Input must be a list!"
#       8 return sum(list_to_sum)

# AssertionError: Input must be a list!

print(sum_up_a_list([1,2,3]))
# 6

# Try - Except
# try-except, hatalara anında tepki verebilen kod oluşturmanın harika bir yoludur. Yapmamız gereken, try ifadesinin içine çalışmasını istediğimiz kod bloğu koymak, ardından except ifadesine de try kısmında yazdığımız kodda bir hata meydana geldiğinde de "nasıl bir davranış izlemesini istediğimizi belirtiriz".

x = "1" # 1 sayısının string versiyonu, bununla matematiksel işlemler gerçekleştirilemez

try:
    print("Trying to divide")
    print(x/2)
    print("This won't happen because of the error")
    
except:
    print("\nOops, forgot to make it a number")
    print(int(x)/2)
# Trying to divide

# Oops, forgot to make it a number
# 0.5

del x # del fonksiyonu tanımladığımız değişkeni tamamen silmemizi sağlar

try:
    str(x)
except:
    print("¯\_(ツ)_/¯")
# ¯\_(ツ)_/¯

# Referans Değerler vs Gerçek Değerler

a = [1,2,3]
b = a
b.append(4)

# Aslında sadece b listesine bir ekleme yapmamıza rağmen, neden a listesine de aynı eklemeyi yaptı?
print(a)
print(b)
# [1, 2, 3, 4]
# [1, 2, 3, 4]

# b = a yazımı bizim için b adını verdiğimiz yeni bir değişken tanımlamaz. Sadece b değişkenimizi a değişkenine bağlı yeni bir değişken olarak oluşturur.

# Eğer yeni bir değişken oluşturmak istersek, a değişkenindeki değerleri kullanarak yeni bir veri yapısı tanımlamamız gerekir (Python'a a değişkenindeki değerleri kullanarak bir liste veri tipine yazarak oluşturulan bu listeyi b değişkenine eşitle gibi).

a = [1,2,3]
b = a.copy()
b.append(4)

print(a)
print(b)
# [1, 2, 3]
# [1, 2, 3, 4]

# Özet
# Python'da kodlama yaparken yalnızca en yaygın yazım standartlarının bazılarına değindik. Eğer incelemek isterseniz, standartların burada bulunabilecek daha bir çok bölümü var:
    # https://peps.python.org/pep-0008/

    
    
    # HATIRLATMA: Gelecekte kendinin ve ekip arkadaşlarının size teşekkür etmeleri için kodlarınızı kolay okunabilir ve anlaşılabilir bir şekilde yazmayı unutmayın :)
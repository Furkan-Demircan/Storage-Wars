from abc import ABC, abstractmethod
import random
import gc
import time

minRate = 9
maxRate = 12


# Base class
class DepoSavaslari(ABC):

    # Tum Classlarda override edilmesi gereken info methodu abstract method olarak tanimlarin
    @abstractmethod
    def info(self):
        pass

    # rastgele sayi alirken kullanilacak olan static  method
    @staticmethod
    def getRandomNumber(minValue, maxValue):
        return random.randrange(minValue, maxValue)

# Depolarin bilgilerini ve methodlarini tutan class
class Warehouse(DepoSavaslari):
    # constructor tanimlanir
    def __init__(self, warehouseID, value, auctionValue: int, productList=[]):
        self.__warehouseID = warehouseID
        self.__productList = productList
        self.__value = value
        self.__auctionValue = auctionValue

    # Depo bilgilerini gosteren method
    def info(self):
        print(f"""
Depo ID`si: {self.__warehouseID}
Depo Fiyati: {self.__value}
Deponun icindeki urunlerin listesi: {self.__productList}
                """)

    # Deponun içine rastgele ürünler atar ve depo olusturur.
    def randomWarehouseCreator(self, productList):
        result = random.randint(3, 8)
        listLength = len(productList)
        list = []
        for i in range(result):
            randIndex = self.getRandomNumber(0, listLength)
            list.append(productList[randIndex])
        self.__productList = list

    # Deponun fiyatini hesaplayan method
    def setWarehouseValue(self):
        result = 0
        productList = self.__productList
        for i in productList:
            result = result + i.getValue()
            self.__value = int(result/len(productList))
        return self.__value

    # Deponun acik arttirmaya baslama fiyatini hesaplayan method
    def setAuctionValue(self):
        value = self.__value
        auctionValue = random.uniform(
            value-value*0.3, value + value*0.1)
        self.__auctionValue = int(auctionValue) + 10

# getter methods
    # Deponun ID'sini return ettiren method
    def getID(self):
        id = self.__warehouseID
        return id

    # deponun acik arttirmaya baslama fiyatini return ettiren method
    def getAuctionValue(self):
        value = self.__auctionValue
        return value

    # Deponun icindeki urun listesini getirmeye yarayan method
    def getProductList(self):
        productList = self.__productList
        return productList


# magazalarin bilgilerini ve methodlarini tutan class
class Shop(DepoSavaslari):
    def __init__(self, name, minValue, maxValue):
        self.__name = name
        self.__minValue = minValue
        self.__maxValue = maxValue

    # Magazanin bilgilerini return ettiren method
    def info(self):
        print(f"""
 Magaza Adi: {self.name}
 Magaza Sermaye: {self.__balance}
                """)

    # magazanin urunlere teklif vermesini saglayan method
    def buyValue(self, object):
        value = object.getValue()
        minValue = value - value*self.__minValue/100
        maxValue = value + value*self.__maxValue/100
        value = int(random.uniform(minValue, maxValue))
        return value

# getter methods
    # Magazanin ismini degistirmeye yarayan method
    def getName(self):
        name = self.__name
        return name


# Urunlerin blgilerini ve methodlarini tutan Class
class Product(DepoSavaslari):
    productList = []

    # constructor tanimlanir
    def __init__(self, name, categories, productionDate, value):
        self.__name = name
        self.__infrequency = categories
        self.__productionYear = productionDate
        self.__value = value

    # Urun bilgilerini gosteren method
    def info(self):
        print(f"""Urun Adi: {self.__name}
Urun Nadirligi : {self.__infrequency}
Urun Uretim Tarihi: {self.__productionYear}
Tahmini Urun Fiyati: {self.catchValue()}""")

# setter methods
    # urunun degerini degistirmeye yarayan method
    def setValue(self, newValue):
        self.__value = newValue

# getter methods
    # Urunun fiyatini return ettiren method
    def getValue(self,):
        value = self.__value
        return value

    # urunun nadirlik seviyesini getiren method
    def getCategories(self):
        categories = self.__infrequency
        return categories

    # urunun yapim yilini getiren method
    def getProductionDate(self):
        return self.__productionYear
    
    # urunlerin tahmini fiyatini belirleyen method
    def catchValue(self):
        value = self.__value
        minValue = value - value*0.1
        maxValue = value + value*0.1
        return self.getRandomNumber(int(minValue), int(maxValue))

    # Urunlerin Listesini getiren class method
    @classmethod
    def getProductList(cls):
        return cls.productList


# Acik arttirmanin bilgilerini ve methodlarini tutan class
class Auction():
    def __init__(self,  customerList: list, warehouse: Warehouse):
        self.__lastBidValue = warehouse.getAuctionValue()
        self.__isDone = False
        self.__customerList = customerList
        self.__lastBidCustomerId = None

# getter methods
    # depoya verilen son fiyati return ettiren method
    def getLastBidValue(self):
        value = self.__lastBidValue
        return value

    # Depoya son teklif veren alicinin ID'sini return ettiren method
    def getLastBidCustomerId(self):
        value = self.__lastBidCustomerId
        return value

    # Deponun kazananini return ettiren method
    def getWinner(self):
        value = self.__winner
        return value

    # acik arttirmadaki kisilerin listesini dondurmeye yarayan method
    def getCustomerList(self):
        value = self.__customerList
        return value

# setter methods
    # Son teklif fiyatini ve son teklif veren alicinin ID'sini degistiren method
    def setLastBidValue(self, value, customerId):
        self.__lastBidValue = value
        self.__lastBidCustomerId = customerId

    # Acik arttirma bittiginde yapilmasi gereken islemleri yapan method
    def completeAuction(self, customer):
        self.__isDone = True
        self.__winner = customer
        customer.winAuction(self.__lastBidValue, depo.getProductList().copy())

    # Acik arttirmadan ayrilanlari listeden silen method
    def removeCustomer(self, customer):
        self.__customerList.remove(customer)

    # Alicilari siralayan method
    def sortCustomer(self, customer):
        self.__customerList.sort(reverse=True, key=customer.getIsAI)


# Alicilarin bilgilerini tutan class
class Customer(DepoSavaslari, ABC):
    def __init__(self, id, name, surname, age, gender, isBid, money, inventory: list, isAI=True):
        self.__id = id
        self.__name = name
        self.__surname = surname
        self.__age = age
        self.__gender = gender
        self.__inventory = inventory
        self.__money = money
        self.__inAuction = True
        self.__isBid = isBid
        self.__isAI = isAI
        self.__lastBidValue = 0
        self.__canBid = True

    # Alicinin bilgilerini return ettiren method
    def info(self):
        print(f"""
Alici Adi: {self.__name}
Alicinin Soyadi : {self.__surname}
Alicinin yasi: {self.__age}
Alicinin cinsiyeti: {self.__gender}
Alicinin sahip oldugu urunler: {self.__inventory}
Alicinin parasi : {self.__money}
                """)

# getter methodlari
    # alicinin ID'sini return ettiren method
    def getId(self):
        value = self.__id
        return value

    # Alicinin adini return ettiren method
    def getName(self):
        name = self.__name
        return name

    # Alicinin soyadini return ettiren method
    def getSurname(self):
        surname = self.__surname
        return surname

    # Alicinin parasin return ettiren method
    def getMoney(self):
        money = self.__money
        return money

    # Alicinin envanterini return ettiren method
    def getInventory(self):
        inventory = self.__inventory
        return inventory

    # alicinin son verdigi teklifi return ettiren method
    def getLastBidValue(self):
        value = self.__lastBidValue
        return value

    # alicinin bot olup olmadigini return ettiren method
    def getIsAI(self):
        value = self.__isAI
        return value

    # alicinin hala acik arttirmada olup olmadigini return ettiren method
    def getInAuction(self):
        value = self.__inAuction
        return value

    # alicinin teklifini getiren method
    def getBid(self):
        value = self.__lastBidValue
        return value

    def getCanBid(self):
        value = self.__canBid
        return value

# Setter methodlari
    # Alicinin parasini degistirmeye yarayan Method
    def setMoney(self, newMoney):
        self.__money = newMoney

    # alicinin teklif verip vermedigini degistiren method
    def setIsBid(self, value):
        self.__isBid = value

    # alicinin teklif verebilip veremeyecegini degistiren method
    def setCanBid(self, value):
        self.__canBid = value

    # alicinin son verdigi teklifi degistiren method
    def setLastBidValue(self, value):
        self.__lastBidValue = value

    # alicinin acik arttirmanin icinde olup olmadigini degistiren method
    def leaveAuction(self):
        self.__inAuction = False

    # Urun satiminda yapilmasi gereken seyleri yapam method
    def sellItem(self, fiyat, item: Product):
        money = self.getMoney()
        money = money + fiyat
        self.setMoney(money)
        self.deleteItemInventory(item)

    # alicinin her yeni acik arttirmada sifirlanmasi gereken attributelari degistiren method
    def resetCustomer(self):
        self.__lastBidValue = 0
        self.__inAuction = True
        self.__canBid = True

    # alicinin acik arttirmayi kazandiginda yapilacak islemleri tutan fonksiyon
    def winAuction(self, value, warehouseItems: list):
        self.__money = self.__money - value
        for item in warehouseItems:
            self.__inventory.append(item)

    # urunu envanterden silen method
    def deleteItemInventory(self, item: Product):
        list = self.__inventory
        list.remove(item)

    @abstractmethod
    def applyBid(self, auction: Auction):
        pass


# Oyuncunun bilgilerini ve methodlarini tutan class
class Player(Customer):
    def __init__(self, id, name, surname, age, gender, isBid, money, inventory):
        super().__init__(id, name, surname, age, gender, isBid, money, inventory, False)

    # Oyuncunun teklif verdiginde yapilmasi gereken islemleri yapan method
    def applyBid(self, auction: Auction):
        if self.getInAuction() == True:
            if self.getCanBid() == True:
                if auction.getLastBidCustomerId() == self.getId():
                    print(
                        f"{self.getName()} en yuksek teklifi verdigi icin sira atlaniyor\n")
                else:
                    bidValue = auction.getLastBidValue()
                    if bidValue < self.getMoney():
                        maxBidValue = bidValue + bidValue*20/100
                        while True:
                            print(
                                f"Paraniz: {self.getMoney()}\nDepoya verilen son teklif: {auction.getLastBidValue()}\n1-Teklif ver\n2-Teklif verme\n3-Acik arttirmadan cekil\n")
                            result = int(
                                input("Yapmak istediginiz islemi seciniz: "))
                            if result == 1:
                                print(
                                    f"Paraniz: {self.getMoney()}\n{int(auction.getLastBidValue())}-{int(maxBidValue)} degerleri arasinda bir deger giriniz!")
                                lastBidValue = int(
                                    input("Teklif vermek istediginiz tutari giriniz: "))
                                if lastBidValue != bidValue:
                                    if lastBidValue <= self.getMoney():
                                        if lastBidValue >= auction.getLastBidValue() and lastBidValue <= maxBidValue:
                                            self.setIsBid(True)
                                            auction.setLastBidValue(
                                                lastBidValue, self.getId())
                                            self.setLastBidValue(lastBidValue)
                                            print(
                                                f"""-------------------------------\n{self.getName()} teklif veriyor!\nVerdiginiz Teklif: {self.getLastBidValue()}\n-------------------------------""")
                                            return lastBidValue
                                        else:
                                            print(
                                                "\nBelirtilen aralikta deger giriniz!\n")
                                    else:
                                        print(
                                            "\nParanizdan yuksek deger giremezsiniz!\n")
                                else:
                                    print(
                                        "\nBaskasiyla ayni teklifi veremezsiniz!\n")
                            elif result == 2:
                                self.setIsBid(False)
                                print(f"\n{self.getName()} teklif vermedi\n")
                                return auction.getLastBidValue()
                            elif result == 3:
                                self.leaveAuction()
                                print(
                                    f"{self.getName()} acik arttirmadan ayrildi\n")
                                auction.removeCustomer(self)
                                return auction.getLastBidValue()
                            else:
                                print("Lutfen gecerli bir sayi giriniz!")
                    else:
                        print(
                            "Paraniz yetmediginden dolayi acik arttirmadan cekiliyorsunuz! :(\n")
                        self.leaveAuction()
                        self.setCanBid(False)
                        auction.removeCustomer(self)


# Bilgisayar oyuncularinin bilgilerini ve methodlarini tutan class
class AI(Customer):
    def __init__(self, id, name, surname, age, gender, isBid, money, inventory):
        super().__init__(id, name, surname, age, gender, isBid, money, inventory)

    # Botlar teklif verdiginde yapilmasi gereken islemleri yapan method
    def applyBid(self, auction: Auction):
        if self.getInAuction() == True:
            if self.getCanBid() == True:
                if auction.getLastBidCustomerId() == self.getId():
                    print(
                        f"{self.getName()} en yuksek teklifi verdigi icin sira atlaniyor")
                else:
                    bidValue = auction.getLastBidValue()
                    if bidValue < self.getMoney():
                        result = self.getRandomNumber(0, 16)
                        if result <= minRate:
                            maxBidValue = bidValue + bidValue*0.2
                            lastBidValue = self.getRandomNumber(
                                int(auction.getLastBidValue())+1, int(maxBidValue))
                            if lastBidValue > self.getMoney():
                                lastBidValue = self.getMoney()
                            auction.setLastBidValue(
                                lastBidValue, self.getId())
                            self.setLastBidValue(lastBidValue)
                            self.setIsBid(True)
                            print(
                                f"""-------------------------------\n{self.getName()} teklif veriyor!\nVerdigi Teklif: {self.getLastBidValue()}\n-------------------------------""")
                            return lastBidValue
                        elif result > minRate and result <= maxRate:
                            self.setIsBid(False)
                            print(f"\n{self.getName()} teklif vermedi\n")
                            return auction.getLastBidValue()
                        else:
                            self.leaveAuction()
                            self.setIsBid(False)
                            print(f"{self.getName()} acik arttirmadan ayrildi\n")
                            auction.removeCustomer(self)
                            return auction.getLastBidValue()
                    else:
                        print(
                            f"{self.getName()} Parasi yetmediginden dolayi acik arttirmadan cekildi! :(\n")
                        self.leaveAuction()
                        self.setCanBid(False)
                        auction.removeCustomer(self)

# UI ile ilgili kodalar
# region


def mainMenu():
    print("""
1-Depo acik arttirmasina katil
2-Envanterine bak
3-Urun sat
0-Cikis
    """)
# endregion


# Obje ve gereli tanimlamalarin yapildigi yer
# region
# Urun tanimlamalari
mouse = Product("mouse", "Cok Yaygin", "2021", 5)
kulaklik = Product("kulaklik", "Cok Yaygin", "2022", 30)
borcam = Product("borcam", "Cok Yaygin", "2020", 3)
kettle = Product("kettle", "Cok Yaygin", "2022", 1)
televizyon = Product("televizyon", "Yaygin", "2022", 399)
soba = Product("soba", "Yaygin", "1090", 80)
saat = Product("saat", "Cok Nadir", "2017", 7000)
telefonKilifi = Product("telefon Kilifi", "Cok Yaygin", "2020", 3)
duba = Product("duba", "Cok Yaygin", "2020", 1)
aycicekYagi = Product("aycicek Yagi", "Efsanevi", "2022", 100)
ayakkabi = Product("ayakkabi", "yaygin", "2022", 39)
antikaTablo = Product("antikaTablo", "Efsanevi", "1940", 5000)
corap = Product("corap", "Efsanevi", "1940", 1)
damacana = Product("damacana", "Cok Yaygin", "2022", 1)
gramAltin = Product("gram Altin", "Yaygin", "2022", 55)
netflixHediyeKarti = Product("netflix Hediye Karti", "Cok Yaygin", "2022", 7)
matkap = Product("matkap", "Yaygin", "2022", 20)
cuval = Product("cuval", "Cok Yaygin", "2022", 1)
OyuncuKoltugu = Product("Oyuncu Koltugu", "Yaygin", "2022", 49)
vantilator = Product("vantilator", "Cok Yaygin", "2020", 9)
kisLastigi = Product("kis Lastigi", "Nadir", "2020", 50)
dolap = Product("dolap", "Nadir", "2010", 12)
kasa = Product("kasa", "Nadir", "2015", 52)
bisiklet = Product("bisiklet", "Nadir", "2019", 30)
tencere = Product("tencere", "Cok Yaygin", "2021", 6)
scooter = Product("scooter", "Yaygin", "2019", 30)
makas = Product("makas", "Cok Yaygin", "2018", 1)
kurek = Product("kurek", "Cok Yaygin", "2012", 4)
tohum = Product("tohum", "Efsanevi", "1960", 1000)
tepsi = Product("tepsi", "Cok Yaygin", "2005", 2)
usbKablo = Product("usbKablo", "Cok Yaygin", "2022", 1)
gramofon = Product("gramofon", "Cok Nadir", "1980", 600)
durTabelasi = Product("dur Tabelasi", "Cok Nadir", "2022", 5)
sabun = Product("sabun", "Cok Nadir", "2022", 1)
vazo = Product("vazo", "yaygin", "2022", 5)
tespih = Product("tespih", "yaygin", "2020", 2)
canta = Product("canta", "yaygin", "2020", 15)
balon = Product("balon", "cok yaygin", "2022", 1)
romanTaslak = Product("dostoyevski'nin roman taslaklari",
                      "Efsanevi", "1900", 3500)
cubaMotor = Product("cuba Motor", "yaygin", "1970", 10000)
iranHalisi = Product("iran Halisi", "Efsanevi", "2090", 1500)
bufaloKafsi = Product("bufalo Kafasi", "Nadir", "2015", 80)


# magaza tanimlamalari
magaza1 = Shop("Ölucu Mehmet", 15, 10)
magaza2 = Shop("Spotcu Mahmut", 15, 20)
magaza3 = Shop("Antikaci Faruk", 10, 20)

# Oyuncu ve bot tanimlamalar
player = Player(1, "Furkan", "Demircan", 19, "erkek", True, 500, [])
alici2 = AI(2, "Eren", "Elagoz", "12", "erkek", True, 300, [])
alici3 = AI(3, "Ahmet", "Fatih", "19", "Erkek", True, 600, [])
alici4 = AI(4, "Mucahit", "Faruk", "19", "Erkek", True, 400, [])
alici5 = AI(5, "Akif", "Ayan", "19", "Erkek", True, 500, [])
depo = Warehouse("1", 0, [])
#productList = Product.productList
productList = []
customerList = [player, alici2, alici3, alici4, alici5]
loop = True

for item in gc.get_objects():
    if isinstance(item, Product):
        productList.append(item)
# endregion

# alici listesi siralamasi yaoilirken kullanilan fonksiyon


def sortCustomers(customer: Customer):
    return customer.getIsAI()


while True:
    mainMenu()
    result = input(
        "Lutfen islem yapmak istediginiz menunun numarasini giriniz: ")
    if result == "1":
        result1 = input(
            "Katilmak istediginize emin misiniz?\n1-Evet\n2-Hayir\n")

        if result1 == "1":
            depo.randomWarehouseCreator(productList.copy())
            depo.setWarehouseValue()
            depo.setAuctionValue()
            auction = Auction(customerList.copy(), depo)
            print(
                f"""\n------------------------------\nAcik arttirma {depo.getAuctionValue()} alt limitinden basliyor.\nAcik arttirma basliyorrrrr!\n------------------------------""")

            while len(auction.getCustomerList()) > 1:
                sortedList = sorted(auction.getCustomerList(
                ), reverse=False, key=lambda customer: customer.getIsAI())
                for i in sortedList:
                    time.sleep(1)
                    i.applyBid(auction)

            if len(auction.getCustomerList()) == 1:
                winner = auction.getCustomerList()[0]
                auction.completeAuction(winner)

                print(
                    f"""+++++++++++++++++++\nDeponun Kazanani: {auction.getWinner().getName()} {auction.getWinner().getSurname()}\nVerdigi Para: {auction.getLastBidValue()}\nDepodan cikan urun sayisi: {len(depo.getProductList())}\nURUNLER: """)
                for i in depo.getProductList():
                    print("---------------------")
                    i.info()
                    time.sleep(1)
                print("======================")
            else:
                time.sleep(0.5)
                print("alicilarin parasi yetmedigi icin acik arttirma iptal olmustur!")

            for i in customerList:
                i.resetCustomer()
        else:
            mainMenu()

    if result == "2":
        if len(player.getInventory()):
            for i in player.getInventory():
                print("---------------------")
                i.info()
        else:
            print("Envanteriniz Bos!")
    if result == "3":
        while True:
            list = player.getInventory()
            if len(list) >= 1:
                for i in list:
                    print("--------------------------")
                    print(f"Urun Id: {list.index(i)+1}")
                    i.info()
                print("==========================")
                x = int(input("Satmak istediginiz urunun id'sini giriniz: "))
                try:
                    sellingItem = list[x-1]
                except:
                    print("gecerli bir deger giriniz!")
                    break
                fiyat1 = magaza1.buyValue(sellingItem)
                fiyat2 = magaza2.buyValue(sellingItem)
                fiyat3 = magaza3.buyValue(sellingItem)
                print(f"1-{magaza1.getName()} magazasi {fiyat1} fiyatini verdi.")
                print(f"2-{magaza2.getName()} magazasi {fiyat2} fiyatini verdi.")
                print(f"3-{magaza3.getName()} magazasi {fiyat3} fiyatini verdi.")

                secim = int(
                    input("Satmaktan vazgecmek icin 0 giriniz.\nSatmak istediginiz saticinin numarasini giriniz: "))

                if secim == 1:
                    player.sellItem(fiyat1, sellingItem)
                    break
                elif secim == 2:
                    player.sellItem(fiyat2, sellingItem)
                    break
                elif secim == 3:
                    player.sellItem(fiyat3, sellingItem)
                    break
                else:
                    break

                print(f"Guncel paraniz: {player.getMoney()}")
            else:
                print("\nEnvanterinizde urun yok! satis yapamazsiniz")
                break
    if result == "0":
        break

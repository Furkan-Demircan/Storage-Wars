# Storage Wars

Storage Wars, açık artırma tabanlı bir oyun ve simülasyon yazılımıdır. Proje, depoların açık artırmayla satıldığı ve oyuncuların, botların (AI) ve çeşitli ürünlerin dahil olduğu bir sistem oluşturur. Oyuncular, açık artırmalarda teklif verir, ürünleri envanterlerine ekler ve ticaret yapabilir.

[**Read this document in English**](./README_EN.md)

## Özellikler

- **Depo Yönetimi**: Depolar oluşturulabilir, rastgele ürünlerle doldurulabilir ve açık artırmaya sunulabilir.
- **Ürünler**: Farklı nadirlik seviyelerine, üretim tarihlerine ve değerlere sahip çok sayıda ürün.
- **Açık Artırma**: Hem gerçek oyuncuların hem de yapay zeka (AI) oyuncularının teklif verebildiği dinamik bir açık artırma sistemi.
- **Mağazalar**: Oyuncular, ürünlerini mağazalara satarak para kazanabilir.
- **Oyuncu Yönetimi**: Oyuncular ve yapay zeka tabanlı müşteriler oluşturulabilir ve yönetilebilir.

## Gereksinimler

- Python 3.8 veya daha üstü

Proje, Python'un yerleşik modüllerinden (ör. `random`, `time`) ve standart kütüphanelerden yararlanır. Ekstra bir bağımlılık yoktur.

## Kurulum

1. Bu projeyi yerel makinenize klonlayın:
    ```bash
    git clone https://github.com/kullanici-adi/storage-wars.git
    cd storage-wars
    ```

2. Python'u ve gerekli sürümünü kurduğunuzdan emin olun.

3. Projeyi çalıştırmak için aşağıdaki komutu kullanın:
    ```bash
    python Storage-wars.py
    ```

## Kullanım

1. Program başlatıldığında ana menü ile karşılaşacaksınız:
    - Açık artırmaya katılabilir
    - Envanterinizi kontrol edebilir
    - Ürün satışı yapabilirsiniz.

2. Açık artırmada, oyuncular sırayla teklif verebilir. Oyuncu, teklif vermemeyi veya açık artırmadan çekilmeyi seçebilir.

3. Açık artırma sonucunda kazanan kişi, deponun tüm ürünlerini alır ve bu ürünler envanterine eklenir.

4. Oyuncular ürünlerini mağazalara satarak para kazanabilir ve açık artırmalar için daha fazla bütçe oluşturabilir.

## Kod Yapısı

- **`DepoSavaslari`**: Temel sınıf. Diğer tüm sınıflar bu sınıftan türetilir.
- **`Warehouse`**: Depoları ve ilgili işlemleri yönetir.
- **`Product`**: Ürünler ve özelliklerini içerir.
- **`Shop`**: Mağazalar ve ürün alım satım işlemlerini içerir.
- **`Auction`**: Açık artırma sürecini ve kurallarını yönetir.
- **`Customer`, `Player`, `AI`**: Oyuncuları ve botları temsil eden sınıflar.

## Geliştirme

Projeyi geliştirmek için aşağıdaki adımları izleyebilirsiniz:

1. Yeni ürünler veya mağazalar eklemek için `Product` veya `Shop` sınıflarını genişletin.
2. Açık artırma sürecine yeni kurallar veya özellikler eklemek için `Auction` sınıfını düzenleyin.
3. Yapay zeka teklif verme mantığını geliştirmek için `AI` sınıfını düzenleyin.

## Katkıda Bulunma

Katkılar memnuniyetle karşılanır! Lütfen katkıda bulunmadan önce bir konu açarak değişikliklerinizi tartışın.

1. Fork'layın (Çatal oluşturun).
2. Kendi dalınızı oluşturun (`git checkout -b ozellik/yenilik`).
3. Değişikliklerinizi commit edin (`git commit -m 'Yeni özellik ekle'`).
4. Dalınıza push yapın (`git push origin ozellik/yenilik`).
5. Bir pull isteği (PR) açın.

## Lisans

Bu proje MIT Lisansı ile lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasına göz atabilirsiniz.

## İletişim

Proje hakkında sorularınız veya önerileriniz için bizimle iletişime geçebilirsiniz:

- **E-posta**: goooglenudle@gmail.com
- **GitHub**: [Furkan-Demircan](https://github.com/Furkan-Demircan)

---

İyi eğlenceler ve iyi şanslar!

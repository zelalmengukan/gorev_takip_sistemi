# Liste Tanımlamaları
gorevler = []
tamamlananlar = []


def gorev_ekle():
    """Kullanıcıdan alınan yeni görevi listeye ekler."""
    yeni_gorev = input("\nEklenecek görevi giriniz: ").strip()
    if yeni_gorev:
        gorevler.append(yeni_gorev)
        print(f"'{yeni_gorev}' görevi eklendi.")
    else:
        print("Hata: Boş görev eklenemez.")


def gorev_listele():
    """Mevcut tüm görevleri numaralarıyla ekrana yazdırır."""
    print("\n--- MEVCUT GÖREVLER ---")
    if not gorevler:
        print("Listede herhangi bir görev bulunmuyor.")
    else:
        for indeks, gorev in enumerate(gorevler):
            print(f"[{indeks}] {gorev}")


def gorev_tamamla():
    """Seçilen görevi tamamlananlar listesine aktarır."""
    if not gorevler:
        print("\nTamamlanacak görev yok.")
        return

    gorev_listele()

    try:
        secim = int(
            input("\nTamamlanan görevin numarasını giriniz: ").strip()
        )
        if 0 <= secim < len(gorevler):
            tamamlanan = gorevler.pop(secim)
            tamamlananlar.append(tamamlanan)
            print(f"'{tamamlanan}' görevi tamamlandı olarak işaretlendi.")
        else:
            print("Hata: Geçersiz görev numarası.")
    except ValueError:
        print("Hata: Lütfen sayısal bir değer giriniz.")


def tamamlanan_liste():
    """Tamamlanan tüm görevleri gösterir."""
    print("\n--- TAMAMLANAN GÖREVLER ---")
    if not tamamlananlar:
        print("Tamamlanmış görev bulunmuyor.")
    else:
        for indeks, gorev in enumerate(tamamlananlar, 1):
            print(f"{indeks}. {gorev}")


def ana_menu():
    """Uygulama ana menü döngüsü."""
    while True:
        print("\n" + "=" * 30)
        print("     GÖREV TAKİP SİSTEMİ")
        print("=" * 30)
        print("1. Görevleri Listele")
        print("2. Görev Ekle")
        print("3. Görev Tamamla")
        print("4. Tamamlanan Görevleri Göster")
        print("5. Çıkış")

        secim = input("İşlem seçiniz (1-5): ").strip()

        if secim == "1":
            gorev_listele()
        elif secim == "2":
            gorev_ekle()
        elif secim == "3":
            gorev_tamamla()
        elif secim == "4":
            tamamlanan_liste()
        elif secim == "5":
            print("Programdan çıkılıyor...")
            break
        else:
            print("Geçersiz seçim! Lütfen 1 ile 5 arasında bir değer giriniz.")


if __name__ == "__main__":
    ana_menu()

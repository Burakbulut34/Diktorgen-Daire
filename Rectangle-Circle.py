def alan_hesapla():
    try:
        sekil = input("Hangi şeklin alanını hesaplamak istiyorsunuz? (dikdörtgen/daire):").strip().lower()
        if sekil == 'dikdörtgen':
            uzunluk = float(input("Dikdörtgenin uzunluğunu girin: "))
            genislik = float(input("Dikdörtgen genişliğini girin:"))
            if uzunluk <= 0 or genislik <= 0:
                raise ValueError("Uzunluk ve genişlik pozitif olmalıdır.")
            return f"Dikdörtgenin alanı:{uzunluk * genislik}" # Alan hesaplaması toplama değil, çarpma olmalı
        elif sekil == 'daire':
            yaricap = float(input("Dairenin yarıçapını girin:"))
            if yaricap <= 0:
                raise ValueError("Yarıçap pozitif olmalıdır.")
            return f"Dairenin alanı: {3.14 * yaricap ** 2}"
        else:
            raise ValueError("Geçersiz şekil seçimi")
    except ValueError as e:
        return f"Hata: {e}"
    except Exception as e:
        return f"Bilinmeyen bir hata oluştu: {e}"

print(alan_hesapla())

import requests
import json

def main():
    # Vavoo ana API adresi
    api_url = "https://www2.vavoo.to/live2/index"
    
    # Filtreleme anahtar kelimeleri (Büyük harf duyarsız)
    target_tags = ["TURKEY", "TÜRKİYE", "TR", "BEIN", "SPORT", "EXXEN", "TIVIBU"]
    
    # Engellenmemesi için istek başlığı
    headers = {
        'User-Agent': 'VAVOO/2.6',
        'Accept': 'application/json'
    }

    try:
        print("Veriler çekiliyor...")
        response = requests.get(api_url, headers=headers, timeout=30)
        response.raise_for_status()
        data = response.json()
        
        with open("playlist.m3u", "w", encoding="utf-8") as f:
            f.write("#EXTM3U\n")
            
            count = 0
            for item in data:
                name = item.get('name', '').upper()
                group = item.get('group', '').upper()
                url = item.get('url')
                logo = item.get('logo', '')

                # Sadece hedef kelimeleri içeren kanalları filtrele
                if any(tag in name or tag in group for tag in target_tags):
                    if url:
                        # Televizo uyumluluğu için User-Agent linke gömülür
                        f.write(f'#EXTINF:-1 tvg-logo="{logo}" group-title="{group}",{name}\n')
                        f.write(f"{url}|User-Agent=VAVOO/2.6\n")
                        count += 1
        
        print(f"İşlem tamam! {count} adet kanal listeye eklendi.")

    except Exception as e:
        print(f"Hata oluştu: {e}")

if __name__ == "__main__":
    main()
    

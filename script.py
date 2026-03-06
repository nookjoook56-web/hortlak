import requests

def main():
    # Vavoo'nun ana veri kaynağı
    api_url = "https://www2.vavoo.to/live2/index"
    
    # Filtrelemek istediğimiz anahtar kelimeler
    target_tags = ["TURKEY", "TÜRKİYE", "TR", "BEIN", "SPORT"]
    
    try:
        # Veriyi çekiyoruz
        response = requests.get(api_url, timeout=30)
        data = response.json()
        
        with open("playlist.m3u", "w", encoding="utf-8") as f:
            f.write("#EXTM3U\n")
            
            for item in data:
                # Kanal adı ve grup ismini büyük harfe çevirerek kontrol ediyoruz
                name = item.get('name', '').upper()
                group = item.get('group', '').upper()
                url = item.get('url')
                logo = item.get('logo', '')
                
                # Eğer kanal adı veya grup adı listedeki kelimelerden birini içeriyorsa ekle
                if any(tag in name or tag in group for tag in target_tags):
                    if url:
                        # Televizo ve diğer oynatıcılar için User-Agent zorunludur
                        f.write(f'#EXTINF:-1 tvg-logo="{logo}" group-title="{group}",{name}\n')
                        f.write(f"{url}|User-Agent=VAVOO/2.6\n")
        
        print("Playlist başarıyla filtrelendi ve güncellendi.")
        
    except Exception as e:
        print(f"Hata oluştu: {e}")

if __name__ == "__main__":
    main()

import requests

def main():
    api_url = "https://www2.vavoo.to/live2/index"
    # Filtrelemek istediğimiz anahtar kelimeler
    target_groups = ["Turkey", "TURKIYE", "TR", "BEIN", "SPORTS"]
    
    try:
        response = requests.get(api_url, timeout=30)
        data = response.json()
        
        with open("playlist.m3u", "w", encoding="utf-8") as f:
            f.write("#EXTM3U\n")
            
            for item in data:
                name = item.get('name', '').upper()
                group = item.get('group', '').upper()
                url = item.get('url')
                logo = item.get('logo', '')
                
                # Sadece Türkiye kanalları ve beIN/Sports içerenleri filtrele
                if any(tag in group or tag in name for tag in target_groups):
                    if url:
                        f.write(f'#EXTINF:-1 tvg-logo="{logo}" group-title="{group}",{name}\n')
                        # Televizo için User-Agent zorunludur
                        f.write(f"{url}|User-Agent=VAVOO/2.6\n")
        
        print("Filtreleme tamamlandı: Sadece TR ve beIN kanalları eklendi.")
        
    except Exception as e:
        print(f"Hata oluştu: {e}")

if __name__ == "__main__":
    main()
    

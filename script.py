import requests

def main():
    api_url = "https://www2.vavoo.to/live2/index"
    try:
        # Vavoo API'den verileri çekiyoruz
        response = requests.get(api_url, timeout=30)
        data = response.json()
        
        with open("playlist.m3u", "w", encoding="utf-8") as f:
            f.write("#EXTM3U\n")
            for item in data:
                name = item.get('name', 'Kanal')
                url = item.get('url')
                group = item.get('group', 'Genel')
                logo = item.get('logo', '')
                
                if url:
                    # Televizo'nun tanıması için User-Agent'ı linkin sonuna ekliyoruz
                    f.write(f'#EXTINF:-1 tvg-logo="{logo}" group-title="{group}",{name}\n')
                    f.write(f"{url}|User-Agent=VAVOO/2.6\n")
        
        print("Playlist Televizo için uygun formatta güncellendi.")
    except Exception as e:
        print(f"Hata: {e}")

if __name__ == "__main__":
    main()
    

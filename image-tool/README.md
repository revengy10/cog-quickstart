# Image Tool - Cog Input Interface Exercise

Cog'un "getting started with your own model" rehberindeki arayüz
kavramlarını uyguladığım mini proje: PIL tabanlı görüntü ölçekleme ve
efekt aracı.

## Öğrendiklerim / Kullandıklarım

- **cog init** ile şablon proje oluşturma
- **Çoklu girdi:** run() fonksiyonunda image + scale + effect parametreleri
- **Input seçenekleri:**
  - default (opsiyonel parametre; verilmezse 2.0 / "none")
  - ge / le ile sayısal sınır (0.1-8.0 dışı değerler otomatik reddediliyor)
  - choices ile izinli değer listesi (none/blur/sharpen/grayscale)
- **Path çıktısı:** dict yerine üretilen PNG dosyasını döndürme
- **/docs** uç noktası: Input tanımlarından otomatik üretilen interaktif
  API dokümantasyonu

## Kullanım

```bash
cog run -i image=@input.jpg
cog run -i image=@input.jpg -i scale=3.0 -i effect=grayscale

# HTTP API olarak:
cog build -t cog-image-tool
docker run -d --rm -p 5000:5000 cog-image-tool
```

## Karşılaştığım sorun

İlk build'de cog.yaml'da python_requirements satırı eksikti;
konteyner "ModuleNotFoundError: No module named 'PIL'" ile çöktü.
Ders: imaja koymadığın hiçbir bağımlılık konteynerde yoktur —
requirements zinciri (cog.yaml -> requirements.txt) tam olmalı.

# Cog ile ML Modeli Paketleme

Replicate'in Cog aracıyla ResNet50 görüntü sınıflandırma modelini
konteynerize edip HTTP API olarak sunma çalışmam.

- cog.yaml: build ortamı tanımı (Python 3.13 + torch/torchvision)
- run.py: setup() ile model yükleme, run() ile tahmin
- cog build ile imaj, docker run ile 5000 portunda tahmin API'si

Docker temelim: https://github.com/revengy10/docker-egitimi

## Alt proje: image-tool/
Input arayüz seçeneklerini (default, ge/le, choices) ve Path çıktısını
uyguladığım görüntü işleme aracı. Detaylar: image-tool/README.md

## Deploy notları
Cog konteynerleri Docker'ın çalıştığı her yerde deploy edilebiliyor.
cog serve ile tek komutta build+serve; --gpus all ile GPU erişimi;
/openapi.json ile Input tanımlarından üretilen makine-okur API şeması;
/health-check (STARTING/READY/BUSY/SETUP_FAILED/DEFUNCT) ile readiness
probe; concurrency.max ile eşzamanlı istek sayısı.
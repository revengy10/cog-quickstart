# Cog ile ML Modeli Paketleme

Replicate'in Cog aracıyla ResNet50 görüntü sınıflandırma modelini
konteynerize edip HTTP API olarak sunma çalışmam.

- cog.yaml: build ortamı tanımı (Python 3.13 + torch/torchvision)
- run.py: setup() ile model yükleme, run() ile tahmin
- cog build ile imaj, docker run ile 5000 portunda tahmin API'si

Docker temelim: https://github.com/revengy10/docker-egitimi

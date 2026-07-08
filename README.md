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

## cog.yaml referans notları
build altında: python_version, python_requirements (python_packages
deprecated), system_packages (APT), run (Dockerfile RUN karşılığı, kod
görünmez), gpu/cuda, sdk_version. concurrency.max async predict()
gerektiriyor. image anahtarı (r8.im/kullanici/model) cog push'un hedefini
belirliyor — Docker imaj adı anatomisiyle aynı mantık.
## Python API referans notları
BaseRunner/run() güncel API (BasePredictor/predict deprecated). Yeni
kullandıklarım: cog.BaseModel ile çok alanlı yapılandırılmış çıktı,
tempfile.mkdtemp() ile güvenli çıktı yolu, self.record_metric() ile özel
ölçümler. Bilgi düzeyinde: async run + @cog.concurrent, @streaming ile
Iterator çıktısı, cog.Secret, CancelationException, Optional/Union/list
girdi tipleri ve tip sınırlamaları.

# Meme Kanseri Sınıflandırma (Makine Öğrenmesi)

scikit-learn ile tümörleri iyi huylu / kötü huylu olarak sınıflandıran bir ML projesi.

## Ne Yapıyor?
- Breast Cancer veri setini yükler
- Veriyi eğitim/test olarak böler (%80/%20)
- KNN modeli eğitir ve tahmin yapar
- Accuracy, confusion matrix ve precision/recall ile değerlendirir

## Sonuç
- Doğruluk (accuracy): ~%93
- Kötü huylu (kanser) sınıfı için recall değeri, kritik metrik olarak takip edildi

## Kullanılan Teknolojiler
- Python, scikit-learn

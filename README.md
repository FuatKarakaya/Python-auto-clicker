# **Python Auto Clicker (İTÜ Ders Seçim)**

## **Açıklama**
Bu Python scripti, kullanıcı tarafından belirlenen koordinatlarda fare tıklamaları yapar ve İTÜ ders seçim sürecinde yardımcı olabilir.

### **Özellikler**
- **Koordinat Belirleme**: Dinamik olarak tıklama yapılacak noktaları belirleme veya varsayılan koordinatları kullanma.
- **Zamanlayıcı**: Belirli bir saatte tıklamalara başlama (örneğin. ders seçim saatinde).
- **Spam Modu**: Tıklamaların sonsuz döngüede devam etmesi.
- **Sayfa Yenileme**: Tıklamalardan önce tarayıcıyı Ctrl+R ile yenileme.
- **Küresel Tuş Dinleyici**: `e` tuşuna basarak scripti istediğiniz zaman durdurabilirsiniz.

---

## **İTÜ Ders Seçim İçin Kullanım**

### **Terminalden Yönetici Olarak Çalıştırın**
1. Scriptin doğru çalışabilmesi için terminali **yönetici olarak** açmanız gerekiyor.
2. Aşağıdaki komutla dosyanın bulunduğu klasöre gidip scripti çalıştırın:
   ```bash
   cd C:\Users\KULLANICI_ADINIZ\Desktop
   python "auto clicker.py"
   ```

### **Tarayıcı Ayarları**
- Script çalışmaya başlamadan önce tarayıcıyı **açık bırakın** ve odakta tarayıcı kalacak şekilde bir kez tıklayın.

### **Script Nasıl Çalışır**
1. **Program size bir dizi soru soracaktır:**
   - **Zamanlayıcı Modu**: Belirli bir saatte mi (\u00f6rneğin `09:00:00`) yoksa geri sayım sonrasında mı başlasın?
   - **Spam Modu**: Tıklamalar sonsuz döngüede devam etsin mi yoksa yalnızca bir kez mi tıklasın?
   - **Koordinatlar**: Yeni koordinatlar belirlemek ister misiniz, yoksa varsayılan koordinatlar mı kullanılsın?
2. **Scripti Durdurmak**:
   - Script çalışırken istediğiniz zaman `e` tuşuna basarak programı **anında sonlandırabilirsiniz**.

---

## **Kurulum**

### **Gerekli Kütüphaneleri Yükleyin**
Terminalde aşağıdaki komutları çalıştırarak gerekli kütüphaneleri yükleyin:
```bash
pip install pyautogui
pip install pynput
```

---

## **Kullanım Talimatları**

1. **Python dosyasını çalıştırın**:
   ```bash
   python auto_clicker.py
   ```

2. **Soruları yanıtlayın**:
   - **Zamanlayıcı Modu**: Ders seçim saatine göre çalışmasını sağlayabilirsiniz.
   - **Koordinat Seçimi**: Tıklama noktalarını belirleyebilir veya varsayılanları kullanabilirsiniz.
   - **Spam Modu**: Sürekli tekrar eden tıklamalar için spam modunu seçebilirsiniz.

3. **Sayfa Yenileme**:
   - Program, isterseniz tıklamalardan önce tarayıcıyı otomatik olarak yenileyebilir (Ctrl+R).

4. **Tıklamalar Başlar**:
   - Belirlenen koordinatlarda tıklamalar yapılır.

---

## **Yapılandırılabilir Ayarlar**

### Scriptteki şu parametreleri düzenleyerek ihtiyacınıza göre uyarlayabilirsiniz:
- **`time_delay_btw_clicks`**:  
  - Tıklamalar arasındaki süre.  
  - **Varsayılan**: `0.01` (10 milisaniye).  

- **`time_delay_each_round`**:  
  - Her tıklama döngüsü arasındaki süre (spam modunda).  
  - **Varsayılan**: `3 saniye`.  

- **`default_coordinates`**:  
  - Varsayılan fare tıklama koordinatları.  
  - **Örnek**:  
    ```python
    default_coordinates = [(100, 200), (300, 400), (500, 600)]
    ```

---

## **Örnek Senaryolar**

### **1. Ders Seçim Saati için Hazırlık**
- **Timer Modu**: Saat `14:00:00` gibi bir zaman belirleyin.
- **Spam Modu**: Tıklamaları sürekli tekrar eden bir döngüe ayarlayın.
- **Sayfa Yenileme**: Tıklamalardan önce sayfanın yenilenmesini seçin.

### **2. Varsayılan Koordinatlarla Tek Tıklama**
- **Timer Modu**: Kapatın ve 10 saniyelik geri sayımla başlatın.
- Varsayılan koordinatları kullanarak tek bir tur tıklama yapın.

### **3. Yeni Koordinatlarla Spam Modu**
- Yeni tıklama noktaları belirleyin.
- Spam modunu açarak tıklamaların sürekli tekrar etmesini sağlayın.

---

## **Notlar**

- **Tüş Algılama**: `e` tuşuna basarak scripti **anında durdurabilirsiniz**.
- **Yönetici Olarak Çalıştırın**: Tam işlevsellik için terminali yönetici modunda çalıştırın.
- **Hızlı Tıklamalar için Test**: Tıklama süreşini (`time_delay_btw_clicks`) çok düşük ayarlarsanız hedef uygulamanızın bunu desteklediğinden emin olun.

---

## **Sorumluluk Reddi**
Bu script yalnızca eğitim ve otomasyon amaçlıdır. İTÜ veya başka platformlarda kullanımınızın ilgili hizmet koşullarına uygun olduğundan emin olun. Yanlış kullanımdan doğacak sorumluluk kullanıcıya aittir.

---

## **Lisans**
Bu proje MIT Lisansı altında lisanslanmıştır. Daha fazla bilgi için LICENSE dosyasına göz atabilirsiniz.

---


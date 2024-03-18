# Santiment-Auto-Cleanup

### Genel Bakış
-------------
  Bilindiği üzere Santiment üzerinde node(readonly) çalıştıranlarda yoğun olarak bir disk kullanımı ve bu kullanıma mevcut olarak boş disk alanınında hızlı bir şekilde azalma görülüyordu.
Son olarak ekip bunun üzerine gereksiz verileri silen bir komut satırı paylaştı.
Ben de bunun üzerine diski her 6 saatte bir kontrol eden ve disk alanının %90 üzerine çıkıldığında bu komutu otomatik olarak çalıştıran bir bash yazdım. Kendim test ettim, paylaşmak istedim.

### Özellikler
-------------

- Disk kullanımını her 6 saatte bir düzenli olarak kontrol eder.
- Belirlenen disk kullanım limitini aştığında Santiment Node için Prune işlemi başlatır.
- Log kayıtlarını DtractusSanrLog.log dosyasına yazar.



### Önkoşullar
-------------

- Santiment Node kurulu ve çalışıyor olmalıdır.
- Disk adınızı bilmeniz gerekiyor. Konsolunuzda `df -h` komutunu kullandığınızd aşağıdaki görsel gibi bir çıktı alırsınız. Burada disk adımız /dev/sda1'dir. Bu disk adınızı öğrenmeli ve bash size sorduğunda bu şekilde girmelisiniz.

    ![image](https://github.com/Dtractus/Santiment-Auto-Cleanup/assets/55835876/86ea3c62-788c-4722-8560-ce9f68a6e55f)


### Kurulum Adımları
-------------

1. **Aşağıdaki komutu kullanarak kurulum betiğini çalıştırın:**

    ```   
    source <(curl -s https://raw.githubusercontent.com/Dtractus/Santiment-Auto-Cleanup/main/DtractusAutoPrune.sh)
    ```
  Bu komut, gerekli bağımlılıkları kurar, Python script'inizi indirir ve gereken yapılandırmaları yapar.
  
2. **Kurulum sırasında, script sizden aşağıdaki bilgileri isteyecektir:**
  
    * **DISK_NAME:** Disk bölümünün adı (Yukarıda aldığınız disk adı. Örneğin: /dev/sda1)
    * **MAX_DISK_USAGE_PERCENT:** Disk kullanımı bu yüzdeyi aştığında temizleme işleminin tetiklenmesi gereken yüzde (Örneğin: 90)

3. **Kurulum tamamlandığında, araç otomatik olarak her 6 saatte bir çalışacak şekilde yapılandırılacaktır.**


### Log Kayıtları

  Script çalıştırıldığında, çıktılar ve olası hata mesajları $HOME/DtractusAutoPrune/DtractusSanrLog.log dosyasına yazılır. Bu log dosyası, aracın çalışması ve olası sorunları hakkında bilgi edinmek için incelenebilir. Loglarınızı aşağıdaki komut ile görüntüleyebilirsiniz;

```
tail -f $HOME/DtractusAutoPrune/DtractusSanrLog.log
```

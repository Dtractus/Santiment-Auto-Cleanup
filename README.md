# Santiment-Auto-Cleanup

### Genel Bakış
-------------
  Bilindiği üzere Santiment üzerinde node(readonly) çalıştıranlarda yoğun olarak bir disk kullanımı ve bu kullanıma mevcut olarak boş disk alanınında hızlı bir şekilde azalma görülüyordu.
Son olarak ekip bunun üzerine gereksiz verileri silen bir komut satırı paylaştı.
Ben de bunun üzerine diski her 12 saatte bir kontrol eden ve disk alanının %90 üzerine çıkıldığında bu komutu otomatik olarak çalıştıran bir script yazdım. Kendim test ettim, paylaşmak istedim.


### Kurulum
-------------

Öncelikle bize `Python 3.x` gerekiyor. Olup olmadığını öğrenerek başlayabiliriz.
```
# Aşağıdaki kodu ekranımıza yazalım
python3 --version

# Yukarıdaki komut size Python 3.8.10 gibi bir çıktı veriyorsa kurulu demektir.
# Eğer kurulu değil ise endişelenmeyin, gelin beraber kuralım.

# Öncelikle sunucudaki güncellemelerimizi ve yükseltmelerimizi yapalım.
sudo apt update -y && sudo apt upgrade -y

# Ardından python'u kurabiliriz.
sudo apt install python3

# Kurulum tamamlandıktan sonra doğrulayalım;
python3 --version
```

Şimdi bize Python 3.x için `pip` gerekiyor.
Aşağıdaki kod ile pip kurulumunu yapalım.

```
sudo apt install python3-pip
```

Python 3.x ve pip kurulumlarını tamamladık. Repomuzu klonlayarak işlemlere başlayabiliriz.

```
# Aşağıdaki komut ile gerekli dosyamızı klonlayalım.
https://github.com/Dtractus/Santiment-Auto-Cleanup.git

# Dosyamıza izin verelim.
chmod +x /root/Santiment-Auto-Cleanup/sanr-cleanup.py
```
Harika! Şimdi Disk Adımıza bir göz atalım, farklılık var ise değiştirelim ve 12 saatte bir çalışması için gerekli cronumuzu oluşturalım.

```
# Disk adınızı öğrenmek için aşağıdaki komutu kullanın.
df -h

# Aşağıdaki gibi bir çıktı ile karşılacaksınız. Genelde /dev/sda1 olur fakat değişkenlik var ise kontrol etmeniz açısından gösterdim.
# Eğer sda1'den farklı bir isme sahipseniz sunucunuzda "Santiment-Auto-Cleanup" klasörü altındaki sanr-cleanup.py içerisinde DISK_NAME = "/dev/sda1" kısmını değiştirin.
```

![image](https://github.com/Dtractus/Santiment-Auto-Cleanup/assets/55835876/86ea3c62-788c-4722-8560-ce9f68a6e55f)

```
# Aşağıdaki komut ile cronjob'ımızı ayarlayalım.
crontab -e

# Yukarıdaki komutu daha önce hiç kullanmadıysanız sizden editör seçmenizi ister. Nano'yu seçip devam edebilirsiniz.
# Açılan ekranda birden fazla yorum satırı göreceksiniz, silebilirsiniz fakat silmeden en alttaki satırın altınada bir aşağıdaki ekleyebilirsiniz.
0 0,12 * * * /usr/bin/python3 /root/Santiment-Auto-Cleanup/test.py >> /root/sanrplog.log 2>&1

# Kodumuzu ekledikten sonra sırasıyla CTRL +X , Y ve Enter tuşlayarak çıkalım.
```
Tebrikler! Her şey bu kadardı. Loglarınızı manuel veya terminalinizde `tail -f /root/sanrplog.log` komutuyla görebilirsiniz.

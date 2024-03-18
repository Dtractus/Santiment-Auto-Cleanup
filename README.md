# Santiment-Auto-Cleanup

### Genel Bakış
-------------
  Bilindiği üzere Santiment üzerinde node(readonly) çalıştıranlarda yoğun olarak bir disk kullanımı ve bu kullanıma mevcut olarak boş disk alanınında hızlı bir şekilde azalma görülüyordu.
Son olarak ekip bunun üzerine gereksiz verileri silen bir komut satırı paylaştı.
Ben de bunun üzerine diski her 6 saatte bir kontrol eden ve disk alanının %90 üzerine çıkıldığında bu komutu otomatik olarak çalıştıran bir bash yazdım. Kendim test ettim, paylaşmak istedim.


### Kurulum
-------------

Öncelikle bize `Python 3.x` gerekiyor. Olup olmadığını öğrenerek başlayabiliriz.
```
BASH ADRESİ
```

```
# Disk adınızı öğrenmek için aşağıdaki komutu kullanın.
df -h

# Aşağıdaki gibi bir çıktı ile karşılacaksınız. Genelde /dev/sda1 olur fakat değişkenlik var ise kontrol etmeniz açısından gösterdim.
# Burada görünen /dev/sda1 bizim disk adımız. Sizin diskinizin adı ne ise başlangıçta disk adı sorusuna bu şekilde yanıt verin.
```

![image](https://github.com/Dtractus/Santiment-Auto-Cleanup/assets/55835876/86ea3c62-788c-4722-8560-ce9f68a6e55f)

```
# Kodumuzu ekledikten sonra sırasıyla CTRL +X , Y ve Enter tuşlayarak çıkalım.
```
Tebrikler! Her şey bu kadardı. Loglarınızı manuel veya terminalinizde `tail -f /root/sanrplog.log` komutuyla görebilirsiniz.

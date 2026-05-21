# Slatro Portfolio | İnteraktif Proje Vitrini Hub

Bu proje, geliştirdiğiniz veya tasarladığınız web uygulamalarını, akıllı sözleşmeleri, oyunları ve şablonları tek bir şık arayüzde toplamanızı ve yönetmenizi sağlayan **tamamen sıfırdan oluşturulmuş, yüksek performanslı ve interaktif tek sayfalık (single-page) bir portföy uygulamasıdır**.

Görsel olarak glassmorphism estetiğine, arka planda yavaşça yüzen akışkan küre animasyonlarına, responsive (mobil uyumlu) yapıya ve tarayıcıda çalışan yerleşik bir yönetim paneline sahiptir.

---

## 🚀 Hızlı Başlangıç

1. **Uygulamayı Çalıştırın:**
   Uygulama tamamen yerel olarak çalışabilecek şekilde tasarlanmıştır. `index.html` dosyasını doğrudan tarayıcınızda çift tıklayarak açabilir veya bir geliştirici sunucusu ile ayağa kaldırabilirsiniz.
   
2. **Yönetim Paneline Giriş:**
   Sağ üstte bulunan **"Manage Site"** butonuna basın. Karşınıza gelecek olan şık güvenlik kapısında şifrenizi girin.
   * **Varsayılan Yönetici Şifresi:** `slatro2026`

3. **Verileri Canlı Düzenleme:**
   Giriş yaptıktan sonra **Profile** sekmesinden isminizi, unvanınızı, avatar resminizi, biyografinizi ve sosyal medya hesaplarınızı; **Projects** sekmesinden ise yaptığınız uygulamaları ekleyebilir, düzenleyebilir veya silebilirsiniz.
   * Yapılan değişiklikler tarayıcınızın yerel belleğine (`localStorage`) anında kaydedilir ve sayfa yenilense bile kaybolmaz!

---

## 💾 Değişiklikleri Kalıcı Hale Getirme (Baking)

Yerel tarayıcınızda yaptığınız düzenlemeleri **kod dosyasına tamamen kalıcı olarak gömmek (böylece internette yayınladığınızda herkesin görebilmesi için)** çok kolaydır:

1. Yönetici paneline girip **Export / Backup** sekmesini açın.
2. Sayfanın en üstünde yer alan **"Exportable Data Configuration Block"** alanındaki JavaScript kod blokunu **Copy to Clipboard** butonuna tıklayarak kopyalayın.
3. `index.html` dosyanızı herhangi bir kod editörüyle (VS Code, Notepad, vb.) açın.
4. Kodun alt kısımlarında bulunan `const INITIAL_DATA = { ... };` tanımını bulun.
5. Kopyaladığınız yeni veri kodunu bu alanın üzerine yapıştırıp dosyayı kaydedin.
6. Artık sitenizi nereye yüklerseniz yükleyin, eklediğiniz tüm projeler ve güncellediğiniz profiliniz varsayılan olarak görüntülenecektir!

---

## ☁️ Ücretsiz Yayınlama (Deployment)

Bu portföy tamamen tek dosyadan (`index.html`) oluştuğu için internette yayınlamak son derece kolay ve tamamen **ücretsizdir**:

### Seçenek A: Vercel (Önerilen)
1. [Vercel](https://vercel.com) hesabınıza giriş yapın.
2. Yeni bir proje oluşturup bu klasörü yükleyin veya GitHub'a push edip Vercel'e bağlayın.
3. Saniyeler içinde siteniz yayına girecektir.

### Seçenek B: GitHub Pages
1. GitHub üzerinde `slatro-portfolio` adında yeni bir repository (depo) oluşturun.
2. `index.html` dosyasını bu depoya yükleyin.
3. Depo ayarlarından (**Settings > Pages**) GitHub Pages özelliğini aktif edin ve `main` branch'i seçin.
4. Siteniz `kullanıcıadınız.github.io/slatro-portfolio/` adresinde yayına hazır!

---

## 🔒 Güvenlik Şifresini Değiştirme
Varsayılan `slatro2026` şifresini değiştirmek isterseniz:
1. `index.html` dosyasını kod editörünüzle açın.
2. `<script>` etiketinin hemen başında bulunan `const ADMIN_SECRET_KEY = "slatro2026";` satırını bulun.
3. Buradaki tırnak işaretleri arasına istediğiniz yeni şifreyi yazıp kaydedin.

---
*Tasarlayan: Slatro Portfolio Developer*

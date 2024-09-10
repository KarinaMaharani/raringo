Tugas 2 PBP - Karina Maharani 2306165736 PBP A

################

Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

Jawaban:

Membuat sebuah proyek Django baru.

Penjelasan: 
1. Saya membuat project django baru dengan pertama membuat repositori baru di github yang kemudian saya hubungkan dengan repositori lokal. 
2. Kemudian saya membuat virtual environment dimana saya mendownload Django dan dependencies lainnya. 
3. Untuk pembuatan proyek saya jalankan dengan mengunakan "django-admin startproject [NAMA PROYEK] ."
4. Setelah menjalankan perintah tersebut saya akan memperoleh manage.py serta folder/template pada repositori lokal berupa nama proyek dan folder tersebut mengandung file berupa __pycache__, __init__, asgi, wsgi, settings, urls, wsgi. 
5. Untuk memastikan proyek dapat dideploy seecara lokal kita bisa menambahkan host pada settings.py pada list ALLOWED_HOSTS dengan menambahkan "localhost" atau/dan  "127.0.0.1" (keduanya merujuk kepada komputer lokal), list ini akan ditambahkan pula dengan laman web hosting. 


Membuat aplikasi dengan nama main pada proyek tersebut.

Penjelasan:
1. Dalam sebuah proyek kita dapat memiliki banyak aplikasi, karena kita akan membuat aplikasi bernama name kita dapat menginisiasi aplikasi baru dengan perintah "python manage.py startapp [NAMA APLIKASI]". Maka jika nama aplikasi 'main' perintah yang dijalankan ialah "python manage.py startapp main". 
2. Setelah menjalankan perintah, kita akan mendapat folder/template dengan nama aplikasi yang terdiri atas folder migrations untuk models, __init__, admin, apps,  models, tests, urls, views.


Melakukan routing pada proyek agar dapat menjalankan aplikasi main.

Penjelasan :
1. Untuk menambahkan aplikasi proyek kita buka kembali file settings.py di raringo dan tambahkan nama aplikasi pada list INSTALLED_APPS
2. Selanjutnya kita dapat membuat template HTML, untuk mempermudah mengakses semua template kita dapat membuat folder baru bernama templates dalam folder main dan membuat html didalamnya seperti main.html
3. Buat template sesuai dengan kebutuhan situs pada main.html sesuai dengan kebutuhan, untuk variabel pastikan diformat dengan dua kurung kurawal seperti '{{NAMA VARIABEL}}'
4. Dalam tugas ini, main.html diisi sebagai berikut :
"
< h1>Raringo</ h1>
< h2>Run your Erands!</ h2>

< h5>Best Selling Product</ h5>
< p>{{name}}</ p> 
< p>Rp{{price}},00</ p> 
< p>{{description}}</ p> 
< p>{{tags}}</ p> 
< p>Ratings {{ratings}}</ p> 
"



Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib sebagai berikut.
    name
    price
    description

Penjelasan :
1. Kita dapat membuat model pada file models.py di folder aplikasi yaitu main. Pastikan kita mengimpor "from django.db import models"
2. Model kita definisikan dengan membuat kelas yang memiliki superclass models.Model yang berarti kita akan menggunakan Model dari library models.
3. Dalam class ini kita membuat variabel name, price, description, dan variabl lainnya serta tipe field sebagai berikut :
"
class MoodEntry(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    tags = models.CharField(max_length=255)
    ratings = models.DecimalField(max_digits=2, decimal_places=1)

    @property
    def recommend_to_user(self):
        return self.ratings >= 3.7
"
4. Kita boleh menambahkan property sebagai atribut tambahan bersifat read-only yang berupa hasil perhitungan fungsi tertentu 
5. Selanjutnya kita tentunya akan menyimpan model ini pada situs kita maka dengan itu pelru dilakukan migrasi. Tahap ini dibagi menjadi dua yaitu makemigrations dan migrate. Django melakukan pemisahan untuk memastikan bahwa developer punya kontrol lebih dalam memanage models, make migrations HANYA MEMPERESIAPKAN models agar siap dimasukkan ke dalam Database Django Lokal sedangkan migrate baru akan melakkukan migrasi model yang sudah siap ke dalam Database Django Lokal



Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.

Penjelasan:
1. Untuk menyambungkan Models dan Template kita memerlukan controller yaitu View. View ini berada dalam bentuk views.py pada folder main. Bukalah file tersebut dan pastikan pada file tersebut tertulis "from django.shortcuts import render" Library ini akan digunakan untuk mengambil fungsi render dari library Django berupa shortcuts.
2. Kemudian buatlah fungsi untuk mereturn request dengan output dictionary berisikan variabel yang ingin ditampilkan pada halaman html yang dituju seperti format berikut :
"
def show_main(request):
    context = {
        'NAMA VARIABEL PADA TEMPLATE HTML' : 'NILAI VARIABEL',
        ...
    }

    return render(request, "[LAMAN DITUJU].html", context)
"
Dalam situs saya format ini disesuaikan sebagai berikut :
"
def show_main(request):
    context = {
        'name' : 'Eyeshadow Parastyles X Gone',
        'price': 75000,
        'description': 'Trio Best Selling Shades in our combined customer base',
        'tags': 'BEAUTY, LIFESTYLE',
        'ratings': 4.3

    }

    return render(request, "main.html", context)
"


Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.

Penjelasan :
1. Saya membuat url dari aplikasi main terlebih daulu denan membuat file baru urls.py. File ini akkan diisi dengan data terkait aplikasi. Pastikan sudah mengimpor library path dan fungsi penghubun informasi dari file views.py di folder aplikasi yaitu main :
"
from django.urls import path
from main.views import show_main
"
2. Berikut format yan saya gunakan untuk memanggil pembuatan path dan proses view yang menghubungkan models dan template (dibawah baris impor) :
"
app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
"
3. Selanjutnya kita akan menhubungkan url aplikasi denggan url project. Hal ini dapat kita lakukan dengan menambahkan baris impor di file urls.py pada folder proyek "from django.urls import path, include"
4. Selanjutnya kita tambahkan anggota pada list urlpatterns path untuk urls.py di main dengan baris berikut "urlpatterns = [... path('', include('main.urls')), ...]"
5. Kita bisa mengecek apabila situs kita sudah terkoneksi dengan menjalankan server dan mengecek

Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.

Penjelasan :
1. Buka situs webhosting, seperti https://pbp.cs.ui.ac.id. Log In dengan akun SSO
2. Buat proyek baru dengan nama proyek yan diinginkan
3. Setelah proyek berhasil dibuat, tambahkan url pws sebagai item baru pada list ALLOWED_HOSTS pada file settings.py di folder proyek. Gunakkan format yang tersedia. Dalam proyek ini maka url pws adalah  karina-maharani31-raringo.pbp.cs.ui.ac.id
4. Buka cmd prompt dan run project command, isi window yan muncul dengan project credentials, lalu kembalikan  branch utama dari master ke branch utama seblumnya dalam proyek ini berarti branch main.
5. Tunggu Build selesai, lalu buka url di browser pastikan url dimulai dengan http://.
6. Untuk melakukan push kedepannya bisa gunakkan add commit push repositori biasa dilanjutkan dengan "git push pws main:master" untuk mengupdate url.

################

Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

Jawaban:
https://drive.google.com/drive/folders/1bOZaPyMi8Zt2G7YVACV2iO3d93Vlzww2?usp=sharing 

################

Jelaskan fungsi git dalam pengembangan perangkat lunak!

Jawaban:

Git merupakan salah satu alat yang mempermudah pengembangan perangkat kolaboratif pada gawai-gawai berbeda. Hal ini dikarenakan Git menyambung repositori/proyek secara lokal dan cloud. Setiap perubahan yang kita/developer lain lakukan disimpan di Git akibatnya semua developer dapat mengakses versi pembaruan developer lain dengan mengambil perubahan yang dilakukan saja. Tidak hanya itu Git juga bermanfaat dalam meningsolasi atau menggabungkan aspek/fitur proyek pengembanggan perangkat lunak dengan sistem branchnya. Ketika terjadi perubahan yang menyebabkan branch utama dan branch lain bertbrakan, developer dapat melakukan penggabungan kode-kode yang bertabrakan dan memilih fitur yang diperlukan sehingga antar developer tidak saling menghapus kode satu sama lain.    

################

Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

Jawaban:

Hal ini dikarenakan library Django di Python sangat flexible dibandingkan framework lainnya. Dari sisi popularitas, Django sangat relevan karena bahasa Python pada saat ini merupakan bahasa pemrograman yang paling popular. Selain itu bahasa Python jugga bahasa yang cepat untuk diprosees dibandingkan bahasa lain seperti Java yangg cenderung lebih lambat.

Dari sisi fitur Django juga sangat mudah digunakan karena memiliki dokumentasi dan community support yang baik ditambah dengan fleksibilitas pengunaan library python yang tidak memerlukan instalisasi/inisiasi kompleks.Sistem Django juga tidak berbayar, sehinga memudahkan developer pemula untuk bereksperimen. 

Jika kita ambil melalui lensa mata kuliah di Fakultas Ilmu Komputer Universitas Indonesia, Django menjadi pilihan tepat karena menggunakan bahasa yang sebelumnya sudah dipelajari dalam mata kuliah wajib fakultas Dasar-Dasar Pemrograman I yaitu Python.

################

Mengapa model pada Django disebut sebagai ORM?

Jawaban:

[LANJUTIN] 






################


Copyright 2024 Karina Maharani

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
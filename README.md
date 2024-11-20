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

< p>{{name}}</ p> 

< p>{{class}}</ p> 


< h1>{{application}}</ h1>

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

class Product(models.Model):

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

        'name' : 'Karina Maharani',

        'class' : 'PBP A',

        'application' : 'Raringo',


        'product' : 'Eyeshadow Parastyles X Gone',

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

Hal ini dikarenakan library Django di Python sangat flexible dibandingkan framework lainnya. Dari sisi popularitas, Django sangat relevan karena bahasa Python pada saat ini merupakan bahasa pemrograman yang paling popular. Selain itu bahasa Python jugga bahasa yang cepat untuk diproses dibandingkan bahasa lain seperti Java yangg cenderung lebih lambat.

Dari sisi fitur Django juga sangat mudah digunakan karena memiliki dokumentasi dan community support yang baik ditambah dengan fleksibilitas pengunaan library python yang tidak memerlukan instalisasi/inisiasi kompleks.Sistem Django juga tidak berbayar, sehinga memudahkan developer pemula untuk bereksperimen. 

Jika kita ambil melalui lensa mata kuliah di Fakultas Ilmu Komputer Universitas Indonesia, Django menjadi pilihan tepat karena menggunakan bahasa yang sebelumnya sudah dipelajari dalam mata kuliah wajib fakultas Dasar-Dasar Pemrograman I yaitu Python.

################

Mengapa model pada Django disebut sebagai ORM?

Jawaban:

Model pada Django termasuk ORM atau Object-Relational Mapping karena model dapat menghubungkan aplikasi Django dengan database relational yang digunakan oleh developer (MySQL, PorteSQL, dsb.) Hal ini memudahkan developer dalam menggunakan/mengubah/mengakses database tanpa menggunakan query database melalui penggunaan objek nativee dalam python.

Hal ini didukung oleh mekanisme ORM Django yang meliputi abstraksi database, non query database manipulation/creation, migrasi yang terinterasi serta mapping objek ke database. Abstraksi database (serupa mekanisme konsep diagram ERD) memvisualisasi data namun tetap agnostic terhadap platform database dan bahasa pemrograman Django. Non query database manipulation/creation berkaitan dengan implisit translation dari Django sehingga developer dapat melakukan CRUD Create Read Update Delete dengan sintaks python yang lebih ringkas. Migrasi pada Django sudah dibuat secara native ke Django karena kita hanya perlu memanggil file manage.py makemigrations atau managge.py migrate yang diinisiasi saat membuat proyek Django. Mapping objek ke database mengaitkan konsep atribut model pada Django dengan kolom/baris tabel database.   

################

##TUGAS 3 - Karina Maharani 2306165736 PBP A

################

Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

Jawaban :

Implementasi sebuah platform memerlukan data delivery untuk menghubungkan sisi frontend yan ditampilkan ke client dan sisi backeend yang akan memproses data kedalam database atau proses lainnya. Oleh karena itu kita perlu mendefinisikan jalur komunikasi dan jalur transfer data sebagai buffer antara tiap layanan dan setiap sisi program yang kita buat. Tanpa adanya data delivery yang optimal dan rutin, data yang disajikan pada platform bisa saja ouutdated dan tidak merefleksikan kondisi data base program saat ini.


################

Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

Jawaban :

Keduanya memiliki kelebihan dan kekurangan masing-masing. Akan tetapi, secara umum penggunaan JSON lebih disarankan karena JSON lebih mudah digunakan dan cenderung lebih cepat untuk AJAX Application (Asynchronous JavaScript and XML). JSON mencangkup bahasa web dvelopment seperti Java Script sehingga lebih kompatibel. 

Terkait dengan popularitas, JSON lebih populer karena banyak tereintegrasi dengan bahasa lain seperti Java dan Java script. Terdapat fitur native untukk parsing yang sudah built-in yaitu JSON.parse(). Dari sisi visibility/identation readibility, JSON lebih mudah dibaca dengan format curky bracketnya dibandingkan XML yang menggunakan indentasi. Seperti yan disebutkan, JSON juga cenderung lebih cepat sehingga lebih efektif untuk pemrosesan data ukuran besar.


################

Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?

Jawaban :

Untuk memastikan tipe data yang diinput oleh user sesuai dengan tipe data variabel, kita perlu memastikan bahwa input valid, hal ini dapat mudah dicek dengan fungsi is_valid() yang mengecek apabila data bisa diterima (diterima bernilai True, jika sebaliknya bernilai False). Nilai fungsi kemudian dapat digunakan untuk menahan nilai yang tidak valid hingga diperbaiki. Jika fungsi ini tidak di include, banyak bentuk data yang akhirnya tidak valid dan memenuhi kriteria dan menyebabkan kesulitan dalam proses filtering. Misalkan format tanggal MM-DD-YY dengan DD/MM/YYYY sulit di filter, atau nomor hp yang ditulis dengan nilai desimal.


################

Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

Jawaban :

Cross-Site Request Forgery Token (CSRF Token) adalah sistem keamanan Django untuk menghindari serangan. Sepertinya namanya Request Forgery adalah seerangan dalam bentuk request yang dipalsukan oleh pihak tidak berwenang tanpa izin. 

Django memastikan bahwa request yang diterima diverifikasi terlebih dahulu atas pihak siapa yang mengirimkannya. Hal ini dilakukan dengan memastikan request yang diterima berasal dari web yang terdaftar saja dan token valid untuk hanya satu sesi user.

Tanpa adanya CSRF Token, peretas dapat mengekstrak dan mengubah data pada server dan mengoverload server dengan request berlebih. Oleh karena itu amat pentin untuk menaruh CSRF Token demi memastikan wewenang user yang melakukan request.




################

Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

Jawaban :

1. Pertama saya mempeersiapkan template dasar html web dengan base.html pada root folder. Dengan kode berikut :
```
{% load static %}
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    {% block meta %} {% endblock meta %}
  </head>

  <body>
    {% block content %} {% endblock content %}
  </body>
</html>
```
Webpage dari aplikasi akan diload pada bagian body di area block content
Tambahkan template base ke list TEMPLATES pada settings.py
```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
    }
]
```
Lalu ubah bagian dari main.html pada main untuk mengisi block content sebagai berikut :
```
 {% extends 'base.html' %}
 {% block content %}

 ... # kode main html sebelumnya 


 {% endblock content %}
```

2. Buat Model yang akan menjadi data disubmit dari form, saya merevisi model sebelumnya. Kita dapat menggunakan uuid untuk membuat id untik setiap instancee model yan disubmit via form sebagai berikut :
```
import uuid  
...
class [NAMA KELAS MODEL](models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  
    ... # kode sebelumnya
...
```
Lakukan migrasi baru dengan perintah di cmd/terminal (pastikan env sudah diaktifkan) :
```
python manage.py makemigrations
python manage.py migrate
```

3. Selanjutnya saya akan membuat html yang dapat menampilkan form yang telah disubmit dengan membuat berkas value dari data yan disubmit dalam berkas baru bernama forms.py di folder main, sebagai berikut :
```
from django.forms import ModelForm
from main.models import [NAMA KELAS MODEL]

class [NAMA FORM](ModelForm):
    class Meta:
        model = MoodEntry
        fields = ["[NAMA FIELD]", "[NAMA FIELD]", ... ]
```
Untuk memastikan web dapat melakukan redirect antar html tambahkan import di bagian views.py pada folder main untuk redirect, form, dan model :
```
from django.shortcuts import render, redirect 
from main.forms import [NAMA FORM]
from main.models import [NAMA KELAS MODEL]
```
Lalu buat sistem redirect dari main.html ke page form dengan membuat fungsi pada berkas views.py
```
def [NAMA FUNGSI](request):
    form = [NAMA FORM](request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:[FUNGSI MENAMPILKAN MAIN SEPEERTI show_main]')

    context = {'form': form}
    return render(request, "[NAMA PAGE BERISIKAN FORM]", context)
```
Saya menambahkan juga nilai variabe pada views.py di fungsi show_main untuk menampilkan tabel berisikan instance model hasil submit form dengan listing semua objects dan memasukkan kedalam context list :
```
def show_main(request):
    [NAMA var_entries] = [NAMA KELAS MODEL].objects.all()

    context = {
        ...
        '[NAMA var_entris]':[NAMA var_entris]
    }

    return render(request, "main.html", context)
```
Tambahkan fungsi menampilkan form di urls.py pada main folder
```
from main.views import show_main, [NAMA FUNGSI]
...
urlpatterns = [
   ...
   path('[NAMA-FUNGSI]', [NAMA_FUNGSI], name='[NAMA_FUNGSI]'), # antar kata pada parameter pertama dipisahkan denan '-' dan '_' untuk parameter lainnya
]
...
```
Buat pula berkas baru dengan nama [NAMA FUNGSI REDIRECT].html untuk form dengan format serupa denan main.html :
```
{% extends 'base.html' %} 
{% block content %}
...
# isi dengan form, bisa seperti berikut
<form method="POST">
  {% csrf_token %}
  <table>
    {{ form.as_table }}
    <tr>
      <td></td>
      <td>
        <input type="submit" value="[Text pada button submit]" />
      </td>
    </tr>
  </table>
</form>

{% endblock %}
```
Untuk menampilkan nilai dari object dalam bentuk tabel di main.html tambahkan kode seperti berikut untuk menampilkan data :
```
...
{% if not [NAMA var_entries dari show_main] %} # var_entries masih kosong
# isi teks bahwa belum diperoleh data
{% else %} # tampilkan data dalam bentuk tabel
<table>
  <tr>
    <th>[NAMA FIELD1]</th>
    <th>[NAMA FIELD2]</th>
    <th>[NAMA FIELD3]</th>
    ... dst. # ikuti format html table
  </tr>

  {% for [local var] in [NAMA var_entries] %}
  <tr>
    <td>{{[local var].[NAMA FIELD1]}}</td>
    <td>{{[local var].[NAMA FIELD2]}}</td>
    <td>{{[local var].[NAMA FIELD3]}}</td>
    ... dst # ikuti format html table
  </tr>
  {% endfor %}
</table>
{% endif %} # buat line baru

<br />

<a href="{% url 'main:[NAMA HTML FUNGSI REDIRECT]' %}"> # hyperlink dalam button
  <button>[TEXT PADA BUTTON]</button>
</a>

{% endblock %}
```


4. Selanjutnya saya menambahkan library dengan mengimpor di bagian atas berkas views.py di main untuk memberikan website kemampuan mengirim dan menerima request dari website dan Serializer
```
from django.http import HttpResponse
from django.core import serializers
```


5. Kemudian saya menambahkan 4 fungsi baru di berkas views.py di folder main agar dapat membuka HttpResponse dalam format XML dan JSON secara menyeluruh atau per id dari setiap model (hasil submit data dan request) yan dibuat :
```
...

def show_xml(request):
    data = [NAMA KELAS MODEL].objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = [NAMA KELAS MODEL].objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = [NAMA KELAS MODEL].objects.filter(pk=id) #tambahkan filter berupa id
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = [NAMA KELAS MODEL].objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
Untuk memastikan fungsi ini dapat diakses pada url web maka import fungsi tersebut dan tambahkan url pattern untuk mengakses web dengan penambahan pada url web hosting (seperti url.com/xml/) pada berkas urls.py di folder main :
```
from main.views import show_main, [NAMA FUNGSI REDIRECT], show_xml, show_json, show_xml_by_id, show_json_by_id
...
urlspatterns = [
    ...
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    ...
]
```
Untuk mengecek objek dalam XML atau JSON, kita hanya perlu mengisi url dengan tambahan url.com/xml/ atau url.com/json/ sebagai berikut :

Untuk semua objek via XML 

http://localhost:8000/xml/ 
atau 
[URL ALLOWED HOSTS]/xml/ 

Untuk objek dengan id [NILAI ID] via XML 

http://localhost:8000/xml/[NILAI ID]/ 
atau 
[URL ALLOWED HOSTS]/xml/[NILAI ID]/ 


Untuk semua objek via JSON

http://localhost:8000/json/ 
atau 
[URL ALLOWED HOSTS]/json/ 

Untuk objek dengan id [NILAI ID] via JSON 

http://localhost:8000/json/[NILAI ID]/ 
atau 
[URL ALLOWED HOSTS]/json/[NILAI ID]/ 

Catatan : Hanya bisa dibuka saat server diaktifkan



################

Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.
Melakukan add-commit-push ke GitHub.

Jawaban :

XML
![Screenshot 2024-09-18 003134](https://github.com/user-attachments/assets/8daa20c8-1bcd-446a-9fc5-a89757a7ca9c)
![Screenshot 2024-09-18 003206](https://github.com/user-attachments/assets/cee69a6f-e2fc-4a87-9e2e-9e9c67bf69ed)

JSON
![Screenshot 2024-09-18 003146](https://github.com/user-attachments/assets/702c7959-7a67-4055-8b2d-60c7fe96a88e)
![Screenshot 2024-09-18 003246](https://github.com/user-attachments/assets/3c10fd69-23c1-4cfa-887f-d97807d8f590)

################

##TUGAS 4 - Karina Maharani 2306165736 PBP A

Apa perbedaan antara HttpResponseRedirect() dan redirect()

Jawab :
HttpResponseRedirect() dan redirect() digunakan untuk melakukan redirect ke page lain, akan tetapi penggunaan HttpResponseRedirect dan redirect berbeda. HttpResponseRedirect memberikan kustomisasi yang lebih luas dibandingkan redirect karena redirect dibatasi dengan parameternya yaitu link url atau url pattern atau model yang didefiniskan oleh django. 

Hal ini dikarenakan HttpResponseRedirect() berasal dari kelas tersendiri sehingga HttpResponseRedirect() bisa memberikan opsi lebih banyak seperti url absolut atau url eksternal dan kode 302, yang berarti "Redirect Sementara" ke url baru yang ditentukan jika url utama bermasalah. Untuk membantu pencarian url berdasarkan pattern kita menggunakan bantuan reverse()


Jelaskan cara kerja penghubungan model Product dengan User!

Jawab :
Model Product dihubungkan dengan Model User melalui penggunaan Foreign Key pada model tabel relasional database. Hubungan model foreign key bekerja dengan membuat kolom baru pada tabel Product (yang berpartisipasi secara total) pada model ER/EER yang berisikan data yang diperoleh dari primary key entity relationalnya yaitu User.    


Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.

Jawab :
Authentication merujuk pada proses verifikasi pengguna yang melakukan login dengan pengecekan apabila username dan password terdaftar. Jika terdaftar user diterima sebagai user dan bukan guest serta bisa mengakses situs/aplikasi. Authentication tidak hanya sebatas mengisi username dan password tapi berupa two-authentication dimana kita melakukan autentifikasi dengan gawai lain (mengisi kode otp). 

Authorization merujuk pada verfikasi perizinan akses fitur untuk user berdasarkan status/role user. Misalkan mahasiswa akan memiliki akses untuk melakukan unggah tugas sedangkan dosen memiliki fitur untuk merilis kuis dn tugas.

Dalam kasus Django Authentication dan Authorization, Client side akan merequest server untuk melakukan pengecekan apabila credentials yang dikirimkan valid dan memiliki perizinan yang diingikan jika ya maka credentials tersebut akan diproses sebagai identifikasi sebuah session. Session ini akan memberikan Http yang bersifat stateless untuk tetap memberikan informasi yang benar ke user sekalipun banyak request data yang dilakukan, session dengan credentials ini akan menjadi identifikasi terkait response apa yang diberikan.


Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?

Jawab :

Django dapat mengingat sesi login dengan cookies, cookie yang digunakan dibagi menjadi dua yaitu session cookie (temporary) dimana cookie disimpan di browser shingga saat user menutup tab dan membuka kembali tab url yang sama di isntance browser yang sama user tetap terhubung hingga instance browser tersebut dihapus. Adapula persistent cookie yaitu cookie yang disimpan di browser computer sehingga saat instance browser ditutup informasi cookie tetap disimpan. Django sendiri menggunakan keduanya untuk menjalankan situs, temporary cookies akan dihapus setelah user menutup web, kecuali jika pengguna memilih untuk tetap login. Sedangkan persistent cookie Django digunakan untuk menyimpan data sesi di server (biasanya dalam database, tetapi juga bisa di cache atau file) sehingga saat user melakukan log in informasi di instance web/sesi sebelumnya tetap tersimpan.

Selain sistem log in, cookie bisa digunakan untuk menyimpan preferences user, rekomendasi untuk user, dan lain-lainnya. Perlu diketahui bahwa walaupun cookie tidak secara langsung menyimpan informasi pribadi melainkan program data, tidak semua cookie aman. Terutama persistent cookie dari third party cookies yang di manage oleh pihak server jika server atau situs tidak dibuat in-house.



Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

Jawab :
1. Pertama kita akan membuat terlebih dahulu form baru untuk membuat sistem register, login, logout serta objeK user.
Pada views.py di folder main tambahkan imporrt library untuk pembuatan user dan fungsi register serta login dengan sistem authentication sebagai berikut
```
#untuk register
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

#untuk login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login

#untuk log out
from django.contrib.auth import logout

kode sebelumnya...

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:[HTML LOGIN]')
    context = {'form':form}
    return render(request, '[HTML REGISTER]', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main:[FUNGSI MENAMPILAN MAIN]')
   else:
      form = AuthenticationForm(request)

   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('main:login')

```

2. Kemudian untuk mmbuat tampilan pagge register dan login buatlah berkas html untuk tampilan login dan register dengan nama seperti login.html dan register.html pada folder template di folder main dengan conttoh isi seperti berikut :
```
##untuk register.html
{% extends 'base.html' %}

{% block meta %}
<title>Register</title>
{% endblock meta %}

{% block content %}

<div class="login">
  <h1>Register</h1>

  <form method="POST">
    {% csrf_token %}
    <table>
      {{ form.as_table }}
      <tr>
        <td></td>
        <td><input type="submit" name="submit" value="Daftar" /></td>
      </tr>
    </table>
  </form>

  {% if messages %}
  <ul>
    {% for message in messages %}
    <li>{{ message }}</li>
    {% endfor %}
  </ul>
  {% endif %}
</div>

{% endblock content %}
```

```
##untuk login.html
{% extends 'base.html' %}

{% block meta %}
<title>Login</title>
{% endblock meta %}

{% block content %}
<div class="login">
  <h1>Login</h1>

  <form method="POST" action="">
    {% csrf_token %}
    <table>
      {{ form.as_table }}
      <tr>
        <td></td>
        <td><input class="btn login_btn" type="submit" value="Login" /></td>
      </tr>
    </table>
  </form>

  {% if messages %}
  <ul>
    {% for message in messages %}
    <li>{{ message }}</li>
    {% endfor %}
  </ul>
  {% endif %} Don't have an account yet?
  <a href="{% url 'main:register' %}">Register Now</a> #jika user belum punya akun, akkan diminta membuat akun di page register
</div>

{% endblock content %}
```
untuk logout kita dapat menambahkkan button di main page sehingga user bisa melakukan logout dari akun secara lnsgung
```
#main.html

kode sebelumnya...
<a href="{% url 'main:logout' %}">
  <button>Logout</button>
</a>


```


4. tambahkan pula urls agar webpage register, login dan logout dapat diakses dengan menambahan fungsi register dan login pada urls.py di folder main
```
from main.views import register, login_user, logout_user

urlpatterns = [
  ...
  path('register/', register, name='register'),
  path('login/', login_user, name='login'),
  path('logout/', logout_user, name='logout'),
]

```

5. Selanjutnya kita akan memodifikasi bentuk sesi untuk merestrikk akses ke situs agar hanya user yang sudah login saja yang bisa mengakses dengan menambahan requirement pada views.py di folder main untuk login dan berikan property requirement sebelum fungsi yang menampilkan main agar program tidak sembarang masuk ke main tanpa login
```

from django.contrib.auth.decorators import login_required

kode sebelumnya ...

@login_required(login_url='/login')
def show_main(request):
  kode show_main sebelumnya ...

...

```

6. Jika kita ingin menyimpan dan menampilkan login terakhir kita dapat menggunakan cookies sementara. Pertama kita bisa menggunakan import library untu menyimpan time dan juga memberikan response http pada view.py di main.html dengan
```
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

```

7. Ubah fungsi login pada views.py untuk merecord informasi login trakhir sebagai berikut
```
def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

if form.is_valid():
    user = form.get_user()
    login(request, user)
    response = HttpResponseRedirect(reverse("main:[FUNGSI MENAMPILKAN MAIN]"))
    response.set_cookie('last_login', str(datetime.datetime.now()))
    return response
   else:
      form = AuthenticationForm(request)

   context = {'form': form}
   return render(request, 'login.html', context)

```

8. untuk menampilkan nilai last_login pada main kita dapat menambahkan variabel baru di context pada show_main di view.py sebagai berikut :
```
...

  kode show_main sebelumnya ...
  context = {
    kode sebelumnya ...
    'last_login': request.COOKIES['last_login'],
  }
  ...

...

```

9. Untuk keamanan dan saving space jangan lupa untuk menghapus cookies saat melakukan logout, lakukan modifikasi pada sistem logout di views.py sebagai berikut 
```
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```

10. Untuk membuat name pada situs sesuai dengan user yang masuk kita dapat membuat model baru dlaam bentuk user dengan import/menambahkan model pada models.py dan menambahkan parametere user pada model program sebaai berikut :
```
  from django.contrib.auth.models import User
  ...

  class ProductEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    ...
```

11. Tambahkan parameter user agar program dapat mendetect penambahan/permintaan request berdasarkan user tertentu dengan mengubah function yang melakukan request seperti pada views.py di folder main sebagai berikut 
```
def create_product_entry(request):
    form = ProductEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit=False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product_entry.html", context)

```

12. Modifikasi pula data pada context show_main pada views.py untuk mengambil username dari objek user yang logged in
```
def show_main(request):
    ...

    context = {
         'name': request.user.username,
         ...
    }
...
```

13. Untuk menyimpan model yang sudah diprebarui, lakukan migration pada terminal dengan kode
```
python manage.py makemigrations
python manage.py migrate
```
Jika muncul error terkait default value pilih opsi 1 denggan nilai default asal seperti 1 untuk menyelesaikan error tersebut aar database tetap valid.

13. Sebagai tembahan kita dapat mempersiapkan environment production dengan menambahkkan beberapa baris kode di settings.py di folder [nama project]
```
import os

...
#replace debug dengan 2 line ini
PRODUCTION = os.getenv("PRODUCTION", False)
DEBUG = not PRODUCTION

...

```

################

TUGAS 5
Karina Maharani 22306165736

1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!

Prioritas didasarkan oleh hierarki. Secara garis besar terdapat 4 area hierarki sebagai berikut :
 1. Origin & Importance
  Inline CSS > Internal CSS > External CSS (semakin kekanan semakin kurang prioritasnya dan akan dioverridee oleh yang disebelah kirinya) 

 2. Selector Specificity
  id (#id_css_name)> class (.class_css_name) > tag (tag_name atau tidak ada tambahan) (semakin kekanan semakin kurang prioritasnya dan akan dioverridee oleh yang disebelah kirinya) 

 3. Order of Appearance
  Berdasarkan order dari line of code. Kode awal akan dioverride line of code baru karena dibaca dari atas ke bawah dengan lin of code terupdate sebagai rujukan terakhir
 
 4. Initial & Inherited Properties (default values)
 Komponen pada sebuah wadah/container akan meng-inherit CSS Styling dari containernnya. Misalkkan < p> yang ada didalam < div class="text-gray"> akan memiliki text color gray juga walaupun tidak disebut ekplisit pada tag < p>


2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!
Responsive design dapat digunakan pada multiple platform secara dinamis, jika kita meng-hardcode website atau kode gitu, web akan rawann untuk sulit digunakan atau bahkan tidak bisa digunakan karena layout yang digunakan membatasi fitur yang bisa diakses oleh user. 

Manfaat responsive design :
1. Readibility
2. Optimisasi Performa
3. Membantu future development, web lebih mudah di modifikasi jika sekiranya perlu fitur baru atau ingin dibuat aksesibel di platform baru seperti mobile atau IoT.

Contoh aplikasi yang sudah menerapkan responsive design adalah tokopedia yang bisa diakses via web dan mobile. Contoh aplikasi yang belum menerapkan responsive design adalah Mobile BCA yang jika dibuka di web masih mengalami issue sizing/paddingg/margin sehingga sulit digunakan.


3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
Margin adalah jarak antara elemen (elemen bisa memiliki content/elemen lainnya seperti teks), border merupakan outline/batas luar dari content, dan padding merupakan jarak antara content dengan border/elemen yang berperan sebagai container/batas luar content.
Berikut contoh implementasinya
#css_spacing {
    margin: 16px; 
    border: 2px solid black; 
    padding: 15px; 
}
Berikut adalah ilustrasi perbedaan margin, border, padding dari https://www.w3schools.com/
![Screenshot 2024-10-02 103933](https://github.com/user-attachments/assets/285ad530-ff27-4728-a581-90756d74f2d9)
![Screenshot 2024-10-02 103940](https://github.com/user-attachments/assets/e31e0ab3-4233-4d3c-b751-013e779f8546)
![Screenshot 2024-10-02 103952](https://github.com/user-attachments/assets/75c92865-6daa-4293-b15b-bb0c50a52207)


5. Jelaskan konsep flex box dan grid layout beserta kegunaannya!
Flex box adalah sifat elemen yang akan membuat layout responsif dimana setiap item didalam container terebut akan secara dinamis disusun baik itu horizontal maupun vertical, akan tetapi hal ini tentunya memiliki kekurangan dalam bentuk kurangnya kontrol dari developer untuk menyusun lokasi setiap elemen. 
Manfaat dan Kegunaan :
1. Membuat layout responsif yang bisa digunakan pada semua platform
2. Menyusun elemen horizontal atau vertikal dengan mudah dan hemat dalam proses kode

Grid Layout adalah salah satu sifat elemen untuk membuat layout dari elemen yang akan disusun ibarat tabel dua dimensi dengan mengatur elemen dalam kolom dan baris. Sistem ini memberikan kontrol penuh kepada developer untuk membuat layout spesifik, namun perlu menambahkan spesifikasi layout cukup banyak agar tetap bisa digunakan dengan pada platform lain seperti mobile tanpa mengurangi readibility web. 
Manfaat dan Kegunaan :
1. Mengatur layout yang lebih detail dengan lokasi spesifik pada screen
2. Membuat layout kompleks dengan jumlah kolom dan baris yang banyak seperti membuat tabel


5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
1. Melakukan import dari library css yang ingin digunakan seperti Bootstrap atau Tailwind dan library lainnya seperti font dengan menggunakan embed code
```
<head>
...
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Libre+Baskerville:ital,wght@0,400;0,700;1,400&family=Silkscreen:wght@400;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="{% static 'css/global.css' %}"/>
</head>
```
Misalkan seperti berikut :
2. Membuat folder pada root untuk menyimpan css yaitu folder static dan mengisi dengan folder css di dalam folder static tersebut
3. Membuat berkas css pada folder css misalkan global.css, kemudian mengisi berkas dengan styling custom dan styling font
4. Menambahkan formatting untuk setiap platform dengan menambahkan meta pada bagian head base.html
```
<head>
    {% block meta %}
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1">
    {% endblock meta %}
    ...
</head>
```
5. Kemudian ubahlah tiap page sesuai kebutuhan css dan styling ingin digunakan pada semua html seperti main.html, login.html, register.html, dsb.
6. Selanjutnya saya membuat komponen elemen yang diinginkan seperti navbar, card, atau banner dengan membuat html tiap komponen seperti card_product.html 
Misalkan card_product.html seperti berikut :
```
<div class="bg-white shadow-[0_4px_12px_-5px_rgba(0,0,0,0.4)] w-full max-w-sm rounded-lg overflow-hidden mx-auto font-[sans-serif] mt-4">
  <div class="min-h-[256px] flex items-center justify-center">
    {% if product_entry.image_url %}
      <img src="{{ product_entry.image_url }}" class="object-contain h-full w-auto" alt="{{ product_entry.name }}" />
    {% else %}
      <p class="mx-auto text-center text-gray-700">Picture Unavailable</p>
    {% endif %}
  </div>
  <div class="p-6">
    <h3 class="text-gray-800 text-xl font-bold">{{ product_entry.name }}</h3>
    <div class="flex space-x-2 mt-2">
      <span class="text-xs text-white bg-indigo-900 rounded-full px-3 py-1">{{ product_entry.tags }}</span>
      <span class="text-xs text-white bg-indigo-900 rounded-full px-3 py-1">{{ product_entry.ratings }} Stars</span>
    </div>
    <p class="mt-4 text-sm text-gray-500 leading-relaxed">{{ product_entry.description }}</p>
    <p class="mt-12 text-center text-lg text-white leading-relaxed bg-indigo-600 rounded-full silkscreen-regular">Rp.{{ product_entry.price }}</p>
    <p class="mt-4 text-sm text-gray-500 leading-relaxed">Added on {{ product_entry.time }}</p>
    <!-- Buttons for Edit and Delete -->
    <div class="flex space-x-2 justify-center mt-4">
      <a href="{% url 'main:edit_product' product_entry.pk %}" class=" inline-flex items-center bg-yellow-500 hover:bg-yellow-600 text-white rounded-full px-4 py-2 transition duration-300 shadow-md">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" viewBox="0 0 20 20" fill="currentColor">
          <path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z" />
        </svg>
        Edit
      </a>
      <a href="{% url 'main:delete_product' product_entry.pk %}" class=" inline-flex items-center bg-red-500 hover:bg-red-600 text-white rounded-full p-4 transition duration-300 shadow-md">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" viewBox="0 0 20 20" fill="currentColor">
          <path fill-rule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z" clip-rule="evenodd" />
        </svg>
        Delete
      </a>
    </div>
  </div>
</div>
```
7. Impor berkas html komponen pada page seperti main.html, login.html, register.html, dsb.
Misalkan mengimpor pada main.html untuk card_info, card_product.html dan navbar seperti berikut
```
...
{% include 'navbar.html' %}

...
{% include "card_info.html" with name=name npm=npm class=class %}

...
{% for product_entry in product_entries %}
  {% include 'card_product.html' with product_entry=product_entry %}
{% endfor %}

...
```
8. Kita bisa menambahkan static files seperti images dengan menambahkan beberapa hal pada settings.py agar static files tetap disimpan oleh server 
```
# Static files (CSS, JavaScript, Images)
# Dokumentasi: https://docs.djangoproject.com/en/5.1/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'
```
dan menjalakan perintah collectstatic
```

```
Kita bisa menggunakan link src untuk mendapat static file tersebut
```
<img src="{% static 'image/[NAMA FILE IMAGE].png' %}"
```
Dalam web ini saya belum menggunakan static image karena bisa menggunakan image link saja.
9. Lakukan push untuk semua perubahan yang dilakukan

################

TUGAS 5 -  Karina Maharani 2306165736

Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!

Jawab : 

Java script akan bekerja untuk membuat tampilan html dan hiasan css menjadi fungsional dan interaktif dengan menambahkan behaivour. Behaivour seperti membuat button yang dapat menampilan tag < p> merupakan salah satu penggunaan java script.
Java script membantu web agar lebih interaktif dan menghubungkan sisi front end dan back end web. JavaScript, terutama dengan teknologi seperti Node.js, juga bisa digunakan di server-side (back-end), sehingga JavaScript dapat bekerja baik di sisi front-end maupun back-end, misalkkan API atau AJAX, JavaScript memungkinkan pertukaran data client dan server tanpa perlu memuat ulang halaman secara asynchronus. Java script memiliki library yang luas untuk kebutuhan web untuk kebutuhan web lain. Framework dan library JavaScript seperti React dan Angular yang memudahkan pembuatan UI/UX yang dinamis dan kompleks yang membantu mempercepat pengembangan aplikasi web.

Jelaskan fungsi dari penggunaan await ketika kita menggunakan fetch()! Apa yang akan terjadi jika kita tidak menggunakan await?

Jawab : 

Await memastikan request dari fetch() diterima sepenuhnya dan diproses setelah httprequest sepenuhnya diselesaikan. Jika kita tida mengunakan await maka kode berisiko menyebabkan error karena data yang difetch dambil secara lansung tanpa mengecek apabila request sepenuhnya dipenuhi. Oleh karena itu perlu penanganan tambahan untuk memastikakn fetch tanpa await tidak menghasilkan error. Hal ini sangat penting terutama untuk proses asynchronus pada web karena await memastikan bahwa fungsi asynchronous ditahan sementara sampai dengan request sebelumnya selesai.


Mengapa kita perlu menggunakan decorator csrf_exempt pada view yang akan digunakan untuk AJAX POST?

Jawab : 

Kita menambahkann csrf_exempt untuk memastikan bahwa ketika melakukan POST melalui AJAX, input user dapat diterima, dalam csrf biasa django akan membaca token csrf pada request untuk memastikan bahwa token yang diterima benar valid dari requester yaitu penguna website bukan pihak eksternal. Dalam AJAX csrf tidak digunakan karena AJAX tidak menginclude token tersebut, oleh karena itu kita lakukan pennegcualian untuk AJAX dengan meng-exempt token tersebut. Jika kkita tidak melakukan excemption makka Django akan otomatis memblokir request.


Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja?

Jawab : 

Karena front end diakses langsung oleh user maka akan lebih rawan untuk dilakukan serangan oleh peretas, sehingga pembersihan data pentin dilakukan pada backend agar program tetap berjalan saat front end peretas berhasil di modifikasi. Back end juga tidak serentan front end karena lebih platform agnostic, beberapa browser seringkali memiliki arsitektur yang berbeda dan celah mungkin saja muncul di sisi front end. Pembersihan Back end jua mengavoid dillakukannya injksi seperti Cross-Site Scripting dengan memastikan data yang akan masuk ke backend berhasil ditangkap terlebih dahulu. Selain itu Back end juga cenderung lebih lengkap dalam fitur keamanannya karena memiliki validasi yang lebih kuat dibandingkan front end seperti tipe data yang dapat dipertimbangkan



Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

Jawab : 

- Menambah verifikasi user login jika user terdaftar dengan penambahan di kode di views.py pada fungsi login
```
if form.is_valid():
    user = form.get_user()
    login(request, user)
    response = HttpResponseRedirect(reverse("main:show_main"))
    response.set_cookie('last_login', str(datetime.datetime.now()))
    return response
else:
    messages.error(request, "Invalid username or password. Please try again.")
```

- Menambahkan fungsi AJAX untuk penambahan produk

dengan menambahkan csfr exempt dan juga requirement POST 
```
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
```
lanjut denggan pembuatan fungsi penambahan produk ajax di views.py sebagai fungsi baru dan routing
```
# dalam file views.py
@csrf_exempt
@require_POST
def create_product_entry_ajax(request):
    name = strip_tags(request.POST.get("name"))
    price = strip_tags(request.POST.get("price"))
    description = strip_tags(request.POST.get("description"))
    time = strip_tags(request.POST.get("time"))
    tags = strip_tags(request.POST.get("tags"))
    ratings = strip_tags(request.POST.get("ratings"))
    image_url = strip_tags(request.POST.get("image_url"))
    user = request.user

    new_product = Product(
        name=name, price=price,
        description=description,
        time=time,
        tags=tags,
        ratings=ratings,
        image_url=image_url,
        user=user
    )
    new_product.save()

    return HttpResponse(b"CREATED", status=201)
```
```
# dalam file urls.py
from main.views import ..., create_product_entry_ajax
...
urlpatterns = [
    ...
    path('create-product-entry-ajax', create_product_entry_ajax, name='create_product_entry_ajax'),
]
...
```

- Hapus instance dari models show_main di fungsi show_main dan tambahkan baris ke show_json dan show_xml
```
... # fungsi show_main
product_entries = Product.objects.filter(user=request.user) # hapus baris
...
'product_entries': product_entries, # hapus baris
...
```
```
... # fungsi show_json dan show_xml
data = Product.objects.filter(user=request.user)
```

- Hapus sistem card printin di web dan buat div dengan id sebagai container tampilan data saat sudah membuat instannce di database di main.html
```
# hapus
...
    {% if not product_entries %}
        <div class="flex flex-col items-center justify-center min-h-[24rem] p-6">
            <img src="{% static 'image/sedih-banget.png' %}" alt="Sad face" class="w-32 h-32 mb-4"/>
            <p class="text-center text-gray-600 mt-4">Belum ada data produk.</p>
        </div>
    {% else %}
        <div class="columns-1 sm:columns-2 lg:columns-3 gap-6 space-y-6 w-full">
            {% for product_entry in product_entries %}
                {% include 'card_product.html' with product_entry=product_entry %}
            {% endfor %}
        </div>
    {% endif %}

# ganti dengan 
<div id="product_entry_cards"></div>
...
```

- Penambahan fitur DOM dan strip tags pada berkas dan import
```
# dalam forms.py
from django.forms import ModelForm
from main.models import Product
from django.utils.html import strip_tags

class ProductEntryForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "tags", "ratings", "image_url"]

    def clean_name(self):
        name = self.cleaned_data["name"]
        return strip_tags(name)

    def clean_price(self):
        price = self.cleaned_data["price"]
        return strip_tags(price)
    
    def clean_description(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)

    def clean_tags(self):
        tags = self.cleaned_data["tags"]
        return strip_tags(tags)
    
    def clean_ratings(self):
        ratings = self.cleaned_data["ratings"]
        return strip_tags(ratings)
    
    def clean_image_url(self):
        image_url = self.cleaned_data["image_url"]
        return strip_tags(image_url)
```
```
# dalam views.py
...

from django.utils.html import strip_tags

...

@csrf_exempt
@require_POST
def create_product_entry_ajax(request):
    name = strip_tags(request.POST.get("name"))
    price = strip_tags(request.POST.get("price"))
    description = strip_tags(request.POST.get("description"))
    time = strip_tags(request.POST.get("time"))
    tags = strip_tags(request.POST.get("tags"))
    ratings = strip_tags(request.POST.get("ratings"))
    image_url = strip_tags(request.POST.get("image_url"))
    user = request.user

    new_product = Product(
        name=name, price=price,
        description=description,
        time=time,
        tags=tags,
        ratings=ratings,
        image_url=image_url,
        user=user
    )
    new_product.save()

    return HttpResponse(b"CREATED", status=201)
...
```
```
# dalam main.py
...
{% block meta %}
<title>Raringo</title>
<script src="https://cdn.jsdelivr.net/npm/dompurify@3.1.7/dist/purify.min.js"></script>
{% endblock meta %}
{% block content %}
...
```

- Penambahan modal pada mains.html untuk penerimaan forum tanpa membuka web page baru dalam main.html
```
<div class="overflow-x-auto">
      <div class="flex flex-col items-center justify-center min-h-[24rem] p-6">
        <div id="product_entry_cards">
        </div>
        <div id="crudModal" tabindex="-1" aria-hidden="true" class="hidden fixed inset-0 z-50 w-full flex items-center justify-center bg-gray-800 bg-opacity-50 overflow-x-hidden overflow-y-auto transition-opacity duration-300 ease-out">
          <div id="crudModalContent" class="relative bg-white rounded-lg shadow-lg w-5/6 sm:w-3/4 md:w-1/2 lg:w-1/3 mx-4 sm:mx-0 transform scale-95 opacity-0 transition-transform transition-opacity duration-300 ease-out">
            <!-- Modal header -->
            <div class="flex items-center justify-between p-4 border-b rounded-t">
              <h3 class="text-xl font-semibold text-gray-900">
                Add New Product Entry
              </h3>
              <button type="button" class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 ml-auto inline-flex items-center" id="closeModalBtn">
                <svg aria-hidden="true" class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                  <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"></path>
                </svg>
                <span class="sr-only">Close modal</span>
              </button>
            </div>
            <!-- START HERE FOR MODAL--> 
            <div class="px-6 py-4 space-y-6 form-style">
              <form id="productEntryForm">
                <div class="mb-4">
                  <label for="name" class="block text-sm font-medium text-gray-700">Name</label>
                  <input type="text" id="name" name="name" class="mt-1 block w-full border border-gray-300 rounded-md p-2 hover:border-indigo-700" required>
                </div>
                <div class="mb-4">
                  <label for="price" class="block text-sm font-medium text-gray-700">Price</label>
                  <input type="number" id="price" name="price" min="1" class="mt-1 block w-full border border-gray-300 rounded-md p-2 hover:border-indigo-700" required>
                </div>
                <div class="mb-4">
                  <label for="description" class="block text-sm font-medium text-gray-700">Description</label>
                  <textarea id="description" name="description" rows="3" class="mt-1 block w-full h-52 resize-none border border-gray-300 rounded-md p-2 hover:border-indigo-700" placeholder="Describe the product" required></textarea>
                </div>
                <div class="mb-4">
                  <label for="tags" class="block text-sm font-medium text-gray-700">Tags</label>
                  <input type="text" id="tags" name="tags" class="mt-1 block w-full border border-gray-300 rounded-md p-2 hover:border-indigo-700" required>
                </div>
                <div class="mb-4">
                  <label for="ratings" class="block text-sm font-medium text-gray-700">Ratings</label>
                  <input type="number" id="ratings" name="ratings" min="0" max="5" class="mt-1 block w-full border border-gray-300 rounded-md p-2 hover:border-indigo-700" required>
                </div>
                <div class="mb-4">
                  <label for="image_url" class="block text-sm font-medium text-gray-700">Image url</label>
                  <input type="text" id="image_url" name="image_url" class="mt-1 block w-full border border-gray-300 rounded-md p-2 hover:border-indigo-700" required>
                </div>
              </form>
            </div>
            <!-- Modal footer -->
            <div class="flex flex-col space-y-2 md:flex-row md:space-y-0 md:space-x-2 p-6 border-t border-gray-200 rounded-b justify-center md:justify-end">
              <button type="button" class="bg-gray-500 hover:bg-gray-600 text-white font-bold py-2 px-4 rounded-lg" id="cancelButton">Cancel</button>
              <button type="submit" id="submitProductEntry" form="productEntryForm" class="bg-indigo-700 hover:bg-indigo-600 text-white font-bold py-2 px-4 rounded-lg">Save</button>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="flex justify-center mt-16">      
      <h5>Sesi terakhir login: {{ last_login }}</h5>
      <br />
    </div>
```


- Tambahkan sistem submit form, XSS avoidance, data validation, modal dan reefresh data dari database pada di main.html dengan script java script serta memafaat ui/ux dalam tugas 5
```

<script>
    function addProductEntry() {
    fetch("{% url 'main:create_product_entry_ajax' %}", {
      method: "POST",
      body: new FormData(document.querySelector('#productEntryForm')),
    })
    .then(response => refreshProductEntries())

    document.getElementById("productEntryForm").reset(); 
    document.querySelector("[data-modal-toggle='crudModal']").click();

    return false;
  }

  async function getProductEntries(){
      return fetch("{% url 'main:show_json' %}").then((res) => res.json())
  }

  async function refreshProductEntries() {
    document.getElementById("product_entry_cards").innerHTML = "";
    document.getElementById("product_entry_cards").className = "";
    const productEntries = await getProductEntries();
    let htmlString = "";
    let classNameString = "";

    if (productEntries.length === 0) {
        classNameString = "flex flex-col items-center justify-center min-h-[24rem] p-6";
        htmlString = `
            <div class="flex flex-col items-center justify-center min-h-[24rem] p-6">
                <img src="https://www.svgrepo.com/show/525569/upload-minimalistic.svg" alt="No Product Added" class="w-32 h-32 mb-4"/>
                <p class="text-center text-gray-600 mt-4">Please, add at least one product.</p>
            </div>
        `;
    }
    else {
        classNameString = "columns-1 sm:columns-2 lg:columns-3 gap-6 space-y-6 w-full"
        productEntries.forEach((item) => {
            const name = DOMPurify.sanitize(item.fields.name);
            const price = DOMPurify.sanitize(item.fields.price);
            const description = DOMPurify.sanitize(item.fields.description);
            const tags = DOMPurify.sanitize(item.fields.tags);
            const ratings = DOMPurify.sanitize(item.fields.ratings);
            const time = DOMPurify.sanitize(item.fields.time);
            const image_url = DOMPurify.sanitize(item.fields.image_url);
            htmlString += `
            <div class="relative break-inside-avoid">
              <div class="bg-white shadow-[0_4px_12px_-5px_rgba(0,0,0,0.4)] w-full max-w-sm rounded-lg overflow-hidden mx-auto font-[sans-serif] mt-4">
                <div class="min-h-[256px] flex items-center justify-center">
                    <img src="${image_url}" class="object-contain h-full w-auto" alt="${name}" />
                </div>
                <div class="p-6">
                  <h3 class="text-gray-800 text-xl font-bold">${name}</h3>
                  <div class="flex space-x-2 mt-2">
                    <span class="text-xs text-white bg-indigo-900 rounded-full px-3 py-1">${tags}</span>
                    <span class="text-xs text-white bg-indigo-900 rounded-full px-3 py-1">${ratings} Stars</span>
                  </div>
                  <p class="mt-4 text-sm text-gray-500 leading-relaxed">${description}</p>
                  <p class="mt-12 text-center text-lg text-white leading-relaxed bg-indigo-600 rounded-full silkscreen-regular">Rp.${price}</p>
                  <p class="mt-4 text-sm text-gray-500 leading-relaxed">Added on ${time}</p>
                  <!-- Buttons for Edit and Delete -->
                  <div class="flex space-x-2 justify-center mt-4">
                    <a href="/edit-product/${item.pk}" class=" inline-flex items-center bg-yellow-500 hover:bg-yellow-600 text-white rounded-full px-4 py-2 transition duration-300 shadow-md">
                      <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" viewBox="0 0 20 20" fill="currentColor">
                        <path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z" />
                      </svg>
                      Edit
                    </a>
                    <a href="/delete/${item.pk}" class=" inline-flex items-center bg-red-500 hover:bg-red-600 text-white rounded-full p-4 transition duration-300 shadow-md">
                      <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" viewBox="0 0 20 20" fill="currentColor">
                        <path fill-rule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z" clip-rule="evenodd" />
                      </svg>
                      Delete
                    </a>
                  </div>
                </div>
              </div>
            </div>
            `;
        });
    }
    document.getElementById("product_entry_cards").className = classNameString;
    document.getElementById("product_entry_cards").innerHTML = htmlString;
}
refreshProductEntries();

    const modal = document.getElementById('crudModal');
    const modalContent = document.getElementById('crudModalContent');

    function showModal() {
        const modal = document.getElementById('crudModal');
        const modalContent = document.getElementById('crudModalContent');

        modal.classList.remove('hidden'); 
        setTimeout(() => {
          modalContent.classList.remove('opacity-0', 'scale-95');
          modalContent.classList.add('opacity-100', 'scale-100');
        }, 50); 
    }

    function hideModal() {
        const modal = document.getElementById('crudModal');
        const modalContent = document.getElementById('crudModalContent');

        modalContent.classList.remove('opacity-100', 'scale-100');
        modalContent.classList.add('opacity-0', 'scale-95');

        setTimeout(() => {
          modal.classList.add('hidden');
        }, 150); 
    }

    document.getElementById("cancelButton").addEventListener("click", hideModal);
    document.getElementById("closeModalBtn").addEventListener("click", hideModal);

    document.getElementById("productEntryForm").addEventListener("submit", (e) => {
      e.preventDefault();
      addProductEntry();
    })
  
</script>
```

################


Copyright 2024 Karina Maharani

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

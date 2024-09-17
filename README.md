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

##TUGAS 3

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


![Screenshot 2024-09-18 003134](https://github.com/user-attachments/assets/8daa20c8-1bcd-446a-9fc5-a89757a7ca9c)
![Screenshot 2024-09-18 003206](https://github.com/user-attachments/assets/cee69a6f-e2fc-4a87-9e2e-9e9c67bf69ed)
![Screenshot 2024-09-18 003146](https://github.com/user-attachments/assets/702c7959-7a67-4055-8b2d-60c7fe96a88e)
![Screenshot 2024-09-18 003246](https://github.com/user-attachments/assets/3c10fd69-23c1-4cfa-887f-d97807d8f590)

################



################


Copyright 2024 Karina Maharani

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

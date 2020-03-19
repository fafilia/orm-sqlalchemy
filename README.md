# Object Relational Mapper

## Introduction
Well, Hi peeps. Pada kali ini saya akan sedikit bercerita tentang `Object Relational Mapping` atau yang biasa orang sebut sebagai ORM. Apa sih ORM itu? Oke sebelum kita mengenal lebih jauh tentang ORM, yang perlu kita lihat pertama kali adalah apa perbedaan ORM ini dengan Relational database pada umumnya. Di antara dari kalian pasti sudah sangat familiar bukan dengan Relational Database? Yups, Jika kalian perna mendengar MySQL, PostgreSQL, atau Oracle mereka ini adalah ~salah tiga~ contoh dari Relational Database Management System (RDBMS). Singkatnya untuk bekerja dengan mereka, kita biasanya perlu menulis query SQL untuk diteruskan ke db engine kemudian database memparsing hasil query dan dikembalikan sebagai array of records. Nah kemudian apa bedanya dengan si ORM ini? Intinya ORM mencoba untuk mengubah query SQL menjadi query yang bersifat object-oriented. ORM dibuat agar `objek` dapat dipetakan atau bisa saling berelasi pada sebuah record di database. Ibarat kata nih kalo di relational database kalian mengenal adanya tabel-tabel yang saling berelasi, kalau di ORM ini yang saling berelasi adalah objek-objek yang diibaratkan sebagai tabel. Nah sebelum kalian tambah pusing coba untuk merefresh kembali apa itu OOP agar kalian lebih familiar lagi dengan istilah `objek` dan bagaimana karakteristiknya. 

Nah dipembahasan kali ini, saya juga akan mengenalkan salah satu ORM di Python yang sering digunakan yaitu SQLAlchemy. Bahasa pemrograman Python sendiri memiliki banyak sekali ORM seperti Storm, Django ORM, PonyORM, dan masih banyak lagi dan bisa kalian cek [disini](https://www.pythoncentral.io/sqlalchemy-vs-orms/). Selanjutnya kalian bisa cek langsung di repositori ini apa itu ORM dan bagaimana cara kerjanya serta implementasi dari SQLAlchemy di Python.

## Dependencies
Pada repositori ini, kalian akan menemukan file yang tersimpan dalam format `.ipynb` yang berisi tutorial penggunaan SQLAlchemy. Namun sebelum itu, kalian perlu menginstall terlebih dahulu package SQLAlchemy pada environment yang kalian gunakan. Untuk menginstall SQLAlchemy kalian bisa menggunakan conda atau pip dengan perintah sebagai berikut:

- Conda Installation
```
conda install -c anaconda sqlalchemy
```

- Pip Installation
```
pip install SQLAlchemy
```

<center><h1>Object Relational Mapping </center>

## Konsep ORM

<img src="assets/ORM concept.PNG">

Object Relational Mapping (ORM) dalah sebuah teknik pemrograman yang mencoba untuk memetakan objek dengan database. ORM ini nantinya akan bertindak sebagai jembatan antara objek dari lingkungan bahasa pemrograman yang berorientasi objek (OOP) dengan lingkungan database relational. ORM dipilih karena manfaatnya yang lebih efisien dalam penulisan syntaks daripada syntaks database relational sendiri yang terlalu panjang. Bagi Anda yang terbiasa menggunakan SQL, Anda pasti merasakan betapa frustasinya Anda ketika menuliskan query yang sangat panjang belum ditambah jika hasil eksekusinya mengeluarkan error. Hadirnya ORM ini tentunya mempermudah bagi kita orang-orang yang sering bekerja dengan bahasa pemrograman berorientasi objek seperti Python, Java, dll. ORM dibuat agar objek dapat dipetakan atau direlasikan ke suatu record di database, ORM juga mengubah sintaks SQL menjadi sintaks yang bersifat object-oriented. Hal ini tentunya memudahkan programmer dan meningkatkan produktifitas dalam hal menggunakan database karena object sudah terhubung langsung dengan record-record pada database. Untuk jenis ORM sendiri sudah sangat banyak dikembangkan sesuai dengan bahasa pemrograman masing-masing. Kali ini, kita akan melihat salah satu contoh ORM yang ada di Python yaitu SQLAlchemy. Bahasa pemrograman Python sendiri juga memiliki beberapa ORM seperti DjangoORM, PonyORM, Storm, peewee, dll. SQLAlchemy dipilih karena karakteristiknya pada enterprise-level API yang membuat kode yang ditulis lebih robust dan adaptable serta designya yang fleksibel karena tidak membuat kita merasa 'sakit' ketika harus menulis query yang terlalu kompleks. Pembahasan mengenai SQLAlchemy dapat Anda temukan setelah kita membahas kelebihan dari ORM.

## Kelebihan ORM
- Mereduksi query yang sifatnya berulang. Hal ini tentunya akan mempercepat proses pengembangan program.
- Mengantisispasi adanya banyak error yang terjadi mengingat syntaks yang ditulis tidak akan sepanjang jika menuliskan query dengan database relational
- ORM menyediakan query berorientasi objek sehingga kita hanya akan fokus pada model objek dan tidak perlu khawatir dengan struktur database atau semantik SQL. ORM sendiri yang akan menerjemahkan query ke dalam sintaks yang tepat untuk database.

## SQLAlchemy

![](assets/SQLAlchemyStructure.jpg)

SQLAlchemy adalah library yang menjembatani komunikasi antara program Python dengan database. Library ini mencoba untuk menerjemahkan kelas-kelas di Python ke dalam tabel relasional dan juga mengkonversi fungsi-fungsi ke dalam perintah SQL. Dalam SQLAlchemy sendiri terdapat beberapa core yang perlu dipahami peran dan kegunaannya. Secara garis besar, SQLAlchemy dibagi menjadi 2 layer utama yaitu layer SQLAlchemy ORM dan SQLAlchemy Core. Untuk lebih jelasnya, kita akan mebahasanya satu per satu di bawah ini dengan merujuk gambar struktur SQLAlchemy di atas. Untuk dapat menggunakan SQLAlchemy, terlebih dahulu kita harus mengisntall librarynya dengan perinta seperti di bawah ini:
- Conda Installation
```
conda insttal -c sqlalchemy
```
- Pip Installation
```
pip install sqlalchemy
```


### DBAPI

Database API dibuat  untuk menentukan bagaimana modul Python yang berintegrasi dengan database menampilkan antarmukanya (user Interface). Kita akan melihat bagaimana fungsi-fungsi seperti `connect`, `commit`, `close` dan fungsi umum lainnya akan dijalankan ketika eksekusi (karena kita tidak akan berinteraksi secara langsung dengan API). Akibatnya, setiap kali kita menggunakan modul Python, kita akan sering menemukan fungsi-fungsi ini dan memastikan bahwa mereka akan berperilaku seperti yang diharapkan.

Pada pembahasan di artikel ini, kita akan menggunakan modul sqlite3 sebagai API. Modul ini menyediakan anatarmuka SQL yang sesuai dengan spesifikasi DBAPI 2.0  yand dideskripsikan oleh PEP 249.Pastikan di environment Anda terdapat modul dengan nama `sqlite3`. Modul ini biasanya secara otomatis akan terinstal ketika Anda membuat environment pertama kali. 

### SQLAlchemy Engine

Setiap kali kita menggunakan SQLAlchemy untuk berinteraksi dengan database, kita perlu membuat sebuah Engine. Engine ini secara khusus digunakan untuk mengelola 2 bagian, yaitu Pool dan Dialect. Intinya bagian ini digunakan SQLAlchemy untuk berinteraksi dengan fungsi pada DBAPI. 

Untuk dapat membuat Engine dan mulai berinteraksi dengan basis data, kita harus mengimpor fungsi `create_engine` dari library `sqlalchemy` dengan perintah seperti contoh di bawah ini:

```
import sqlalchemy as db
engine = db.create_engine('sqlite:///chinook.sqlite')
```
Kode di atas menjelaskan pembuatan sebuah sqlite engine untuk berkomunikasi dengan sebuah instance yang dijalankan secara lokal. Selain SQLite, SQLAlchemy juga mendukung RDBMS lainnya seperti PostgreSQL, MySQL, Oracle, dll. Jika Anda tertarik untuk membuat engine lain, Anda dapat melihat dokumentasi officialnya [disini](https://docs.sqlalchemy.org/en/11/core/engines.html)


### Connection Pooling
Connection Pool adalah implementasi dari `object pool pattern`. Object pool digunakan sebagai chace dari objek yang telah diinisialisasi dan siap digunakan. Program hanya akan mengambil objek dari sekumpulan objek yang ada dan menggunakannnya sesuai dengan kebutuhan kemudian mengembalikannya ketika sudah selesai. Artinya cara ini sebenarnya dilakukan untuk alasan penghematan karena dengan memanfaatkan pattern ini seperti yang kita tahu bahwa koneksi baru ke database akan menghabiskan waktu, sumber daya, dan biaya yang cukup mahal. Connection Pool juga menyediakan manajemen untuk jumlah total koneksi aplikasi yang mungkin digunakan secara bersamaan. Dalam kasus SQLite, SingletonThreadPool atau NullPool dipilih oleh Dialect untuk memberikan kompatibilitas yang lebih besar terhadap threading SQL dan penguncian modelnya, serta untuk memberikan perilaku default bahwa seluruh dataset dalam lingkup satu koneksi. Connection pooling ini dapat Anda atur pada fungsi `create_engine` dengan menambahkan parameter `pool_size`, `max_overflow`, `pool_recycle`, dan `pool_timeout`. Jika Anda tertarik untuk melakukan tuning pada connection pool, Anda dapat melihat dokumentasi officialnya [disini](https://docs.sqlalchemy.org/en/11/core/pooling.html#sqlalchemy.pool.QueuePool)

### SQLAlchemy Dialect
SQLALchemy mampu membuat Python untuk berkomunikasi dengan lebih dari satu database tetapi bisa menggunakan API yang sama. Hal ini membutuhkan satu bagian yang bernama Dialect. Umumnya database relational menggunakan standart dari SQL, namun memiliki `flavour` yang sedikit berbeda. Misalnya jika kita ingin mengambil 50 baris pada table `artists`, ketika kita menggunakan engine dari MySQL maka SQLALchemy untuk mengeksekusinya memerlukan perintah:
```
SELECT * FROM artists LIMIT 10;
```
Berbeda jika engine yang digunakan adalah Firebird, maka SQLAlchemy akan mengeksekusinya dengan perintah:
```
select first 10 id, name from artists
```
Karena engine yang sangat beragam, maka SQLAlchemy perlu mengetahui jenis database yang dihadapinya untuk memastikan dengan tepat permintaan apa yang akan dikeluarkan. Disinilah peran Dialect untuk membuat SQLAlchemy tahu dia akan berkomunikasi dengan database yang mana.

## SQLAlchemy ORM

Seperti yang telah kita bahas sebelumnya, ORM akan memetakan objek dengan database. Mapper disini memiliki tanggung jawab untuk perpindahan data antar objek dan database akan membuat mereka untuk saling independent satu dengan yang lainnya. Oleh karena itu, perlu pengkodean khusus untuk menerjemahkan skema satu dengan yang lainnya mengingat pendekatan kita yang sekarang berorientasi objek. Misal pada database chinook, kita punya tabel `artists` dan tabel `albums` dimana mereka memiliki relasi seperti seorang artis bisa jadi memiliki satu atau beberapa album. Relasi seperti ini setidaknya membutuhkan beberapa komponen yaitu tabel artis itu sendiri, kemudian tabel album, dan satu kunci atau yang serding disebut sebagai foreign key untuk membuka jalan atau mengaitkan hubungan di antara kedua tabel tersebut. Disinilah peran SQLAlchemy ORM untuk menerjemahkan tabel-tabel yang akan dipetakan dalam bentuk kelas-kelas menggunakan bahasa pemrograman Python dan mengatur perpindahan, penambahan, dan perubahan setiap kelas dari dan ke tabel database.

### SLQAlchemy Data Types

SQLAlchemy juga menyediakan beberapa tipe data yang umumnya kita temukan pada database relational seperti numeric, string, dates, times, boolean, dll. Selain menyediakan abstraksi dari tipe data pada umumnya tersebut, SQLAlchemy juga menyediakan mekanisme untuk menspesifikasi tipe data yang dapat kita custom sendiri. Untuk memahami tipe data pada SQLAlchemy, silahkan perhatikan contoh berikut:

```
class Artist(Base):
    __tablename__ = 'artists'
    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String)
    Album = relationship("Album")
```

Pada contoh di atas, kita memiliki kelas dengan nama`Artist` yang memiliki 4 properti yaitu:
- `__tablename__` : baris ini mengintruksikan SQLAlchemy untuk memetakan tabel `artists` ke kelas Artist.
- `ArtistId` : primary key dari kelas Artist dan tipe datanya dalah Integer
- `Name` : bagian ini menunjukkan bahwa kolom Name memiliki nama yang sama seperti pada tabel relationalnya dan bertipe data String
- `Album` : bagian ini menunjukkan bahwa kelas Artist memiliki hubungan atau relasi dengan kelas Album.

### SQLAlchemy Relationship Types

Relasi adalah hubungan antara tabel yang mempresentasikan hubungan antar objek di dunia nyata. Relasi merupakan hubungan yang terjadi pada suatu tabel dengan lainnya yang mempresentasikan hubungan antar objek di dunia nyata dan berfungsi untuk mengatur mengatur operasi suatu database.
Pada pembahasan sebelumnya, kita telah mengulas tipe data pada SQLAlchemy. Di bagian akhir pada contoh yang ada terdapat satu properti berupa `relationship` yang menandakan adanya hubungan antara kelas Artist dengan kelas Album. Sama halnya dengan database relational, SQLAlchemy juga mendukung beberapa tipe-tipe relationship antar kelasnya. Jenis relasi yang didukung oleh SQLAlchemy adalah `One To Many`, `Many To One`, `One To One`, dan `Many To Many`. Untuk lebih jelasnya, silahkan perhatikan penjelasan di bawah ini.

#### One to Many

One To Many digunakan untuk menandai bahwa instance kelas dapat berhubungan dengan banyak instance dari kelas lain. Misalnya, objek pada kelas Artist dapat memiliki relasi dengan banyak objek yanga ada di kelas Album. Dalam hal ini, SQLAlchemy akan memetakan kelas yang disebutkan dan hubungannya sebagai berikut:

```
class Artist(Base):
    __tablename__ = 'artists'
    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String)
    Album = relationship("Album")

class Album(Base):
    __tablename__ = 'albums'
    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String)
    ArtistId = Column(Integer, ForeignKey('artists.ArtistId'))
    Artist = relationship("Artist")
```

#### Many to One 

Tipe relasi yang kedua adalah Many to One. Tipe ini sebenarnya sama dengan tipe One to Many tetapi hubungannya dijelaskan dari prespektif lain. Misalnya pada database chinook kita tahu bahwa beberapa objek pada kelas Customer dapat di tangani oleh seorang Employee. Pada kasus ini, SQLAlchemy akan memetakan kelas yang disebutkan dan hubungannya sebagai berikut: 

```
class Customer(Base):
    __tablename__ = 'customers'
    CustomerId = Column(Integer, primary_key=True)
    SupportRepId = Column(Integer, ForeignKey('employees.EmployeeId'))
    FirstName = Column(String)
    LastName = Column(String)   
    Company = Column(String)
    Address = Column(String)
    City = Column(String)
    State = Column(String)
    Country = Column(String)
    PostalCode = Column(String)
    Phone = Column(String)
    Fax = Column(String)
    Email = Column(String)
    SupportRep = relationship(Employee,backref=backref('employees',uselist=True,cascade='delete,all'))

class Employee(Base):
    __tablename__ = 'employees'
    EmployeeId = Column(Integer, primary_key=True)
    ReportsTo = Column(Integer, ForeignKey('employees.EmployeeId'))
    FirstName = Column(String)
    LastName = Column(String)
    Title = Column(String)
    BirthDate = Column(DateTime)
    HireDate = Column(DateTime)
    Address = Column(String)
```

### One to One
Tipe ketiga yaitu One To One, mengacu pada hubungan di mana instance dari kelas tertentu hanya dapat dikaitkan dengan satu instance dari kelas lain, dan sebaliknya. Berhubung pada database chinook tidak ada kelas yang memiliki hubungan One to One, Anda dapat memahaminya dengan kasus lain yang ada pada dokumentasi official SQLAlchemy berikut.
```
class Parent(Base):
    __tablename__ = 'parent'
    id = Column(Integer, primary_key=True)
    child = relationship("Child", uselist=False, back_populates="parent")

class Child(Base):
    __tablename__ = 'child'
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey('parent.id'))
    parent = relationship("Parent", back_populates="child")
```
Pada contoh di atas terdapat parameter baru yang belum kita bahas sebelumnya. Parameter `uselist = False` menginstruksikan SQLAlchemy bahwa `parent` hanya akan menyimpan satu instance dan bukan array (beberapa) instance. Yang kedua parameter `back_populates` menginstruksikan SQLAlchemy untuk mengisi sisi lain dari pemetaan. 

#### Many to Many

Tipe terakhir yang didukung oleh SQLAlchemy adalah Many To Many. Tipe ini digunakan ketika instance dari kelas tertentu dapat memiliki nol atau lebih asosiasi untuk instance dari kelas lain. Sebagai contoh, katakanlah kita memetakan hubungan instance Track dan instance Playlist. Karena banyak lagu/track dapat ada dalam satu atau beberapa daftar playlist, maka kita akan memetakan relasinya sebagai berikut:

```
track_playlist_association = Table('playlist_track', Base.metadata, 
    Column('TrackId', Integer, ForeignKey('tracks.TrackId')),
    Column('PlaylistId', Integer, ForeignKey('playlists.PlaylistId'))
)

class Track(Base):
    __tablename__ = 'tracks'
    TrackId = Column(Integer, primary_key=True)
    AlbumId = Column(Integer, ForeignKey('albums.AlbumId'))
    GenreId = Column(Integer, ForeignKey('genres.GenreId'))
    MediaTypeId = Column(Integer, ForeignKey('media_types.MediaTypeId'))
    Name = Column(String)
    Composer = Column(String)
    Miliseconds = Column(Integer)
    Bytes = Column(Integer)
    UnitPrice = Column(Integer)

    album = relationship(Album,backref=backref('albums',uselist=True,cascade='delete,all'))
    mediatype = relationship(MediaType,backref=backref('media_type',uselist=True,cascade='delete,all'))
    genre = relationship(Genre,backref=backref('genres',uselist=True,cascade='delete,all'))
    playlist = relationship("Playlist",secondary=track_playlist_association)

class Playlist(Base):
    __tablename__ = 'playlists'
    PlaylistId = Column(Integer, primary_key=True)
    Name = Column(String)
```

Dari contoh di atas kita membuat sebuah tabel baru yang membantu kita untuk tetap menghubungkan antara tabel `tracks` dan tabel `playlist` atau hal ini lebih dikenal sebagai tabel asosiasi. Agar SQLAlchemy dapat mengenali tabel asosiasi, kita harus menambahkan parameter `secondary` pada fungsi `relationship`. 

Jika Anda telah sampai pada bagian ini, berarti Anda telah belajar banyak hal terkait ORM dan SQLAlchemy termasuk tipe data dan tipe-tipe relasi yang didukung penuh oleh SQLAlchemy. Pembahasan selanjutnya akan lebih mengarahkan Anda untuk mempraktekkan penggunaan SQLAlchemy termasuk bagimana kita akan mengatur session dan melakukan query.

### SQLAlchemy Sessions
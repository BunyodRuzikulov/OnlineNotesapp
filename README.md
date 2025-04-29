Yozuvlar Ilovasi
Yozuvlar Ilovasi — bu foydalanuvchilarga yozuvlarini osongina yaratish, tahrirlash, kategoriyalarga ajratish, arxivlash va ulashish imkonini beruvchi veb-ilova. Ushbu loyiha Django framework’i asosida ishlab chiqilgan bo‘lib, PostgreSQL ma’lumotlar bazasi va zamonaviy frontend texnologiyalaridan foydalanadi. Ilova shaxsiy va professional foydalanish uchun qulay interfeys va keng funksionallikni taqdim etadi.
Loyiha Haqida
Ushbu ilova yozuvlarni samarali boshqarish uchun ishlab chiqilgan bo‘lib, quyidagi asosiy xususiyatlarga ega:

Yozuvlarni boshqarish: Yozuvlarni yaratish, tahrirlash, o‘chirish va arxivlash.
Kategoriyalar va teglar: Yozuvlarni papkalar va teglar orqali tartibga solish.
Fayl yuklash: Yozuvlarga rasm va boshqa fayllarni biriktirish.
Ulashish: Yozuvlarni umumiy yoki shaxsiy rejimda ulashish.
Qidiruv va filtrlar: Yozuvlarni sarlavha, teg yoki sana bo‘yicha qidirish.
Foydalanuvchi profili: Profil ma’lumotlarini tahrirlash va sozlamalarni moslashtirish.
Admin paneli: Foydalanuvchilar, yozuvlar va kategoriyalarni boshqarish.

Ishlatilgan Texnologiyalar

Backend: Django 4.x, Python 3.8+
Ma’lumotlar bazasi: PostgreSQL
Frontend: HTML, Tailwind CSS, Font Awesome, JavaScript
Qo‘shimcha kutubxonalar:
django-crispy-forms — formalar uchun Bootstrap4 integratsiyasi
psycopg2-binary — PostgreSQL bilan ulanish uchun


Fayl boshqaruvi: Django’ning o‘rnatilgan media fayl tizimi

O‘rnatish va Ishga Tushirish
Loyihani mahalliy kompyuteringizda ishga tushirish uchun quyidagi qadamlarni bajaring:

Repozitoriyani klonlash:
git clone https://github.com/sizning-username/yozuvlar-ilovasi.git
cd yozuvlar-ilovasi


Virtual muhitni yaratish va faollashtirish:
python -m venv venv
source venv/bin/activate  # Windows uchun: venv\Scripts\activate


Kerakli kutubxonalarni o‘rnatish:
pip install -r requirements.txt


PostgreSQL ma’lumotlar bazasini sozlash:

PostgreSQL’da yangi ma’lumotlar bazasi yarating:psql -U postgres
CREATE DATABASE yozuvlar_db;
\q


yozuvlar/settings.py faylida ma’lumotlar bazasi sozlamalarini yangilang:DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'yozuvlar_db',
        'USER': 'postgres',
        'PASSWORD': 'sizning-parolingiz',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}




Migratsiyalarni qo‘llash:
python manage.py makemigrations
python manage.py migrate


Superfoydalanuvchi yaratish:
python manage.py createsuperuser


Serverni ishga tushirish:
python manage.py runserver

Brauzerda http://127.0.0.1:8000/ manziliga o‘ting.


Loyiha Tuzilishi
yozuvlar-ilovasi/
├── yozuvlar/                # Django loyiha papkasi
│   ├── settings.py          # Loyiha sozlamalari
│   ├── urls.py              # URL yo‘nalishlari
├── notes/                   # Asosiy ilova papkasi
│   ├── migrations/          # Ma’lumotlar bazasi migratsiyalari
│   ├── templates/notes/     # HTML shablonlar
│   ├── models.py            # Ma’lumotlar bazasi modellari
│   ├── views.py             # Sahifa logikasi
│   ├── forms.py             # Formalar
│   ├── admin.py             # Admin paneli sozlamalari
├── static/                  # CSS, JS va boshqa statik fayllar
├── media/                   # Yuklangan fayllar
├── requirements.txt         # Kerakli kutubxonalar ro‘yxati
├── README.md                # Ushbu fayl

Foydalanish

Bosh sahifa: Ilova haqida umumiy ma’lumot va ro‘yxatdan o‘tish/kirish havolalari.
Ro‘yxatdan o‘tish va kirish: Foydalanuvchilar email va parol orqali hisob yaratishi yoki tizimga kirishi mumkin.
Asosiy panel: Yozuvlar ro‘yxati, qidiruv va yangi yozuv yaratish tugmasi.
Kategoriyalar: Yozuvlarni papkalarga ajratish va boshqarish.
Arxiv: Arxivlangan va o‘chirilgan yozuvlarni ko‘rish va tiklash.
Qidiruv: Yozuvlarni sarlavha, teg yoki sana bo‘yicha filtrlab qidirish.
Profil: Foydalanuvchi ma’lumotlarini tahrirlash.
Sozlamalar: Til, qorong‘i rejim va xavfsizlik sozlamalarini o‘zgartirish.
![image](https://github.com/user-attachments/assets/a46fb9d2-d82c-46db-a92d-bb88864c2ab5)

Hissasi
Loyihaga hissa qo‘shmoqchi bo‘lsangiz:

Repozitoriyani fork qiling.
O‘zgarishlaringizni yangi branch’da amalga oshiring (git checkout -b feature/yangi-funksiya).
O‘zgarishlarni commit qiling (git commit -m "Yangi funksiya qo‘shildi").
Branch’ni push qiling (git push origin feature/yangi-funksiya).
Pull Request oching.


Aloqa
Savollar yoki takliflar uchun:

Email: 
Telegram:(https://t.me/Bunyod_Ruziqulov)


# 🖋️ MusePad — Django Blog Platformasi

🎯 **MusePad** — bu zamonaviy, minimalist blog platformasi bo‘lib, foydalanuvchilarga maqola yozish, o‘chirish, tahrirlash va qidirish imkonini beradi.  
Django asosida yaratilgan, Bootstrap dizayn, SCSS bilan responsive frontend va testlar bilan mustahkam backend asosida ishlab chiqilgan.

![MusePad Preview](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOTgxZGI0bW9rdWx4Y3psODN5Y3k1Ym9ycnN2aHl0dWoxN3BuOHN1bCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/JYsWjlQzsn2xeJjlGL/giphy.gif)

---

## 🚀 Funktsiyalar

- ✍️ Post yaratish, o‘chirish, tahrirlash (admin orqali)
- 🔎 Qidiruv (search by title/body)
- 🗂️ Barcha postlar ro‘yxati (pagination bilan)
- 📄 Har bir post uchun to‘liq sahifa (detail)
- ℹ️ About sahifasi
- 📬 Kontakt formasi (xabar yuborish)
- 📸 Rasm yuklash (media orqali)

---

## 🧭 Sahifalar (Pages)

| Sahifa            | Tavsifi                                          |
|-------------------|--------------------------------------------------|
| 🔎 `/search/`      | Qidiruv — post sarlavha yoki matnga qarab       |
| 📄 `/posts/<slug>` | Post detali sahifasi                             |
| 🗂️ `/` yoki `/posts/` | Barcha postlar ro‘yxati (homepage)         |
| ℹ️ `/about/`       | Loyihani taqdim etuvchi sahifa                  |
| 📬 `/contact/`     | Foydalanuvchi xabarini yuborish formasi         |

---

## 🛠️ Texnologiyalar

| Kategoriya   | Tex Stack                    |
|--------------|-------------------------------|
| 🌐 Backend   | Python, Django                |
| 🎨 Frontend  | HTML5, CSS3, Bootstrap5, SCSS |
| 🧾 Ma'lumotlar | SQLite3 (dev), Media files     |
| 🧪 Test      | `pytest`, `pytest-django`     |
| ⚙️ Tools     | Git, GitHub, Vercel-ready     |

---

## 🎬 GIF Preview

### 🏠 Home + Pagination
![Home Page](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOXZ1bTJ3N2poaGhzNmc0Z2I2aHdkOXRqMHluZnhuaTJmdmlrMXF3YSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/buMa3dtuay7HRZrDMz/giphy.gif)

### 🔍 Post Search
![Search](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZjZ2N2FvM2tqbWhidTdqM3dhcHV5ZWs0aWgyMmlhMnF2eDRwbmx0cCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/XZro45coHiKMvV1IQI/giphy.gif)

### 📄 Post Detail
![Detail](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExemN4amF4Z3BtNGFnNGE0YWg1eGVzdGxlbTY2dGpudGV2ZWYxZGV1eiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/3mPSZJHD59h5EC0uzk/giphy.gif)

---

## 📁 Loyihaning Strukturasi

```bash
.
├── app/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── admin.py
│   └── tests/
├── core/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── templates/
│   ├── home.html, about.html, contact.html, post_detail.html
├── static/
│   ├── css/, js/, img/, scss/
├── media/
│   └── uploads for posts/trends
├── manage.py
├── requirements.txt
└── pytest.ini
⚙️ O‘rnatish (Local Development)
bash
Copy
Edit
git clone https://github.com/USERNAME/musepad.git
cd musepad
python -m venv env
source env/bin/activate  # Windows: env\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
📎 Kirish: http://127.0.0.1:8000/

🧪 Testlarni ishga tushurish
bash
Copy
Edit
pytest
✅ tests/ papkasi: test_models.py, test_views.py, test_forms.py — pytest-django bilan test qilingan

💡 Roadmap (Kelajak Rejalari)
🔐 Login / Register sahifalari

💬 Comment System

🖼️ Image Preview va Compression

🌐 I18n (Ko‘p til qo‘llab-quvvatlash)

📊 Post statistikasi

👨‍💻 Muallif
Ramazon — 15 yoshli Full-Stack Developer 👨‍💻
🔗 GitHub: @ramazon07-cmd
📨 Telegram: @your_username

📜 Litsenziya
MIT License © 2025 Ramazon


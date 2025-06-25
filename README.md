# 🖋️ MusePad — Django Blog Platformasi

🎯 **MusePad** — bu zamonaviy, minimalist blog platformasi bo‘lib, foydalanuvchilarga maqola yozish, o‘chirish, tahrirlash va qidirish imkonini beradi.  
Django asosida yaratilgan, Bootstrap dizayn, SCSS bilan responsive frontend va testlar bilan mustahkam backend asosida ishlab chiqilgan.

---

## 🚀 Funktsiyalar

- ✍️ Post yaratish, o‘chirish, tahrirlash (admin orqali)
- 🔎 Qidiruv (search by title/body)
- 🗂️ Barcha postlar ro‘yxati (pagination bilan)
- 📄 Har bir post uchun to‘liq sahifa (detail)
- ℹ️ About sahifasi
- 📬 Kontakt formasi (xabar yuborish)

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

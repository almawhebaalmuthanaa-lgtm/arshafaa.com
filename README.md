# 📚 نظام الأرشفة الرسمية | Official Archive System

تطبيق ويب متكامل لإدارة ومشاركة الوثائق الرسمية والمحادثات الداخلية بكفاءة عالية.

## ✨ المميزات الرئيسية

- 📄 **إدارة الوثائق:** رفع وتنظيم وبحث الوثائق الرسمية
- 💬 **غرف محادثة:** تواصل آمن بين الأقسام المختلفة
- 🔐 **نظام أمان:** مصادقة قوية وصلاحيات محددة
- 📊 **سجل النشاط:** تتبع كامل لجميع العمليات
- 🌐 **واجهة عربية:** دعم كامل للغة العربية

## 🛠️ التكنولوجيا المستخدمة

- **Backend:** Python Flask
- **Database:** SQLite
- **Frontend:** Bootstrap 5 (RTL)
- **Authentication:** Flask-Login
- **Server:** Gunicorn

## 📋 المتطلبات

```bash
Python 3.8+
```

## 🚀 التثبيت المحلي

```bash
# 1. استنساخ المستودع
git clone https://github.com/almawhebaalmuthanaa-lgtm/arshafaa.com.git
cd arshafaa.com

# 2. إنشاء بيئة افتراضية
python -m venv venv

# 3. تفعيل البيئة الافتراضية
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# 4. تثبيت المتطلبات
pip install -r requirements.txt

# 5. تشغيل التطبيق
python app.py
```

ثم ادخل على `http://localhost:5000`

## 🔑 بيانات الدخول التجريبية

| الحقل | القيمة |
|------|--------|
| اسم المستخدم | `admin` |
| كلمة المرور | `admin123` |

**ملاحظة:** غيّر هذه البيانات قبل النشر على الإنتاج!

## 🌍 نشر على الويب

### ✅ على Render.com (الموصى به)

1. ادخل إلى [render.com](https://render.com)
2. اضغط **New +** → **Web Service**
3. اربط مستودع GitHub الخاص بك
4. اختر الإعدادات:
   - **Runtime:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
5. اضغط **Create Web Service**

### ✅ على Railway.app

1. ادخل إلى [railway.app](https://railway.app)
2. اضغط **Create New Project** → **Deploy from GitHub**
3. حدد المستودع، وRailway سيكتشف كل شيء تلقائياً
4. اضغط **Deploy**

### ✅ على PythonAnywhere

1. ادخل إلى [pythonanywhere.com](https://www.pythonanywhere.com)
2. أنشئ حساباً مجانياً
3. ارفع الملفات أو استخدم Git
4. أنشئ تطبيق WSGI وأشر إلى `app:app`

## 🔧 متغيرات البيئة

أنشئ ملف `.env` في الجذر:

```env
FLASK_ENV=production
FLASK_DEBUG=False
SECRET_KEY=your-very-secure-secret-key-here
DATABASE_URL=sqlite:///archive_system.db
```

## 📁 هيكل المشروع

```
arshafaa.com/
├── app.py                 # التطبيق الرئيسي
├── index.html            # الصفحة الرئيسية
├── requirements.txt      # المتطلبات
├── Procfile             # إعدادات النشر
├── .env.example         # مثال على المتغيرات
├── .gitignore          # ملفات يتم تجاهلها
└── uploads/            # مجلد الملفات المرفوعة
```

## 👥 المستخدمون

يتم إنشاء 3 مستخدمين تجريبيين تلقائياً:

1. **Admin** - دخول كامل (الإدارة العامة)
2. **Sales User** - مسؤول قسم المبيعات
3. **HR User** - مستخدم عادي في الموارد البشرية

## 📝 الميزات المتقدمة

- ✅ صلاحيات محددة (Admin, Manager, User)
- ✅ بحث متقدم عن الوثائق
- ✅ تصنيف الوثائق بالكلمات المفتاحية
- ✅ غرف محادثة خاصة وعامة
- ✅ سجل كامل للأنشطة

## 🔒 الأمان

- ✅ كلمات مرور مشفرة بـ Werkzeug
- ✅ Session Management آمن
- ✅ CSRF Protection
- ✅ صلاحيات محددة للمحتوى

## 📞 الدعم

في حالة وجود أسئلة أو مشاكل، تفضل بالتواصل.

## 📄 الترخيص

هذا المشروع مفتوح المصدر ومتاح للاستخدام التعليمي.

---

**تم التطوير بواسطة:** almawhebaalmuthanaa-lgtm

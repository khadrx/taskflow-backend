# TaskFlow – نظام إدارة مهام Full-Stack

TaskFlow هو مشروع بورتفوليو شخصي كامل (MVP) لإدارة المهام اليومية، مبني بتقنيات حديثة ونظيفة جدًا.  
الهدف: بناء نظام قوي، سريع، ومنظم يدعم الـRTL العربي، dark/light mode، وجاهز للعمل remote.

### Live Demo
- **Frontend (Next.js)**: https://taskflow-portfolio.vercel.app
- **Backend API (FastAPI)**: https://taskflow-backend-production-ea5d.up.railway.app/docs
- **Swagger Docs**: https://taskflow-backend-production-ea5d.up.railway.app/docs

### التقنيات المستخدمة
**Frontend (Next.js 15 – App Router)**
- TypeScript
- Tailwind CSS + shadcn/ui
- Zustand (state management)
- Sonner (toasts)
- Recharts (pie chart & stats)
- Date-fns + Arabic locale
- RTL support + dark/light mode

**Backend (FastAPI)**
- Python 3.11+
- SQLAlchemy + Alembic (migrations)
- PostgreSQL
- JWT Authentication (PyJWT + passlib)
- Pydantic v2
- Uvicorn

**DevOps**
- Vercel (frontend deployment)
- Railway (backend + PostgreSQL)
- GitHub Actions (CI/CD – optional)

### Features الرئيسية
- تسجيل / تسجيل دخول بإيميل وباسورد
- حماية كاملة للـroutes بـJWT
- CRUD كامل للمهام (مرتبطة بكل يوزر – owner_id)
- لوحة تحكم (dashboard) مع:
  - إحصائيات فورية (عدد المهام، نسبة الإنجاز)
  - رسم بياني دائري (Pie Chart)
  - فلتر حسب الحالة (todo / in_progress / done)
  - إضافة/تعديل/حذف مع تأكيد وحذف
  - RTL عربي ممتاز + dark/light mode
- Toasts (نجاح/خطأ) مع Sonner
- تحميل حالة (loading spinner)
- دعم dark/light mode تلقائي

### كيفية التشغيل محليًا

**Backend**
1. `cd taskflow-backend`
2. `python -m venv .venv`
3. `source .venv/bin/activate` (أو `.venv\Scripts\activate` على ويندوز)
4. `pip install -r requirements.txt`
5. أنشئ `.env` وأضف:
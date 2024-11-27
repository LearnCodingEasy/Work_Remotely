# 📄 ملف [ work_remotely/work_remotely_django/website/urls.py ]

# 🌐 استيراد الدالة `path` من مكتبة `django.urls` لتحديد الروابط
from django.urls import path

# 🌍 استيراد واجهات برمجة التطبيقات (API) الخاصة بنا
from . import api

urlpatterns = [
    # 🔗 رابط لعرض قائمة المواقع
    # 🌐 المسار لعرض المواقع
    path("website_list/", api.website_list, name="website_list"),
    path("website_create/", api.website_create, name="website_create"),
]

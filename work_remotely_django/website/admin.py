# 🛠️ استيراد أدوات إدارة Django
from django.contrib import admin

# 🌐 استيراد نموذج (Model) موقع الويب
from .models import Website

# 🖥️ تسجيل نموذج Website في لوحة الإدارة
admin.site.register(Website)

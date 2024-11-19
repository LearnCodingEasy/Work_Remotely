"""
URL configuration for work_remotely_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # 🔗 Include URLs from the 'account' app for API endpoints
    # 🔗 تضمين روابط تطبيق 'account' للنقاط البرمجية
    path("api/", include("account.urls")),
    # 🔧 Admin panel for site management
    # 🔧 لوحة تحكم الإدارة لإدارة الموقع
    path("admin/", admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# 🖼️ Serve media files during development
# 🖼️ عرض ملفات الوسائط أثناء التطوير

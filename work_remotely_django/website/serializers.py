#  📝 Page [ work_remotely/work_remotely_django/website/serializers.py ]

# 🛠️ استيراد إطار Django REST Framework لتحويل البيانات
from rest_framework import serializers

# استيراد نموذج البيانات المراد تحويلة
from .models import Website


# 🧩 سيريالايزر لتحويل بيانات موقع الويب
class WebsiteListSerializer(serializers.ModelSerializer):

    class Meta:
        # 🔗 ربط السيريالايزر بنموذج البيانات
        model = Website
        # 🔍 تستخدم لتحديد الحقول المطلوبة في البيانات المُسترجعة أو المرسلة
        fields = (
            "id",  # 🆔 المعرف الفريد للموقع
            "created_at",  # ⏱️ تاريخ الإنشاء
            "created_at_formatted",  # ⏳ صيغة زمنية منذ الإنشاء
            "last_edit",  # 🖋️ تاريخ آخر تعديل
            "last_edit_formatted",  # ⏳ صيغة زمنية منذ آخر تعديل
            "name",  # 🌐 اسم الموقع
            "url",  # 🔗 رابط الموقع
            "details",  # 📜 تفاصيل الموقع
            "website_type",  
            "website_language",  
            "image",  # 🖼️ صورة الموقع
            "get_image",  # 🖼️ صورة الموقع
        )

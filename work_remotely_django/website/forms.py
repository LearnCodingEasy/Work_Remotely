# 📄 ملف [ work_remotely/work_remotely_django/account/forms.py ]
from django import forms
from .models import Website


class WebsiteForm(forms.ModelForm):
    class Meta:
        model = Website
        fields = (
            # name الاسم
            "name",
            # url
            "url",
            # details
            "details",
            #
            "website_type",
            #
            "website_language",
            # 🖼️ picture صورة
            "image",
        )

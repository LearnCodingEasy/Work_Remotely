# 📄 ملف [ work_remotely/work_remotely_django/account/forms.py ]

from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User


# 📝 نموذج التسجيل
class SignupForm(UserCreationForm):
    # 🔧 إعدادات النموذج: تحديد الحقول المطلوبة
    class Meta:
        model = User
        fields = (
            # 🧑 الاسم الأول
            "name",
            # 🧑 اللقب
            "surname",
            # 📧 البريد الإلكتروني
            "email",
            # 📅 تاريخ الميلاد
            "date_of_birth",
            # ⚧ الجنس
            "gender",
            # 🔑 كلمة المرور
            "password1",
            # 🔑 تأكيد كلمة المرور
            "password2",
        )


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            # 🧑 User's name الاسم الأول
            "name",
            # 🧑 اللقب
            "surname",
            # 📧 User's email البريد الإلكتروني
            "email",
            # 📅 تاريخ الميلاد
            "date_of_birth",
            # ⚧ الجنس
            "gender",
            # 🖼️ User's profile picture صورة ملف تعريف المستخدم
            "avatar",
            # 🖼️ User's Cover picture صورة ملف غلااف المستخدم
            "cover",
            #
            "skills",
        )

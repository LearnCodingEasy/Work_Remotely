from django.db import models
import uuid


# 🕒 استيراد أدوات إدارة الوقت
from django.utils import timezone

# 🔄 استيراد دالة حساب الفارق الزمني
from django.utils.timesince import timesince

# settings: لاستيراد إعدادات
# Django الخاصة بالمشروع.
from django.conf import settings


# Create your models here.
class Website(models.Model):

    # ___________________
    # حقل يتم تعبئة تلقائي
    # ___________________
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(
        default=timezone.now,
    )
    last_edit = models.DateTimeField(
        auto_now=True,
        blank=True,
        null=True,
    )
    # ___________________
    # حقل يتم تعبئة من المستخدام
    # ___________________
    name = models.CharField(max_length=255, blank=True, null=True, default="")
    url = models.URLField(
        max_length=255,
        blank=True,
        null=True,
        default="",
    )
    details = models.TextField(
        blank=True,
        null=True,
        default="",
    )
    image = models.ImageField(
        upload_to="images",
        blank=True,
        null=True,
    )
    # 🛠️ إعداد حالات مختلفة لحالة الدورة
    SERVICES = "services"  # 🛎️ خدمات
    TEMPLATES = "templates"  # 🖼️ قوالب جاهزة
    EMPLOYMENT = "employment"  # 💼 توظيف
    # ✅ تعريف خيارات الحالة
    TYPE_CHOICES = (
        (SERVICES, "Services"),  # 🛎️ مواقع تقديم الخدمة
        (TEMPLATES, "Templates"),  # 🖼️ مواقع بيع القوالب الجاهزة
        (EMPLOYMENT, "Employment"),  # 💼 مواقع التوظيف
    )
    # 🏷️ حقل الحالة في النموذج
    website_type = models.CharField(
        max_length=25,  # ✏️ الحد الأقصى لعدد الأحرف هو 25
        choices=TYPE_CHOICES,  # 🗂️ الخيارات المتاحة للحقل
        default=SERVICES,  # 🛎️ القيمة الافتراضية: مواقع تقديم الخدمة
    )

    # 🛠️ إعداد حالات مختلفة لحالة الدورة website Language
    ARABIC = "arabic"  # 🛎️ خدمات
    ENGLISH = "english"  # 🖼️ قوالب جاهزة
    # ✅ تعريف خيارات الحالة
    LANGUAGE_CHOICES = (
        (ARABIC, "Arabic"),  # 🛎️ مواقع تقديم الخدمة
        (ENGLISH, "English"),  # 🖼️ مواقع بيع القوالب الجاهزة
    )
    # 🏷️ حقل الحالة في النموذج
    website_language = models.CharField(
        max_length=25,  # ✏️ الحد الأقصى لعدد الأحرف هو 25
        choices=LANGUAGE_CHOICES,  # 🗂️ الخيارات المتاحة للحقل
        default=ENGLISH,  # 🛎️ القيمة الافتراضية: مواقع تقديم الخدمة
    )

    def get_image(self):
        if self.image:
            return settings.WEBSITE_URL + self.image.url
        else:
            return "https://placehold.co/300x300?text=Placeholder"

    def last_edit_formatted(self):
        return timesince(self.last_edit)

    def created_at_formatted(self):
        return timesince(self.created_at)

    def __str__(self):
        return "%s" % self.name

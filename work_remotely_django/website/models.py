from django.db import models
import uuid


# 🕒 استيراد أدوات إدارة الوقت
from django.utils import timezone

# 🔄 استيراد دالة حساب الفارق الزمني
from django.utils.timesince import timesince


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

    def last_edit_formatted(self):
        return timesince(self.last_edit)

    def created_at_formatted(self):
        return timesince(self.created_at)

    def __str__(self):
        return "%s" % self.name

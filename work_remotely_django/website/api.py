# 📄 ملف [ work_remotely/work_remotely_django/account/api.py ]


# 🛠️ استيراد ديكورات Django REST Framework لتعريف وحدات الواجهة البرمجية
from rest_framework.decorators import (
    api_view,  # 🏷️ تعريف وجهة برمجية (API View)
    authentication_classes,  # 🔐 لتحديد إعدادات المصادقة
    permission_classes,  # 🔑 لتحديد إعدادات التصاريح
)

# 🔄 استيراد JsonResponse لإرجاع استجابات بصيغة JSON
from django.http import JsonResponse


# 🌐 استيراد نموذج موقع الويب
from .models import Website

# 🔄 استيراد مسلسل لتحويل البيانات من النموذج إلى JSON
from .serializers import WebsiteListSerializer


# إستيراد النماذج المخصصة لتسجيل المستخدم وتعديل الملف الشخصي
from .forms import WebsiteForm


# 🏷️ تعريف دالة لعرض قائمة المواقع
@api_view(["GET"])  # 🛠️ تعريف هذه الدالة كواجهة برمجية تدعم طلبات GET فقط
@authentication_classes([])  # 🔓 تعطيل المصادقة (أي مستخدم يمكنه الوصول)
@permission_classes([])  # 🔓 تعطيل التصاريح (لا قيود على الوصول)
def website_list(request):
    """
    📋 هذه الدالة تقوم بجلب جميع بيانات المواقع من قاعدة البيانات
    وتحويلها إلى صيغة JSON باستخدام المسلسل المحدد.
    """
    # 🌐 جلب جميع السجلات من نموذج Website
    websites = Website.objects.all()

    # 🔄 تحويل البيانات إلى صيغة JSON باستخدام المسلسل
    serializer = WebsiteListSerializer(websites, many=True)

    # 📤 إعادة البيانات بصيغة JSON
    return JsonResponse(serializer.data, safe=False)


# 📝 واجهة برمجية لانشاء
@api_view(["POST"])
@authentication_classes([])  # 🚫 لا تتطلب مصادقة
@permission_classes([])  # 🚫 لا تتطلب أذونات
def website_create(request):
    # ملاحظة: request.FILES للصور
    form = WebsiteForm(request.POST, request.FILES)
    # ✅ Check if form is valid ✅ التحقق من صحة النموذج
    if form.is_valid():
        website = form.save(commit=False)
        website.created_by = request.user
        website.save()
        # Serialize the website and return as JSON response
        serializer = WebsiteListSerializer(website)
        return JsonResponse(serializer.data, status=201)  # HTTP 201 Created
    else:
        # ❌ If errors exist, return them ❌ إذا كان هناك أخطاء
        errors = {
            "website_errors": form.errors,
        }
        return JsonResponse({"error": errors}, status=400)


@api_view(["DELETE"])
def website_delete(request, pk):
    website = Website.objects.filter(created_by=request.user).get(pk=pk)
    user = request.user
    user.website_count = user.website_count - 1
    user.save()
    website.delete()
    return JsonResponse({"message": "website deleted"})
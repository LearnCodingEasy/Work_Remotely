# 📄 ملف [ work_remotely/work_remotely_django/account/api.py ]

# 🌐 API for User Signup and Profile Info Retrieval
# 🌐 API لتسجيل المستخدم واسترجاع معلومات الحساب

# Django إستيراد إعدادات المشروع في
from django.conf import settings

# إستيراد نموذج تغيير كلمة المرور
from django.contrib.auth.forms import PasswordChangeForm

# إستيراد دالة إرسال البريد الإلكتروني
from django.core.mail import send_mail

# JSON لإرجاع استجابات JsonResponse إستيراد
from django.http import JsonResponse

# إستيراد الديكورات لتعريف وحدات الواجهة البرمجية
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)

# إستيراد النماذج المخصصة لتسجيل المستخدم وتعديل الملف الشخصي
from .forms import SignupForm, ProfileForm

# إستيراد النماذج المخصصة للمستخدم وطلبات الصداقة
from .models import User, FriendshipRequest

# إستيراد المسلسلات للمستخدم وطلبات الصداقة
from .serializers import UserSerializer, FriendshipRequestSerializer


# 📝 Signup API Endpoint
# 📝 واجهة برمجية للتسجيل
@api_view(["POST"])
@authentication_classes([])  # 🚫 لا تتطلب مصادقة
@permission_classes([])  # 🚫 لا تتطلب أذونات
def signup(request):
    data = request.data
    message = "success"

    # 🧾 Initialize signup form with request data
    # 🧾 تهيئة نموذج التسجيل باستخدام بيانات الطلب
    form = SignupForm(
        {
            "name": data.get("name"),
            "surname": data.get("surname"),
            "email": data.get("email"),
            "date_of_birth": data.get("date_of_birth"),
            "gender": data.get("gender"),
            "password1": data.get("password1"),
            "password2": data.get("password2"),
        }
    )

    # ✅ Check if form is valid
    # ✅ التحقق من صحة النموذج
    if form.is_valid():
        # 🛠️ Save the new user
        # 🛠️ حفظ المستخدم الجديد
        user = form.save()
        # 🔓 Activate the account
        # 🔓 تأكيد الحساب مباشرة
        user.is_active = True
        user.save()

        return JsonResponse({"message": message, "email_sent": True}, safe=False)
    else:
        # ❌ If errors exist, return them
        # ❌ إذا كان هناك أخطاء
        message = form.errors.as_json()
    # 🔍 Print errors for debugging
    # 🔍 طباعة الأخطاء لأغراض التصحيح
    print(message)
    return JsonResponse({"message": message}, safe=False)


# 👤 User Info API Endpoint
# JSON إرجاع بيانات المستخدم الحالي كاستجابة
# 👤 واجهة برمجية لاسترجاع معلومات المستخدم
@api_view(["GET"])
def me(request):
    if request.user.is_authenticated:
        user_serializer = UserSerializer(request.user)
        return JsonResponse(user_serializer.data, safe=False)
    return JsonResponse({"error": "User not authenticated"}, status=401)


# Profile
@api_view(["GET"])
def profile(request, id):
    # (primary key) استرجاع معلومات المستخدم بناءً على معرفه الفريد
    user = User.objects.get(pk=id)
    # print("Profile User By Id 👉️", user)
    # (primary key)
    # تسلسل بيانات المستخدم باستخدام السيريالايزر المخصص
    user_serializer = UserSerializer(user)
    # print("Profile User By Id 👍", user_serializer)

    #
    can_send_friendship_request = True

    if request.user in user.friends.all():
        can_send_friendship_request = False

    # 🔍 Check if a request already exists between the users
    # 🔍 التحقق مما إذا كان هناك طلب صداقة موجود بالفعل بين المستخدمين
    check1 = FriendshipRequest.objects.filter(created_for=request.user).filter(
        created_by=user
    )
    check2 = FriendshipRequest.objects.filter(created_for=user).filter(
        created_by=request.user
    )
    # For Test
    # print("How Is User check1", check1)
    # print("_______________________________________")
    # print("How Is User check2", check2)
    # print("_______________________________________")

    if check1 or check2:
        can_send_friendship_request = False

    # JSON إرجاع البيانات كاستجابة
    return JsonResponse(
        {
            "user": user_serializer.data,
            "can_send_friendship_request": can_send_friendship_request,
        },
        safe=False,
    )


@api_view(["POST"])
def editprofile(request):
    # 👤 Get current user and new email data
    # 👤 احصل على بيانات بريد إلكتروني حالية وبيانات بريد إلكتروني جديدة
    user = request.user
    email = request.data.get("email")

    # 📧 Check if email is already in use by another user
    # 📧 تحقق مما إذا كان البريد الإلكتروني قيد الاستخدام بالفعل من قبل مستخدم آخر
    if User.objects.exclude(id=user.id).filter(email=email).exists():
        return JsonResponse({"message": "email already exists"})
    else:
        # 📝 Initialize profile form with request data and files
        # 📝 تهيئة نموذج الملف الشخصي مع بيانات الطلب والملفات
        form = ProfileForm(request.POST, request.FILES, instance=user)

        # ✅ Validate and save profile if valid
        # ✅ التحقق من صحة وحفظ الملف الشخصي إذا كان صالحًا
        if form.is_valid():
            form.save()

        # 🔄 Serialize updated user data
        # 🔄 قم بتسلسل بيانات المستخدم المحدثة
        serializer = UserSerializer(user)
        return JsonResponse({"message": "information updated", "user": serializer.data})


@api_view(["POST"])
def editpassword(request):
    # 🔒 Initialize password change form with request data
    # 🔒 تهيئة نموذج تغيير كلمة المرور مع بيانات الطلب
    user = request.user
    form = PasswordChangeForm(data=request.POST, user=user)

    # ✅ Validate and save new password if valid
    # ✅ التحقق من صحة وحفظ كلمة مرور جديدة إذا كانت صالحة
    if form.is_valid():
        form.save()
        return JsonResponse({"message": "success"})
    else:
        # ❌ Return errors if form is invalid
        # ❌ أخطاء الإرجاع إذا كان النموذج غير صالح
        return JsonResponse({"message": form.errors.as_json()}, safe=False)


# 🌐 Friendship Request and Friends Management API
# 🌐 واجهة برمجية لإدارة طلبات الصداقة وإدارة الأصدقاء
@api_view(["POST"])
def send_friendship_request(request, pk):
    # 👤 Get the user to whom the friendship request is being sent
    # 👤 جلب المستخدم الذي يتم إرسال طلب الصداقة إليه
    user = User.objects.get(pk=pk)
    # For Test
    # print("How Is User Send Friend Ship Request", pk)
    # print("_______________________________________")

    # 🔍 Check if a request already exists between the users
    # 🔍 التحقق مما إذا كان هناك طلب صداقة موجود بالفعل بين المستخدمين
    check1 = FriendshipRequest.objects.filter(created_for=request.user).filter(
        created_by=user
    )
    check2 = FriendshipRequest.objects.filter(created_for=user).filter(
        created_by=request.user
    )
    # For Test
    # print("How Is User check1", check1)
    # print("_______________________________________")
    # print("How Is User check2", check2)
    # print("_______________________________________")

    if not check1 or not check2:
        # ✉️ Create a new friendship request if it doesn't exist
        # ✉️ إنشاء طلب صداقة جديد إذا لم يكن موجودًا
        friendrequest = FriendshipRequest.objects.create(
            created_for=user, created_by=request.user
        )
        # For Test
        # print("Friend Ship Request If ", friendrequest)
        # print("_______________________________________")
        # Return = The Message Show In Frontend
        return JsonResponse({"message": "friendship request created"})
    else:
        # Return = The Message Show In Frontend
        return JsonResponse({"message": "request already sent"})


@api_view(["GET"])
def friends(request, pk):
    # 👥 Get the friends and requests for the specified user
    # 👥 جلب الأصدقاء والطلبات للمستخدم المحدد
    user = User.objects.get(pk=pk)
    # print("Friends User By Id 👉️", user)

    requests = []
    # print("Friends Requests By Id 👉️", requests)

    # 📝 Check if the current user is the requested user
    # 📝 التحقق مما إذا كان المستخدم الحالي هو نفس المستخدم المطلوب
    if user == request.user:
        requests = FriendshipRequest.objects.filter(
            created_for=request.user, status=FriendshipRequest.NOT_SENT
        )
        # print("requests Friends", requests)
        requests = FriendshipRequestSerializer(requests, many=True)
        requests = requests.data

        # print("Friends Requests By Id 👉️", requests)

    # 👫 Retrieve all friends of the user
    # 👫 جلب جميع أصدقاء المستخدم
    friends = user.friends.all()
    # print("Friends Friends 👉️", friends)

    return JsonResponse(
        {
            "user": UserSerializer(user).data,
            "friends": UserSerializer(friends, many=True).data,
            "requests": requests,
        },
        safe=False,
    )


@api_view(["GET"])
def my_friendship_suggestions(request):
    # 🤝 Suggest users the current user may know
    # 🤝 اقتراح المستخدمين الذين قد يعرفهم المستخدم الحالي
    serializer = UserSerializer(request.user.people_you_may_know.all(), many=True)
    # print("🤝 Suggest users", serializer)
    return JsonResponse(serializer.data, safe=False)


@api_view(["POST"])
def handle_request(request, pk, status):
    # 🛠️ Handle and update the status of a friendship request
    # 🛠️ معالجة وتحديث حالة طلب الصداقة
    user = User.objects.get(pk=pk)
    # friendship_request = FriendshipRequest.objects.filter(created_for=request.user).get(
    #     created_by=user
    # )
    friendship_request = FriendshipRequest.objects.filter(
        created_for=request.user, created_by=user
    ).first()
    if not friendship_request:
        return JsonResponse(
            {"error": "Friendship request not found or already handled"}, status=404
        )
    # إذا كان يوجد طلب صداقة واحد فقط
    # friendship_request = friendship_requests.first()
    # استخدام first() بدلاً من get()

    if not friendship_request:
        return JsonResponse({"error": "Friendship request not found"}, status=404)

    friendship_request.status = status
    friendship_request.save()

    # 👥 Add each user to the other's friends list if accepted
    # 👥 إضافة كل مستخدم إلى قائمة أصدقاء الآخر إذا تم قبول الطلب
    user.friends.add(request.user)
    user.friends_count += 1
    user.save()

    request_user = request.user
    request_user.friends_count += 1
    request_user.save()

    # return JsonResponse({"message": "friendship request updated"})
    return JsonResponse({"message": f"Friendship request {status} successfully"})

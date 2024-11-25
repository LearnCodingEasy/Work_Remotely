## Models => إنشاء قاعدة البيانات

### UUIDField [ id ]

<div style="font-size:1.2vw; padding: 2rem 0 0 0; font-weight: 900;">
  📝 UUIDField()
</div>

<div dir="rtl" style="font-size:1.2vw; padding: 1rem 0; font-weight: 900;">
  id مُفتاح أساسي يستخدم كمُعرّف فريد لكل نموذج ويتم إنشاؤه بشكل تلقائي باستخدام
  uuid.uuid4.
</div>

```python
import uuid

# 🧑 Custom User Form  نموذج المستخدم المخصص
class User(AbstractBaseUser, PermissionsMixin):
    # ___________________
    # حقل يتم تعبئة تلقائي
    # ___________________
    # id مُفتاح أساسي يستخدم كمُعرّف فريد لكل نموذج ويتم إنشاؤه بشكل تلقائي باستخدام
    # uuid.uuid4.
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
```

### \_\_

### CharField [ Text ]

<div style="font-size: 2vw; padding: 2rem 0 0 0; font-weight: 900;">
  📝 CharField()
</div>

<div dir="rtl" style="font-size:1.5vw; padding: 0 0 1rem 0; ">
  <br>
  🌾 حقل النص يُستخدم لتخزين النصوص
  <br>
  <br>
  [ max_length=255 ]
  <br>
  ⚙️ يمكن للخيار تحديد الحد الأقصى لعدد الأحرف في النص بحد أقصى 255 حرفًا
  <br>
  
  ___________________________________

📝 [ null=False | null=True ]
<br>
أو لا(None) يحدد الحقل ما إذا كان يمكن أن يأخذ قيمة فارغة
<br>
📌 False القيمة الافتراضية هي
<br>
💭 يعني ذلك أن الحقل لا يمكن أن يكون فارغًا
<br>
🌟 True الحقل يمكن أن يكون فارغًا
<br>
👍 بمعنى أنه لا يحتوي على أي محتوى
<br>

---

📝 [ blank=False | blank=True ]
<br>
✔️ يحدد ما إذا كان يمكن ترك الحقل فارغًا عند إنشاء نموذج.
<br>
❌ False القيمة الافتراضية هي
<br>
💭 True مما يعني أنه يجب توفير قيمة لهذا الحقل
<br>

---

[ ... | default="Name" | default=5 ]
<br>
⚙️ يحدد القيمة الافتراضية للحقل عندما لا يتم تقديم قيمة له
<br>
⚙️ في هذه الحالة، ليس هناك قيمة افتراضية محددة
<br>
📌 في هذه الحالة، القيمة الافتراضية هي "اسم المنتج"
<br>
🌟 يمكن أن يكون هناك قيمة افتراضية محددة مثل الارقام
<br>

---

[ verbose_name="Name" ]
<br>
🏷️ يحدد الاسم الذي سيظهر في واجهة المستخدم كعنوان للحقل
<br>
🤔 يساعد في فهم المستخدم لغرض الحقل
<br>

---

[ help_text="Name" ]
<br>
🔍 يوفر نص توضيحي للمستخدمين بجانب الحقل
💡 يساعد في ملء الحقل بشكل صحيح

</div>

```python
# 🧑 Custom User Form  نموذج المستخدم المخصص
class User(AbstractBaseUser, PermissionsMixin):
    # ___________________
    # حقل يتم تعبئة من المستخدام
    # ___________________
    name = models.CharField(max_length=255)
    name = models.CharField(max_length=255, null=True, blank=True, default="Name",
        verbose_name="Name", help_text="Please Enter The Your Name Here",
        choices=[ ("available", "موجود"), ("sold_out", "خلص"), ("reserved", "محجوز"),],)
```

### \_\_\_

### TextField [ Text ]

<div style="font-size:1.5vw; padding: 2rem 0 0 0; font-weight: 900;">
  📝 TextField()
</div>

<div dir="rtl" style="font-size:1.5vw; padding: 0 0 1rem 0; ">
  <br>
  🌾 حقل النص يُستخدم لتخزين النصوص الطويله
  <br>
  <br>
  ---
  [ max_length=255 ]
  <br>
  ⚙️ يمكن للخيار تحديد الحد الأقصى لعدد الأحرف في النص بحد أقصى 255 حرفًا
  <br>
  ---

📝 [ null=False | null=True ]
<br>
أو لا(None) يحدد الحقل ما إذا كان يمكن أن يأخذ قيمة فارغة
<br>
📌 False القيمة الافتراضية هي
<br>
💭 يعني ذلك أن الحقل لا يمكن أن يكون فارغًا
<br>
🌟 True الحقل يمكن أن يكون فارغًا
<br>
👍 بمعنى أنه لا يحتوي على أي محتوى
<br>

---

📝 [ blank=False | blank=True ]
<br>
✔️ يحدد ما إذا كان يمكن ترك الحقل فارغًا عند إنشاء نموذج.
<br>
❌ False القيمة الافتراضية هي
<br>
💭 True مما يعني أنه يجب توفير قيمة لهذا الحقل
<br>

---

[ ... | default="Name" | default=5 ]
<br>
⚙️ يحدد القيمة الافتراضية للحقل عندما لا يتم تقديم قيمة له
<br>
⚙️ في هذه الحالة، ليس هناك قيمة افتراضية محددة
<br>
📌 في هذه الحالة، القيمة الافتراضية هي "اسم المنتج"
<br>
🌟 يمكن أن يكون هناك قيمة افتراضية محددة مثل الارقام
<br>

---

[ verbose_name="Name" ]
<br>
🏷️ يحدد الاسم الذي سيظهر في واجهة المستخدم كعنوان للحقل
<br>
🤔 يساعد في فهم المستخدم لغرض الحقل
<br>

---

[ help_text="Name" ]
<br>
🔍 يوفر نص توضيحي للمستخدمين بجانب الحقل
💡 يساعد في ملء الحقل بشكل صحيح

</div>

```python
# 🧑 Custom User Form  نموذج المستخدم المخصص
class User(AbstractBaseUser, PermissionsMixin):
    # ___________________
    # حقل يتم تعبئة من المستخدام
    # ___________________
    long_description = models.TextField(null=True, blank=True)
    long_description = models.TextField(max_length=255, null=True, blank=True, default="Name",
        verbose_name="Name", help_text="Please Enter The Your Name Here",
        choices=[ ("available", "موجود"), ("sold_out", "خلص"), ("reserved", "محجوز"),],)
```

### \_\_

### All

```python
class User(models.Model):
    # ___________________
    # حقل يتم تعبئة تلقائي
    # ___________________
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # ___________________
    # حقل يتم تعبئة من المستخدام
    # ___________________
    name = models.CharField(max_length=255)
    long_description = models.TextField(null=True, blank=True)
```

# الخطوة 1: استخدام صورة بايثون خفيفة
FROM python:3.9-slim

# الخطوة 2: تحديد مكان العمل داخل الحاوية
WORKDIR /app

# الخطوة 3: نسخ ملف البرمجة الخاص بنا إلى الحاوية
COPY app.py .

# الخطوة 4: الأمر الذي يشغل البرنامج عند تشغيل الحاوية
CMD ["python", "app.py"]

RUN pip install mysql-connector-python

import mysql.connector
import hashlib
import time

def connect_to_db():
    # الكود تبعك اللي بعته (ممتاز جداً)
    for i in range(10): 
        try:
            conn = mysql.connector.connect(
                host="db",
                user="root",
                password="rootpassword",
                database="my_first_db"
            )
            return conn
        except:
            print(f"⏳ Waiting for database... (Attempt {i+1}/10)")
            time.sleep(5) # قللنا الوقت شوي عشان ما تمل
    return None

def setup_database():#هاي "أول مرة" بيشتغل فيها البرنامج، لازم يتأكد إنّ "الرفوف" جاهزة.
    conn = connect_to_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(50) UNIQUE NOT NULL, password_hash VARCHAR(255) NOT NULL)")#CREATE TABLE IF NOT EXISTS: هاي جملة SQL ذكية، بتقول للقاعدة: "إذا ما عندك جدول اسمه users اعملي واحد هسا، وإذا فيه خلص لا تعملي شي".
        conn.close()
        print("✅ Database Table Ready!")

# --- هاد الجزء الناقص عندك اللي بيشغل البرنامج ---
if __name__ == "__main__":
    setup_database()
    
    print("\n--- User Registration System ---")
    u = input("Enter Username: ")
    p = input("Enter Password: ")
    
    conn = connect_to_db()
    if conn:
        cursor = conn.cursor()#الـ Cursor هو بمثابة "المندوب" أو "المؤشر" اللي بياخد أوامر SQL من البايثون وبيوديها لقاعدة البيانات. بدونه، البايثون ما بيعرف يحكي مع الجداول
        password_hash = hashlib.sha256(p.encode()).hexdigest()
        try:
            cursor.execute("INSERT INTO users (username, password_hash) VALUES (%s, %s)", (u, password_hash))#INSERT INTO: أمر SQL لإضافة سطر جديد.
            conn.commit()#4. تثبيت العملية (commit)
            #في قواعد البيانات، الإدخال ما بصير "نهائي" بمجرد الإرسال. لازم تبعت أمر Commit (تأكيد)، كأنك بتضغط "Save" للملف. لو ما عملت هيك، البيانات رح تضيع بمجرد ما يسكر البرنامج.
            print(f"🎉 Success! User '{u}' registered.")
        except Exception as e:
            print(f"❌ Error: {e}")
        finally:
            conn.close()
            
            #سواء العملية نجحت أو فشلت، لازم نسكر "خط التليفون" مع القاعدة. هاد بيمنع استهلاك موارد السيرفر على الفاضي.

           
            #ملخص العملية:
#           #بنتصل بقاعدة البيانات.
           #بنعمل "مندوب" (Cursor) للتواصل مع القاعدة.
           #بنشفر الباسورد.
           #بنحاول نضيف المستخدم الجديد.
           #بنطبع رسالة نجاح أو فشل.
           #بنبعث الاسم والهاش للمندوب.
           #بناكد الحفظ (Commit).
           # بنسكر الاتصال
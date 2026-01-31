# استيراد المكتبات (مثل #include في C++)
import mysql.connector
import time

# --- تعريف دالة الاتصال ---
# في C++: MySQL* connect_db()
def connect_db():
    return mysql.connector.connect(
        host="db",           # اسم السيرفر (اسم الحاوية في دوكر)
        user="root",         # المستخدم
        password="rootpassword", 
        database="my_first_db"
    )

# --- دالة الحذف (الخيار الجديد) ---
# نمرر الـ cursor والـ connection كبارامترات
def delete_user(cursor, conn):
    # input تأخذ نصاً من المستخدم (مثل cin)
    user_id = input("Enter the ID of the user you want to delete: ")
    
    # أمر الحذف SQL
    # %s تحمي من SQL Injection (ثغرات أمنية)
    sql_query = "DELETE FROM users WHERE id = %s"
    
    # تنفيذ الأمر: نضع الـ ID داخل tuple (بين قوسين)
    cursor.execute(sql_query, (user_id,))
    
    # في القواعد، أي تعديل (Insert/Delete/Update) يحتاج تثبيت (Commit)
    conn.commit()
    print(f"🗑️ User with ID {user_id} deleted!")

# --- الدالة الرئيسية (مثل int main() ) ---
def main():
    # انتظار ثانيتين (للتأكد أن حاوية MySQL اشتغلت تماماً)
    time.sleep(2)
    
    # إنشاء كائن الاتصال والمؤشر
    conn = connect_db() #conn: هو الجسر (Connection Object).
    cursor = conn.cursor()#هو العامل الذي سيرسل الأوامر (Cursor Object).

    # إنشاء الجدول (إذا لم يكن موجوداً)
    # AUTO_INCREMENT تعني أن الـ ID يزداد تلقائياً (1, 2, 3...)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY, 
            name VARCHAR(255)
        )
    """)

    # الحلقة الرئيسية (مثل while(true) )
    while True:
        print("\n--- Python & Docker Database Manager ---")
        print("1. Add New Name")
        print("2. Show All Names")
        print("3. Delete User (By ID)")
        print("4. Exit")
        
        # قراءة خيار المستخدم
        choice = input("Select an option (1-4): ")

        if choice == '1':
            name = input("Enter name to save: ")
            # إضافة بيانات (INSERT)
            cursor.execute("INSERT INTO users (name) VALUES (%s)", (name,))
            conn.commit()
            print(f"✅ {name} added!")
            
        elif choice == '2':
            # قراءة البيانات (SELECT)
            cursor.execute("SELECT * FROM users")
            # fetchall ترجع قائمة (List) تحتوي على كل الصفوف
            results = cursor.fetchall()
            
            print("\n--- Users List ---")
            # حلقة for تمشي على النتائج (مثل for-each loop)
            for row in results:
                # row[0] هو الـ ID، و row[1] هو الاسم
                print(f"ID: {row[0]} | Name: {row[1]}")
            
        elif choice == '3':
            # استدعاء دالة الحذف التي عرفناها في الأعلى
            delete_user(cursor, conn)
            
        elif choice == '4':
            print("Goodbye!")
            break # الخروج من الـ while loop
            
        else:
            print("Invalid choice! Try again.")

    # إغلاق الاتصال (جيد لإدارة الذاكرة)
    conn.close()

# السطر التالي يخبر بايثون أن يبدأ من دالة main
# هو العرف البرمجي لبداية أي تطبيق بايثون
if __name__ == "__main__":
    main()
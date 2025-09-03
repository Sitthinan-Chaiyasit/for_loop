# ร้านขายพวงกุญแจ by phattharawadee

โปรเจกต์นี้เป็นเว็บแอปพลิเคชันร้านขายพวงกุญแจ พัฒนาด้วย Django และ Bootstrap สำหรับแสดงสินค้าและฟีเจอร์การคำนวณต่างๆ

## โครงสร้างโปรเจกต์

- `wedpang/` : Django app หลัก มี views, urls, และไฟล์ wsgi สำหรับ deploy
- `templates/` : เก็บไฟล์ HTML template เช่น `base.html`, `index.html`, `for.html`, `multiplication.html`
- `static/` : เก็บไฟล์ static เช่น CSS, JS, รูปภาพ
- `vercel.json` : สำหรับ deploy บน Vercel
- `build_files.sh` : สคริปต์สำหรับ build static files

## ฟีเจอร์หลัก

- **หน้าแรก** (`index.html`) : แสดงข้อความต้อนรับและ carousel รูปภาพสินค้า
- **เกี่ยวกับ** (`about.html`) : ข้อมูลเกี่ยวกับร้าน
- **ติดต่อ** (`contact.html`) : ช่องทางการติดต่อร้าน
- **วนซ้ำข้อมูล** (`for.html`) : รับตัวเลขจากผู้ใช้และแสดงลำดับตามจำนวนที่กรอก
- **ตารางสูตรคูณ** (`multiplication.html`) : รับตัวเลขจากผู้ใช้และแสดงตารางสูตรคูณ 1-12

## การทำงานของโค้ด

- `views.py` : กำหนดฟังก์ชัน view สำหรับแต่ละหน้า เช่น `index`, `about`, `contact`, `for_view`, `multipli`
    - `for_view` รับค่าจากฟอร์มและสร้างลิสต์ลำดับ
    - `multipli` รับค่าจากฟอร์มและสร้างตารางสูตรคูณ
- `base.html` : Template หลัก มี navbar และ block content สำหรับแสดงเนื้อหาแต่ละหน้า
- Routing ใน Django กำหนดผ่าน `urls.py` ให้แต่ละ view ตรงกับ url ที่ต้องการ

## วิธีใช้งาน

1. ติดตั้ง Django
    ```
    pip install django
    ```
2. รันเซิร์ฟเวอร์
    ```
    python [manage.py](http://_vscodecontentref_/0) runserver
    ```
3. เปิดเว็บเบราว์เซอร์ไปที่ `http://127.0.0.1:8000/`

## การ deploy บน Vercel

- ใช้ไฟล์ `vercel.json` กำหนด entry point และ static files
- สั่ง build static files ด้วย `build_files.sh`
- อัปโหลดโปรเจกต์ขึ้น Vercel

## ผู้พัฒนา

- พัฒนาโดย phattharawadee
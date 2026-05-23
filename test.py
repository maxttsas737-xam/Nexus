import os
from dotenv import load_dotenv
import google.generativeai as genai

# แก้ไขตรงนี้: สั่งให้ค้นหาและโหลดไฟล์ .env จากโฟลเดอร์ปัจจุบันที่รันอยู่
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '.env'))

# ดึงค่าคีย์มาใช้งาน
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# บรรทัดนี้จะช่วยเช็คใน Terminal ตอนรันว่าดึงคีย์สำเร็จไหม
if not GEMINI_API_KEY:
    print("❌ Error: หา GEMINI_API_KEY ในไฟล์ .env ไม่เจอครับ!")
else:
    print(f"✅ โหลด GEMINI_API_KEY สำเร็จ! (คีย์ขึ้นต้นด้วย: {GEMINI_API_KEY[:7]}...)")

# ตั้งค่าเข้าตัวไลบรารี
genai.configure(api_key=GEMINI_API_KEY)
VisionGesture AI: Advanced System Control & Telemetry
Bilingual Documentation: English | فارسی

<a name="english"></a>

🇺🇸 English Version
VisionGesture AI is a high-performance Human-Computer Interaction (HCI) desktop application designed for real-time system-level control through computer vision. By leveraging advanced hand landmark detection, it transforms physical movements into digital commands, providing a touchless interface for system tasks like volume management.

📸 App Preview
<p align="center">

</p>

✨ Key Features
🎯 Precision Tracking: Real-time tracking of 21 hand landmarks with high-frequency updates using MediaPipe.

🔊 Gesture Audio Control: Intuitively manage Windows system volume by adjusting the distance between the thumb and index finger.

📊 Live Telemetry HUD: Professional sidebar dashboard displaying Euclidean distance metrics, FPS, and volume mapping percentages.

🛡️ Smart Data Filtering: Integrated linear interpolation (Lerp) and smoothing to ensure stable, jitter-free system adjustments.

🛠️ Tech Stack
Language: Python 3.11 (Optimized for MediaPipe Stability).

CV Engine: MediaPipe, OpenCV.

OS Bridge: Pycaw (Python Computer Audio Utilities).

Mathematics: NumPy (Linear Interpolation & Mapping).

<a name="فارسی"></a>

🇮🇷 نسخه فارسی
VisionGesture AI یک اپلیکیشن دسکتاپ پیشرفته در حوزه تعامل انسان و کامپیوتر (HCI) است که برای کنترل پارامترهای سیستمی از طریق بینایی ماشین طراحی شده است. این برنامه با استفاده از تشخیص دقیق مفصل‌های دست، حرکات فیزیکی را به دستورات دیجیتالی تبدیل کرده و یک رابط کاربری بدون لمس برای مدیریت ویندوز (مانند کنترل صدا) فراهم می‌کند.

📸 پیش‌نمایش برنامه
<p align="center">

</p>

✨ قابلیت‌های کلیدی
🎯 ردیابی دقیق: شناسایی و ردیابی زنده ۲۱ نقطه کلیدی دست با فرکانس بالا با استفاده از MediaPipe.

🔊 کنترل صوتی با اشاره: مدیریت هوشمند ولوم صدای ویندوز از طریق تغییر فاصله بین انگشت شست و اشاره.

📊 داشبورد تلمتری زنده: نمایشگر حرفه‌ای HUD برای تحلیل لحظه‌ای فاصله اقلیدسی، نرخ فریم (FPS) و درصد نگاشت صدا.

🛡️ فیلتر هوشمند داده‌ها: پیاده‌سازی درون‌یابی خطی و فیلترهای نرم‌کننده برای جلوگیری از لرزش و پرش‌های ناخواسته صدا.

🛠️ تکنولوژی‌های استفاده شده
زبان برنامه نویسی: پایتون ۳.۱۱ (بهینه شده برای پایداری MediaPipe).

موتور بینایی ماشین: MediaPipe, OpenCV.

ارتباط با سیستم‌عامل: Pycaw (کنترل مستقیم لایه صوتی ویندوز).

محاسبات ریاضی: NumPy (برای محاسبات هندسی و نگاشت داده‌ها).

🚀 Setup & Installation / راهنمای نصب
Clone the repository / کلون کردن پروژه:

Bash

git clone https://github.com/yourusername/VisionGesture-AI.git
cd VisionGesture-AI
Environment Setup / آماده‌سازی محیط:

It is highly recommended to use Python 3.11 for library compatibility.

اکیداً توصیه می‌شود برای سازگاری کامل کتابخانه‌ها از پایتون ۳.۱۱ استفاده کنید.

Install Dependencies / نصب کتابخانه‌ها:

Bash

pip install opencv-python mediapipe pycaw comtypes numpy
Run the App / اجرای برنامه:

Bash

python main.py
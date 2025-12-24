# 🚀 VisionGesture AI: Advanced System Control & Telemetry
> **Bilingual Documentation: [English](#english) | [فارسی](#فارسی)**

---

<a name="english"></a>
## 🇺🇸 English Version

VisionGesture AI is a high-performance **Human-Computer Interaction (HCI)** tool designed for real-time system-level control via Computer Vision. By leveraging advanced landmark detection, it transforms physical hand gestures into digital commands, providing a touchless interface for Windows volume management.

---

## 📸 App Preview
<p align="center">
  <img src="https://socialify.git.ci/YourGitHubUsername/VisionGesture-AI/image?description=1&descriptionEditable=Advanced%20Hand%20Telemetry%20%26%20Volume%20Control&font=Inter&name=1&owner=1&pattern=Circuit%20Board&theme=Dark" width="800" alt="Project Banner">
</p>

---

### ✨ Key Features
* **🎯 Precision Tracking**: Real-time tracking of 21 hand landmarks using MediaPipe.
* **🔊 Gesture Audio Control**: Intuitively manage system volume by adjusting the distance between the thumb and index finger.
* **📊 Live Telemetry HUD**: Features a professional sidebar dashboard displaying Euclidean distance metrics, FPS, and volume mapping.
* **🛡️ Smart Data Filtering**: Uses linear interpolation and smoothing to ensure stable, jitter-free system adjustments.
* **⚡ High Performance**: Optimized for PC environments, ensuring high FPS during processing.

### 🛠️ Tech Stack
* **Language**: Python 3.11 (Highly recommended for library stability).
* **CV Engine**: MediaPipe, OpenCV.
* **OS Bridge**: Pycaw (Python Computer Audio Utilities).
* **Mathematics**: NumPy (Used for linear mapping and coordinate normalization).

---

<a name="فارسی"></a>
## 🇮🇷 نسخه فارسی

**VisionGesture AI** یک ابزار پیشرفته در حوزه **تعامل انسان و کامپیوتر (HCI)** است که برای کنترل پارامترهای سیستمی از طریق بینایی ماشین طراحی شده است. این برنامه با ردیابی دقیق نقاط کلیدی دست، حرکات فیزیکی را به دستورات دیجیتالی (مانند مدیریت صدای ویندوز) تبدیل می‌کند.

---

### ✨ قابلیت‌های کلیدی
* **🎯 ردیابی دقیق**: شناسایی و ردیابی زنده ۲۱ نقطه کلیدی دست با استفاده از MediaPipe.
* **🔊 کنترل صوتی با اشاره**: مدیریت هوشمند صدای سیستم از طریق تغییر فاصله بین انگشت شست و اشاره.
* **📊 داشبورد تلمتری زنده**: دارای نمایشگر HUD حرفه‌ای برای تحلیل لحظه‌ای فاصله اقلیدسی، نرخ فریم (FPS) و درصد نگاشت صدا.
* **🛡️ فیلتر هوشمند داده‌ها**: پیاده‌سازی فیلترهای نرم‌کننده برای جلوگیری از لرزش و پرش‌های ناخواسته در خروجی.
* **⚡ کارایی بالا**: بهینه‌سازی شده برای اجرا روی PC با نرخ فریم بالا.

---

### 🛠️ تکنولوژی‌های استفاده شده
* **زبان برنامه نویسی**: پایتون ۳.۱۱ (بهترین نسخه برای پایداری کتابخانه‌ها).
* **موتور بینایی ماشین**: MediaPipe, OpenCV.
* **ارتباط با سیستم‌عامل**: Pycaw (برای کنترل مستقیم صدای ویندوز).

---

## 🚀 Setup & Installation / راهنمای نصب

### 1. Requirements | پیش‌نیازها
* **OS**: Windows (Required for Pycaw integration).
* **Python**: 3.11 or 3.12 (Python 3.13 is currently not supported for MediaPipe).

### 2. Installation | نصب
```bash
# Clone the repository
git clone [https://github.com/YourUsername/VisionGesture-AI.git](https://github.com/YourUsername/VisionGesture-AI.git)
cd VisionGesture-AI

# Install dependencies
pip install opencv-python mediapipe pycaw comtypes numpy
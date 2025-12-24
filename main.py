import cv2
import mediapipe as mp
import numpy as np
import math
import time
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# ۱. تنظیمات فوق‌پایدار برای کنترل صدای ویندوز
def init_stable_volume():
    try:
        # استفاده از Enumerator برای پیدا کردن دقیق دیوایس فعال خروجی
        enumerator = AudioUtilities.GetDeviceEnumerator()
        devices = enumerator.GetDefaultAudioEndpoint(0, 1) # 0: Render, 1: Multimedia
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        vol_ctrl = cast(interface, POINTER(IAudioEndpointVolume))
        print("✅ اتصال به کارت صدا با موفقیت برقرار شد.")
        return vol_ctrl
    except Exception as e:
        print(f"⚠️ هشدار: سیستم صوتی شناسایی نشد یا دسترسی محدود است: {e}")
        return None

volume = init_stable_volume()

if volume:
    volRange = volume.GetVolumeRange() # بازه استاندارد دسی‌بل ویندوز
    minVol, maxVol = volRange[0], volRange[1]
else:
    minVol, maxVol = -65.25, 0.0

# ۲. پیکربندی هوش مصنوعی MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.8,
    min_tracking_confidence=0.5
)
mp_draw = mp.solutions.drawing_utils

# ۳. تابع هوشمند شناسایی دوربین
def get_cap():
    for i in [1, 0, 2]: # اولویت با دوربین مجازی Iriun
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            print(f"✅ دوربین روی ایندکس {i} فعال شد.")
            return cap
    return None

cap = get_cap()
pTime = 0
volBar = 400
volPer = 0
smoothness = 5 # فیلتر برای جلوگیری از لرزش صدا

while cap and cap.isOpened():
    success, img = cap.read()
    if not success: break
    
    img = cv2.flip(img, 1) # حالت آینه‌ای برای تعامل بهتر کاربر
    h, w, c = img.shape
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    # ۴. طراحی داشبورد جانبی (HUD)
    cv2.rectangle(img, (w-220, 0), (w, h), (20, 20, 20), cv2.FILLED)
    cv2.line(img, (w-220, 0), (w-220, h), (0, 255, 0), 2)
    cv2.putText(img, "AI TELEMETRY", (w-200, 40), cv2.FONT_HERSHEY_DUPLEX, 0.6, (0, 255, 0), 1)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            # رسم اسکلت دست با استایل نئونی
            mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS,
                                 mp_draw.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2),
                                 mp_draw.DrawingSpec(color=(255, 255, 255), thickness=1))

            lmList = [[id, int(lm.x * w), int(lm.y * h)] for id, lm in enumerate(handLms.landmark)]

            if lmList:
                # مختصات نوک شست (۴) و نوک اشاره (۸)
                x1, y1 = lmList[4][1], lmList[4][2]
                x2, y2 = lmList[8][1], lmList[8][2]
                cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

                # محاسبه فاصله اقلیدسی: $Length = \sqrt{(x2-x1)^2 + (y2-y1)^2}$
                length = math.hypot(x2 - x1, y2 - y1)
                
                # نگاشت فاصله به درصد صدا (بازه ۳۰ تا ۱۸۰ پیکسل)
                volPer = np.interp(length, [30, 180], [0, 100])
                volPer = smoothness * round(volPer / smoothness) # اعمال فیلتر نرم‌کننده
                
                # ۵. کنترل مستقیم ولوم ویندوز
                if volume:
                    vol_to_set = np.interp(volPer, [0, 100], [minVol, maxVol])
                    volume.SetMasterVolumeLevel(vol_to_set, None)

                # نمایش گرافیکی روی دست کاربر
                line_color = (0, 255, 255) if length > 30 else (0, 0, 255)
                cv2.line(img, (x1, y1), (x2, y2), line_color, 3)
                cv2.circle(img, (cx, cy), 7, (255, 0, 0), cv2.FILLED)

                # نمایش زنده داده‌ها در داشبورد
                cv2.putText(img, f"Dist: {int(length)} px", (w-200, 100), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 1)
                cv2.putText(img, f"Level: {int(volPer)} %", (w-200, 130), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 1)

    # ۶. المان‌های بصری ثابت (Vertical Vol-Bar)
    volBar = np.interp(volPer, [0, 100], [400, 150])
    cv2.rectangle(img, (w-130, 150), (w-100, 400), (50, 50, 50), 3)
    cv2.rectangle(img, (w-130, int(volBar)), (w-100, 400), (0, 255, 0), cv2.FILLED)
    cv2.putText(img, f'{int(volPer)}%', (w-135, 450), cv2.FONT_HERSHEY_DUPLEX, 0.7, (0, 255, 0), 2)

    # نمایش FPS (تضمین کارایی کد)
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f"FPS: {int(fps)}", (20, 50), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)

    cv2.imshow("AI Advanced System Controller", img)
    if cv2.waitKey(1) & 0xFF == ord('q'): break

if cap: cap.release()
cv2.destroyAllWindows()
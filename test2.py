import cv2
import numpy as np
import base64
import socketio

# เชื่อมต่อไปยัง server.js ที่ใช้ socket.io
sio = socketio.Client()

print("Connecting to server...")  # แสดง log ก่อนการเชื่อมต่อ
sio.connect('http://localhost:5501')

print("Connected to server from python.")  # แสดง log เมื่อเชื่อมต่อสำเร็จ

# ตั้งค่าการบันทึกวิดีโอ
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # กำหนด codec
output = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))  # สร้าง VideoWriter

def frame_callback(frame_data):
    # แปลง base64 กลับเป็นภาพ
    frame_data = frame_data.split(',')[1]
    frame = np.frombuffer(base64.b64decode(frame_data), np.uint8)
    frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)

    # เซฟภาพลงในวิดีโอ
    output.write(frame)

sio.on('to_python_frame', frame_callback)

try:
    # รอรับข้อมูลจากเซิร์ฟเวอร์
    sio.wait()
except KeyboardInterrupt:
    print("Stopping...")
finally:
    output.release()  # ปิดการบันทึกวิดีโอเมื่อจบ
    cv2.destroyAllWindows()  # ปิดหน้าต่าง OpenCV
    sio.disconnect()  # ตัดการเชื่อมต่อจากเซิร์ฟเวอร์

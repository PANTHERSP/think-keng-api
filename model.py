# # import cv2
# # from ultralytics import YOLO
# # import numpy as np
# # import random
# # import torch
# # import base64
# # import socketio


# # # เชื่อมต่อไปยัง server.js ที่ใช้ socket.io
# # sio = socketio.Client()

# # print("Connecting to server...")  # แสดง log ก่อนการเชื่อมต่อ
# # sio.connect('http://localhost:5501')

# # print("Connected to server from python.")  # แสดง log เมื่อเชื่อมต่อสำเร็จ


# # print("Loading YOLO model...")
# # model = YOLO('best.pt')

# # device = 'cuda:0' if torch.cuda.is_available() else 'cpu'
# # print(f"Using device: {device}")
# # model.to(device)


# # redBin = ['battery', 'mobile-phone', 'mouse', 'light-bulb', 'fluorescent-lamp', 'earphone', 'cable', 'spray']
# # yellowBin = ['PET-plastic-bottle', 'PE-plastic-bag', 'broken-glass', 'metal-can', 'paper', 'taobin', 'transparent-plastic-bottle']
# # greenBin = ['animal-waste', 'banana-peel', 'orange-peel']
# # blueBin = ['snack-package', 'tissue-paper', 'foam']

# # label_color = (1, 1, 1)

# # def frame_callback(frame_data):
    
# #     # แปลง base64 กลับเป็นภาพ
# #     frame_data = frame_data.split(',')[1]
# #     frame = np.frombuffer(base64.b64decode(frame_data), np.uint8)
# #     frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)
    
# #     # print(f"frame: {type(frame)}, {frame.shape}")
# #     # print("Pixel value range:", frame.min(), frame.max())
# #     print("frame:", frame)

# #     # print("Running YOLO inference...")
# #     # results = model(frame, batch=1)
# #     results = model(frame, batch=1)

# #     # print('results: ', results)

# #     annotated_frame = frame.copy()
        
# #     all_labels = []
# #     if results[0].masks is not None:
# #         for i, mask in enumerate(results[0].masks.data):
# #             binary_mask = mask.cpu().numpy().astype('uint8') * 255
# #             contours, _ = cv2.findContours(binary_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# #             # ดึงสีของ label
# #             label = results[0].names[results[0].boxes.cls[i].item()]
# #             # label_color = get_label_color(label)
# #             if label in redBin:
# #                 label_color = (0, 0, 255)
# #             elif label in greenBin:
# #                 label_color = (0, 255, 0)
# #             elif label in blueBin:
# #                 label_color = (255, 0, 0)
# #             elif label in yellowBin:
# #                 label_color = (0, 255, 255)
# #             else:
# #                 label_color = (1, 1, 1)
# #             # print(label_colors[label])

                
# #             print('label: ', label)

# #             all_labels.append(label)

# #             # วาดเส้นรอบ mask
# #             cv2.drawContours(annotated_frame, contours, -1, label_color, 4)

# #             # แสดง label และ score
# #             score = results[0].boxes.conf[i].item() * 100
# #             label_text = f'{label} {score:.2f}%'
                

# #             (text_width, text_height), baseline = cv2.getTextSize(label_text, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 2)
# #             x, y = int(results[0].boxes.xyxy[i][0]), int(results[0].boxes.xyxy[i][1])

# #             # วาดพื้นหลังสีตาม label
# #             cv2.rectangle(annotated_frame, (x, y - text_height - baseline), (x + text_width, y), label_color, -1)

# #             # วาดตัวอักษรสีขาว
# #             cv2.putText(annotated_frame, label_text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

# #     # แปลงภาพเป็น base64
# #     _, buffer = cv2.imencode('.jpg', annotated_frame)
# #     frame_base64 = base64.b64encode(buffer).decode('utf-8')

# #     # ส่งข้อมูลไปที่ server.js
# #     print("Sending frame to server...")
# #     sio.emit('from_python_frame', frame_base64)
        
    

# # sio.on('to_python_frame', frame_callback)

# # sio.wait()

# # import cv2
# # from ultralytics import YOLO
# # import numpy as np
# # import random
# # import torch
# # import base64
# # import socketio

# # np.set_printoptions(threshold=np.inf)

# # # เชื่อมต่อไปยัง server.js ที่ใช้ socket.io
# # sio = socketio.Client()

# # print("Connecting to server...")  # แสดง log ก่อนการเชื่อมต่อ
# # sio.connect('http://localhost:5501')

# # print("Connected to server from python.")  # แสดง log เมื่อเชื่อมต่อสำเร็จ

# # try:
# #     print("Loading YOLO model...")
# #     model = YOLO('best.pt')
# #     print("YOLO model loaded successfully.")
# # except Exception as e:
# #     print(f"Error loading YOLO model: {e}")
# #     exit(1)  # ออกจากโปรแกรมถ้าโหลดโมเดลไม่สำเร็จ

# # device = 'cuda:0' if torch.cuda.is_available() else 'cpu'
# # # device = 'cpu'
# # print(f"Using device: {device}")
# # model.to(device)

# # # print(model)

# # redBin = ['battery', 'mobile-phone', 'mouse', 'light-bulb', 'fluorescent-lamp', 'earphone', 'cable', 'spray']
# # yellowBin = ['PET-plastic-bottle', 'PE-plastic-bag', 'broken-glass', 'metal-can', 'paper', 'taobin', 'transparent-plastic-bottle']
# # greenBin = ['animal-waste', 'banana-peel', 'orange-peel']
# # blueBin = ['snack-package', 'tissue-paper', 'foam']

# # label_color = (1, 1, 1)

# # def frame_callback(frame_data):
# #     # แปลง base64 กลับเป็นภาพ
# #     frame_data = frame_data.split(',')[1]
# #     frame = np.frombuffer(base64.b64decode(frame_data), np.uint8)
# #     frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)
    
# #     print("frame:", frame)

# #     # รัน YOLO inference
# #     # results = model(frame, batch=1)
# #     try:
# #         results = model(frame, batch=1)
# #         print('results: ', results)
# #     except Exception as e:
# #         print(f"Error during YOLO inference: {e}")
# #         results = None

# #     # print('results: ', results)

# #     annotated_frame = frame.copy()
# #     all_labels = []
    
# #     if results[0].masks is not None:
# #         for i, mask in enumerate(results[0].masks.data):
# #             binary_mask = mask.cpu().numpy().astype('uint8') * 255
# #             contours, _ = cv2.findContours(binary_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# #             # ดึงสีของ label
# #             label = results[0].names[results[0].boxes.cls[i].item()]
# #             if label in redBin:
# #                 label_color = (0, 0, 255)
# #             elif label in greenBin:
# #                 label_color = (0, 255, 0)
# #             elif label in blueBin:
# #                 label_color = (255, 0, 0)
# #             elif label in yellowBin:
# #                 label_color = (0, 255, 255)
# #             else:
# #                 label_color = (1, 1, 1)

# #             print('label: ', label)
# #             all_labels.append(label)

# #             # วาดเส้นรอบ mask
# #             cv2.drawContours(annotated_frame, contours, -1, label_color, 4)

# #             # แสดง label และ score
# #             score = results[0].boxes.conf[i].item() * 100
# #             label_text = f'{label} {score:.2f}%'

# #             (text_width, text_height), baseline = cv2.getTextSize(label_text, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 2)
# #             x, y = int(results[0].boxes.xyxy[i][0]), int(results[0].boxes.xyxy[i][1])

# #             # วาดพื้นหลังสีตาม label
# #             cv2.rectangle(annotated_frame, (x, y - text_height - baseline), (x + text_width, y), label_color, -1)

# #             # วาดตัวอักษรสีขาว
# #             cv2.putText(annotated_frame, label_text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

# #     # แปลงภาพเป็น base64
# #     _, buffer = cv2.imencode('.jpg', annotated_frame)
# #     frame_base64 = base64.b64encode(buffer).decode('utf-8')

# #     # ส่งข้อมูลไปที่ server.js
# #     print("Sending frame to server...")
# #     sio.emit('from_python_frame', frame_base64)

# # sio.on('to_python_frame', frame_callback)

# # sio.wait()


# # import cv2
# # from ultralytics import YOLO
# # import numpy as np
# # import random
# # import torch
# # import base64
# # import socketio

# # np.set_printoptions(threshold=np.inf)

# # # เชื่อมต่อไปยัง server.js ที่ใช้ socket.io
# # sio = socketio.Client()

# # print("Connecting to server...")  # แสดง log ก่อนการเชื่อมต่อ
# # sio.connect('http://localhost:5501')

# # print("Connected to server from python.")  # แสดง log เมื่อเชื่อมต่อสำเร็จ

# # try:
# #     print("Loading YOLO model...")
# #     model = YOLO('best.pt')
# #     print("YOLO model loaded successfully.")
# # except Exception as e:
# #     print(f"Error loading YOLO model: {e}")
# #     exit(1)  # ออกจากโปรแกรมถ้าโหลดโมเดลไม่สำเร็จ

# # device = 'cuda:0' if torch.cuda.is_available() else 'cpu'
# # # device = 'cpu'
# # print(f"Using device: {device}")
# # model.to(device)

# # # print(model)

# # redBin = ['battery', 'mobile-phone', 'mouse', 'light-bulb', 'fluorescent-lamp', 'earphone', 'cable', 'spray']
# # yellowBin = ['PET-plastic-bottle', 'PE-plastic-bag', 'broken-glass', 'metal-can', 'paper', 'taobin', 'transparent-plastic-bottle']
# # greenBin = ['animal-waste', 'banana-peel', 'orange-peel']
# # blueBin = ['snack-package', 'tissue-paper', 'foam']

# # label_color = (1, 1, 1)

# # callback_count = 0


# # def frame_callback(frame_data):

# #     print("Received frame data from server")
# #     global callback_count
# #     callback_count += 1
# #     print(f"Callback count: {callback_count}")
# #     try:
# #         # แปลง base64 กลับเป็นภาพ
# #         frame_data = frame_data.split(',')[1]
# #         frame = np.frombuffer(base64.b64decode(frame_data), np.uint8)
# #         frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)
# #     except Exception as e:
# #         print(f"เกิดข้อผิดพลาดในการแปลงข้อมูลเฟรม: {e}")
# #         return

# #     # print("กำลังประมวลผลเฟรม...")

# #     if not model:
# #         print("ไม่มีโมเดล YOLO ที่ต้องการประมวลผล.")
# #         return

# #     try:
# #         # รัน YOLO inference
# #         results = model(frame, batch=1)
# #         if results is None or not results:
# #             print("ไม่มีผลลัพธ์จาก YOLO.")
# #             return
# #         # print('ผลลัพธ์: ', results)
# #     except Exception as e:
# #         print(f"เกิดข้อผิดพลาดระหว่างการประมวลผล YOLO: {e}")
# #         return

# #     annotated_frame = frame.copy()
# #     all_labels = []

# #     if results[0].masks is not None:
# #         for i, mask in enumerate(results[0].masks.data):
# #             binary_mask = mask.cpu().numpy().astype('uint8') * 255
# #             contours, _ = cv2.findContours(binary_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# #             # ตรวจสอบว่าเจอ contours หรือไม่
# #             if not contours:
# #                 continue

# #             # ดึงสีของ label
# #             label = results[0].names[results[0].boxes.cls[i].item()]
# #             if label in redBin:
# #                 label_color = (0, 0, 255)
# #             elif label in greenBin:
# #                 label_color = (0, 255, 0)
# #             elif label in blueBin:
# #                 label_color = (255, 0, 0)
# #             elif label in yellowBin:
# #                 label_color = (0, 255, 255)
# #             else:
# #                 label_color = (255, 255, 255)  # เปลี่ยนเป็นสีขาว (255, 255, 255)

# #             print('เลเบล: ', label)
# #             all_labels.append(label)

# #             # วาดเส้นรอบมาสก์
# #             cv2.drawContours(annotated_frame, contours, -1, label_color, 4)

# #             # แสดงเลเบลและคะแนน
# #             score = results[0].boxes.conf[i].item() * 100
# #             label_text = f'{label} {score:.2f}%'

# #             (text_width, text_height), baseline = cv2.getTextSize(label_text, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 2)
# #             x, y = int(results[0].boxes.xyxy[i][0]), int(results[0].boxes.xyxy[i][1])

# #             # วาดพื้นหลังสีตามเลเบล
# #             cv2.rectangle(annotated_frame, (x, y - text_height - baseline), (x + text_width, y), label_color, -1)

# #             # วาดตัวอักษรสีขาว
# #             cv2.putText(annotated_frame, label_text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

# #     # แปลงภาพเป็น base64
# #     _, buffer = cv2.imencode('.jpg', annotated_frame)
# #     frame_base64 = base64.b64encode(buffer).decode('utf-8')

# #     # ส่งข้อมูลไปยัง server.js
# #     # print("กำลังส่งเฟรมไปยังเซิร์ฟเวอร์...")
# #     try:
# #         sio.emit('from_python_frame', frame_base64)
# #     except Exception as e:
# #         print(f"เกิดข้อผิดพลาดในการส่งเฟรมไปยังเซิร์ฟเวอร์: {e}")


# # sio.on('to_python_frame', frame_callback)

# # sio.wait()


# import cv2
# from ultralytics import YOLO
# import numpy as np
# import torch
# import base64
# import socketio
# from collections import deque
# import threading

# np.set_printoptions(threshold=np.inf)

# # เชื่อมต่อไปยัง server.js ที่ใช้ socket.io
# sio = socketio.Client()

# print("Connecting to server...")  # แสดง log ก่อนการเชื่อมต่อ
# sio.connect('http://localhost:5501')
# # sio.connect('https://16a8-171-6-111-222.ngrok-free.app/')

# print("Connected to server from python.")  # แสดง log เมื่อเชื่อมต่อสำเร็จ

# try:
#     print("Loading YOLO model...")
#     model = YOLO('best.pt')
#     print("YOLO model loaded successfully.")
# except Exception as e:
#     print(f"Error loading YOLO model: {e}")
#     exit(1)  # ออกจากโปรแกรมถ้าโหลดโมเดลไม่สำเร็จ

# device = 'cuda:0' if torch.cuda.is_available() else 'cpu'
# model.to(device)

# # คิวเพื่อจัดเก็บเฟรมที่ต้องการประมวลผล
# frame_queue = deque()
# is_processing = False

# def process_frames():
#     global is_processing
#     while True:
#         if frame_queue and not is_processing:
#             is_processing = True
#             frame_data = frame_queue.popleft()  # ดึงเฟรมออกจากคิว
#             frame_callback(frame_data)  # ประมวลผลเฟรม
#             is_processing = False  # ประมวลผลเสร็จสิ้น

# # เริ่ม thread สำหรับการประมวลผลเฟรม
# threading.Thread(target=process_frames, daemon=True).start()

# redBin = ['battery', 'mobile-phone', 'mouse', 'light-bulb', 'fluorescent-lamp', 'earphone', 'cable', 'spray']
# yellowBin = ['PET-plastic-bottle', 'PE-plastic-bag', 'broken-glass', 'metal-can', 'paper', 'taobin', 'transparent-plastic-bottle']
# greenBin = ['animal-waste', 'banana-peel', 'orange-peel']
# blueBin = ['snack-package', 'tissue-paper', 'foam']

# label_color = (1, 1, 1)
# callback_count = 0

# def frame_callback(frame_data):
#     print("Received frame data from server")
#     global callback_count
#     callback_count += 1
#     print(f"Callback count: {callback_count}")

#     try:
#         # แปลง base64 กลับเป็นภาพ
#         frame_data = frame_data.split(',')[1]
#         frame = np.frombuffer(base64.b64decode(frame_data), np.uint8)
#         frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)
#     except Exception as e:
#         print(f"เกิดข้อผิดพลาดในการแปลงข้อมูลเฟรม: {e}")
#         return

#     if not model:
#         print("ไม่มีโมเดล YOLO ที่ต้องการประมวลผล.")
#         return

#     try:
#         # รัน YOLO inference
#         results = model(frame, batch=1)
#         if results is None or not results:
#             print("ไม่มีผลลัพธ์จาก YOLO.")
#             return
#     except Exception as e:
#         print(f"เกิดข้อผิดพลาดระหว่างการประมวลผล YOLO: {e}")
#         return

#     annotated_frame = frame.copy()
#     all_labels = []

#     if results[0].masks is not None:
#         for i, mask in enumerate(results[0].masks.data):
#             binary_mask = mask.cpu().numpy().astype('uint8') * 255
#             contours, _ = cv2.findContours(binary_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#             if not contours:
#                 continue

#             label = results[0].names[results[0].boxes.cls[i].item()]
#             if label in redBin:
#                 label_color = (0, 0, 255)
#             elif label in greenBin:
#                 label_color = (0, 255, 0)
#             elif label in blueBin:
#                 label_color = (255, 0, 0)
#             elif label in yellowBin:
#                 label_color = (0, 255, 255)
#             else:
#                 label_color = (255, 255, 255)

#             if label in yellowBin:
#                 label_text_color = (0, 0, 0)
#             else:
#                 label_text_color = (255, 255, 255)

#             print('label: ', label)
#             all_labels.append(label)

#             cv2.drawContours(annotated_frame, contours, -1, label_color, 4)

#             score = results[0].boxes.conf[i].item() * 100
#             label_text = f'{label} {score:.2f}%'
#             (text_width, text_height), baseline = cv2.getTextSize(label_text, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 2)
#             x, y = int(results[0].boxes.xyxy[i][0]), int(results[0].boxes.xyxy[i][1])

#             cv2.rectangle(annotated_frame, (x, y - text_height - baseline), (x + text_width, y), label_color, -1)
#             cv2.putText(annotated_frame, label_text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, label_text_color, 2)

#     _, buffer = cv2.imencode('.jpg', annotated_frame)
#     frame_base64 = base64.b64encode(buffer).decode('utf-8')

#     try:
#         sio.emit('from_python_frame', frame_base64)
#     except Exception as e:
#         print(f"เกิดข้อผิดพลาดในการส่งเฟรมไปยังเซิร์ฟเวอร์: {e}")

# # ปรับการรับเฟรมจากเซิร์ฟเวอร์
# sio.on('to_python_frame', lambda frame: frame_queue.append(frame))  # เพิ่มเฟรมลงในคิว

# sio.wait()


import cv2
from ultralytics import YOLO
import numpy as np
import torch
import base64
import socketio
from collections import deque
import threading

np.set_printoptions(threshold=np.inf)

# เชื่อมต่อไปยัง server.js ที่ใช้ socket.io
sio = socketio.Client()

print("Connecting to server...")  # แสดง log ก่อนการเชื่อมต่อ
sio.connect('http://localhost:5501')
# sio.connect('https://16a8-171-6-111-222.ngrok-free.app/')

print("Connected to server from python.")  # แสดง log เมื่อเชื่อมต่อสำเร็จ

try:
    print("Loading YOLO model...")
    model = YOLO('best.pt')
    print("YOLO model loaded successfully.")
except Exception as e:
    print(f"Error loading YOLO model: {e}")
    exit(1)  # ออกจากโปรแกรมถ้าโหลดโมเดลไม่สำเร็จ

device = 'cuda:0' if torch.cuda.is_available() else 'cpu'
model.to(device)

# คิวเพื่อจัดเก็บเฟรมที่ต้องการประมวลผล
frame_queue = deque()
is_processing = False

def process_frames():
    global is_processing
    while True:
        if frame_queue and not is_processing:
            is_processing = True
            frame_data = frame_queue.popleft()  # ดึงเฟรมออกจากคิว
            frame_callback(frame_data)  # ประมวลผลเฟรม
            is_processing = False  # ประมวลผลเสร็จสิ้น

# เริ่ม thread สำหรับการประมวลผลเฟรม
# threading.Thread(target=process_frames, daemon=True).start()

redBin = ['battery', 'mobile-phone', 'mouse', 'light-bulb', 'fluorescent-lamp', 'earphone', 'cable', 'spray']
yellowBin = ['PET-plastic-bottle', 'PE-plastic-bag', 'broken-glass', 'metal-can', 'paper', 'taobin', 'transparent-plastic-bottle']
greenBin = ['animal-waste', 'banana-peel', 'orange-peel']
blueBin = ['snack-package', 'tissue-paper', 'foam']

label_color = (1, 1, 1)
callback_count = 0

def frame_callback(frame_data):
    print("Received frame data from server")
    global callback_count
    callback_count += 1
    print(f"Callback count: {callback_count}")


    try:
        # แปลง base64 กลับเป็นภาพ
        frame_data = frame_data.split(',')[1]
        frame = np.frombuffer(base64.b64decode(frame_data), np.uint8)
        frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)
        original_image_width, original_image_height, _ = frame.shape
        frame = cv2.resize(frame, (640, 480))
        
    except Exception as e:
        print(f"เกิดข้อผิดพลาดในการแปลงข้อมูลเฟรม: {e}")
        return

    if not model:
        print("ไม่มีโมเดล YOLO ที่ต้องการประมวลผล.")
        return

    try:
        height, width, channels = frame.shape
        print(f"before => width: {width}, height: {height}, channels: {channels}")
        # รัน YOLO inference
        results = model(frame, batch=1)
        if results is None or not results:
            print("ไม่มีผลลัพธ์จาก YOLO.")
            return
    except Exception as e:
        print(f"เกิดข้อผิดพลาดระหว่างการประมวลผล YOLO: {e}")
        return

    annotated_frame = frame.copy()
    all_labels = []

    if results[0].masks is not None:
        for i, mask in enumerate(results[0].masks.data):
            binary_mask = mask.cpu().numpy().astype('uint8') * 255
            contours, _ = cv2.findContours(binary_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            if not contours:
                continue

            label = results[0].names[results[0].boxes.cls[i].item()]
            if label in redBin:
                label_color = (0, 0, 255)
            elif label in greenBin:
                label_color = (0, 255, 0)
            elif label in blueBin:
                label_color = (255, 0, 0)
            elif label in yellowBin:
                label_color = (0, 255, 255)
            else:
                label_color = (255, 255, 255)

            if label in yellowBin:
                label_text_color = (0, 0, 0)
            else:
                label_text_color = (255, 255, 255)

            print('label: ', label)
            all_labels.append(label)

            cv2.drawContours(annotated_frame, contours, -1, label_color, 4)

            score = results[0].boxes.conf[i].item() * 100
            label_text = f'{label} {score:.2f}%'
            (text_width, text_height), baseline = cv2.getTextSize(label_text, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 2)
            x, y = int(results[0].boxes.xyxy[i][0]), int(results[0].boxes.xyxy[i][1])

            cv2.rectangle(annotated_frame, (x, y - text_height - baseline), (x + text_width, y), label_color, -1)
            cv2.putText(annotated_frame, label_text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, label_text_color, 2)
    
    # cv2.imshow('annotated_frame', annotated_frame)
    # cv2.imwrite('annotated_frame.jpg', annotated_frame)
    # print('annotated_frame: ', annotated_frame)
    annotated_frame = cv2.resize(annotated_frame, (original_image_height, original_image_width))
    height, width, channels = annotated_frame.shape
    print(f"after => width: {width}, height: {height}, channels: {channels}")

    _, buffer = cv2.imencode('.jpg', annotated_frame)
    frame_base64 = base64.b64encode(buffer).decode('utf-8')

    try:
        sio.emit('from_python_frame', {'frame': frame_base64, 'labels': all_labels})  # ส่งเฟรมไปยัง server.js โดยใช้ emit frame_base64)
    except Exception as e:
        print(f"เกิดข้อผิดพลาดในการส่งเฟรมไปยังเซิร์ฟเวอร์: {e}")

# ปรับการรับเฟรมจากเซิร์ฟเวอร์
sio.on('to_python_frame', frame_callback)  # เพิ่มเฟรมลงในคิว

sio.wait()

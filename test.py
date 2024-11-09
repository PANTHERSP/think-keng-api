# import cv2

# # เปิดการเชื่อมต่อกับกล้อง
# cap = cv2.VideoCapture(0)

# if not cap.isOpened():
#     print("Cannot open camera")
#     exit()

# while True:
#     # อ่านภาพจากกล้อง
#     ret, frame = cap.read()
#     if not ret:
#         print("Failed to grab frame")
#         break

#     # แปลงจาก BGR เป็น RGB
#     # frame_rgb = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2RGB)

#     # แสดงภาพ BGR และ RGB เพื่อเปรียบเทียบ
#     cv2.imshow("original Frame", frame)
#     # cv2.imshow("RGB Frame", frame_rgb)

#     # กด 'q' เพื่อออกจากลูป
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # ปิดการเชื่อมต่อกับกล้องและปิดหน้าต่างทั้งหมด
# cap.release()
# cv2.destroyAllWindows()

import cv2

# เปิดการเชื่อมต่อกับกล้อง
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

# อ่านภาพจากกล้องในรูปแบบ BGR
ret, frame = cap.read()
if not ret:
    print("Failed to capture frame")
else:
    # บันทึกภาพโดยตรงในรูปแบบ BGR
    cv2.imwrite("image.jpg", frame)
    print("Saved image.jpg (original format)")

    # แปลงจาก BGR เป็น RGB ก่อนบันทึก
    # frame_rgb = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2RGB)
    # cv2.imwrite("image_rgb.jpg", frame_rgb)
    # print("Saved image_rgb.jpg (RGB format)")

# ปิดการเชื่อมต่อกับกล้อง
cap.release()


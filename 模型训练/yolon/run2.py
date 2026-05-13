from ultralytics import YOLO
import cv2
from collections import deque
import statistics
import time

model = YOLO("yolo26s.pt")  # 或 yolo26s.pt

print("模型加载成功，类别0:", model.names[0])

# 使用探测到的索引 0
source = 1

cap = cv2.VideoCapture(source, cv2.CAP_DSHOW)  # 强制 DirectShow 后端
if not cap.isOpened():
    print("摄像头打不开")
    exit()

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# 验证第一帧
ret, frame = cap.read()
if not ret:
    print("读不到第一帧")
    cap.release()
    exit()

print("摄像头就绪，开始手动实时检测... (按 q 退出窗口)")

count_history = deque(maxlen=7)
previous_count = 0
frame_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        print("读取帧失败，尝试重新初始化...")
        cap.release()
        cap = cv2.VideoCapture(source, cv2.CAP_DSHOW)
        time.sleep(1)
        continue

    # 每隔几帧处理一次（提 FPS）
    frame_count += 1
    if frame_count % 2 == 0:  # 每2帧处理1次
        results = model.track(
            frame,                  # 直接喂当前帧
            persist=True,
            classes=[0],
            conf=0.05,
            iou=0.6,
            tracker="botsort.yaml",
            imgsz=416,
            verbose=True
        )

        current_count = 0
        if results[0].boxes is not None:
            person_mask = results[0].boxes.cls == 0
            current_count = person_mask.sum().item()

        count_history.append(current_count)
        smoothed_count = statistics.median(count_history) if count_history else 0

        print(f"原始: {current_count} | 平滑: {smoothed_count}")

        # 可选：显示带框画面（调试用，正式可关掉提速）
        annotated_frame = results[0].plot()
        cv2.imshow("YOLO Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print("结束")
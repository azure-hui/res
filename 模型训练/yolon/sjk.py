from ultralytics import YOLO
import cv2
from collections import deque
import statistics
import time
import psycopg2
from psycopg2 import Error
from datetime import datetime

# ────────────────────────────────────────────────
#  1. YOLO 模型 & 摄像头设置
# ────────────────────────────────────────────────

model = YOLO("yolo26s.pt")  #  "yolo26s.pt"

print("模型加载成功，类别0:", model.names[0])

source = 1  #  摄像头索引（从 test_usb.py 确认）

cap = cv2.VideoCapture(source, cv2.CAP_DSHOW)
if not cap.isOpened():
    print("摄像头打不开，请检查索引或驱动")
    exit()

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

ret, frame = cap.read()
if not ret:
    print("读不到第一帧")
    cap.release()
    exit()

print("摄像头就绪，开始实时 person 检测... (按 q 退出窗口)")

# ────────────────────────────────────────────────
#  2. 平滑缓冲 & 计数
# ────────────────────────────────────────────────

count_history = deque(maxlen=10)
previous_smoothed = 0
frame_count = 0

# ────────────────────────────────────────────────
#  3. 数据库连接参数（请替换成你的真实值）
# ────────────────────────────────────────────────

DB_PARAMS = {
    "dbname":   "restaurant_db",
    "user":     "postgres",          # 
    "password": "4432",          # 
    "host":     "localhost",
    "port":     "5432"
}

last_insert_time = time.time()
INSERT_INTERVAL = 10  # 每 10 秒插入一次（测试用，可改成 10/30）

# ────────────────────────────────────────────────
#  主循环
# ────────────────────────────────────────────────

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("读取帧失败，重新初始化...")
            cap.release()
            cap = cv2.VideoCapture(source, cv2.CAP_DSHOW)
            time.sleep(0.5)
            continue

        frame_count += 1

        # 每 2 帧处理一次（提 FPS）
        if frame_count % 2 == 0:
            results = model.track(
                frame,
                persist=True,
                classes=[0],
                conf=0.35,          # 已调高，避免衣服误检
                iou=0.6,
                tracker="botsort.yaml",
                imgsz=416,
                verbose=False
            )

            current_count = 0
            avg_conf = 0.0
            if results and results[0].boxes is not None:
                person_mask = results[0].boxes.cls == 0
                current_count = person_mask.sum().item()
                if current_count > 0:
                    avg_conf = results[0].boxes.conf[person_mask].mean().item()

            count_history.append(current_count)
            smoothed_count = statistics.median(count_history) if count_history else 0

            # 打印变化或每 5 次
            if smoothed_count != previous_smoothed or frame_count % 10 == 0:
                print(f"原始: {current_count} | 平滑: {smoothed_count} | avg_conf: {avg_conf:.3f}")

            previous_smoothed = smoothed_count

            # 可选显示（调试用，正式可注释掉提速）
            annotated = results[0].plot() if results else frame
            cv2.imshow("YOLO Detection", annotated)

        # ────────────────────────────────────────────────
        #  4. 每 INSERT_INTERVAL 秒插入一次数据库
        # ────────────────────────────────────────────────
        current_time = time.time()
        if current_time - last_insert_time >= INSERT_INTERVAL:
            try:
                conn = psycopg2.connect(**DB_PARAMS)
                cur = conn.cursor()

                cur.execute("""
                    INSERT INTO occupancy_logs 
                    (time, camera_id, current_count, smoothed_count, raw_conf_avg)
                    VALUES (NOW(), %s, %s, %s, %s)
                """, (
                    'cam_usb_1080p',      # camera_id
                    current_count,
                    smoothed_count,
                    avg_conf if avg_conf > 0 else None
                ))

                conn.commit()
                print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 已插入数据库: 平滑人数 = {smoothed_count}")

                last_insert_time = current_time

            except (Exception, Error) as error:
                print("数据库插入失败:", error)
                if conn:
                    conn.rollback()
            finally:
                if cur:
                    cur.close()
                if conn:
                    conn.close()

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    print("用户中断 (Ctrl+C)")

except Exception as e:
    print("运行异常:", str(e))

finally:
    cap.release()
    cv2.destroyAllWindows()
    print("程序结束，摄像头已释放")
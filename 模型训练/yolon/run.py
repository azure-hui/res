from ultralytics import YOLO
import cv2

model = YOLO("yolo26s.pt")
print("模型信息：", model.info())  # 打印模型详情
print("类别名称：", model.names)
print("person 类索引：", list(model.names.keys())[0] if 0 in model.names else "无 class 0")

source = 1  # ← 改成你外接摄像头的索引（从上面脚本找到的，比如 1 或 2）

cap = cv2.VideoCapture(source)
if not cap.isOpened():
    print("外接摄像头打不开！检查索引、驱动或 USB 连接")
    exit()

# 可选：设置分辨率到 1080P（很多 USB 摄像头支持）
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
# 或降到 640x480 测试速度（YOLO 实时更友好）
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

print("外接摄像头打开成功，开始检测...")

results = model.track(
    source=source,
    stream=True,
    show=True,
    classes=[0],          # person
    persist=True,
    tracker="bytetrack.yaml",
    conf=0.02,            # 先用 0.25，必要时降到 0.2 或 0.15
    verbose=True,
)

current_count = 0
for result in results:
    boxes = result.boxes
    if boxes is not None:
        current_count = len([b for b in boxes if b.cls == 0])
        print(f"当前检测到人数: {current_count}")
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

for result in results:
    boxes = result.boxes
    if boxes is None or len(boxes) == 0:
        print("这一帧：无任何检测框（boxes 为空）")
    else:
        print(f"这一帧检测到 {len(boxes)} 个物体")
        print("类别：", boxes.cls.tolist())  # 应该有 0.0 表示 person
        print("置信度：", boxes.conf.tolist())  # 看 conf 值是否低于阈值
        current_count = len([b for b in boxes if int(b.cls) == 0])
        print(f"person 人数: {current_count}")

cap.release()
cv2.destroyAllWindows()
import cv2

print("测试所有摄像头索引（0~5）...")

for i in range(6):
    cap = cv2.VideoCapture(i, cv2.CAP_DSHOW)
    if cap.isOpened():
        ret, frame = cap.read()
        if ret:
            h, w = frame.shape[:2]
            title = f"Camera {i} - {w}x{h}"
            print(f"索引 {i}：打开成功，分辨率 {w}x{h}")
            cv2.imshow(title, frame)
            cv2.waitKey(0)  # 按任意键关闭当前窗口
            cv2.destroyWindow(title)  # 用同一个英文标题销毁
        else:
            print(f"索引 {i}：打开了，但读不到帧")
        cap.release()
    else:
        print(f"索引 {i}：无法打开")

print("测试结束")
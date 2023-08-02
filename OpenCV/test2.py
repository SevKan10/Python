import cv2

def main():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Không thể mở camera.")
        return

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Không thể đọc hình ảnh từ camera.")
            break

        # Hiển thị hình ảnh từ camera
        cv2.imshow('Camera', frame)

        # Thoát khỏi vòng lặp khi nhấn phím 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

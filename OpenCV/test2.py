import cv2

def display_image(image_path):
    # Đọc hình ảnh từ đường dẫn
    img = cv2.imread(image_path)

    # Kiểm tra xem hình ảnh đã được đọc thành công chưa
    if img is None:
        print("Không thể đọc hình ảnh. Vui lòng kiểm tra lại đường dẫn.")
        return

    # Hiển thị hình ảnh trong một cửa sổ
    cv2.imshow("Hình ảnh", img)

    # Đợi người dùng nhấn phím bất kỳ trước khi đóng cửa sổ
    cv2.waitKey(0)

    # Đóng tất cả các cửa sổ hiển thị
    cv2.destroyAllWindows()

# Ví dụ sử dụng
image_path = "OpenCV/img/z4533842960509_92f4ffbf7b11c54cbe5a2102aa643814.jpg"  # Thay đổi đường dẫn này thành đường dẫn đến hình ảnh của bạn
display_image(image_path)

import os

# Đường dẫn đến thư mục chứa các file ảnh
folder_path = ''

# Lấy danh sách các file trong thư mục
file_list = os.listdir(folder_path)

# Sắp xếp danh sách các file theo thứ tự (nếu cần)
file_list.sort()

# Đặt tên mới cho từng file và di chuyển nó
for index, old_name in enumerate(file_list):
    # Tạo tên mới theo định dạng của bạn, ví dụ: image_001.jpg, image_002.jpg, ...
    new_name = f'image_{index + 1}.jpg'
    # Đường dẫn cũ và mới
    old_path = os.path.join(folder_path, old_name)
    new_path = os.path.join(folder_path, new_name)
    # Di chuyển và đổi tên file
    os.rename(old_path, new_path)
    print(f'Da doi ten file {old_name} thanh {new_name}')

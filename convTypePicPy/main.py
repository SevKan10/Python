import os
from PIL import Image

# Đường dẫn thư mục chứa ảnh .webp
input_folder = 'input'
output_folder = 'output'
max_images = 100  # Giới hạn số lượng ảnh cần chuyển

# Tạo thư mục đầu ra nếu chưa có
os.makedirs(output_folder, exist_ok=True)

# Lấy danh sách tất cả các file .webp trong thư mục
webp_files = [f for f in os.listdir(input_folder) if f.lower().endswith('.webp')]

# Giới hạn 100 ảnh
webp_files = webp_files[:max_images]

for idx, filename in enumerate(webp_files, start=1):
    input_path = os.path.join(input_folder, filename)
    output_filename = os.path.splitext(filename)[0] + '.jpg'
    output_path = os.path.join(output_folder, output_filename)

    try:
        with Image.open(input_path) as img:
            rgb_img = img.convert('RGB')  # JPG không hỗ trợ alpha channel
            rgb_img.save(output_path, 'JPEG')
        print(f"[{idx}] Đã chuyển: {filename} → {output_filename}")
    except Exception as e:
        print(f"Lỗi khi chuyển {filename}: {e}")

print(f"\n✅ Đã chuyển xong {len(webp_files)} ảnh.")

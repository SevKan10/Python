import matplotlib.pyplot as plt

# Dữ liệu
categories = ["Trâu", "Bò", "Lợn", "Gia cầm"]
data_2010 = [2.9, 5.9, 27.3, 301.9]
data_2015 = [2.6, 5.7, 28.9, 369.5]
data_2021 = [2.3, 6.4, 23.1, 524.1]

# Vẽ biểu đồ tròn
fig, axes = plt.subplots(1, 3, figsize=(18, 6))

# Biểu đồ năm 2010
axes[0].pie(data_2010, labels=categories, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors[:4])
axes[0].set_title("Cơ cấu năm 2010")

# Biểu đồ năm 2015
axes[1].pie(data_2015, labels=categories, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors[4:8])
axes[1].set_title("Cơ cấu năm 2015")

# Biểu đồ năm 2021
axes[2].pie(data_2021, labels=categories, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors[8:12])
axes[2].set_title("Cơ cấu năm 2021")

# Tiêu đề chung
fig.suptitle("Biểu đồ tròn: Cơ cấu số lượng gia súc và gia cầm giai đoạn 2010 - 2021", fontsize=14)

plt.tight_layout()
plt.show()

print("Hello")
mon = float(input("Hãy nhập số tiền quý khách đã mua: "))

if mon > 100000000:
    print("Số tiền được tặng là: ", mon * 0.065)
elif mon > 50000000:
    print("Số tiền được tặng là: ", mon * 0.055)
elif mon > 20000000:
    print("Số tiền được tặng là: ", mon * 0.04)
else:
    print("Không có khuyến mãi!")


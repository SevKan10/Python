print("Chương trình kiểm tra năm")
year = int(input("Hãy nhập số năm: "))

if year%4 == 0 and year%100 !=0: 
    # để biết được năm nhuậ thì ta lấy số năm %4==0 hoặc %400==0 và %100 !=0
    print(year,"Là năm nhuận")
else:
    print(year,"Không là năm nhuận")
    
print('รายการซื้อของ ร้านแห่งหนึี่ง')
a = int(input('จำนวนสินค้า(ชิ้น):'))
b = float(input('ราคาสินค้า:'))
x = a*b
print('ราคารวมที่ต้องจ่าย:',x)

c = float(input('จำนวนเงินที่จ่าย:'))
total = c-x
print('เงินทอน:',total)


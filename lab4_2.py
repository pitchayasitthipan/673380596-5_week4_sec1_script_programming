# lab4_2.py
# Lab 4.2: Geometric Calculations (Tuples & Immutability)
import math

# 1. กำหนดจุดเป็น Tuple
point1 = (3, 4)
point2 = (6, 8)

# เข้าถึงและพิมพ์พิกัด x, y
print(f"Point 1: x = {point1[0]}, y = {point1[1]}")
print(f"Point 2: x = {point2[0]}, y = {point2[1]}")

# 2. ทดลองแก้ไขค่า (พิสูจน์ Immutability)
# point1[0] = 5
# ผลที่ได้: TypeError: 'tuple' object does not support item assignment
# เหตุผล: Tuple เป็นข้อมูลชนิด immutable สร้างแล้วเปลี่ยนค่าสมาชิกไม่ได้
#         (ต่างจาก list ที่เป็น mutable) จึงเหมาะกับข้อมูลที่ไม่ควรเปลี่ยน เช่น พิกัด

# 3. คำนวณระยะห่าง: sqrt((x2-x1)^2 + (y2-y1)^2)
x1, y1 = point1
x2, y2 = point2
distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print(f"Distance between point1 and point2 = {distance}")  # 5.0

# ---------------------------------------------------------------
# Challenge: รับค่าพิกัดจากผู้ใช้
# ---------------------------------------------------------------
print("\n=== Challenge: Enter your own points ===")


def read_point(label):
    """อ่านพิกัด x, y จาก input() แปลงเป็น float แล้วคืนค่าเป็น tuple"""
    while True:
        try:
            x = float(input(f"{label} x: "))
            y = float(input(f"{label} y: "))
            return (x, y)
        except ValueError:
            print("กรุณากรอกเป็นตัวเลข")


new_point1 = read_point("Point 1")
new_point2 = read_point("Point 2")
new_distance = math.sqrt((new_point2[0] - new_point1[0]) ** 2
                         + (new_point2[1] - new_point1[1]) ** 2)
print(f"Distance between {new_point1} and {new_point2} = {new_distance:.2f}")

# lab4_1.py
# Lab 4.1: Student Management System (List Operations)

# 1. สร้าง List ว่างเปล่า
student_names = []

# ---------------------------------------------------------------
# ส่วนที่ 1: ทำตามขั้นตอนที่ 2-6 ตามลำดับ
# ---------------------------------------------------------------

# 2. เพิ่มรายชื่อนักเรียน (กรอก 3-5 คน)
print("=== 2. Add Students ===")
count = 0
while count < 5:
    name = input(f"Enter student name #{count + 1} (กด Enter เว้นว่างเพื่อหยุด เมื่อครบ 3 คนแล้ว): ").strip()
    if name == "":
        if count >= 3:
            break
        print("ต้องกรอกอย่างน้อย 3 คน")
        continue
    student_names.append(name)
    count += 1
print("Current list:", student_names)

# 3. ค้นหารายชื่อนักเรียน
print("\n=== 3. Find a Student ===")
target = input("Enter a name to search: ").strip()
if target in student_names:
    print(f"Found '{target}' at index {student_names.index(target)}")
else:
    print(f"'{target}' not found")

# 4. ลบรายชื่อนักเรียน
print("\n=== 4. Remove a Student ===")
target = input("Enter a name to remove: ").strip()
if target in student_names:
    student_names.remove(target)
    print(f"Removed '{target}'")
else:
    print(f"'{target}' not found, nothing removed")
print("Updated list:", student_names)

# 5. จัดเรียงรายชื่อ
print("\n=== 5. Sort Students ===")
student_names.sort()
print("Sorted list:", student_names)

# 6. นับจำนวนนักเรียน
print("\n=== 6. Count Students ===")
print("Total students:", len(student_names))


# ---------------------------------------------------------------
# Challenge: ระบบเมนูด้วย while loop
# ---------------------------------------------------------------
print("\n=== Challenge: Menu System ===")
students = []  # เริ่มรายชื่อใหม่สำหรับระบบเมนู

while True:
    print("\n1. เพิ่ม")
    print("2. ลบ")
    print("3. ค้นหา")
    print("4. เรียงลำดับ")
    print("5. ออกจากโปรแกรม")
    choice = input("เลือกเมนู (1-5): ").strip()

    if choice == "1":
        name = input("ชื่อที่ต้องการเพิ่ม: ").strip()
        if name:
            students.append(name)
            print(f"เพิ่ม '{name}' แล้ว")
        else:
            print("ชื่อห้ามว่าง")
    elif choice == "2":
        name = input("ชื่อที่ต้องการลบ: ").strip()
        if name in students:
            students.remove(name)
            print(f"ลบ '{name}' แล้ว")
        else:
            print(f"ไม่พบ '{name}'")
    elif choice == "3":
        name = input("ชื่อที่ต้องการค้นหา: ").strip()
        if name in students:
            print(f"พบ '{name}' ที่ตำแหน่ง index {students.index(name)}")
        else:
            print(f"ไม่พบ '{name}'")
    elif choice == "4":
        students.sort()
        print("เรียงลำดับแล้ว")
    elif choice == "5":
        print("ออกจากโปรแกรม")
        break
    else:
        print("กรุณาเลือก 1-5 เท่านั้น")
        continue

    print("รายชื่อปัจจุบัน:", students, "| จำนวน:", len(students))

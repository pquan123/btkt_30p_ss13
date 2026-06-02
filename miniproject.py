list_employees = [
    {
        "id": 101,
        "name": "Admin",
        "salary": 10000
    }
]

while True:
    choice = input("""

      QUAN LY NHAN SU - STAFF MANAGER

1. Them nhan vien moi
2. Danh sach nhan vien
3. Tim kiem nhan vien theo ID
4. Xoa nhan vien khoi he thong
5. Thoat chuong trinh

Nhap lua chon cua ban: 
""")

    if not choice.isdigit():
        print("Vui long nhap so tu 1 den 5!")
        continue

    choice = int(choice)

    match choice:

        case 1:
            id_employee = list_employees[-1]["id"] + 1

            while True:
                name_employee = input("Nhap ten nhan vien: ")

                if name_employee.strip() == "":
                    print("Ten nhan vien khong duoc de trong!")
                else:
                    break

            while True:
                salary_employee = input("Nhap muc luong: ")

                try:
                    salary_employee = float(salary_employee)

                    if salary_employee > 0:
                        break
                    else:
                        print("Luong phai lon hon 0!")

                except:
                    print("Vui long nhap dung dinh dang so!")

            employee = {
                "id": id_employee,
                "name": name_employee,
                "salary": salary_employee
            }

            list_employees.append(employee)

            print(f"Them nhan vien thanh cong! ID: {id_employee}")

        case 2:
            if len(list_employees) == 0:
                print("Chua co du lieu nhan su!")
            else:
                print("\n{:<10}{:<25}{:<15}".format("ID", "TEN", "LUONG"))

                for employee in list_employees:
                    print("{:<10}{:<25}{:<15}".format(
                        employee["id"],
                        employee["name"],
                        employee["salary"]
                    ))

        case 3:
            try:
                search_id = int(input("Nhap ID can tim: "))
            except:
                print("ID khong hop le!")
                continue

            found = False

            for employee in list_employees:
                if employee["id"] == search_id:
                    print(employee)
                    found = True
                    break

            if not found:
                print(f"Khong tim thay nhan vien co ID {search_id}!")

        case 4:
            try:
                delete_id = int(input("Nhap ID can xoa: "))
            except:
                print("ID khong hop le!")
                continue

            found = False

            for employee in list_employees:
                if employee["id"] == delete_id:
                    list_employees.remove(employee)
                    print(f"Da xoa nhan vien ID {delete_id} thanh cong!")
                    found = True
                    break

            if not found:
                print("Khong tim thay nhan vien de xoa!")

        case 5:
            print("Da thoat chuong trinh!")
            break

        case _:
            print("Lua chon khong hop le!")



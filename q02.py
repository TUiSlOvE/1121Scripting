employee_list = []

while True:
    eName = input("請輸入姓名: ")
    if not eName:
        break
    eSalary = float(input("請輸入薪資: "))
    employee = {"eName": eName, "eSalary": eSalary}
    employee_list.append(employee)

total_salary = sum(employee["eSalary"] for employee in employee_list)
average_salary = total_salary / len(employee_list) if len(employee_list) > 0 else 0

print("----------------------------")
print("員工薪資輸入")
print("若姓名處未輸入則代表結束")
print("----------------------------")

for employee in employee_list:
    print(f"員工{employee['eName']} 的薪資為 {employee['eSalary']:>13,.2f}")

print("----------------------------")
print(f"合計薪資：{total_salary:>18,.2f}")
print(f"平均薪資：{average_salary:>18,.2f}")
print("============================")

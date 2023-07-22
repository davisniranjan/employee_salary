import tkinter as tk

class Employee:
    def __init__(self, emp_id, name, basic_salary, allowances, deductions):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary
        self.allowances = allowances
        self.deductions = deductions

    def calculate_net_salary(self):
        total_allowances = sum(self.allowances.values())
        total_deductions = sum(self.deductions.values())
        net_salary = self.basic_salary + total_allowances - total_deductions
        return net_salary

def calculate_salary():
    emp_id = int(emp_id_entry.get())
    name = name_entry.get()
    basic_salary = float(basic_salary_entry.get())

    allowances = {
        "HRA": float(hra_entry.get()),
        "TA": float(ta_entry.get())
    }

    deductions = {
        "PF": float(pf_entry.get()),
        "Tax": float(tax_entry.get())
    }

    emp = Employee(emp_id, name, basic_salary, allowances, deductions)
    net_salary = emp.calculate_net_salary()
    net_salary_label.config(text=f"Net Salary: {net_salary}")

# Create GUI
root = tk.Tk()
root.title("Employee Salary Distribution Management Calculator")

# Employee Details
emp_id_label = tk.Label(root, text="Employee ID:")
emp_id_label.grid(row=0, column=0)
emp_id_entry = tk.Entry(root)
emp_id_entry.grid(row=0, column=1)

name_label = tk.Label(root, text="Name:")
name_label.grid(row=1, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=1, column=1)

basic_salary_label = tk.Label(root, text="Basic Salary:")
basic_salary_label.grid(row=2, column=0)
basic_salary_entry = tk.Entry(root)
basic_salary_entry.grid(row=2, column=1)

# Allowances
hra_label = tk.Label(root, text="HRA:")
hra_label.grid(row=3, column=0)
hra_entry = tk.Entry(root)
hra_entry.grid(row=3, column=1)

ta_label = tk.Label(root, text="TA:")
ta_label.grid(row=4, column=0)
ta_entry = tk.Entry(root)
ta_entry.grid(row=4, column=1)

# Deductions
pf_label = tk.Label(root, text="PF:")
pf_label.grid(row=5, column=0)
pf_entry = tk.Entry(root)
pf_entry.grid(row=5, column=1)

tax_label = tk.Label(root, text="Tax:")
tax_label.grid(row=6, column=0)
tax_entry = tk.Entry(root)
tax_entry.grid(row=6, column=1)

calculate_button = tk.Button(root, text="Calculate Net Salary", command=calculate_salary)
calculate_button.grid(row=7, columnspan=2)

net_salary_label = tk.Label(root, text="")
net_salary_label.grid(row=8, columnspan=2)

root.mainloop()

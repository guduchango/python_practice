import report

# generar reportes de ventas y gastos usando funciones del modulo
sales_report = report.generate_sales_report('Octubre',1000)
expense_report = report.generate_expenses_report('Octubre',5000)


print(sales_report)
print(expense_report)


import statistics
import csv

# leer los datos de ventas mensuales desde un archivo csv

monthly_sales = {}
with open('monthly_sales.csv', mode="r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        month = row['month']
        sales = int(row['sales'])
        monthly_sales[month] = sales

sales = list(monthly_sales.values())
print(sales)

#hallar la media
mean_sales = statistics.mean(sales)
print(f"La media es: {mean_sales}")

# hallar la mediana
median_sales = statistics.median(sales)
print(f"La mediana es: {median_sales}")

#hallar la moda
mode_sales = statistics.mode(sales)
print(f"La moda es: {mode_sales}")

#hallar la desviación standar
stdev_sales = statistics.stdev(sales)
print(f"La desviación standar es: {stdev_sales}")

#hallar la desviación standar
variance_sales = statistics.variance(sales)
print(f"La vaiansa es: {stdev_sales}")

max_sales = max(sales)
min_sales = min(sales)

range_sales = max_sales - min_sales
print(f"rango de ventas: {range_sales}")
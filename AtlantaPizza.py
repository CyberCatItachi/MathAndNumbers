num_pizzas = int(input("Сколько пицц вы хотели бы? ")) #количество пицц
cost_per_pizza = int(input("Сколько стоит пицца? "))   #стоимость за пиццу
subtotal = num_pizzas * cost_per_pizza   #подытог
tax_rate = 0.08   #величина налога
sales_tax = subtotal * tax_rate  #сумма налога
total = subtotal + sales_tax   #итог
print("Подытог: ", subtotal)   
print("НДС: ", sales_tax)   
print("Итог: ", total)
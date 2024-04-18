no_orders_text = "0 orders"
no_orders_text_list = no_orders_text.split(" ")
print(no_orders_text_list[0])
count = no_orders_text_list[0]
if int(count) == 0:
    print("zero")
else:
    print("more than 0")
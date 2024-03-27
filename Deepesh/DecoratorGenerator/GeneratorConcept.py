def greeting():
    return "Good Morning"
    return "How are you"

val = greeting()
print(val)

def greeting_gen():
    yield "Good Morning"
    yield "How are you?"
    yield "Hope you are Enjoying leaning"
    yield "See you tomorrow"

gen_obj = greeting_gen()
print(gen_obj)
# print(next(gen_obj))
# print(next(gen_obj))
# print(next(gen_obj))
# print(next(gen_obj))
# print(next(gen_obj))

for data in gen_obj:
    print(data)

list1 = [5, 7, 8, 2, 8, 3]
log_list = list1*25
def get_square(n):
    yield n**2

for val in log_list:
    print(next(get_square(val)))

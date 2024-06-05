def do_twice(f):
    f()
    f()

def print_spam():
    print("spam")



do_twice(print_spam)

print("-------------------------------------")


def do_twice(f,n):
    f(n)
    f(n)

def print_twice(bruce):
    print(bruce)
    print(bruce)

do_twice(print_twice,"spam")


print("-------------------------------------")

def do_four(f,n):
    do_twice(f,n)
    do_twice(f,n)


do_four(print_twice, "spam")
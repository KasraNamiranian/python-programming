def right_justify1(s):
    lengths=len(s)
    lengths=70 - lengths
    for i in range (lengths):
        print(" " , end="")
    print(s)
right_justify1("salam")
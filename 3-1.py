def right_justify(s):
    lengths=len(s)
    lengths=70-lengths
    print(lengths)
    print(' '*lengths + s)

right_justify('salam')
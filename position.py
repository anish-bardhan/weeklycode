def pos_average(s):
    arr = list(s)
    matrix = []
    new_arr = []
    for x in arr:
        if x != " " and x != ",":
          new_arr.append(x)
    print(new_arr)
    for x in range(len(new_arr)/6):
        

pos_average("466960, 069060, 494940, 060069, 060090, 640009, 496464, 606900, 004000, 944096")

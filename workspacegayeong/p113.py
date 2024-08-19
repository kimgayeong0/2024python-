def P(space, space_num, *args):
    str =args[0]
    for i in range(1, len(args)):
        str =str + (space*space_num)+args[i]
    print(str)
P(",",3,"o","p","q")

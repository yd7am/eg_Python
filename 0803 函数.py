# try 8-9
magicians = ['abc', 'def', 'ghi']
def show_magicians(magicians):
    for magician in magicians:
        print(magician)

show_magicians(magicians)

# 8-10
def make_great(magicians):
    for index in range(len(magicians)):
        magicians[index] = "The Great " + magicians[index]
    return magicians

gm = make_great(magicians[:])
show_magicians(magicians)
show_magicians(gm)

# 8.5 传递任何数量的实参
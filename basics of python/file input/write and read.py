"""
    Modes:-
        1 => 'r' =>  reading mode  => by defualt
        2 => 'w' =>  writing mode  => over write problum
        3 => 'x' => create file if not present
        4 => 'a' => append mode  => not overwrite the content
    file:-
        "t" => text mode
        "b" => binary mode
        "+" => read and write both
"""

# writing in file

# ptr = open("abcd.txt", "w")
# data = ptr.write("Hi my self dhaval \n 2 hello world")
# print(data)
# ptr.close()

# reading in file

# p = open("abcd.txt")
# print(p.read(10))   # 10 charctor print
# print(p.readline())
# print(p.readlines())  # list form content read
# for line in p:
#     print(line,end="")
# p.close()


# with open
with open("abcd.txt") as f:
    print(f.read())

string = ""


def add_hello():
    global string
    string = string + "Hello"


def add_space():
    global string
    string = string + " "


def add_world():
    global string
    string = string + "World"


add_hello()
add_space()
add_world()

print(string)

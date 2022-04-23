# Global variables
x = 5
y = 10

# Function Definition
def add():
    # Local variables
    # x = 12
    # y = 11
    z = x + y
    print("Sum is",z)

def sub():
    # Local Variables
    # x = 10
    # y = 5

    global x, y
    x = 20
    y = 15
    z = x - y
    print("Sub is",z)

# Function calling
add()
sub()
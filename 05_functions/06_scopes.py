# def serve_chai():
#     chai_type = "Masala" # local scope
#     print(f"Inside function {chai_type}")


# chai_type = "lemon"
# serve_chai()

# print(f"Outside function: {chai_type}")


def chai_counter():
    chai_order = "lemon"  # Enclosing scope
    def print_order():
        chai_order = "Ginger"
        print(f"Inner: {chai_order}")
    print_order()
    print(f"Outer: {chai_order}")
chai_counter()


# chai_order = "Tulsi" # Global Scope
# chai_counter()

# print(f"Global : {chai_order}")


# def fun1():
#     print("This is function 1")
#     def fun2():
#         print("This is function 2")
#     fun2()

# fun1()
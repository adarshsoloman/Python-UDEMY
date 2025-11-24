chai_type = "ginger"

def update_order():
    chai_type = "Elaichi"
    def kitchen():
        # nonlocal  chai_type 
        chai_type = "kesar"
    kitchen()
    print(f'After kitchen update {chai_type}')

update_order()
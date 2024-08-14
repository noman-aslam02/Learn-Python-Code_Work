class MyClass:
    def __init__(self, f_name, l_name):
        self.f_name = f_name
        self.l_name = l_name
        self.email = self.f_name + self.l_name + "@gmail.com"

    def email_1(self):
        return self.email

my_inst = MyClass("noman", "aslam")

# main guard syntax
if __name__ == "__main__":  # yeh ab kssi aur script may apni script ko run nhi hone deghi
    print(my_inst.email_1())
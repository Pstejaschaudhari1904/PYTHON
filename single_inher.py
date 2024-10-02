class Demo:
    n=10
    def disp(self):
        print("Helloooo")
class test(Demo):
    def show(self):
        print("asdsjisgdfjhip")

#create the object
d=test()
print("value of n",d.n)
print(d.disp())
print(d.show())
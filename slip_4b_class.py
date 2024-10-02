''' Define a class Employee having members id, name, department, salary. Create a 
subclass called manager with member bonus. Define methods accept and display in both the 
classes. Create n objects of the manager class and display the details of the manager having 
the maximum total salary'''

        #5a    8b
#create the class for employee

class Employee:
    def AcceptEmp(self):
        self.Id=int(input("Enter emp id:"))
        self.Dept=input("Enter emp Dept:")
        self.Name=input("Enter emp name:")
        self.Sal=int(input("Enter emp Salary:"))
    def DisplayEmp(self):
        print("Emp id:",self.Id)
        print("Emp Name:",self.Name)
        print("Emp Dept:",self.Dept)
        print("Emp Salary:",self.Sal)
class Manager(Employee):
    def AcceptMgr(self):
        self.bonus=int(input("Enter Manager Bonus"))
    def DisplayMgr(self):
        print("Manger Bonus is:",self.bonus)
        self.TotalSal=self.Sal+self.bonus
        print("Total Salary: ", self.TotalSal)
    n=int(input("Enter How may Managers:"))
    lst=[]
    for i in range(0,n):
        obj=input("Enter Object Name:")
    lst.append(obj)
    print(lst)
    for j in range(0,n):
        lst[j]=Manager()
        lst[j].AcceptEmp()
        lst[j].AcceptMgr()
        print("\nDisplay Details of Manager",j+1)
        lst[j].DisplayEmp()
        lst[j].DisplayMgr()

#maximum logic
maxTotalSal= lst[0].TotalSal
maxIndex=0
for j in range(1,n):
    if lst[j].TotalSal > maxTotalSal:
            maxTotalSal= lst[j].TotalSal
            maxIndex=j
print("\nDisplay Details of Manager Having Maximum Salary(Salary+Bonus)")
lst[maxIndex].DisplayEmp()
lst[maxIndex].DisplayMgr()

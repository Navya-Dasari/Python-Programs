class Employee:
    def getdata(self, eno, ename, designation, basic, hra, da, ta):
        self.eno = eno
        self.ename = ename
        self.designation = designation
        self.basic = basic
        self.hra = hra
        self.da = da
        self.ta = ta

    def putdata(self):
        print("Emp No:", self.eno)
        print("Emp Name:", self.ename)
        print("Designation:", self.designation)
        print("Basic:", self.basic)
        print("HRA:", self.hra)
        print("DA:", self.da)
        print("TA:", self.ta)
        netsalary = self.basic + self.hra + self.da + self.ta
        print("Net Salary:", netsalary)
        if netsalary > 50000:
            return 0.05 * netsalary
        elif netsalary > 35000:
            return 0.03 * netsalary
        elif netsalary > 20000:
            return 0.01 * netsalary
        else:
            return 0
emp = Employee()
eno=int(input("Enter emp no:"))
ename=input("Enter emp name:")
designation=input("Enter designation:")
basic=int(input("Enter basic:"))
hra=int(input("Enter HRA:"))
da=int(input("Enter DA:"))
ta=int(input("Enter TA:"))
emp.getdata(eno, ename, designation, basic, hra, da, ta)
emp.putdata()

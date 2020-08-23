class Employee:
   empCount = 0;

   def __init__(self, name, salary):
      self.name = name;
      self.salary = salary;
      Employee.empCount += 1;
	  
   def displayCount(self):
     print "\nTotal Employee %d", Employee.empCount;

   def displayEmployee(self):
      print "\nName: ", self.name,  ",Salary: ", self.salary;

emp1 = Employee("ABC", 2000);
emp2 = Employee("XYZ", 5000);
emp1.displayEmployee();
emp2.displayEmployee();
print ("\nTotal Employee: "+Employee.empCount);

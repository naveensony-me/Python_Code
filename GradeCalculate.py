class GradeCalculator:
    
    def __init__(self,name):
        self.name=name
        self.marks=[]
    def grades(self):
        
            print("Enter the marks of  5 subjects\n")
            for i in range(0,5):
                self.marks.append(int(input()))
                if self.marks[-1] > 100:
                    raise ValueError("The number should not be greater than 100")
                    
    def calculate(self):
        sum = 0
       
        for i in range(0,5):
            
            sum += self.marks[i]
        avg = sum/5
        if avg >= 90 and avg <= 100:
            print("Merit")
        elif avg >=60 and avg <=89:
            print("1st Division")
        elif avg >=50 and avg<=59:
            print("Second Division")
        elif avg >=33 and avg <=49:
            print("Third Division")
        else:
            print("Fail")
    def display(self):
        print("****REPORT CARD****")
        print("Name: ",self.name)
        for i in range(0,5):
            print("Subject ",i+1,": ",self.marks[i])
        print("Total Marks: ",sum(self.marks))
if __name__ == "__main__":
    obj = GradeCalculator("Naveen")
    obj.grades()
    obj.display()
    obj.calculate()
    
                                # OUTPUT :- According User Input
    
# Enter the marks of  5 subjects

# 98
# 68
# 75
# 83
# 86
# ****REPORT CARD****
# Name:  Naveen
# Subject  1 :  98
# Subject  2 :  68
# Subject  3 :  75
# Subject  4 :  83
# Subject  5 :  86
# Total Marks:  410
# 1st Division

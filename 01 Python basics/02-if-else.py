class result:
    def grade(self,marks):
     
        
        if marks>=90:
            print("Grade A\n")
        elif marks>=70:
            print("Grade B\n")
        elif marks>=50:
            print("Grade C\n")
        elif marks>=35:
            print("Pass\n")
        else:
            print("Fail\n")
obj=result()
obj.grade(95)

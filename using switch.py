class week:
    def day(self,d):
        match d:
            case 1:
                print("monday\n")
            case 2:
                print("tuesday\n")
            case 3:
                print("wednesday\n")
            case 4:
                print("thursday\n")
            case 5:
                print("friday\n")
            case 6:
                print("saturday\n")
            case 7:
                print("sunday\n")
            case _:
                print("invalid\n")


obj=week()
obj.day(2)
            

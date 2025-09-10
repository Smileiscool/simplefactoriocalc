def main():
    print("You need", FindAssemPerSec(),"assemblers.")
    main()

def setReqItemsPerSec():
    ReqItemsPerSec = float(0)
    while True:
        try:
            Choice = float(input("Choose wanted Items Per second: "))
            ReqItemsPerSec = Choice
            return ReqItemsPerSec
        except:
            print("Invalid choice.")

def setCraftSpeed():
    AssemCraftSpeed = float(0)
    while True:
        try:
            Choice = int(input("Choose assembler 1, 2, or 3: "))
            if Choice == 1:
                AssemCraftSpeed = .5
                return AssemCraftSpeed
            elif Choice == 2:
                AssemCraftSpeed = .75
                return AssemCraftSpeed
            elif Choice == 3:
                AssemCraftSpeed = 1.25
                return AssemCraftSpeed
            else:
                print("Invalid choice.")
        except:
            print("Invalid choice.")

def setCraftTime():
    ItemCraftTime = float(0)
    while True:
        try:
            Choice = float(input("How long to craft item in seconds (ex. 1 or .5): "))
            ItemCraftTime = Choice
            return ItemCraftTime
        except:
            print("Invalid choice.")

def FindAssemPerSec():
    AssemPerSec = float(0)
    RealCraftTime = float(0)
    ItemsPerSec = float(0)

    RealCraftTime = setCraftTime() / setCraftSpeed()
    ItemsPerSec = 1 / RealCraftTime
    AssemPerSec = setReqItemsPerSec() / ItemsPerSec
    return AssemPerSec

main()
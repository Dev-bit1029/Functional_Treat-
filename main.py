# NOTE :- Summary Function Error  (2D Arrey )

print("Welcome To The Data Analyzer And Transformer Program ")

data = []

def input_Data():
    """1D Arrey and 2D Arrey """
    global data 
    
    print("select option ")
    print("1. 1D Arrey ")
    print("2. 2D Arrey ")
    
    num = input("Enter The Number (1 Or 2 )")
    if num == "1":
        num = input("Enter The Number (SepArated By Spaces :- )\n")
        data = list(map(int,num.split()))
        print ("Data Has Been Store  Successfully !")
    elif num == "2":
        row = int(input("Enter The Number Of Rows :- "))
        column = int(input("Enter The Number Of column :- "))
        
        data = []
        
        for r in range(row):
            r=[]
            for c in range(column):
                num = int(input("Enter A Number :- "))
                r.append(num)
            data.extend(r)
            
        print("2D Arrey Are Store !")
        
        
    
def Summary():
    
    """Summary Of Data (1D and 2D)"""
    
    print("1. 1D Arrey ")
    print("2. 2D Arrey ")
    
    num = input("Enter The Number (1 Or 2 )")
    

    if num == "1" :

        print("\nData Summary")
        print(f"- Total Element :- {len(data)}")
        print(f"- Minimum Value :- {min(data)}")
        print(f"- Maximum Value :- {max(data)}")
        print(f"- Sum Of All Element :- {sum(data)}")
        print(f"- Average Value :- {sum(data) / len(data)}")

    elif num == "2" :
       


        print(f"- Total Element :- {len(data)}")
        print(f"- Minimum data :- {min(data)}")
        print(f"- Maximum data :- {max(data)}")
        print(f"- Sum Of All Element :- {sum(data)}")
        print(f"- Average data :- {sum(data) / len(data)}")



        
def fact(n):
    """Calculate the factorial of a number using recursion."""
    if n<=0:
        return 1
    return n*fact(n-1)
    
    
def Factorial():
    """Calculate the factorial of a number using recursion."""
    num = int(input("Enter A Number To Calculate Factorial :-  "))
    print(f"Factorial of {num} is {fact(num)}")
    return num


def threshold(data):
    """Filter data based on a threshold value."""
    
    dataa = int(input("Enter A Threshold Value To Filter Out Data About THis Value\n "))
    print(f"Filtered Data (Values >= {dataa}):\t")
    dataa = list(filter(lambda x : x > dataa , data ))
    print(dataa)

def sort(data):
    """Sort data in ascending or descending order."""
    print("Choose Sorting option :- ")
    print("1. Accending Order ")
    print("2. Descending Order ")
    
    choose = int(input("Enter Your Choose (1-2) :- "))
    
    if choose == 1:
        accending= sorted(data)
        print(accending)
    elif choose == 2 :
        descending = sorted(data, reverse=True)
        print(descending)        
    
def data_statistics(data):
    """Calculate and return statistics of the data."""
    minimun = min(data)
    maximun = max(data)
    total = sum(data)
    average = total/len(data)
    return minimun,maximun,total,average

def statistics():
    """Display statistics of the data."""
    if len(data) == 0:
        print("No Data Store")
        return 
    minimun,maximun,total,average = data_statistics(data)
    print(f"- Minimun Value {minimun}")
    print(f"- Maximun Value {maximun}")
    print(f"- Sum Of All Value {total}")
    print(f"- Average  Value {average}")

    
while True:
    print(" Main Menu ")
    print("1. Input Data ")
    print("2. Display Data Summary ")
    print("3. Calculate Factorial (Recursion)")
    print("4. Filter Data By Threshold ")
    print("5. Sort Data ")
    print("6. Display Dataset Statistics (Retune Matliple Value )")
    print("7. Exit Program ")
    
    
    choice = int(input("Please Enter Your Choice :- "))
    
    if choice == 1 :
        print(input_data.__doc__)
        input_Data()
    elif choice == 2 :
        print(summary().__doc__)
        Summary()
    elif choice == 3 :
        print(factorial().__doc__)
        Factorial()
    elif choice == 4:
        print(threshold().__doc__)
        threshold(data)
    elif choice == 5 :
        print(sort().__doc__)
        sort(data)
    elif choice == 6:
        print(statistics().__doc__)
        statistics()
    elif choice == 7 :
        print("Thank You For Using Data Analyzer And Transformer Program ")
        break
    else:
        print("Invaild Choice (1-7)")

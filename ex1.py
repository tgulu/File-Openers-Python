import sys


list_file_open = False


while list_file_open == False:  

    filename = input("Enter filename: ")
    fileOpen = filename + ".txt"

    try:
        raw_list= open(fileOpen)
        list_file_open = True
                
    except IOError:
        print('The file could not be opened.')
        continue
    
list_file = []


#Adds the lines into a list a splits the strings
for i in raw_list:
    list_file.append(i.split())



    
try :
    fIn = open(fileOpen, "r")
    fopen = True
    line = fIn.readline()
    while len(line)>0:
        #dataBase.append(worker(line[:-1]))
        line = fIn.readline()
    #myLine = fIn.readline()
    #while (len(myLine)>0) :
        
        #print(myLine[:-1])
        #myLine = fIn.readline()
    #print ("File fully opened")
    

except IOError as e :
    fIn = False
    fopen = False
    print("There was a problem opening the file:",fileOpen,", program terminated.")
status = True

def worker():
    workerIDlist = list()
    #the fuctions that work out the positions of the info from the file
    fIn.seek(0,0)
    for line in fIn:
        details = line
        details2 = details.split(" ", 3)
        details = details.split()
        
        workerID = format(details2[0], "<5s")
        workerIDlist.insert(0,workerID)
        
        payroll = format(details2[1], "<6s")
        payrolls = format("£" + details2[1], "<6s")
        job = format(details2[2], "<15s")
        names = details[3:-1]
        split = ""
        surname= details[-1]
        fname = format(details[4], " <5s")

        for j in range(len(names)):
            split = split + " " +names[j]
        fullname = format((surname +" ," + split), "<30s")
        print (fullname, workerID, job, payrolls)
        



if fopen:
    worker()

#question = input("Do you want to find out information about employee? answer (yes) or (no)")
#while question == "yes":
    print("\nTo find out full details, please choose numbers 1,2,3:")
    print("1. Search by payroll number")
    print("2. Search by salary range")
    print("3. Search by job title")
    print("4. Exit program")
   
loop = True

# Goes through the 4 processes
while loop == True:
    opt = str(input("\nPlease Enter An Option :"))
    found = False
    if opt == '1':
        payroll = str(input("Enter payroll number :"))
        for i in list_file:            
            if i[0] == payroll:
                found = True
                print(i)
        if found == False:
            print("Payroll number could not be found")        
    elif opt == '2':
        salMax = int(input(" Enter Salary Maximum : "))
        salMin = int(input(" Enter Salary Minimum : "))
        for i in list_file:
            if int(i[1]) >= salMin and int(i[1]) <= salMax:
                found = True
                print(i)
        if found == False:
            print("Salary cant be found")
    elif opt == '3':
        jobTitle = str(input("Enter Job title :"))
        for i in list_file:            
            if i[2] == jobTitle:
                found = True
                print(i)
        if found == False:
            print("job Title can not be found")
    elif opt == '4':
        print("File Closing")
        break
            
            
        
    
              

        


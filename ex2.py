list_file_open = False


while list_file_open == False:  

    list_get_file =input(str("Please enter a filename for word search: "))
    list_user_file = list_get_file + ".txt"

    try:
        list_file = open(list_user_file)
        list_file_open = True
                
    except IOError:
        print('The file could not be opened.')
        continue

with open(list_user_file) as f:    
    list_content = f.read().splitlines()
    

print ("\n".join(list_content))
#####
#Flips the list
flipped_list = []
for n in range (len(list_content[0])):
    letters = ""
    for i in list_content:
        letters += i[n]

    flipped_list.append(letters)
for i in flipped_list:
    print(i)
#####



# Open file with the words
search_file_open = False


while search_file_open == False:  

    search_get_file =input(str("Please enter a filename for words to be searched: "))
    search_user_file = search_get_file + ".txt"

    try:
        search_file = open(search_user_file)
        search_file_open = True
                
    except IOError:
        print('The file could not be opened.')
        continue

with open(search_user_file) as f:
    search_content = f.read().splitlines()
    search_content = sorted(search_content)




def horz(user_word ,user_list):
    # This is for the column 
    y = 0
    
    confirm = False
    # For reversing the string
    reverse_string = "".join(reversed(user_word))
    # Loop Through the list
    for i in user_list:
        # Find the word in the list
        if user_word in user_list[y]:            
            x = user_list[y].index(user_word) + 1
            #Tuple of how far along it is in the row and how far up and down
            #print("the word was found in, row, column ")
            found = (x,y+1)            
            confirm = True
            #adds it to the file
            print(user_word + " found at (row,columm)" + str(found))
            file = open('dicts.txt', "a")
            file.write(user_word + str(found)+"\n")
            return found
            break
       
        elif reverse_string in user_list[y]:
            # checks to see if its a reversed word instead            
            x = user_list[y].index(reverse_string) + 1
            found = (x,y+1)            
            
            confirm = True
            file = open('dicts.txt', "a")
            file.write(user_word + str(found)+ " \n")
            return found
            break             
        y += 1
    if confirm == False: 
                
        return


def vert(user_word,user_list):
    # This is for the column 
    y = 0
    
    confirm = False
    # For reversing the string
    reverse_string = "".join(reversed(user_word))
    # Loop Through the list
    for i in user_list:
        # Find the word in the list
        if user_word in user_list[y]:            
            x = user_list[y].index(user_word) + 1
            #Tuple of how far along it is in the row and how far up and down
            #print("the word was found in, column, row ")
            found = (y+1,x)            
            confirm = True
            #adds it to the file
            print(user_word + " found at (row,columm)" + str(found) )
            file = open('dicts.txt', "a")
            file.write(user_word + str(found)+"\n")
            
            return found
            break
       
        elif reverse_string in user_list[y]:
            # checks to see if its a reversed word instead            
            x = user_list[y].index(reverse_string) + 1
            found = (y+1,x)            
            print(user_word + " found at (row,columm)" + str(found) )
            confirm = True
            file = open('dicts.txt', "a")
            file.write(user_word + str(found)+ " \n")
            return found
            break             
        y += 1
    if confirm == False: 
                
        return
#searches for words and sees if they can be found
j =0
not_found_list = []
found_list = []
not_found_list_final = []
for i in search_content:
    output= horz(search_content[j],list_content)
    if output != None:
        found_list.append(search_content[j])    
    output= vert(search_content[j],flipped_list)
    if output != None:
        found_list.append(search_content[j])

    if output == None:
        not_found_list.append(search_content[j]) 
  
    
        
    j += 1


for word in list(not_found_list):
    if word in found_list:
        not_found_list.remove(word)
        
for i in not_found_list:
  if i not in not_found_list_final:
    not_found_list_final.append(i)

print("\n Words Not found:")
for i in not_found_list_final:
    print(i)




#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

f= open("./Input/Letters/starting_letter.txt")
list_1 = f.read()


g= open("./Input/Names/invited_names.txt")
list_2 = g.readlines()

for items in list_2:
    #print(items)
    stripped_name= items.strip()
    x= list_1.replace("[name]",stripped_name)
    print(x)
    with open(f"./Output/ReadyToSend/letter_to_{stripped_name}.txt", mode = "w") as f2:

        f2.write(x)


#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

m_name = []

with open('Mail Merge Project Start/Input/Names/invited_names.txt',mode='r') as name_file:
    for item in name_file.read().split():
        m_name.append(item)

with open('Mail Merge Project Start/Input/Letters/starting_letter.txt',mode= "r") as text_file:
    list_of_line = text_file.readlines()
for item in m_name:
    file = open(f'Mail Merge Project Start/Output/ReadyToSend/{item}.txt',mode="w")
    for text in list_of_line:
        file.writelines(text.replace('[name]', item))
    file.close()
# print(m_name[0])
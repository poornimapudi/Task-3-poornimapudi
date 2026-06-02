'''
** PROJECT : RANDOM PASSWORD GENERATOR **
=> Using a "random" module for randomization.
=> using "string" module for manupulation of strings.
=> Generating multiple random passwords of length required by the user.
=> And also randomization excluding user choices.
=> At last writing those generate random passwords into a text file..

'''

#Importing 'random' and 'string' modules
import random
import string

Letters = string.ascii_letters    #Includes all the uppercase and lowercase letters     
Numbers = string.digits           #Includes all the digits from '0'to '9'.
Special_characters = string.punctuation #Includes all the special characters

#Stores all the letters , numbers and Special characters.
Total_Characters = Letters + Numbers + Special_characters
#Stores all the characters excluding letters.
Total_characters_exc_letters = Numbers + Special_characters
#Stores all the characters excluding numbers.
Total_characters_exc_numbers = Letters + Special_characters
#Stores all the characters excluding special characters.
Total_characters_exc_Spec_characters = Letters + Numbers
print("Select the choice which you want to exclude..","1.Letters","2.Numbers",
      "3.Special Characters","4.Don't want to exclude",sep="\n")
#Asking the user to enter their choice of preference.
Choice = input("Enter the choice you want:")
if Choice == "1": #If user wants to exclude letters.
    file = open("passwords.txt","w")
    No_of_passwords = int(input("Enter the number of passwords you want to generate:"))
    Length_of_password = int(input("Enter the length of password:"))
    for i in range(No_of_passwords):
        password = ""
        for j in range(Length_of_password):
            password += random.choice(Total_characters_exc_letters)
        file.write(f'password {i+1} = {password} \n')
    print("passwords are written to a file successfully")
    file.close()

elif Choice == "2":  #If user wants to exclude Numbers.
    file = open("passwords.txt" , "w")
    No_of_passwords = int(input("Enter the number of passwords you want to generate:"))
    Length_of_password = int(input("Enter the length of password:"))
    for i in range(No_of_passwords):
        password = ""
        for j in range(Length_of_password):
            password += random.choice(Total_characters_exc_numbers)
        file.write(f'password {i+1} = {password} \n')
    print("Passwords are written into a file successfully")
    file.close()

elif Choice == "3": #If user wants to exclude Special Characters
    file = open("passwords.txt" , "w")
    No_of_passwords = int(input("Enter the number of passwords you want to generate:"))
    Length_of_password = int(input("Enter the length of password:"))
    for i in range(No_of_passwords):
        password = ""
        for j in range(Length_of_password):
            password += random.choice(Total_characters_exc_Spec_characters)
        file.write(f'password {i+1} = {password} \n')
    print("Passwords are written into a file successfully")
    file.close()

elif Choice == "4": #If user doesn't wants to exclude any character.
    file = open("passwords.txt" , "w")
    No_of_passwords = int(input("Enter the number of passwords you want to generate:"))
    Length_of_password = int(input("Enter the length of password:"))
    for i in range(No_of_passwords):
        password = ""
        for j in range(Length_of_password):
            password += random.choice(Total_Characters)
        file.write(f'password {i+1} = {password} \n')
    print("Passwords are written into a file successfully")
    file.close()

else:
    print("Select the correct choice")






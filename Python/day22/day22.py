##1.Write a python script to read the text file content and
##print the output in form of line wise total words in the file. 
##filename = 'demo.txt'  
##file = open(filename, 'r')
##line_number = 1
##word_counts = []
##for line in file:

##    words = line.split()
##    word_count = len(words)
##    word_counts.append((line_number, word_count))
##    line_number += 1
##file.close()
##print(word_counts)

#2.Open a text file using with statement
#and write and read the content from that file.

##with open("demo.txt","r") as file:
##    for line in file:
##        print(line.strip())

##3.Take the user input for data to be written in the text file.
##Enter the data line by line,till ‘@’ character
##is entered by the user at the end.

# Open a text file in write mode
filename = 'user_input.txt'  # You can change the file name as needed

# Open the file for writing
file = open(filename, 'w')

print("Enter your data line by line. Type '@' to end.")


while True:
    user_input = input("Enter line: ")
    
    
    if user_input == '@':
        break
    
    
    file.write(user_input + '\n')


file.close()

print(f"Data has been written to {filename}.")




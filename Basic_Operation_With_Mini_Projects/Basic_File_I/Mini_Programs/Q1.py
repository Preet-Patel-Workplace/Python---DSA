##Create a new file "practice.txt" using python. Add the following data in it:
# Hi everyone
# we are learning File I/O
# using Java.
# I like programming in Java.
# WAF that replace all occurrences of "java" with "python" in above file.
# Search if the word "learning" exists in the file or not.

#Q1
with open("practise.txt" , 'w') as f:
    f.write("Hi everyone \nwe are learning File I/O  \nusing Java. \nI like programming in Java.")

#Q2
with open("Basic_Operation_With_Mini_Projects\Basic_File_I\Mini_Programs\practise.txt" , 'r') as f:
    data = f.read()

new_data = data.replace("Java" , "Python")


with open("Basic_Operation_With_Mini_Projects\Basic_File_I\Mini_Programs\practise.txt" , 'w') as f:
    f.write(new_data)

#Q3
with open("Basic_Operation_With_Mini_Projects\Basic_File_I\Mini_Programs\practise.txt" , "r") as f:
    data = f.read()
    if(data.find("learning") != -1 ):
        print("Found")





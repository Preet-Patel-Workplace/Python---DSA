#Basic of Input/Output of files


from ast import With


f = open("Basic_Operation_With_Mini_Projects\Basic_File_I\import.txt" , "r")

data = f.read()

print(data)
print(type(data)) 


#ReadLine

line1 = f.readline()
print(line1)

line2 = f.readline()
print(line2)


#Writing

file = open("Basic_Operation_With_Mini_Projects\Basic_File_I\Writen.txt" , "w")

file.write("I am Preet Patel")


file = open("Basic_Operation_With_Mini_Projects\Basic_File_I\Writen.txt" , "a")

file.write("\n I am Learning python")

 
#WITH Syntax

with open("Basic_Operation_With_Mini_Projects\Basic_File_I\import.txt" , "r") as f:
    data = f.read()
    print(data)

with open("Basic_Operation_With_Mini_Projects\Basic_File_I\Writen.txt" , "w") as w:
    w.write('Input/Output')
 
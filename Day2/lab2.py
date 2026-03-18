# ========================================
#                   Task1
# ========================================
def remove_vowels(string):
    vowels = "aeiouAEIOU"
    result = ""
    for char in string:
        if char not in vowels:
            result+=char
    return result

print(remove_vowels("Hello World"))

def replace_Fn(list):
    list_new = []
    for string in list:
        list_new.append(remove_vowels(string))
    return list_new

print(replace_Fn(["Hello World", "Python", "Programming"]))

# ========================================
#                   Task2
# ========================================
def findIndex(string,char):
    list_index = []
    for i in range(len(string)):
        if string[i]==char:
            list_index.append(i)
    return list_index

print(findIndex("Hello World", "l"))

# ========================================
#                   Task3
# ========================================
def multiplyTable(num):
    list_table = []
    for i in range(1,num+1):
        list_row = []
        for j in range(1,i+1):
            list_row.append(i*j)
        list_table.append(list_row)
    return list_table

print(multiplyTable(5))

# ========================================
#                   Task4
# ========================================
def calculateArea(char,num1,num2):
    if char == "c":
        return 3.14159 * num1 * num1
    elif char == "s":
        return num1 * num1
    elif char == "r":
        return num1 * num2
    elif char == "t":
        return 0.5 * num1 * num2
    else:
        return "Invalid shape"

print("The area is: ",calculateArea("c",5,0))

# ========================================
#                   Task5
# ========================================
def dictionaryList(list):
    list.sort()
    res = {}
    for i in list:
        if i[0] not in res:
            res[i[0]] = []
        res[i[0]].append(i)
    return res

print(dictionaryList(["fatma","ahmed","fathya" ,"ibrahim"]))

# ========================================
#                   Task6
# ========================================
def buildPyramid(num):
    for i in range(num):
        line = " " * (num - i) + "*" * (i + 1)
        print(line)

buildPyramid(5)            


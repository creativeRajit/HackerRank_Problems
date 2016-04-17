# Enter your code here. Read input from STDIN. Print output to STDOUT

# input from user
inp_str = raw_input()
list_str = list(inp_str)

# read every character and Swap case

count = 0
for character in list_str:
    if character.isupper():
        list_str[count] = character.lower()
    else:
        list_str[count] = character.upper()
    count += 1

    
# print
req_str = ''.join(list_str)
print req_str

# Enter your code here. Read input from STDIN. Print output to STDOUT

# input from user
inp_str = raw_input()

# split
inp_splitted = inp_str.split()


# change first character to Upper case

final_words = ""
for words in inp_splitted:
    first_letter = words[0]
    U = first_letter.upper()
    
    # convert to list and change
    words_list = list(words)
    words_list[0] = U
    words = ''.join(words_list)
    
    final_words = final_words + words + ' '


# print

print final_words

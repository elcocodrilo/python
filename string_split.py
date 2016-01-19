splitlist = ' ,!:.'
source = "The whole world! is here, today... Welcome."

def is_char(i, source, split_splitlist):
    for splitters in split_splitlist:
        if source[i] == splitters:
            return True
    return False

def split_string(source, splitlist):
    len_splitlist = len(splitlist)
    split_splitlist = []
    for i in splitlist:
        split_splitlist.append(i)

    splitter_list = [-1]

    for i in range(0, len(source)):
        if is_char(i, source, split_splitlist):
            splitter_list.append(i)

    if is_char((len(source) - 1), source, split_splitlist) == False:
        splitter_list.append(len(source))

    string_list = []

    for i in range(0, (len(splitter_list) - 1)):
        if splitter_list[i] + 1 != splitter_list[i + 1]:
            string = source[(splitter_list[i] + 1):splitter_list[i + 1]]
            string_list.append(string)

    return string_list

# print split_string(source, splitlist)

out = split_string("First Name,Last Name,Street Address,City,State,Zip Code",",")
print out

## as solved on udacity Lesson 4 problem set

def u_split_string(source, splitlist):
    output = [ ]
    atsplit = True #At a split point
    for char in source:
        if char in splitlist:
            atsplit = True
        else:
            if atsplit:
                output.append(char)
                atsplit = False
            else:
                # add character to last words
                # output[-1] finds the last character in the output list and we append the character
                output[-1] = output[-1] + char
    return output

out = u_split_string("First Name,Last Name,Street Address,City,State,Zip Code",",")
print out

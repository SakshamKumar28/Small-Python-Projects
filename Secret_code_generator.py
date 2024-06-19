import random as r
import string as s


def secret_code_converter(string):

    if len(string) <= 3:
        string = string[::-1]
        return string
    else:
        s1 = string[1::]
        #creating 3 random characters
        c1 = r.choice(s.ascii_letters)
        c2 = r.choice(s.ascii_letters)
        c3 = r.choice(s.ascii_letters)
        #creating list of these random characters
        list_of_random_characters = [c1, c2, c3]
        #shuffling list every time when new string is entered
        r.shuffle(list_of_random_characters)
        #creating list of new string (s1) and the first letter of main string
        list = [s1, string[0]]
        #creating a new list by adding created lists
        final_list = list_of_random_characters + list + list_of_random_characters
        return "".join(final_list)



#main program
#taking input
a = input("Enter String: ")
#using function
res = secret_code_converter(a)
print("String After Converting into code: ",res)

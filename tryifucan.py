"""That is a simple challenge , here the only thing that you are suposed to do its to discover the key
good luck ana , lets see how fast you understand it :)"""

simple_list = ["one", "two", "three", "four", "five"] # contains a list of strings
complex_list = list() #Opening a list , but leeting it empty

def my_func(x): # Def its the way that you say to python  that this part of  code its a function it means meaning u can
                # you can repeat it the much times you want
    for item in x : # You might know it by the name of FOR LOOPING
        item = str(item) # This is called Method i use it to transform from list on string again
        complex_list.append(item[:1]) # [:] Its used manipulate the list :)


my_func(simple_list) # Iam calling the function here , and it its returning something

def my_2func(y):
    str1 = "" # string without nothing
    for item in y:
        str1 += item
    fi = str1.encode().hex()
    show = input("Please input here the correct awnser to pass:")
    if show.encode().hex() == fi :
        print("Uhulllllllllllllllllllll you made it , great job ana ")
    else:
        print("Almost there , keep trying")

my_2func(complex_list)

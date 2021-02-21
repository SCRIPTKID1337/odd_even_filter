def single_filter (l):
    if l % 2 == 0:
        return ("\nthis is even number")
    else :
        return ("\nthis is odd number")

def multiple_filter (l):
    odd_list = []
    even_list = []
    for i in l:
        if i % 2 == 0:
            even_list.append(i)    
        else:
            odd_list.append(i)
    return (f"\nthis is odd numbers :- {odd_list}  \n\nthis is even numbers :- {even_list}")
           
 
print ("..........welcome to odd, even number filter.............")

while True:
    print("\n\nchose a option ...\n\n1. single number cheak \n2. multiple number cheak \n\n")
    t = int(input("type your option : "))
    if t == 1:
        s_n = int(input("\ntype your number for cheak "))
        print()
        print (single_filter(s_n))
        input("\npress enter to continue")
    else:
        f_n = int(input("type your first number : "))
        l_n = int(input("type your last number : "))
        t_n = range(f_n, l_n)
        print()
        print (multiple_filter(t_n))
        input("\npress enter to continue")











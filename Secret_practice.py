#Program to convert a message into secret code and to decode the secret code
m = input("Enter your message ")
l = m.split(" ")
print(l)
x = int(input("Enter your choice:"
              " 1.Encode"
              " 2.Decode  "))

def reverse(i):
    for letter in i:
        r =" " +i[1:] + i[0]
    return r


if(x==1):
    new_word = " "
    for i in l:
        if(len(i)>=3):

            r1="arb"
            r2="lkj"
            new_word +=" " +r1+ i[1:] + i[0] + r2
        else:
            new_word += reverse(i)

    print(new_word)
elif(x==2):
    new_word = " "
    for i in l:
        isize=len(i)

        if(isize >= 3):
            new_word +=" " + i[isize-4] + i[3:isize-4]
        else:
            new_word += reverse(i)

    print(new_word)



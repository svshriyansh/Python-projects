import random
#initializing a array
word = [ "grapess","mangoo","apple","car","bike"]
life = 5
x = random.choice(word)
y = x
blank = ""
for i in range(0,len(x)):
    blank+="_"
print(blank)
#input
while life>0:
    if blank == y :
        print("Right Answer")
        break
        # x = random.choice(word)
        # y = x
        # blank = ""
        # for i in range(0,len(x)):
        #     blank+="_"
        # print(blank)
    try:
        data = input("Enter the character\n")[0]
        index=""
        count=0
        for j in range(0,len(x)):
            if x[j] == data:
                count +=1
                if count == 1:
                    index += str(j)
                else:
                    index +=str(j)
        if count ==0:
            print("wrong Answer")
            life-=1
        if count > 0:
            if count ==1:
                x = x[:int(index[0])]+ "_" + x[int(index[0])+1:]
                blank = blank[:int(index[0])] + data + blank[int(index[0])+1:]
                print(blank)
            else:
                length = len(index)
                for k in range(0,length):
                    x = x[:int(index[k])]+ "_" + x[int(index[k])+1:]
                    blank = blank[:int(index[k])] + data + blank[int(index[k])+1:]
                print(blank)

    except IndexError:
        print("Data not entered")
if life ==0:
    print("You Lose")
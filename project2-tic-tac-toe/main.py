a =f"|1|2|3|\n|4|5|6|\n|7|8|9|"
print(a)
# setting the outlay

b = [" ", " ", " ", " "," "," "," "," "," "]
b1 = [11,2,3,4,5,6,7,8,9]

#judge
def judge(b,b1):
    if b1[0] == b1[1] and b1[2] == b1[0]:
        print(f"{b[0]} is the winner")
        i = 10
        return i
    elif b1[3] == b1[4] and b1[5] == b1[3]:
        print(f"{b[3]} is the winner")
        i = 10
        return i
    elif b1[6] == b1[7] and b1[8] == b1[6]:
        print(f"{b[6]} is the winner")
        i = 10
        return i
    elif b1[0] ==b1[3] and b1[6] == b1[0]:
        print(f"{b[0]} is the winner")
        i = 10
        return i
    elif b1[1] == b1[4] and b1[7] == b1[1]:
        print(f"{b[1]} is the winner")
        i = 10
        return i
    elif b1[2]== b1[5] and b1[8] == b1[2]:
        print(f"{b[2]} is the winner")
        i = 10
        return i
    elif b1[0] == b1[4] and b1[8]== b1[0]:
        print(f"{b[0]} is the winner")
        i = 10
        return i
    elif b1[2] == b1[4] and b1[6] == b1[2]:
        print(f"{b[2]} is the winner")
        i = 10
        return i
    elif " " not in b:
        i = 10
        print("draw")
        return i
    
    
#input content


    
def main():
    i=0
    input_num = []
    while i <9:
        where = int(input('which location you want to put your x/o? entre numbers from 1 to 9:'))
        if where <= 9:
            num = where-1
            if num not in input_num:
                i +=1
                input_num.append(num)
                if i%2 != 0:
                    b[num] = 'x'
                    b1[num] = 1
                else:
                    b[num] = 'o'
                    b1[num]= 0
            else:
                print("you can't choose the position that already be selected.")
        else:
            print("Please choose the number which is under 10!")
                
        outlay = f"|{b[0]}|{b[1]}|{b[2]}|\n|{b[3]}|{b[4]}|{b[5]}|\n|{b[6]}|{b[7]}|{b[8]}|"
        print(a)
        print(outlay)
        ans = judge(b,b1)
        if ans == 10:
            break

if __name__ == "__main__":
    main()
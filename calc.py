#-*- coding: utf-8 -*-

#first_num = input()
#calc = raw_input()
#last_num = input()
def sum(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def rem(a,b):
    return a%b


total_input = raw_input()
split_count = 0
i_cnt = 0

while True:
    if total_input[i_cnt] == "+":
        break
    elif total_input[i_cnt] == "-":
        break
    elif total_input[i_cnt] == "*":
        break
    elif total_input[i_cnt] == "/":
        break
    elif total_input[i_cnt] == "%":
        break
    else:
        print("Wrong Input")
        quit()
    
    i_cnt = i_cnt + 1

first_num = float(total_input[0:i_cnt])
last_num = float(total_input[i_cnt+1:])
#print first_num   
#print last_num
calc = total_input[i_cnt]

if calc == "+":
    print(sum(first_num,last_num))
elif calc == "-":
    print(sub(first_num,last_num))
elif calc == "*":
    print(mul(first_num,last_num))
elif calc == "/":
    print(div(first_num,last_num))
elif calc == "%":
    print(rem(first_num,last_num))
else:
    print("Wrong Input")
#calc_array = ['+','-','*','/','%']

#r_add = first_num + last_num

#if calc == '+':
#    #print(ss)
#    print(r_add)
#
#print(first_num)
#print(calc)
#print(last_num)
#print(r_add)
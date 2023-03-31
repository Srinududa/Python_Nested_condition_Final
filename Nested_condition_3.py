a = 15
j = a % 10 == 0
h = a % 5 == 0
if j:
    print("Divisible by 10")
elif h:
    print("Divisible by 5")
else:
    print("Not Divisible by 10 or 5")

result==>> Divisible by 5



a = 10
b = 15
c = 20
is_a_great = (a > b) and (a > c)
is_b_great =  (b >c)

if is_a_great:
    print(a)
elif is_b_great:
    print(b)
else:
    print(c)

result==>>20


a = 93
j = a >= 90
k = a >= 50

if j:
    print("Discount is 200")
elif k:
    print("Discount is 100")
else:
    print("No Discount")

result =>> Discount is 200


a = 26
b = 47

if a>b:
    print("Win")
elif a==b:
    print("Draw")
else:
    print("Lose")


result==>>Lose


a = 12.5(input())
if a>0:
    print("Positive")
elif a<0:
    print("Negative")
else:
    print("Negative")

result==>> Positive



cp = 143
sp = 155
profit = sp > cp
loss = sp < cp
No_pf_ls = sp == cp

if profit:
    print("Profit")
elif loss:
    print("Loss")
elif No_pf_ls:
    print("No Profit - No Loss")
else:
    print("No Profit - No Loss")

result==>> Profit



a=1
if a==11 or a==12 or a==1:
    print("Winter")
elif a==2 or a==3:
    print("Spring")
elif a==4 or a==5 or a==6:
    print("Summer")
elif a==7 or a==8:
    print("Rainy")
elif a==9 or a==10:
    print("Autumn")
else:
    print("Autumn")

result=>>Autumn



y=2016
if (y%4==0) and (y%100!=0):
    print("True")
elif (y%400!=0) and (y%100==0):
    print("False")
elif (y%400==0):
    print("True")
else:
    print("False")
result=>>True


a=3
b=4
if a>b:
    print("A > B")
elif a<b:
    print("A < B")
else:
    print("A == B")

result=>>A < B




a=3
if a==1:
    print("Monday")
elif a==2:
    print ("Tuesday")
elif a==3:
    print ("Wednesday")
elif a==4:
    print ("Thursday")
elif a==5:
    print ("Friday")
elif a==6:
    print ("Saturday")
elif a==7:
    print ("Sunday")


 result=>>Wednesday


str = "34T"
first_two = str[:-1]
int_first_two = int(first_two)

str_end_T = str[-1:] == "T"
str_end_H = str[-1:] == "H"
str_end_K = str[-1:] == "K"

if str_end_T:
    print(int_first_two * 10)
elif str_end_H:
    print(int_first_two * 100)
elif str_end_K:
    print(int_first_two * 1000)
else:
    print(int_first_two * 1000)
    
result==>>> True




a = 30
s = (a-50)
j= s*5 + 50*3
if a<=50:
    print(a*3)
elif a>=50:
    print(j)
    
result==>>90
    
    
    
    









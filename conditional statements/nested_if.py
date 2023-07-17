rocket = True
count_down = int(input("Enter countdown:"))
#if value 20 --- 20 hours, value =29 ---- 1day 5hours -- 49 hours then 2 days 1 hour
if rocket == True:
    print("I have a rocket")
    if count_down<=24:
        print("Timer:",count_down,"hours left")
    else:
        day = count_down//24
        hours = count_down%24
        print("Timer:","days:",day,hours,"left")
else:
    print("I dont have rocket")

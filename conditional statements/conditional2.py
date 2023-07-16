#if loop will execute first
rating = float(input("enter movie rating:"))

if rating>=0 and rating<2.0:
    print("flop")
elif rating>=2 and rating<4:
    print("average movie")
elif rating>=4 and rating<=5:
    print("industry hit")
else:
    print("Invalid input enter value between 0 to 5")




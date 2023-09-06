from datetime import datetime

name =input("enter item name: ")
#Lists of items
lists='''
Rice    $ 2/lb
Sugar   $ 3/lb
salt    $ 1/lb
Oil     $ 5/litre
Paneer  $ 1.5/lb
Maggi   $ 1/lb
Boost   $ 4/each
Colgate $ 4/each
'''

#declaration
price=0
pricelist = []
totalprice=0
finalprice=0
ilist = []
qlist = []
plist = []

#rates for items
items={'rice':2,'sugar':3,'salt':2,'oil':5,'paneer':1.5,'maggi':1,'boost':4,'colgate':4}

option=int(input("for list of items press 1:"))
if option == 1:
    print(lists)
for i in range(len(items)):
    inp1=int(input("if you want to buy press 1 or 2 for exit:"))
    if inp1==2:
        break
    if inp1==1:
        item=input("Enter your items:")
        quantity=int(input("Enter quantity:"))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print("Sorry you entered item is not available")
    else:
        print("you entered wrong number")
    inp=input("can i bill the items yes/no:")
    if inp=='yes':
        pass
        if finalamount!=0:
            print(25*"=","Walmart",25*"=")
            print(28*" ","Pickering")
            print("Name:",name,30*" ","date",datetime.now())
            print(75*"-")
            print("sno",8*" ",'items',8*" ","quantity",3*" ",'price') 
            for i in range(len(pricelist)):
                print(i,8*' ',5*' ',ilist[i],3*' ',qlist[i],8*" ",plist[i])
            print(75*"-")
            print(50*" ",'Totalamount:','$',totalprice)
            print("gst amount",50*" ",'$',gst)
            print(75*"-")
            print(50*" ",'finalamount:','$',finalamount)
            print(75*"-")
            print(20*" ","Thanks for visiting")
            print(75*"-")


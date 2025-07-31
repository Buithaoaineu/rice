print("1. Borrow book")
print("2. Return book")
print("3. View book")

choice = input ("Choose a number :")

if choice ==1 :
    print ("Book is not available to borrow")

elif choice == 2 : 
    print ("Book is successfully returned")

elif choice == 3 :
    print ("You're viewing a book :D")

if choice < 0 and choice > 3 :
    print ("Error")

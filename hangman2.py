choice ="yes"
while (choice == "yes"):
    turns=6
    from random import *
    words={"Himanchal": "Hill station in the north",
           "Punjab": "Five rivers in this state",
           "Haryana":"Neighbour of punjab" ,
           "Assam":"North-eastern state",
           "Chandigarh":"Capital of two states",
           "Maharashtra":"Commericial capital of India",
           "Tamil Nadu":"South state in India",
           "Bihar": "Nalanda university",
           "Telangana": "The newly formed state",
           "Kashmir":"Switzerland of India"}
    r=Random()
    wrandom=r.choice(list(words.keys()))
    print("Hint - ", words[wrandom])
    guesses = ' '
    while turns > 0:
        failed = 0
        for i in wrandom.lower() :
            if i in guesses:
                print(i)
            else:
                print("_")
                failed += 1
        if failed == 0:        
            print("You won")
            break 
        guess = input("guess a character:") 
        guesses += guess                    
        if guess not in wrandom.lower():  
            turns -= 1        
            print ("Wrong")
            print ("You have", + turns, 'more guesses')  
            if turns == 0:           
                print("You Lose")
    choice= input("Do you want to continue: ")
    if (choice == "yes"):     
        continue
    elif (choice == "no"):
        break
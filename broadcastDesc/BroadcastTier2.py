#defining broadcast tiers
hrt=int(input("Highest rated player's rating="))
if hrt>=2700:
    print("Best tier.")
else:
    GM=input("Are there GMs playing? Y/N ")
    if GM=="Y" or GM=="y":
        if hrt<=2500:
            print("Normal tier.")
        elif hrt>=2600:
            twentysixhundred=int(input("Number of GMs above 2600="))
            if twentysixhundred>=3:
                print("High tier.")
            else:
                twentyfivehundred=int(input("Number of GMs above 2500="))
                diff=3-twentysixhundred
                if twentyfivehundred>=diff:
                    print("High tier.")
                else:
                    print("Normal tier.")
        else:
            twofivezerozero=int(input("Number of GMs above 2500="))
            if twofivezerozero>=6:
                print("High tier.")
            else:
                print("Normal tier.")
    elif GM=="N" or GM=="n":
        print("Normal tier.")
    else:
        print("Please enter Y or N as the answer to the above question and try again.")

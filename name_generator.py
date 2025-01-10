#Winni Ma
#10/17/24

print("Find Out What Barbie Character You Are Quiz")
print("Answer the following questions.")

ans = input("black (b) or pink(p)?")
if ans == "b":
    ans = input("fashion (f) or music(m)?")
    if ans == "f":
        ans = input("dogs (d) or cats (c)?")
        if ans == "d":
            print("Your Barbie character is Raquel!")
        else:
            print("Your Barbie character is Blissa!")
    if ans == "m":
        ans = input("sing (s) or listen (l)?")
        if ans == "s":
            print("Your Barbie character is Ryan!")
        else:
            print("Your Barbie character is Skipper!")

else:
    ans = input("kid (k) or adult (a)?")
    if ans == "k":
        ans = input("baking (b) or sports (sp)?")
        if ans == "b":
            print("Your Barbie character is Chelsea!")
        else:
            print("Your Barbie character is Stacie!")

    if ans == "a":
        input("shopping (sh) or inventing (in)?")
        if ans == "sh":
            print("Your Barbie character is Barbie!")
        else:
            print("Your Barbie character is Ken!")


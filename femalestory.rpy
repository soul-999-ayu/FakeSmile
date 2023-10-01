label female:
    "You are playing as a female character."
    $main = renpy.input("Enter Main Character's Name:", default="Anshika", length=20)
    $bff1 = renpy.input("Enter Your Best Friend's Name:", default="Sarika", length=20)
    $bff2 = renpy.input("Enter Your 2nd Best Friend's Name:", default="Divya", length=20)
    define main = Character("[main]")
    define bff1 = Character("[bff1]")
    define bff2 = Character("[bff2]")
    "Thanks for entering the names."
    "The story begins now..."
    ""
    
    return

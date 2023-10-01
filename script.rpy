# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# The game starts here.

screen Guide(guideMessage):
    frame:
        xalign 0.5
        yalign 0.5
        xsize 500
        vbox:
            text guideMessage
            text ""
            hbox:
                button:
                    text "Male"
                    xpos 90
                    action Jump("male")
                button:
                    text "Female"
                    xpos 210
                    action Jump("female")

label start:
    window hide dissolve
    play movie "images/Intro/soul.ogv"
    $ renpy.pause(14.0, hard=True)
    play movie "images/Intro/smile.ogv"
    $ renpy.pause(15.0, hard=True)
    # "This game has two different perspectives..."
    # "And you have to choose one to begin with."
    # call screen Guide("You wanna play as?:")
    # scene dark
    call male from _call_male
    # This ends the game.
    return

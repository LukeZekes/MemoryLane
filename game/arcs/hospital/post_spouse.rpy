default num_people = 0
label post_spouse:
    scene bg hospital with memory_fade
    nurse "Dang what a ride"
    nurse "Okay who's here?"
    if(sibling_close):
        "Ruby"
        $ num_people += 1
    if(friend_close):
        "Vincent"
        $ num_people += 1
    if(spouse_close):
        "[s.name!q]"
        $ num_people += 1

    if(num_people == 0):
        nurse "..."
        nurse "...oh..."
        nurse "Nobody is here lmao"

    nurse "Do you regret the way you lived your life?"
    menu:
        "Do you?"
        "Yes":
            nurse "K"
        "No":
            nurse "K"

    narrator "And then I died the end"
    jump end_credits

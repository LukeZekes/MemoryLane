label spmstuffs:
    show morel older happy with cd
    show vincent older happy with cd

    hide morel
    show vincent older happy
    with cd

    hide vincent
    show morel older happy
    with cd

label spouse_marriage:
    if (sibling_close == False) and (friend_close == False):
        jump cheat_on_spouse
    if(spouse_score >= spouse_threshold): #If you cheat, there's a separate check in cheat_on_spouse to see if they cheat too
        jump spouse_cheats
    else:
        jump have_child

label cheat_on_spouse:
    "Homewrecker" "You wanna cheat?"
    menu:
        "What did you do?"
        "Cheat on [s.name!q]":
            if (spouse_score >= spouse_threshold):
                s "Oh dang I was cheating too lmao"
                m "Oh dang this is an unhealthy relationship"
            else:
                s "I can't believe you cheated on me you suck goodbye"
            $ spouse_close = False #You break up regardless
            jump post_spouse

        "Don't cheat":
            m "No thank you not today"
            if (spouse_score >= spouse_threshold):
                jump spouse_cheats
            else:
                jump have_child

label spouse_cheats: #When you don't cheat but spouse does
    s "You kinda aren't a good husband so I cheated sowwyyyyyy"
    menu:
        "Did you forgive her?"
        "Yes":
            jump have_child
        "No":
            s "Ok wanna stay friends?"
            menu:
                "Yes":
                    s "Ok bye see you around"
                "No":
                    s "Fair enough see you never"
                    $ spouse_close = False

    jump post_spouse

label have_child:
    "Hey baby wanna have a baby?"
    menu:
        "What did you say?"
        "Yes":
            s "Okay lets make a baby"
            $ has_child = True
        "No":
            s "Okay no babies for us"
            $ has_child = False
    jump post_spouse

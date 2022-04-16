default spouse_score = 0
default spouse_threshold = 2

default spouse_gender = "M"
default s = j
default s_C = "Johnny"
default s_he = "he"
default s_he_C = "He"
default s_his = "his"
default s_his_C = "His"
default s_him = "him"
default s_him_C = "Him"



default spouse_close = True
default has_child = False

label spouse_teen:
    scene bg playground with memory_fade
    "Today’s the day."
    "After countless periods spent doodling [s_his] name in my Biology notebook,
    after [s_he] started signing [s_his] name with a heart on our peer reviews..."
    "...after running into [s_him] at the party last month."

    "Today’s finally the day I’m going to ask out [s] Grant."
    show morel teen happy at left with cd
    m "He-y, [s]!"

    "My voice cracks halfway through, and I swallow, trying to appear more confident than I feel."
    "[s_he_C] turns and grins at me."
    show spouse_teen_happy at right with cd
    s "Hi, Morel! What’s up?"

    m "I was just, uh. Just wondering if you were interested in, um…"

    "I trail off, breaking eye contact."
    "Everything I’ve practiced in the mirror abandons me, and I’m left feeling bare in front of my crush."

    s "Yeah?"
    hide spouse_teen_happy
    hide morel
    with cd

menu:
    "What do you say?"
    "I love you":
        $ spouse_score += 1
        show morel teen happy at left with cd
        m "I love you."
        show spouse_teen_happy at right with cd
        "..."
        show spouse_teen_upset at right
        hide spouse_teen_happy
        show morel upset at left
        with cd

        s "What?"

        "[s_his_C] face is pretty unreadable, but [s_he] seems off-put by my forwardness.
        I guess I am coming on a little strong..."
        hide morel
        hide spouse_teen_upset
        with cd
        menu:
            "What do you say to fix this?"
            "Is it hot in here, or is it just you?":
                show morel teen happy at left with cd
                m "Is it hot in here, or is it just you?"
                "[s_he_C] responds without missing a beat."
                show spouse_teen_happy at right with cd
                s "Sorry, it’s just that you’re always so cool that I wanted to warm you up."
                "A counter pick-up line?! Maybe I really am in love."

            "Apologize profusely":
                $ preferences.afm_time = 0.1
                $ preferences.afm_enable = True
                $ preferences.text_cps = 60
                $ spouse_score += 1
                show morel teen upset at left with cd
                m "I’m! Really sorry! I don’t know where that came from, honestly. I do love you, I think?"
                m "I mean, obviously I didn’t know you existed until last"
                m "month, but you’re an amazing person and I love being around you"
                m "and I’d like to be around you more, I guess? And"

                $ preferences.afm_time = 15
                $ preferences.afm_enable = False
                $ preferences.text_cps = 2
                $ spouse_score += 1
                show spouse_teen_upset at right with cd
                s "Uh..."
                $ preferences.text_cps = 80

    "Are you trash? Because I wanna take you out":
        show morel teen happy at left with cd
        m "Are you trash? Because I wanna take you out."
        show spouse_teen_happy at right with cd
        "[s_he_C] giggles."
        s "Well, I might not be the trash you’re looking for, but..."
        "I sense my opportunity and spring to take it."

m "Will you go out with me, [s]?"
if(spouse_score >= 2):
    show spouse_teen_upset at right with cd
    s "..."
    s "...Sorry, no..."
    "My stomach drops."
    "Sure, I had been awkward, but I had hoped it was in a charming way."
    "Turns out it was just in an awkward way."
    "Hopefully I get another chance some other time..."
else:
    #show spouse_teen_happy at right with cd
    s "I'd love to!"
jump spouse_early_adult

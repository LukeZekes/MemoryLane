default party_threshold = 2
label ftstuffs:
    show morel teen happy with cd
    show vincent teen happy with cd

    hide morel
    show vincent teen happy
    with cd

    hide vincent
    show morel teen happy
    with cd


label friend_teen:
    scene bg party with memory_fade
    "The party is even bigger than I imagined."

"I recognize most of them as classmates from school, and other I don’t recognize at all."
"There is a cute guy in one corner, nodding his head to the music."
"There is a cute girl in the other corner, swaying her hips and talking to her friend."
menu:
    "What do you do?"
    "Wink at the girl":
        "I wink at the cute girl."

        "She smirks at me, and winks back."
        "My stomach flutters."
        $ spouse_gender = "F"
        $ s = g
        $ s_C = "Genny"
        $ s_he = "she"
        $ s_he_C = "She"
        $ s_his = "her"
        $ s_his_C = "Hes"
        $ s_him = "her"
        $ s_him_C = "Her"
        image spouse_teen_happy = "genny teen happy.png"
        image spouse_teen_upset = "genny teen upset.png"
        image spouse_older_happy = "genny older happy.png"
        image spouse_older_upset = "genny older upset.png"
    "Wink at the guy":
        "I wink at the cute guy."
        "He smirks at me, and winks back."
        "My stomach flutters."
        image spouse_teen_happy = "johnny teen happy.png"
        image spouse_teen_upset = "johnny teen upset.png"
        image spouse_older_happy = "johnny older happy.png"
        image spouse_older_upset = "johnny older upset.png"


"As I smile back at [s_him], ‘You Are My Sunshine’ begins to play over the speakers."

"What a ridiculous song for a party."
if(spouse_gender == "M"):
    show johnny teen happy at right with cd
else:
    show genny teen happy at right with cd
s "This is a ridiculous song for a party."
show morel teen happy at left with cd
m "Right? I get it’s popular, but it’s not, like. Party popular, or anything."

"[s_he_C] laughs, and I feel the room get warmer."

m "What’s your name?"

s "My name’s [s]. And you’re Morel, right?"

m "How—"

s "We’re in the same Bio class."

s "Don’t feel too bad! I sit in the corner.
Plus, Morel is a much easier name to remember than [s]."

"Random Person ""[s]!"

s "Sorry, I gotta go! It was really nice officially meeting you!"
if(spouse_gender == "M"):
    hide johnny teen happy at right with cd
else:
    hide genny teen happy at right with cd
"[s_he_C]’s gone before I can say goodbye."

v "Hey, Morel! You made it!"
show vincent teen happy at right with cd
"I turn and see Vincent. I can tell that he’s more comfortable now that I’m here, and I grin at him."

m "Yep, I made it."

hide morel
"Drunk Girl" "Heyyyyyy, Vincent!"

v "Oh, hello! Do I know you?"

"Drunk Girl" "I sit behind you innnnn English!"

v "Um, actually, I sit in the back—"

"Drunk Girl" "Oh, no!
No, no, I meant--sorryyyyyy.
I meant math class!"

v "Oh, Penelope! Sorry, I didn’t recognize you."

"I don’t blame him; I hadn’t recognized her either."
"She’s dressed in a tiny dress that leaves absolutely nothing to the imagination."
"I’m not nearly as timid as Vincent, but I can hardly blame him for the way his eyes dart away and his voice goes even softer than usual."

"Penelope" "That’s okayyyyyy, Vincent~"

"To add insult to injury, based on the slur in her voice and the flush high in her cheeks, Penelope is completely wasted."

"Penelope" "Hey, Vincent…"
"Her voice is soft, almost a whisper."
"She looks at him intently despite her swaying. "
"There’s a certain look in her half-lidded eyes that I’ve only seen in, ah, videos."

"Penelope" "They say...the quiet ones are loudest in bed."

"She grabs onto Vincent’s arm and tugs on it."

"Penelope" "C’mon, Vincent. I wanna see if that’s truuuue~"
show vincent teen upset at right with cd
v "Uh, Morel?!"

"Vincent’s voice is barely more than a squeak, and his eyes are wider than saucers."

"It’s almost cute seeing my best friend like this."
"He’s an attractive guy, but he rarely gets attention from girls because of his quiet demeanor--especially not attention like this."
"A part of me wants to act oblivious, just to see how he’ll handle Penelope’s drunken affection."
"But I can see from the pleading look in his eyes that he wants to be anywhere but here."

hide vincent
hide morel
menu:
    "What did you do then?"
    "Interfere":
        show morel teen happy at left
        show vincent teen upset at right
        with cd
        m "I’m parched, Vincent! Let’s go get some water or something."
        hide morel
        hide vincent
        with cd
        "Without giving either Vincent or Penelope time to think, I grab his other arm and yank him away from her."
        "We speed walk down the hallway to what turns out to be the bathroom."
        "I throw the door open."
        "It’s a more spacious bathroom than I thought, and cleaner than I thought the host would keep it."

        "Vincent throws himself down on the toilet seat cover and buries his burning face in his shaking hands."
        "I close the door behind us, and sit down on the side of the bathtub next him."
        show morel teen upset at left with cd

        m "Vincent?"

        "Vincent looks up at me."

        m "You okay? You look kinda…"

        "I make a little motion with my hands, and he smiles weakly."
        show vincent teen upset at right with cd

        v "Yeah, I am a little…"

        "He repeats the motion."

        v "Thank you, Morel. I’d like to be more out there one day, I just...I get nervous, you know?"
        "Penelope’s swell, but it all happened so fast, and—"

        m "You don’t have to justify yourself to me, dude.
        I would’ve freaked out too; she was coming on way too strong."

        "Vincent nods a little, looking back down at his lap."

        m "And you don’t have to be super smooth or loud to be confident.
        You’ve got this sort of quiet confidence. It’s nice, Vincent."
        show vincent teen happy at right with cd

        "Vincent smiles genuinely for the first time since I’ve seen him tonight."

        v "Thanks.
        Do you wanna head home?"
        show morel teen happy at left with cd

        m "Please! I’m glad I came, but I don’t know if the party life is quite the life for me."
        m "I’m gonna head to the kitchen really quick before I leave, but I’ll see you in school on Monday, okay?"

        v "Bye, Morel! See you then!"

        jump friend_adult


    "Let him have his fun":
        $ friend_score += 1
        show vincent teen upset at right with cd

        "I wait to see how he handles her alone."

        "As I watch, Penelope’s hand wanders from his arm, and goes lower, lower, lower, lower..."
        hide vincent
        "Vincent gives a high-pitched squeak, slaps her away with a vigor I’ve never seen from him, and he grabs my arm and drags me down the hallway."

        "He throws us into what I barely register as a bathroom, and slams the door shut."

        if(friend_score == 1):
            show morel teen upset at left with cd
            m "I just wanted to get you out of your comfort zone.
            Sorry I misinterpreted the signs."

            "He frowns, then looks away."
            show vincent teen upset at right with cd

            v "Thanks, I guess. For trying to help."

            m "No problem."

            "The statement feels hollow."
            "I had really thought that I was helping him, but he’s so upset…"

            m "Do you want to go dance? I don’t think Penelope’s out there—"

            v "I’d like to go home, please.
            I’m not having fun."
            jump friend_adult


        else:
            show vincent teen upset at right with cd

            "Vincent says nothing, but the disappointment in his eyes speaks volumes."
            show morel teen upset at left with cd

            m "I’m sorry. I was trying to let you have fun! I knew you were uncomfortable, but I thought it was maybe first time jitters, or something."

            v "But even when we were kids, with Kenneth…"

            "It’s sad, but I don’t know exactly which instance he’s referring to."
            "He’s had plenty of run-ins with our elementary school and middle school bully..."
            "...and I wasn’t always the best with standing up to the guy who used to be my friend."

            v "Morel…"

            m "..."

            v "It’s like you don’t even care about me."

            "Coming from anyone else, I would’ve taken the comment as manipulation and gotten defensive."
            "From the look in his teary eyes, though, I can tell that he’s serious."
            menu:
                "What do you say to Vincent?"
                "Apologize":
                    m "Look, Vincent.
                    You’re right, I’m not always there for you.
                    You’re my best friend, and you’re one of the kindest people I’ve ever known."
                    "I’m sorry if it seems like I take you for granted.
                    I won’t be able to change overnight, but I can start by promising that I do care about you."

                    "Vincent is quiet, then nods."

                    v "Thank you. I was...I was getting a little worried that you don’t like me, but—"

                    m "What? Of course, I like you, dude."
                    show vicent teen happy at right with cd

                    "Vincent beams, hurt feelings forgotten."
                    show morel teen happy at left with cd
                    m "C’mon, let’s go home."
                    jump friend_adult
                "Stand your ground":
                    $ friend_close = False
                    m "Vincent.
                    I’m not going to apologize for trying to help you!
                    I just wanted to you and Penelope to—"

                    v "It’s not just about that, Morel!"

                    m "You know, maybe if you weren’t such a pansy, you wouldn’t be so nervous around girls!"

                    v "..."

                    "My words hang in the air between us."

                    v "You’re not a good friend, Morel."
                    #Transition to post_friend
                    jump post_friend

    #    [this ends the Vincent chapter. Vincent does not appear by his bedside.]

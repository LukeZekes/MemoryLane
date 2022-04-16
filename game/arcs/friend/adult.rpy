label fastuffs:
    show morel older happy with cd
    show vincent older happy with cd
    show lily happy with cd

    hide morel
    show vincent older happy
    with cd

    hide vincent
    show morel older happy
    with cd

label friend_adult:
    scene bg house with memory_fade
    show vincent adult happy at right with cd
    v "Thank you so much again for doing this on short notice, Morel."

    "He’s still shorter than me, as shown by the way that he looks up at me as he beams."
    show morel adult happy at left with cd
    m "No problem! Always love hanging out with my gal."
    show lili happy at right
    hide vincent
    with cd
    l "Morel!"

    m "There she is!"

    "Lili, Vincent’s daughter, runs up to me. I get down on one knee and hug her.
    She inherited her father’s curls and dimples, and they’re shining full force."
    show vincent adult happy at right
    hide lili
    with cd
    v "Have fun with Uncle Morel, honey!"
    show lili happy at right
    hide vincent
    with cd
    l "Bye, Daddy!"
    show vincent adult happy at right
    hide lili
    with cd
    "Vincent turns to me, a crease in his brow."

    v "And please, please call me if she needs anything."

    m "Don’t worry, Vincent, I got her!"

    "Vincent smiles."

    v "I know you do."
    hide vincent with cd
    "With that, he leaves."
    show lili at right with cd
    m "Upsie-daisy, Lili!"

    "I pick her up, and she giggles."
    hide morel
    hide lili
    with cd
    "It’s been a while since I’ve been to Vincent’s house."
    "There was a time we went over to each other’s places every day, just after we got our first ‘real jobs.’"
    "Now, with Penelope having the second baby and me planning on going to the next level soon in my own relationship, we hardly have time to see one another."

    "I turn the corner, put Lili down, and look around the kitchen."
    "It’s uncharacteristic for Vincent and Penelope to be this messy."
    "I barely know where to start with preparing Lili’s lunch — there are dirty dishes in the sink and scattered all over the counters, and the table is covered with yet-unpaid bills."

    "Lili pulls at my leg."
    show lili at right with cd
    l "Morellllll, I wanna watch Flintstones! Watch Flintstones, watch Flintstones!"
    hide morel
    hide lili

menu:
    "What do you do?"
    "Clean the kitched first":
        $ friend_score -= 1
        show morel adult happy at left with cd
        m "We can watch in a minute, okay, kiddo? I want to clean this mess up for your daddy first."

        "Lili pouts. I ruffle her hair."

        m "It’s okay, sweetie! You can watch me clean."
        show lili happy at right with cd
        l "I don’t wanna watch you clean! Wanna watch Flintstones!"
        hide morel
        hide lily
        with cd
        "I make a big production of filling the sink with dish detergent; within seconds, Lili is next to me, trying to pop all of the bubbles."
        "I work through the rest of the mess similarly, and I end up having much more fun than I intend to."
        show morel adult happy at left
        show lily happy at right
        with cd
        m "See, all done! Now we can go watch Flintstones, okay?"

        l "Yay!!"
        hide morel
        hide lily
        with cd
        "The Flintstones is more mesmerizing than I remember. Both Lili and I watch enraptured until we hear a knock on the door."
        show vincent adult happy at right with cd
        v "Hey, Lili! Hey, Morel!"
        hide vincent
        show lili happy at right
        with cd
        l "Daddy!"
        hide lili
        show vincent adult happy at right
        with cd
        v "Hi, sugarpot. Did you have fun?"
        hide vincent
        show lili happy at right
        with cd
        l "Yeah! Morel and I cleaned then had nuggies and watched Flintstones!"
        hide lili
        show vincent adult upset at right
        with cd
        "Vincent turns to me."

        v "You cleaned the kitchen?"

        "He wraps his arms around me and lays his head on my shoulder."

        v "Thank you, so much."

        "When he pulls away, his eyes are shiny and wet with gratitude.
        Uncomfortable, I respond the only way I know how."
        show morel adult happy at left with cd
        m "You’re still such a crybaby, after all these years."

        "It comes out a little meaner than I mean it to, but he laughs anyway and wipes his face."
        show vincent adult happy with cd
        v "You know you miss it."

        m "I do. We gotta hang out soon, man."

        "Vincent nods solemnly."

        v "Children are not an excuse."

        m "Children are not an excuse."

        "We smile at each other."
        #Transition to post_friend


    "We watched TV":
        "ChildName" "Owie help I grabbed a fork and stabbed a socket"
        menu:
            "What did you do?"
            "I called Vincent and explained what happened":
                m "Vincent your kid is electrocuted"
                v "Ugh again okay thanks for telling me"

            "I didn't tell Vincent":
                v "Hey wtf my kid is electrocuted why didint u tell me"
                m "Sorry lmao"
                v "I dont wanna see you again"
                $ friend_close = False
jump post_friend

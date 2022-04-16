label sastuffs:
    show morel older happy with cd
    show ruby older happy with cd

    hide morel
    show ruby older happy
    with cd

    hide ruby
    show morel older happy
    with cd

label sibling_adult:
    scene bg funeral with memory_fade
    "Pastor" "Dearly beloved, we gather here to say our goodbyes to the unique life of James Bailey."

    "It’s a funeral my dad would have appreciated, I think."
    "My hair is combed neatly, for once, and I wear a black suit that feels specifically tailored for this moment."
    "And it’s quiet, just like he liked."

    "I feel mean for thinking so, but a part of me is surprised to see so many people at his funeral."
    "I don’t recognize half of them; I can only assume they’re friends from work or the golf course he frequented."

    "I’m not sure if I’m upset or not."
    "He wasn’t the perfect father, or even a very good one, but he was my father."
    "I have good memories of him, but I also have not-so-good memories of him."

    "Everything feels fuzzy, as if the world is fading in and out with every blink."

    "My mom sits beside me, silent tears streaming down her face, her eyes fixed on the closed casket my father lies in."
    "Her face is blank."

    "Blink."

    "I go up and say a few words."
    "I barely remember them as soon as they leave my lips, and I’m sitting back down after what feels like seconds."

    "Blink."

    "My suit itches."

    "I blink again, and now Ruby is standing at the podium."

    "She’s shaking."
    "I break out of my fog enough to be concerned."
    "I hadn’t expected her to be so affected; she and Dad had never really seen eye-to-eye, especially after her art career started taking off."
    show ruby older happy at right with cd
    r "My father...he was a great man, and a better father. He was kind, loving, and everything a child could ask for."
    r "When I would show him my art—"

    "Ruby stops short, something shifting in her eyes."

    r upset"You know what, no.
    We’re all adults; we can stop playing whatever game of pretend this is."

    "There are gasps and murmurs."

    "Ruby turns to the casket and speaks directly to it."

    r "My father was an awful, cruel man, and he deserved a worse death than one of natural causes."

    "I speak up with a soft voice, cutting through my own fog."
    show morel adult upset at left with cd
    m "Ruby, that’s enough. He was our dad, and he loved us—"

    r "Then maybe he should have showed it, Morel!"
    r "It’s not our job to make excuses for a dead man who hurt us when we only ever wanted to please him."

    "There are tears streaming down her face now; she scrubs them away roughly with the sleeve of her dress."

    r "And he cheated on Mom. Did you know that, Morel?"

    "What?"

    m "He—what?"

    r "How can you be a terrible person, husband, and father? Pick a struggle, dude."

    "She laughs, the sound sharp and mirthless."

    "Mom" "This isn’t the place for this."

    "My mother stands now as well."
    "In the back of my mind, I register that all the funeral attendees are staring at us."

    "Never mind, my father wouldn’t have liked this."
    "He hated making a scene."

    "Mom" "Ruby, Morel, we can discuss this once we get home.
    Let the man at least get into the ground, for goodness’s sake!"

    r "Mom—"

#    if(sibling_score >= sibling_threshold):
    #    r "Die alone lmao"
    #    narrator "And I never saw her again"
    #    $ sibling_close = False
    #else:
    hide ruby
    hide morel
    with cd
    menu:
        "What will you do?"
        "Defend your dad":
            $ sibling_score += 1
            show morel adult upset at left with cd
            m "You’re lying! Dad would never do something like that."
            show ruby older upset at right with cd
            r "What?"
            "Mom" "..."
            r "What would you know about what Dad would do?
            You never knew what it was like."
            r "You were his favorite, you know.
            It was always about you. ‘Morel this, Morel that.’
            ‘Be more like Morel, Ruby.’"
            r "He never destroyed your paintings or mocked your mistakes. So don’t talk to me about what Dad was like."
            m "..."
            if(sibling_score >= sibling_threshold):
                r "You know what, whatever. You’re just like him, Morel."
                hide ruby with cd
                "That stings. I want to yell back, but she’s gone before I can figure out what to say."
                scene bg black with fade
                "After the funeral, I tried to talk to Ruby, but she just yelled at me"
                "She accused me of always being a bad brother, from tattling on her when we were kids..."
                "...to wrecking her beloved car and jeopardizing her career."
                "We quickly grew apart after that, and now we don't talk anymore."
                "Not that I blame her..."
                $ sibling_close = False
            else:
                r "...I'm sorry. It's not your fault he was such a dick, Morel."
                m "Ruby-"
                r "I just...I need some air"
                hide ruby with cd
                "Ruby pushes past me and hurries out of the sanctuary"
                hide morel with cd
                "I hesitate for a moment before following her outside"
                scene bg white with fade
                show ruby older upset at right with cd
                r "How can they do that?
                How can they act like he was this good guy, and tell all these nostalgic stories like he wasn’t some cruel prick?"
                r "And what if…"

                "She hiccups, and continues."

                r "What if he really was a good guy, and he was only awful to us?
                What then?"

                m "..."

                r "I hate him, Morel, I hate him."
                hide ruby
                hide morel
                with cd
                "She throws her arms around me and sobs into my shoulder."
                "I feel my own eyes fill with tears for the first time today, and I let them fall."

            #if(sibling_score >= sibling_threshold):
            #    r "Die alone lmao"
            #    narrator "And I never saw her again"
            #    $ sibling_close = False
            #else:
            #    r "Ugh see you on your deathbed"

        "Listen to your mother":
            "I walk up the podium, thankful for my aisle seat."
            show morel adult upset at left with cd
            m "C’mon, Ruby, let’s go to the bathroom."

            "I take care to keep my voice soft without sounding belittling."
            if(sibling_score > sibling_threshold):
                hide morel with cd
                "Ruby just pushed me away from her, knocking me over."
                show ruby older upset at right with cd
                r "You know what, whatever. You’re just like him, Morel."
                hide ruby with cd
                "That stings. I want to yell back, but she’s gone before I can figure out what to say."
                scene bg black with fade
                "After the funeral, I tried to talk to Ruby, but she just yelled at me"
                "She accused me of always being a bad brother, from tattling on her when we were kids..."
                "...to wrecking her beloved car and jeopardizing her career."
                "We quickly grew apart after that, and now we don't talk anymore."
                "Not that I blame her..."
                $ sibling_close = False

            else:
                "It seems to work—she follows me as I lead her out of the sanctuary."
                scene bg white with fade
                "As soon as we’re past the double-doors, she shatters."
                show ruby older upset at right with cd
                r "How can they do that?
                How can they act like he was this good guy, and tell all these nostalgic stories like he wasn’t some cruel prick?"
                r "And what if…"

                "She hiccups, and continues."

                r "What if he really was a good guy, and he was only awful to us?
                What then?"
                show morel adult upset at left with cd
                m "..."

                r "I hate him, Morel, I hate him."
                hide ruby
                hide morel
                with cd
                "She throws her arms around me and sobs into my shoulder."
                "I feel my own eyes fill with tears for the first time today, and I let them fall."

    jump post_sibling

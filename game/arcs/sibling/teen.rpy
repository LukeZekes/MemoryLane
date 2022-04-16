label ststuffs:
    show morel teen happy with cd
    show ruby teen happy with cd

    hide morel
    show ruby teen happy
    with cd

    hide ruby
    show morel teen happy
    with cd


label sibling_teen:
    scene bg bedroom with memory_fade
    "Mom and Dad aren’t home, off on another one of their infinite dates to pretend their marriage is going well."
    "Ruby’s nowhere to be found either."
    "Since she graduated high school last year, she’s almost always away at some art conference, art gallery, or doing some art thing."
    "I’m proud of her—it’ll only be a matter of time before she’s...published, or whatever the art equivalent of that is."

    "Usually I’d be celebrating the lack of supervision, but this is the worst day for it..."
    show ruby teen happy at right with cd
    r "Hey, bro!"
    show morel teen happy at left with cd
    m "Ruby!"

    "Summoned by my thoughts, Ruby appears at the top of the stairs."
    "She looks unusually put-together, wearing a blouse instead of her usual oversized, paint-stained t-shirts."
    "She beams at me and runs down the stair two at a time."

    r "I didn’t know you were home from school!"

    "I can’t help but smile as well."
    "Between me trying to not to flunk junior year and her art escapades, we’re rarely in the same place anymore."

    m "Hey, Ruby! Actually, I was going to ask you a favor."

    r "Yeah, what’s up?"

    "Well, here goes nothing..."

    m "So there’s this party."

    r upset "There’s always ‘this party.’"

    "I ignore the condescension of my career-bound older sister and press on."

    m "Vincent and I really want to go. It’s the biggest one of the year, and everyone’s going to be there."
    show ruby teen happy with cd
    "The mention of Vincent perks her up a bit."
    "She loves my best friend like a second brother, and she knows he wouldn’t let me go anywhere unsafe."

    r "Where is this party happening?"

    "Here it is."

    m "It’s across town. So I couldn’t walk there or anything."

    r "...can Vincent give you a ride?"

    m "He’s riding his bike there, and he lives closer."

    r "Alright, kid. Just come out and say it. What do you want?"

    m "Can I borrow your car?"

    r upset "Absolutely not."

    show morel teen upset with cd
    "I sigh at the expected answer."
    "I understand her protectiveness over her baby."
    "It took her forever to save up for that car, and she pays for all of its upkeep and washes it weekly."

    "She’d be devastated if something were to happen to Sylvia, especially something out of her control."

    m "Please? I won’t be able to go otherwise."

    r "And what’s so wrong with that?"
    r "Just because everyone’s going to be there doesn’t mean that you have to be."

    "It’s as if the second she walked across the graduation stage, she turned into our parents."
    "I should’ve known she wouldn’t understand."

    if(sibling_score == 0):
        "My final tactic..."
        show morel teen happy with cd
        m "What about that one time you accidentally drew on the wall when we were kids and I didn’t tell Dad?"

        "..."

        r "Dude, I was ten. You were eight, I think."

        "She’s right. I’m surprised I remember at all. Dang, I thought that might work. Still..."
        show morel teen upset with cd

    m "Please, Ruby?"

    "Ruby considers the genuine pleading in my eyes, and I sigh."

    r "I really am sorry, Morel, but I’m busy tonight."
    r "Even if I were comfortable with you driving Sylvia, which I’m not, I’ve got somewhere to go tonight."

    "That explains why she looks like this, at least."

    r happy "There’s this art gallery I want to go to."

    "Her eyes gain the shine that they have when she talks about her work."

    "‘That doesn’t seem like a valid reason,’ I want to say, but I bite my tongue."

    r "And I know I go to galleries every other week at this point, but this one’s different, trust me."

    m "..."

    r "I’m gonna go freshen up a little more. Be right back!"
    hide ruby with cd
    "She practically skips up the stairs as she heads to her bedroom."

    "As I watch her go, something flashes in the corner of my eye, and I glance over instinctively."

    "There sit her keys shining in the fading sunlight, enticing as a Siren’s song."

    hide morel with cd
    menu:
        "Steal car?"
        "Yes":
            $ sibling_score += 1
            "I grab the keys off the counter without a second thought and slide them into my jacket pocket."
            "The art gallery will be open for a while longer."

            "This party, however, was one night only."

            "I rush out of the house with my stolen prize before Ruby comes back down or I have the chance to feel guilty."
            jump stolen_car
        "No":
            "I stare at the keys for a moment, then look away."
            "There’ll be other parties, but I guess I’ll have to miss this one."
            show morel teen upset at left with cd
            m "..."
            show ruby teen upset at right with cd
            r "Don’t look so down, kid."

            "I jump; I hadn’t even noticed that she’d come back."

            r "What’s it about this party, anyway? Somebody you like there?"

            "I shrug, not looking at her."

            r "..."

            "Ruby heaves a small sigh."
            show ruby teen happy at right with cd
            r "I think I can be a little late to the art gallery to drop you off."
            show morel teen happy at left with cd

            m "Really?"

            r "C’mon before I change my mind!"
            scene bg black with fade
            "I rush behind her as she runs to her car."
            "Both of us are laughing as we hop into Sylvia. It reminds me of when we used to joyride around town when she first got her car."
            "Then she pulls off, and there’s a comfortable silence, broken only by me directing her to the house."

            "It takes less than ten minutes, versus the probable hour it would take me to walk there and back in the dark."
            "Once she parks alongside the curb, Ruby turns to me."
            show ruby teen upset at right with cd
            r "You know you don’t have to go to some lame party to be cool, right? You're pretty cool as you are."

            "That means a lot, coming from her."

            r happy "Well, cool for a kid brother."
            show morel teen happy at left with cd
            m "I’m not a kid."

            "My protest is half-hearted; I’m still absorbing her kind words."

            r "Yeah, whatever."

            m "Thank you, Ruby."

            r "Whatever."

            "Her response is flippant, though there’s something shining in her eyes."
            "She ruffles my hair."

            r "Enjoy your party, bro. Tell Vincent I say hey."

            jump sibling_adult

label stolen_car:
    scene bg black with fade
    "I hop into the car and look at the controls."
    "Suddenly, this task seems a little more intimidating."
    "This is only the second time I’ve driven, but it’s gotta be intuitive, right?"
    "I drive slowly all the way there."
    "It’s like a bike, almost. I keep that in mind as I miss stop signs and narrowly avoid hitting the fire hydrants along the curb."
    m "Jeez."

    scene bg party with memory_fade
    "By some miracle, I arrive to the party with no damage to person nor car."
    "I breathe out."

    "Now comes the hard part."

    "The party is dimmer than I had expected."
    "It reminds me more of a club I’d see on TV than of a stereotypical high school party."
    "Still, I dance, and talk to people I’ve never talked to before."
    "I run into Vincent at some point during the night, and we hang out as well."
    "The party is just as incredible as I’d hoped, and I can’t bring myself to feel bad about how I got here."

    "Hopefully Ruby isn’t missing her art show too much..."

    "A little after Vincent leaves, I go to the kitchen, half-wandering before the night ends, and half-looking for the exit."

    "As I enter, I bump into a girl."
    show morel teen happy at left with cd
    m "Oh, sorry!"

    "She only laughs, eyes not quite focusing on me."
    "It’s Gertrude Scott, the most popular girl in our class, and the hostess of the party."
    "I swear I could feel my heart speed up from the close contact."

    m "Hey, Gertrude! Sorry, I was just leaving—"

    "She grabs my arm before I can turn away, and pulls me in close."

    "Gertrude" "Want some?"

    m "Some—?"

    "I look down at the hand she’s not using to hold me in place."
    "She holds a cup filled just about to the brim with a clear liquid."
    hide morel with cd
    menu:
        "Take the drink?"
        "Yes":
            $ sibling_score += 1
            "I take the drink from her hand and take a sip."

            "It tastes how I’d imagine hand sanitizer to taste, with maybe a hint of peach."
            "It burns my chest going down my throat, and I try to stifle my reflexive coughs."

            "Gertrude crows."

            "Gertrude" "That’s it, Morel! Chug, chug, chug, chug!"

            "From years of lunch tables and having an older sister, I’ve developed a bad habit: when someone says 'chug,' I do so automatically."
            "I have a faraway realization of how out of hand this has gotten..."
            "...but it doesn’t entirely register until the cup is empty and I’m swaying."

            "Gertrude’s laughter seems further away now."
            "Is this what being drunk feels like?"

            "As I stumble out of her house, I realize I still have to get home somehow."
            "I know driving isn’t the best idea, but my alcohol-addled brain insists that leaving Sylvia at Gertrude’s house is even worse."
            "So I climb into the car, the controls seeming even more foreign than before, and I pray no one is out at this time of night."

            "For a while, everything seems to go smoothly. No deer, no wrong turns, no hitting the fire hydrants—"

            "I don’t see the tree until it’s too late."
            #crash
            scene bg carcrash with memory_fade
            "The sound of the crash feels impossibly loud and silent at the same time."
            "The impact slams me against the steering wheel, and I hiss in pain, grateful to have worn my seatbelt."

            "I’ve hit the pine tree next to our house, to make matters worse."
            "The tree is dented, somehow, and sweet Sylvia is absolutely totaled."

            "Something in me wants to cry."

            "Instead I stare blearily at the dent I created in our pine tree."

            "As I see Ruby sprint out of the house, no doubt summoned by the huge bang, I’m distantly grateful that our parents aren’t home."
            show ruby teen upset at right with cd
            r "Morel?!"

            "Her face is panicked."

            r "Morel. Morel, say something."

            "I try, though it’s barely coherent."
            "The side of my head feels wet, and that’s all I can focus on."

            r "What—are you drunk?!"
            show morel teen upset at left with cd
            m "‘m sorry I crashed your car."

            "I barely recognize my own voice."
            "I feel far away from the scene, as if I’m floating somewhere above, watching everything play out."

            r "What were you thinking?!"

            "I tune back into the world, unsure of how much of her talking I missed."

            r "And you stole my car, and I had to miss the art gallery. But that’s not what I’m talking about, you idiot."

            "My head is buzzing, both from the impact and the alcohol in my system."
            "I can barely decipher her loud, quick words, let alone interpret any subtext she’s trying to send to me."
            "I blink blearily at her."

            r "What you did was incredibly unsafe, Morel."
            r "You could’ve died. Your cuts look mostly superficial, and you probably have a concussion."
            r "You’re lucky that’s all."

            "Something about her calling me 'lucky' makes me want to laugh."
            "Even in my drunken state, though, I recognize that that’s not the best idea, so I stay quiet and try to keep my eyes open."

            "Ruby sighs gruffly."

            r "Let’s get you inside. And just so you know, you’re gonna pay me back for Sylvia."
            r "Hope your party was worth it."

        "No":
            "Gertrude" "Whatever."

            "She pulls away from me and pouts."

            "Gertrude" "You’re so lame, Morel."

            "It’s late enough—I leave the party not long after that."

            "When I get back home, Ruby is standing on our front lawn."
            "Her eyes widen then narrow as she sees me in Sylvia."
            show ruby teen upset at right with cd
            r "Dude, you stole my car???\nWhat the hell!!"
            "She’s angrier than I’ve ever seen her."
            "As soon as I park, she rips me out of the car and drags me inside."
            show morel teen upset at left with cd
            r "I had to miss the art gallery because of you."

            m "Can’t you just go another night?"

            "I’m surprised I have the voice to speak at all."
            "It feels like my stomach is in my throat; I hate disappointing my sister."

            r "No, I can’t just go another night.
            Jackson Pollock was there tonight."
            r "Maybe I could’ve talked to him and advanced my art career, but now that’s all ruined!"

            m "Oh."

            r "Yeah, 'oh.'"

            "She exaggerates my guilty voice."

            r "Hope your dumb party was worth it."

    jump sibling_adult

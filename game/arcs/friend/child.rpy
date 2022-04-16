default friend_score = 0
default friend_close = True

label fcstuffs:
    show morel kid happy at left with cd
    show vincent kid happy at right with cd

    hide morel
    show vincent kid happy at right
    with cd

    hide vincent
    show morel kid happy at left
    with cd

label friend_child:
    scene bg playground with memory_fade


    show morel kid happy at left with cd
    m "Argh!"

    k "Argh!"

    "It’s recess, and Kenneth and I are playing pirates like we have every other day this week."
    "Kenneth can be bossy, but I don’t mind. I like playing with him, and he’s good at pirate noises."
    "Plus, we get to switch off on who’s captain and who’s first mate."
    "I’m just first mate today, but tomorrow I’ll be captain."

    k "Argh!"

    m "Argh!"

    k "Morel, me matey! We need someone has to be our third pirate! Argh!"

    "I use my high vantage point to scan the field. Then, using my best pirate voice:"

    m "What about him? Argh!"

    "I point across the field to a small boy squatting in the nearby flowers alone."
    "As I watch, he plucks a few, examines them each in turn, smiles, and puts them in his pocket."

    m "I’ve seen him before. He’s the new kid in our class; I can’t remember his name, even the first letter."
    "Kenneth calls across the field to him."

    k "Hey, new kid! Wanna play with us?"

    "The boy’s head jerks up from where he was looking down at flowers"
    "Once he sees us, his cheeks redden, a stark contrast against his otherwise pale face."
    show vincent kid happy at right with cd
    "???" "I dunno how to play."

    "I have to strain my ears to hear him, even though he really isn’t too far away."

    k "We just need a third. You don’t hafta be good at it."

    "???" "Oh, okay."

    "His voice is somehow even smaller than before, and he stands with clear reluctance, looking down the flower patch with despondent longing."

    k "What are you even doing down there? Playing with flowers like a pansy?"
    show vincent kid upset with cd
    "The boy’s face flushes, and he stutters out an apology."

    k "S-s-s-sorry."

    "He laughs, and I laugh along, because I’m first mate."

    k "Argh! C’mon, new matey!"

    "At Kenneth’s beckoning, the younger boy climbs the jungle gym with wobbly, inexperienced hands."

    k "Argh!"

    m "Argh!"
    show vincent kid happy with cd
    "???" "Argh...?"

    "There’s a pause, then Kenneth laughs. I can’t help but grin as well--he doesn’t sound anything like a pirate."
    show vincent kid upset with cd
    k "Haha! You sound more like a damsel in distress than a pirate!"
    k "Hey, I know! You can be the one who walks the plank!"

    "???" "Th—the plank??"
    show morel kid upset with cd
    "Kenneth steps closer to him and smiles toothily. For a second, he reminds me of the sharks we’re learning about in science class."

    k "Yeah. The plank."

    "The boy leans away, fear in his eyes."
    hide vincent
    hide morel
    with cd
menu:
    "What do you do?"
    "Interfere":
        show morel kid upset at left with cd
        m "Hey, knock it off!"

        "Kenneth turns his weird smile to me, and I stand my ground."

        k "Don’t talk back to your captain!"

        "I don’t say anything. Kenneth’s smile drops."

        k "What, you’re defending this loser?"

        m "No, I’m defending my friend. I don’t wanna play pirates with you anymore!"

        "Kenneth scowls."

        k "Next recess, you’re dead meat."

        "I’m not afraid of him. He’s only a little bigger than me, and all that’s fat, anyway."
        "He glares at me, and I puff out my chest to look taller."
        "Maybe it works because he mutters something to himself, goes down the slide, and runs to play with someone else."
        show vincent kid upset at right with cd
        "???" "Thank you for helping me!"

        "The boy reaches into his pocket and shyly hands me a crumpled dandelion."
        "I take it and put it in my own pocket."

        "???" "I’m Vincent."
        show morel kid happy with cd
        m "My name’s Morel!"

        "Vincent nods seriously, as if committing my name to memory. Then he gives me a tiny smile and blinks up at me with his huge, emerald eyes."

        v "Didja really mean it when you said we’re friends?"

        m "Well, yeah, if you wanna be!"
        show vincent kid happy with cd
        "Vincent’s smile grows impossibly wider, in a non-shark-like way, and I return it gleefully."

        m "Do you wanna hang out after school today? I have to ask my parents if you can come over, but I think they’ll be okay with it!"

        v "Would that really be okay?"

        m "Yeah!"

        v "Thank you so much!"

        "He laughs, the sound sending warmth to my cheeks."
        "I have a feeling we’re going to be great friends."

    "See what Kenneth will do":
        $friend_score += 1
        "I watch them as the moment becomes a sort of portrait: Kenneth sneering, the smaller boy cowering."
        "Then, Kenneth shoves the boy down the slide behind him."

        "For a moment, the slight boy is nearly airborne. Then he yelps as he slides down on his back, headfirst."

        "Kenneth snorts and chortles when the boy crashes to the ground at the bottom of the slide."

        k "Haha! He even falls like a damsel. C’mon, first matey, let’s go find someone else to play with."

        "Without looking to see if I’ll follow, he jumps down the ladder and runs across the field."
        "I hop down the ladder and rush to the boy on the ground."
        show morel kid upset at left with cd
        m "Hey, are you okay?"
        show vincent kid upset at right with cd
        "There’s mulch in his curls, and some of the flowers have fallen out of his pocket."

        "The boy looks at me with distrust in his wide emerald eyes, and my stomach drops a bit with guilt."
        "I almost want to apologize for not stepping in, but it seems too late for that now."
        "Instead, I reach out my hand to him."

        "He looks at my hand as if I’m going to pull it away at any second as some cruel joke. "
        "When I don’t, he takes it and lets me pull him up."

        m "I’m Morel, by the way."

        "???" "Vincent."

        m "I’m sorry my friend pushed you, Vincent."

        v "S’okay."

        "His voice is remarkably together, almost practiced."
        "I’m surprised he isn’t crying; I definitely would be after a fall like that."

        "He rubs his head and makes an involuntary noise of pain."


        m "I’ll take you to the nurse, c’mon."
        hide morel
        hide vincent
        with cd
        "It feels like the least I can do."
        "He follows behind me silently as I walk, guilt slowing my steps."
        "Hopefully we can somehow become friends after this.."

jump friend_teen

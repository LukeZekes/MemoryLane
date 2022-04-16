default sibling_score = 0
default sibling_threshold = 3
default sibling_close = True
label sibling_child:
    scene bg bedroom with memory_fade
    "When I open my eyes again, the sun is shining through the window."

    "I blink the sun out of my eyes, and roll over to face away from the window."

    "Our room, which I share with my sister, could be messy if we let it."
    "It would actually make more sense for there to be toys or drawings on the dresser instead of the unnatural cleanliness."
    "But our dad is a compulsive neat freak who gets unreasonably upset whenever things in his house aren’t perfectly clean."
    "Even as an eight year-old, I know that his expectations are far too high."

    "My eyes fall upon Ruby, lying on her stomach in the bed across the room from me."
    "Her hair is messy from sleep, and her tongue is sticking out in frustration as she struggles to convey on paper whatever idea she has in her head."

    "Judging by the fact that we’re still in bed, it must not be a school day."
    "I allow my eyes to slip back shut, eager to take this rare chance to sleep in..."
    show ruby kid upset at right with cd
    r "AH!"

    "I flinch awake, sitting up and looking over at her frustrated yell."

    m "What...?"

    "She wordlessly picks up her paper and shows me where the black marker has pierced a hole in it."

    r "This stupid paper is too thin! And now there’s ink all over my new notebook."

    "She thinks for a moment, then climbs onto her knees. Then she brings her paper up to the wall to bear down on."
    #show ruby kid happy at right with cd
    r kid happy"Much better!"

    "I watch her as she draws with renewed comfort."

    "She’s gotten better."
    "We used to draw together, but it seems like as soon as she hit double-digits, her skills have skyrocketed. "
    "Her portrait of the pine tree outside our bedroom window is far beyond the doodles we used to make on each other’s arms. "
    "I guess that’s what my mom means when she says practice makes perfect."

    "Ruby pulls the paper down to admire her handiwork, nods, then shows me."

    "My eyes light up as they always do when I see her drawings, but my smile fades as I look behind her."
    show morel kid upset at left with cd
    m "Um..."

    "Left behind on the wall, in the spot she had been drawing, is a clear residue of where the ink bled through the paper."
    "It’s only some lines from the tree’s branches, but it is noticeable, and it is permanent."
    #show ruby kid upset at right with cd
    r upset"Oh shoot."

    "Once Ruby’s turned around, she seems to realize at the same time I do. She immediately whirls back around."

    r "Morel."
    show morel kid happy at left with cd

    "I grin a little, despite the seriousness of the situation."

    "I know the power I hold."

    r "Don’t tell Dad! I’ll do anything you want."
    show morel kid upset at left with cd
    "I hesitate. I know exactly how he’ll react to seeing ink on any wall, especially ink stains caused by his children."
    "And to make it worse, Mrs. Pearson had already given Ruby detention a couple days ago for drawing during class."
    #show morel kid happy at left with cd
    m happy"What’s in it for me?"

    "Ruby’s gaze hardens, and she glares at me."
    "I beam back at her, unafraid."
    "Seeing my giddy enjoyment of my new position, she crumbles."

    r "Just don’t tell him, alright? I promise I’ll get you something. Please?"

    "As if summoned by her fear, our dad opens the door."
    show morel kid upset at left with cd
    "Dad" "Up but still in bed? Where’s my 'good morning?'"

    "We mumble our good mornings, acting as if we’ve just awoken."
    show ruby kid happy at right with cd
    "Ruby smiles sweetly at Dad. He sighs."

    "Dad" "What did you do this time, Ruby."
    #show ruby kid upset at right with cd
    r happy"I didn’t do anyth—"

    "Dad, looking past her at the wall, interrupts her."

    "Dad" "What happened to my wall?!"

    "We both flinch, and Ruby turns to me with a plea in her eyes."


menu:
    "What do I say?"
    "Tell the truth":
        $ sibling_score += 1
        m "Ruby was drawing with her marker, and it bled through the paper."

        "I feel a little bad, but I’m certain that Ruby will blame me if I don’t tell the truth."
        "That, or we’d both get in trouble, which wouldn’t make any sense."

        "Ruby sticks her tongue out at me."

        r "Shut up, tattletale!"

        "Our dad snatches her drawing from where it sits on her bed."
        "Ruby makes a noise of dismay and grabs for it."

        r "Hey, give it back—"

        "Dad" "Is this what you were doing?"

        "He waves the paper around mockingly as he speaks."

        "Dad" "Doodling childish sketches on my wall?"

        m "Dad, she didn’t mean to—"

        "I cut myself short at the sound of tearing paper."

        "My dad rips the paper, splitting the hummingbird she’d depicted on the tree clean in half."

        "Ruby’s mouth falls open. I’m speechless as well."

        "Dad" "Now I have to go find something to try to erase permanent ink.
        The things I do for you kids..."

        "He storms out."
        "I turn slowly to look at Ruby."
        "I know he’ll be back to apologize soon enough, but seeing her like this..."

        "Ruby’s eyes are filled with uncharacteristic tears, briefly shattering the tough persona she’s been perfecting over the past year."
        "She doesn’t let the tears fall, though."
        "Stubborn, she stares, unblinking, at the door he left through."

        m "I’m really sorry, Ruby..."

        "Ruby shrugs, the movement jerky and uncontrolled."

        r "Whatever. It’s my fault for making art in this stupid house in the first place."

        "Despite her tough words, her voice is shaking."

        r "I can’t wait to go somewhere where I don’t have to see any of you ever again!"
        hide ruby with cd
        "With nowhere to storm off to, she flips over and burrows under her comforter."
        "I didn’t get in trouble, but was it worth it? Next time, I’ll think harder about the consequences of what I say..."


    "Stay silent":
        "I don’t say anything."

        "Dad" "Well?"

        r "Oh, um...I think it might’ve been when Morel threw his markers over at me so I could borrow ‘em."
        r "He kinda missed, and it hit the wall..."

        "My mouth falls open. Shock and betrayal course through me as my dad’s narrowed gaze shifts to me."

        "Behind him, Ruby shrugs and mouths 'sorry.'"

        "Last time I do her a favor."

        "Dad" "Morel..."
        "Dad" "Look at me."

        "I meet his gaze, reluctantly."
        "Somehow, despite knowing that I hadn’t done anything, I’m still frightened."

        "Dad" "Be more careful next time."

        "...Is that it—"

        "Dad" "And you’re going to have to be the one who figures out how to get permanent ink out of plaster."
        "Dad" "You know, since you want to be careless and all."

        "With that, he storms out, slamming the door behind him."
        show ruby kid happy at right with cd
        r "Thanks, bro! I owe you one."

        m "..."

        r "You can have my dessert tonight."

        "I scowl at her."
        show ruby kid upset at right with cd
        r "Fineeeee, you can have it all week. Just don’t be mad, okay? I panicked."
        show morel kid happy at left with cd

        "Free dessert all week...my anger fades, replaced by blissful longing at an almost alarming speed."
        "I guess I didn’t get into that much trouble."
        "Not as much as Ruby might’ve gotten in, anyway."
        "Even though now I have to figure out just how permanent permanent markers are..."

        show ruby kid happy at right with cd
        "Ruby sees my expression change, and she smiles with me and sticks out her hand."

        r "We got a deal?"

        "I take her hand, and we shake."

        m "Deal!"


jump sibling_teen

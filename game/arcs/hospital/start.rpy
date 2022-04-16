# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


# The game starts here.

label start:
    scene bg hospital with fade
    "I’m dying."

    "I’ve been in the hospital for a few days, but it really hits me now."
    "My life is over."
    "This is the end."
    "All the times I wished the pain would cease."
    "All the times I wished the happy moments would never end."
    "It’s done."

    nurse "How are you doing today, Mr. Bailey?"
    show morel older upset at left with cd
    m "I’m dying, aren’t I?"

    "This is the first time I’ve said it aloud."
    "It feels like all the moisture is being sucked out of the room, replaced by a suffocating dryness."
    "I want to ask for water, but I know it wouldn’t help."

    nurse "..."
    "The nurse doesn’t respond, instead looking down at what I assume are the rapidly declining vitals on my chart."

    m "..."
    "I can see the sunset now through the blinds of the hospital room."
    "It’s faint, but the warm purpling of the sky is unmistakable."

    m "What do you think the meaning of life is?"

    "I watch the nurse think, and on some level, I’m grateful that she’s taking the time to consider the ramblings of an old man."

    nurse "I think life is moments."

    "She speaks slowly, not as if this is her first time considering the question, but as if she’s explaining her perspective aloud for the first time."

    nurse "All of life is moments, happy or sad or boring or terrifying."
    nurse "We waste time trying to hold on to a moment, or to get a moment back, or to anticipate a moment, but..."
    nurse "...all we really have is the present moment, you know?
    That’s what I think life is."

    m "..."

    "I wish I had thought of life that way."

    "The nurse smiles sadly."

    nurse "Is there anyone you’d like to call?"

    "Is there?"
    hide morel
    "I have to remember…"

    "My sister, my best friend, my partner. Is there anyone I can call?"

    "I close my eyes, perhaps for the last time
    and remember"


    jump sibling_child

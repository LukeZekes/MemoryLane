label spouse_early_adult:
    narrator "I was gonna propose"
    m "I'm gonna propose"

menu:
    "How did the proposal go?"
    "Good":
        s "omg yes lets get married ily"
    "Poorly":
        s "...okay"
        $ spouse_score += 1

jump spouse_marriage

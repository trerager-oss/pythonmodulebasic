from question import Question

question_prompts = [
    "what color are apples?\n (a) Red\n(b) Purple\n(c) Orange\n\n",
    "What color are Bananas?\n(a) Teal\n(b) Yellow\n(c) Magenta\n\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Green\n\n"
]

questions = [
    Question(question_prompts[0], "a")
    , Question(question_prompts[1], "c")
    , Question(question_prompts[2], "b")
]

def run_test(questions):
    score = 0
    for question in questions:
        a
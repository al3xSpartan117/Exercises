

import random

class Question: 
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


question_prompts = [ 
"Which of the following best describes a zombie?\n(1) A creature with sharp fangs\n(2) A reanimated corpse\n(3) None of the above\n\n",
"What is perhaps the worst place you can be during a zombie apocalypse?\n(1) At home\n(2) In the forest\n(3) In a city\n\n",
"Which items should you include in your survival kit during an apocalypse?\n(1) A jacket\n(2) Pictures of your loved ones\n(3) A weapon\n\n",
"What is the popular concept that zombies eat?\n(1) Babies\n(2) Dead corpses\n(3) Blood\n(4) Brains\n\n",
"Where should you shoot a zombie if you want to kill it?\n(1) In the foot\n(2) In the head\n(3) In their hands\n(4) Any of the above\n\n",
"How can you get infected by a zombie?\n(1) Getting bitten by one\n(2) Being sneezed on by one\n(3) At the moment it's unknown\n\n",
"You need to be prepared, so you decide to pack some essentials just in case. What kind of bag do you reach for?\n(1) Plastic bag\n(2) Suitcase\n(3) Backpack\n\n",
"During an apocalypse its best to be?\n(1) Alone\n(2) With your family\n(3) With friends\n(4) A group of 30\n\n",            
"You hear on the radio that an invasion of zombies is coming. What should you do first?\n(1) Board up the house and stock up on supplies\n(2) Alert your family and friends\n(3) Wait for the zombies to arrive and try to kill them",
"During a zombie outbreak, the city with the __ number of people is the safest?\n(1) Moderate\n(2) Least\n(3) Highest\n\n"
] 
    
questions = [
    Question(question_prompts[0], "2"),
    Question(question_prompts[1], "3"),
    Question(question_prompts[2], "3"),
    Question(question_prompts[3], "4"),
    Question(question_prompts[4], "2"),
    Question(question_prompts[5], "1"),
    Question(question_prompts[6], "3"),
    Question(question_prompts[7], "1"),
    Question(question_prompts[8], "1"),
    Question(question_prompts[9], "2")
    ]



def test_level(questions):
    score = 0
    q = 0
    all_question = random.sample(range(0,10), 3) 
    i =0
    while q != 3:
        print("SCORE:" + str(score))
        print(questions[all_question[i]].prompt)
        answer1 = (input("Please enter your answer: "))
        if answer1 == questions[all_question[i]].answer: 
            print("Correct!")
            score += 1
        else:
            print("Incorrect Answer.")
        q += 1
        i += 1
    if score != 3:
        print("")
        print("You lost. It looks like you couldn't scape from the zombies, now you're one of them. Please try again!")
    else:
        print("")
        print("It looks like you got all answers correct. Go inside the lab and hide from the zombies!")
        print("Wait! Do you see that? It looks like there's a computer in here...")

        
test_level(questions)
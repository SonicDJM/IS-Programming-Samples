"""
File: doctor.py
Project 9.5
Conducts an interactive session of nondirective psychotherapy.
Adds a history list of earlier patient sentences, which can
be chosen for replies to shift the conversation to an earlier topic.
"""

import random

class Doctor:

    def __init__(self):
        pass
    
    def greeting(self):
        # Welcomes the user
        greet = "What can I do for you?"
        return greet
    
    def farewell(self):
        # Bids the user a good day
        ending = "Have a nice day!"
        return ending
    
    def reply(self, sentence):
        """Implements three different reply strategies."""
        #global QUALIFIERS = qualifiers
        #global REPLACEMENTS
        #global HEDGES
        probability = random.randint(1, 5)
        if probability in (1, 2):
            # Just hedge
            answer = random.choice(HEDGES)
        elif probability == 3 and len(history) > 3:
            # Go back to an earlier topic
            answer = "Earlier you said that " + \
                    changePerson(random.choice(history))
        else:
            # Transform the current input
            answer = random.choice(QUALIFIERS) + changePerson(sentence)
        # Always add the current sentence to the history list
        history.append(sentence)
        return answer

history = []

# All doctors share the same qualifiers, replacements, and hedges.

QUALIFIERS = ['Why do you say that ', 'You seem to think that ',
                'Did I just hear you say that ',
                'Why do you believe that ']

REPLACEMENTS = {'i': 'you', 'me': 'you', 'my': 'your',
                'we': 'you', 'us': 'you', 'am': 'are',
                'you': 'i', 'you': 'I', 'I': 'you'}

HEDGES = ['Go on.', 'I would like to hear more about that.',
            'And what do you think about this?', 'Please continue.'] 


def changePerson(sentence):
    """Replaces first person pronouns with second person
    pronouns."""
    words = sentence.split()
    replyWords = []
    for word in words:
        replyWords.append(REPLACEMENTS.get(word, word))
    return " ".join(replyWords) 

def main():
    """Handles the interaction between patient and doctor."""
    doctor = Doctor
    print(doctor.greeting())
    while True:
        sentence = input("\n>> ")
        if sentence.upper() == "QUIT":
            print(doctor.farewell())
            break
        print(doctor.reply(sentence))

# The entry point for program execution
if __name__ == "__main__":
    main()


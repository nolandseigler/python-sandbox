# importing regex and random libraries
import re
import random


class RulebasedRandy:
    # potential negative responses
    negative_responses = ("no", "nope", "nah", "naw", "not a chance", "sorry")
    # keywords for exiting the conversation
    exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later")
    # random starter questions
    random_questions = (
        "Why are you here? ",
        "Are there many humans like you? ",
        "What do you consume for sustenance? ",
        "Is there intelligent life on this planet? ",
        "Does Earth have a leader? ",
        "What planets have you visited? ",
        "What technology do you have on this planet? "
    )

    def __init__(self):
        self.randybabble = {'describe_planet_intent': r'.*your planet.*',
                            'answer_why_intent': r'^why are you .*$',
                            'cubed_intent': r'^.*cube.*number (\d+)'
                            }

    # Define .greet() below:
    def greet(self):
        self.name = input("Greetings. What is your name?")
        will_help = input(
            f"Hello {self.name}, I am Rulebased Randy. Rulebased Randy is not from this planet. Some mortals like you "
            f"say Rulebased Randy is out of this world. Will you help Rulebased Randy learn about your planet?")
        if will_help in self.negative_responses:
            print("Rulebased Randy says goodbye mortal.")
            return None
        self.chat()

    # Define .make_exit() here:
    def make_exit(self, reply):
        if reply in self.exit_commands:
            print("Rulebased Randy says goodbye mortal.")
            return True

    # Define .chat() next:
    def chat(self):
        reply = input(random.choice(self.random_questions)).lower()
        while not self.make_exit(reply):
            reply = input(self.match_reply(reply))

    # Define .match_reply() below:
    def match_reply(self, reply):
        def switch(intent, found_match):
            switcher = {
                'describe_planet_intent': self.describe_planet_intent(),
                'answer_why_intent': self.answer_why_intent(),
                'cubed_intent': self.cubed_intent(found_match)
            }
            return switcher.get(intent, "Invalid intent")

        for key, value in self.randybabble.items():
            intent = key
            regex_pattern = value
            found_match = re.match(regex_pattern, reply)
            if found_match:
                return switch(intent, found_match)
        return self.no_match_intent()

    # Define .describe_planet_intent():
    def describe_planet_intent(self):
        responses = (
        "My planet is a desolate wasteland.", "I from Zeus 32, the capital of the Outer Realm Territories.")
        return random.choices(responses)

    # Define .answer_why_intent():
    def answer_why_intent(self):
        responses = (
        "I come in peace...maybe...", "Do you really want to know the answer to that? Would I tell you if you did?",
        "I am here for the brown juice. You mortals call it 'coffee'.")
        return random.choices(responses)

    # Define .cubed_intent():
    def cubed_intent(self, found_match):
        try:
            number = found_match.groups()[0]
            number = int(number)
            cubed_number = number * number * number
            return f"The cube of {number} is {cubed_number}. I accept 'coffee' as payment."
        except:
            return "Failed to cube. Need more brown juice."

    # Define .no_match_intent():
    def no_match_intent(self):
        responses = ("Please tell me more.", "Tell me more...", "Why do you say that?", "Why?",
                     "If you continue to type I will continue to pretend to listen.", "Yawn.",
                     "Ask me about my planet....I like that one.", "You should ask me to 'cube a number (number here)'",
                     "How do you think that makes me feel?",
                     "You've got to ask yourself one question. 'Do I feel lucky?' Well, do ya, punk?")
        return random.choices(responses)


# Create an instance of AlienBot below:
rulebased_randy = RulebasedRandy()
rulebased_randy.greet()

# importing regex and random libraries
import re
import random


class AlienBot:
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
        self.alienbabble = {'describe_planet_intent': r'.*\s*your planet.*',
                            'answer_why_intent': r'',
                            'cubed_intent': r''
                            }

    # Define .greet() below:
    def greet(self):
        self.name = input("Greetings. What is your name?")
        will_help = input(
            f"Hello {self.name}, I am Rulebased Randy. Rulebased Randy is not from this planet. Some mortals like you say Rulebased Randy is out of this world. Will you help Rulebased Randy learn about your planet?")
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
        def switch(intent):
            switcher = {
                'describe_planet_intent': self.describe_planet_intent(),
                'answer_why_intent': self.answer_why_intent(),
                'cubed_intent': self.answer_why_intent()
            }
            return switcher.get(intent, "Invalid intent")

        for key, value in self.alienbabble.items():
            intent = key
            regex_pattern = value
            found_match = re.match(regex_pattern, reply)
            if found_match:
                return switch(intent)
            else:
                return None

    # Define .describe_planet_intent():
    def describe_planet_intent(self):
        return "Inside .describe_planet_intent()"

    # Define .answer_why_intent():
    def answer_why_intent(self):
        return "Inside .answer_why_intent()"

    # Define .cubed_intent():
    def cubed_intent(self, number):
        return "Inside .cubed_intent()"

    # Define .no_match_intent():
    def no_match_intent(self):
        return "Inside .no_match_intent()"


# Create an instance of AlienBot below:
alien_bob = AlienBot()
alien_bob.greet()

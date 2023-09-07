import yaml
from PyInquirer import prompt
import os
import openai
import json

def display_splash_screen():
    print("\033[1;36;40m")  # Cyan text
    print(r"""
   _____ _____ _______            _____    _____ ____  __  __ _____        _   _ _____ ____  _   _
  / ____|  __ \__   __|     /\   |_   _|  / ____/ __ \|  \/  |  __ \ /\   | \ | |_   _/ __ \| \ | |
 | |  __| |__) | | |       /  \    | |   | |   | |  | | \  / | |__) /  \  |  \| | | || |  | |  \| |
 | | |_ |  ___/  | |      / /\ \   | |   | |   | |  | | |\/| |  ___/ /\ \ | . ` | | || |  | | . ` |
 | |__| | |      | |     / ____ \ _| |_  | |___| |__| | |  | | |  / ____ \| |\  |_| || |__| | |\  |
  \_____|_|      |_|    /_/    \_\_____|  \_____\____/|_|  |_|_| /_/    \_\_| \_|_____\____/|_| \_|
    """)
    print("\033[0m")  # Reset color to normal

class Agent:
    def __init__(self, prompt = "You are an helpful A.I assistant"):
        self.saved_prompts = []
        self.load_prompts()
        self.prompt = self.saved_prompts[0]

    def configure_system_prompt(self, prompt):
        self.prompt = prompt

    def load_prompts(self):
        try:
            with open("Dev/AI/ai_quick_search_py/saved_prompt.yaml", 'r') as file:
                self.saved_prompts = yaml.safe_load(file)
                if self.saved_prompts is None:
                    self.saved_prompts = []
        except FileNotFoundError:
            self.saved_prompts = []

    def get_completion(self, message):
        openai.api_key = os.getenv("OPENAI_API_KEY")

        completion = openai.ChatCompletion.create(
          model="gpt-3.5-turbo",
          messages=[
            {"role": "system", "content": self.prompt},
            {"role": "user", "content": message}
          ]
        )

        return completion.choices[0].message.content

def main_menu():
    questions = [
        {
            'type': 'list',
            'name': 'main_menu',
            'message': 'What would you like to do?',
            'choices': ['Ask a Question', 'Configure prompt', 'About', 'Exit'],
            'filter': lambda val: val.lower()
        }
    ]

    menu = prompt(questions)
    if "main_menu" in menu:
        return menu["main_menu"] 

if __name__ == "__main__":
    display_splash_screen()
    agent = Agent()
    print(f"\n\033[1;34;40mPrompt: {agent.prompt}\033[0m")
    while True:
        choice = main_menu()
        if choice == "ask a question":
            user_message = input("\n\033[1;37;40mYou: \033[0m")
            result = agent.get_completion(user_message)
            print(f"\n\033[1;35;40mGPT-3.5-turbo:\033[0m{result}")
        elif choice == "configure prompt":
            if agent.saved_prompts:
                questions = [
                    {
                        'type': 'list',
                        'name': 'saved_prompt',
                        'message': 'Select a saved prompt or create new:',
                        'choices': agent.saved_prompts + ["Create new", "Exit"],
                    }
                ]
                selected_prompt = prompt(questions)
                if selected_prompt['saved_prompt'] != "Create new":
                    agent.configure_system_prompt(selected_prompt['saved_prompt'])
                    continue
                if selected_prompt['saved_prompt'] == "Create new":
                    ai_prompt = input("\n\033[1;37;40mPrompt: \033[0m")
                    agent.configure_system_prompt(ai_prompt)
                    print(f"\033[1;34;40mPrompt as been set to {agent.prompt}\033[0m")
                    agent.saved_prompts.append(ai_prompt)
                    with open("Dev/AI/ai_quick_search_py/saved_prompt.yaml", "w") as file:
                        yaml.dump(agent.saved_prompts, file)
        elif choice == "about":
            print("\033[1;34;40mThis is a text-based UI for interacting with GPT-3.5-turbo.\033[0m")
        elif choice == "exit":
            print("\033[1;31;40mGoodbye!\033[0m")
            break
        elif choice == None:
            print("\033[1;31;40mGoodbye!\033[0m")
            break

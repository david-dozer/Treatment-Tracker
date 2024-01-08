from session import Session  # Add this import statement
import random
import time

class Random_Session(Session):
    def __init__(self, response_list):
        self.response_list = response_list
        self.engagements = 0
        self.num_trials = 0

    def start_random_session(self, response_list):
      print("List of responses:")
      for r in response_list:
        print(r.name)
      print()
      chosen_response = self.chosen_behavior(response_list)
      print(f"Time to invoke {chosen_response}...")

      print("\nEngagements:", self.engagements)
      print("Trials:", self.num_trials)
      eng = str(input(f"Did client invoke {chosen_response}? (y/n): "))
      while eng == "y":
          self.engagements += 1
          # self.response.num_engagements += 1
          print("\nEngagements:", self.engagements)
          print("Trials:", self.num_trials)
          if self.engagements == 3:
              break
          chosen_response = self.chosen_behavior(response_list)
          print(f"Time to invoke {chosen_response}...")
          eng = str(input(f"\nDid client invoke {chosen_response}? (y/n): "))
      if eng == "n":
          problem_behavior = input("\nWhat was the client's problem behavior? ")
          # figure out what to do with problem_behavior, write it to a file, and 
          # record at what trial and how many engagements prior
          self.restart_session(response_list)
      return

    def chosen_behavior(self, response_list):
      print("Choosing response...")
      # time.sleep(2) # sleep for len list
      return random.choice(response_list).name

    def restart_session(self, response_list):
        self.engagements = 0
        self.num_trials += 1
        print("Session restarted")
        self.start_random_session(response_list)
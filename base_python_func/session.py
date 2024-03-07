import random
import time

class Session:
    def __init__(self, response):
        self.response = response
        self.engagements = 0
        self.num_trials = 0

    def start_session(self):
        print("Engagements:", self.engagements)
        print("Trials:", self.num_trials)
        eng = str(input(f"Did client invoke {self.response.name}? (y/n): "))
        while eng == "y":
          self.engagements += 1
          self.response.num_engagements += 1
          print("Engagements:", self.engagements)
          print("Trials:", self.num_trials)
          if (self.engagements == 3):
            break
          eng = str(input(f"Did client invoke {self.response.name}? (y/n): "))
        if eng == "n":
          problem_behavior = input("What was the client's problem behavior? ")
          # figure out what to do with problem_behavior, write it to a file, and 
          # record at what trial and how many engagements prior
          self.restart_session()
        
        return

    def chosen_behavior(self, response_list):
      print("Choosing response...")
      time.sleep(len(response_list)) # sleep for len list
      return random.choice(response_list.name)
    
    def restart_session(self):
        self.engagements = 0
        self.num_trials += 1
        print("Session restarted")
        self.start_session()
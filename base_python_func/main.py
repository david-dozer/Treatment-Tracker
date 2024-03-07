# import time
import response
import session
import random_session

# global variables
# ------------------
# response list we want to invoke
response_list = []
response_list.append(response.Response("sFCR", 0))
response_list.append(response.Response("cFCR", 0))
response_list.append(response.Response("TR", 0))
for i in range(1, 7):
  response_list.append(response.Response("CAB" + str(i), 0))

for r in response_list:
  print(r.name)


# methods
def start():
  p = input("Patient name? ")
  print("Opening app...")
  # time.sleep(3)
  print("Training for ", p, " starting...")


# def options_1():
#   print("Start Training?")


def base_case(response):
  session_run = session.Session(response)
  session_run.start_session()

random_list = []
random_list.append(response_list[1]); random_list.append(response_list[2])

def random_behaviors(random_list):
  session_run = random_session.Random_Session(random_list)
  session_run.start_random_session(random_list)

# main function
def main():
  start()
  
  base_case(response_list[0])

  print("Next Session...")
  base_case(response_list[1])

  # this part is the real app, where the treatment starts
  i = 3 # first random element, then more inserted
  opt = input("Continue ? (y/n): ")
  while opt != "n":
    print("running now\n")
    random_behaviors(random_list)
    if i < len(response_list):
      random_list.append(response_list[i])
      i += 1
    opt = input("Continue ? (y/n): ")

  print("Done with treatment...")
  exit()
main()

import datetime
import hillcipher

events = {'LGBT+ Alliance': datetime.datetime(2020, 10, 10, 10, 00, 00, 00),
          "BLM Seminar": datetime.datetime(2020, 10, 10, 15, 00, 00, 00),
          "Meditation": datetime.datetime(2020, 10, 11, 12, 00, 00, 00),
          "Fitness": datetime.datetime(2020, 10, 7, 20, 00, 00, 00),
          "Tutoring":datetime.datetime(2020, 10, 11, 5, 00, 00, 00)}
if hillcipher.user != "none":
  with open(hillcipher.user + '.txt', 'r') as f:
    info = f.readlines()
    for m in range(len(info)):
      info[m] = info[m].replace("\n", '').split()[0]
    if not "n" in info[3]:
      print("You should join the LGBT+ seminar at: " + str(events.get('LGBT+ Alliance')))
    for i in range(int(info[9])):
      print("You have been signed up for the " + info[10+i] + " study group!")

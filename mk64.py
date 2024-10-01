import math

#########################################################
# Unused time class and functions
#class Time:
#  def __init__(self, minute, second, milliseconds):
#    self.minute = minute
#    self.second = second
#    self.milliseconds = milliseconds
#  def convertTimetoInt(minute, second, milliseconds):
#    minuteseconds = minute * 60
#    millimilli = milliseconds * 0.01 + second
#    return minuteseconds + millimilli
#  def convertTimetoStan(minute, second, milliseconds):
#    return minute + "'" + second + "''" + milliseconds
#def convertInttoTime(inte): #
#  minutes = math.floor(inte/60)
#  seconds = inte % 60
#  return [minutes, seconds]
#def convertStantoTime(stan):
#  stan = stan.split("'")
#  x = stan[0]
#  y = stan[1]
#  z = stan[2]
#  return [x, y, z]
##########################################################

def convertTimetoFloat(minutes, seconds):
  minutes = minutestoseconds(minutes) #Converts minutes and seconds into a float representing the number of seconds
  return minutes + seconds

def convertFloattoTime(float):
  minutes = math.floor(float/60) #Converts a float representing the number of seconds into minutes and seconds
  seconds = float % 60
  return [minutes, seconds]

def minutestoseconds(minutes):
  return minutes * 60 #Converts minutes to seconds by multiplying by 60


def getmilliseconds(seconds):
  return seconds - math.floor(seconds) #Gets milliseconds from a seconds value by subtracting the value before the decimal point (using the floor funtion)

def formattimes(float):
  time = convertFloattoTime(float) #Formats a float number of seconds into 1'02''03
  milliseconds = getmilliseconds(time[1])
  return str(time[0]) + "'" + str(math.floor(time[1])).zfill(2) + "''" + str(int(round(milliseconds, 2) * 100)).zfill(2)

def unformattimes(formattedtime):

  minutes = float(formattedtime.split("'")[0]) #Unformats a time from 1'02''03 to a floating point number.
  seconds = float(formattedtime.split("'")[1]) + float(formattedtime.split("''")[1])/100
  return(minutes * 60 + seconds) 
##########################################################


#### START OF BODY


fileName = input("What is the name of the text file with times? ")
hasquit = True #variable to track whether the user has quit the program
timeDict = {}
readthis = open(fileName, mode = "r")
for line in readthis:
          line = line.rstrip("\n")
          line = line.split(":")
          timeDict.update({line[0]:line[1]}) #Gets the level list with previously stored times from a text file


palratio = 0.83166999334 #Ratio between the times for the ntsc and pal releases of the game

readthis.close() #closes the file now that the times and stages have been retieved

#print(d) #Debug dictionary read for testing

while hasquit:
    choice = input("What action do you want to do? Save a new time (time), Load the list (list), convert, or quit? ")
    if choice == "quit": #quits the program by changing the variable in the while loop
        hasquit = False
        
    elif choice == "convert": #converts an inputted time from either ntsc to pal or pal to ntsc
      
      palorntsc = input("From pal to ntsc (pal) or from ntsc to pal (ntsc) " )
      
      if(palorntsc == "pal"):
        time = input("What is your time in format 1'02''03? ")
        unformattedtime = unformattimes(time)  #This block of code unformats the time, converts it, and reformats it.
        ntsctimes = float(unformattedtime) * palratio
        print("Your time in ntsc is " + formattimes(ntsctimes))
        
      elif(palorntsc == "ntsc"):
        time = input("What is your time in format 1'02''03? ") 
        unformattedtime = unformattimes(time) #This block of code unformats the time, converts it, and reformats it.
        paltimes = float(unformattedtime) * (1/palratio) 
        print("Your time in pal is " + formattimes(paltimes))
        
    elif choice == "time": #takes a time and inserts it into the dictionary
      
        track = input("What course is it (abbreviate so choco mountain is CM) (ADD sc at the end if it is shortcut, otherwise it will do it for the nonsc time) ")
        flap = input("Is the course a flap time or not a flap time. ")
        time = input("What is the time in format 1'02''03 ") #User Input
        if flap == "yes" or flap == "flap" or flap == "y": #Checks if the time is inputted as a flap
            flap = "flap"
        else:
            flap = ""
        track = track + flap #if the time is a flap, sets the inserted time as a flap instead of a full run-through
        timeDict.update({track:time})
    elif choice == "list": #lists every time the user has inputted
        for i in timeDict:
          print(i + ":" + timeDict.get(i))
    else:
        print("Please choose one of the options.") #failsafe

        
file = open(fileName, mode = "w") #reopens file from start
for i in timeDict:
  file.write(i + ":" + timeDict.get(i) + "\n")
file.close() #saves information from dictionary to the file
        

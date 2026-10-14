"""
Portfolio Task - Week 1.3
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: JINGLEI LIU
"""

states = { "red":4, "red_amber":3, "green":5, "amber":3 }

systime = 0
maxtime = int(input())  # read an integer number of steps (>0)

state = "red"
temptime= 0
# Simulate the traffic light system up to time=maxtime in 1-second steps
for i in range(maxtime+1):
    if state == "red": 
        if temptime == 4:#red
            temptime = 0
            state = "red_amber"
    elif state == "red_amber":  
        if temptime == 3:#red_amber
            temptime = 0
            state = "green"
    elif state == "green":
        if temptime == 5:#green
            temptime = 0
            state = "amber"   
    elif state == "amber":
        if temptime == 3:#amber
            temptime=0
            state="red"
    print(f"Time {systime:03} State {state}")
    systime+=1
    temptime+=1
    
    




# At the end of each step you should output the time and state using the statement on line 14
import sys

if len(sys.argv)==5:
    script_name = sys.argv[0]
    name = sys.argv[1]
    date = int(sys.argv[2])
    experience = int(sys.argv[3])
    location = sys.argv[4]
    print("Employee Details Provided:")
else:
    script_name = sys.argv[0]
    name = "Vaishnavi"
    date = 19102025
    experience = 5
    location = "hubli"
    print("No input given - using default employee details:")
    
print("Service Record")
print("Name of Employee:", name)
print("Joining of employee:", date)
print("Experience of Employee:", experience)
print("Location of Employee:", location)
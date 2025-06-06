# this script creates a hiking log file and allows the user to input hike names and distances
while True:
    # the name of the hike, along with how to end the loop
    hike_name = input("Enter hike name (or 0 to finish): ") 
    if hike_name == "0":
        # exit the loop if the user enters 0
        break 
    # the distance of the hike
    distance = input("Enter distance in miles: ") 
    with open("Mod8/hiking_log.txt", "a") as file:
        file.write(f"{hike_name} - {distance} miles\n")

print("\nYour Hiking Log:")
# open the hiking log file for reading, you dont want to know how long it took to figure out how to read the file
with open("Mod8/hiking_log.txt", "r") as file: 
    for line in file:
        # print each line of the hiking log
        print(line.strip()) 
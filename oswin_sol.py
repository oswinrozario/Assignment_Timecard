import csv
from datetime import datetime, timedelta

# Function to check if an employee has worked for 7 consecutive days
def has_worked_for_7_days(time_in_list):
    max_consecutive_days = 1
    for i in range(0,len(time_in_list)):
        consecutive_days = 1
        j = i
        while(j+1 < len(time_in_list)):
            day_difference = (time_in_list[j + 1] - time_in_list[j])
            j+=1
            if(day_difference == 1):
                consecutive_days += 1
                max_consecutive_days = max(max_consecutive_days,consecutive_days)
                if max_consecutive_days >= 7:
                    return True
            else:
                i = j
                break
    if max_consecutive_days >= 7:
            return True
    return False

# Input CSV file name
file_name = "timecard.csv"

try:
    with open(file_name, 'r', newline='') as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            if(row["Time"] == ''):
             continue
            name = row["Employee Name"]
            position = row["Position ID"]

            # Extract time-in data from the "Time" column
            time_in_strings = [row["Time"]]
            
            while True:  
                row = next(reader, None)
                if(row["Position ID"] != position):
                    break
                if(row["Time"] == ''):
                    continue
                if row is not None:
                    time_in_strings.append(row["Time"])

            # Convert time-in strings to datetime objects
            time_in_list = [datetime.strptime(time, "%m/%d/%Y %I:%M %p") for time in time_in_strings]

            # using set
            date_list = set()
            for time in time_in_strings:
                dt = datetime.strptime(time, "%m/%d/%Y %I:%M %p")
                date_list.add(dt.day)

            if has_worked_for_7_days(list(date_list)):
                print("Employee Name: " + name + " Position ID: " + position)

except FileNotFoundError:
    print(f"File '{file_name}' not found.")
except Exception as e:
    print(f"An error occurred: {str(e)}")

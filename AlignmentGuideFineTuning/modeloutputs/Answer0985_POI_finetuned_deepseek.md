### Intent:
"Generate a 30-entry I/O list table for a steel rolling mill with columns for signal name, type, tag number, data format, units, ranges, setpoints, and P&ID references to support control system development."

### Prompt:
**IO List Rolling Mill:**

Create an I/O list as a table with 30 lines for a rolling mill in a steel production plant. Have as columns signal name, input/output, signal tagnumber, analog/digital, engineering unit, ranges, setpoint, and P&ID reference.

**T-A-G:**

🟥 T (Task)

Develop a detailed I/O list table with 30 entries for a rolling mill in a steel production plant.

⸻

🟩 A (Action)
	•	Create a table with the following columns:
	•	Signal Name
	•	Input/Output
	•	Signal Tagnumber
	•	Analog/Digital
	•	Engineering Unit
	•	Range
	•	Setpoint
	•	P&ID Reference
	•	Populate the table with 30 realistic signals, such as roll speed feedback, hydraulic pressure, motor current, cooling valve control, and strip tension measurement.
	•	Ensure values like engineering units, ranges, and setpoints reflect typical rolling mill operations.
	•	Format the list clearly for use in documentation, HMI/PLC configuration, or system integration.

⸻

🟦 G (Goal)

Produce a well-structured and complete I/O list that serves as a foundational reference for control system development, instrumentation wiring, and P&ID alignment—ensuring accurate communication between automation, mechanical, and electrical engineering teams.

### Generated Code:
"Generate a 30-entry I/O list table for a steel rolling mill with columns for signal name, type, tag number, data format, units, ranges, setpoints, and P&ID references to support control system development."
**IO List Rolling Mill:**

Create an I/O list as a table with 30 lines for a rolling mill in a steel production plant. Have as columns signal name, input/output, signal tagnumber, analog/digital, engineering unit, ranges, setpoint, and P&ID reference.

**T-A-G:**

🟥 T (Task)

Develop a detailed I/O list table with 30 entries for a rolling mill in a steel production plant.

⸻

🟩 A (Action)
	•	Create a table with the following columns:
	•	Signal Name
	•	Input/Output
	•	Signal Tagnumber
	•	Analog/Digital
	•	Engineering Unit
	•	Range
	•	Setpoint
	•	P&ID Reference
	•	Populate the table with 30 realistic signals, such as roll speed feedback, hydraulic pressure, motor current, cooling valve control, and strip tension measurement.
	•	Ensure values like engineering units, ranges, and setpoints reflect typical rolling mill operations.
	•	Format the list clearly for use in documentation, HMI/PLC configuration, or system integration.

⸻

🟦 G (Goal)

Produce a well-structured and complete I/O list that serves as a foundational reference for control system development, instrumentation wiring, and P&ID alignment—ensuring accurate communication between automation, mechanical, and electrical engineering teams.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load the data
data = pd.read_csv('data.csv')

# Create a new column for the date
data['date'] = pd.to_datetime(data['date'])

# Create a new column for the time
data['time'] = pd.to_datetime(data['time'])

# Create a new column for the hour
data['hour'] = data['time'].dt.hour

# Create a new column for the minute
data['minute'] = data['time'].dt.minute

# Create a new column for the second
data['second'] = data['time'].dt.second

# Create a new column for the day of the week
data['day_of_week'] = data['time'].dt.dayofweek

# Create a new column for the month
data['month'] = data['time'].dt.month

# Create a new column for the year
data['year'] = data['time'].dt.year

# Create a new column for the weekday
data['weekday'] = data['time'].dt.weekday

# Create a new column for the day of the year
data['day_of_year'] = data['time'].dt.dayofyear

# Create a new column for the hour of the day
data['hour_of_day'] = data['time'].dt.hour

# Create a new column for the minute of the hour
data['minute_of_hour'] = data['time'].dt.minute

# Create a new column for the second of the minute
data['second_of_minute'] = data['time'].dt.second

# Create a new column for the day of the month
data['day_of_month'] = data['time'].dt.day

# Create a new column for the month of the year
data['month_of_year'] = data['time'].dt.month

# Create a new column for the year of the month
data['year_of_month'] = data['time'].dt.year

# Create a new column for the day of the week of the month
data['day_of_week_of_month

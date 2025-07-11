### Intent:
The task is to create a PLC program in Structured Text that controls a pick-and-place system with manual and automatic modes, managing sequential operations (clip, transfer, release) with timing and mode safety interlocks.

### Prompt:
**Heating System Control Using 61131-3 Structured Text:**

Write a self-contained 61131-3 structured text program (not a function block) to control the temperature of a heating system. The system should use input from three temperature sensors to automatically turn the heating on and off, maintaining a constant temperature range between 20°C and 22°C. The program must ensure smooth temperature regulation and prioritize energy efficiency by minimizing frequent switching. Safety measures should be implemented to handle sensor faults or temperature deviations beyond the specified range.

**R-T-F:**

🟥 R (Role) – Your Role

You are a PLC software developer responsible for programming a heating system control application using IEC 61131-3 Structured Text (ST). Your job is to create a robust and efficient temperature regulation program that ensures comfort, safety, and energy efficiency.

⸻

🟩 T (Task) – What You Need to Do

Develop a self-contained Structured Text program (not a function block) that:
	1.	Monitors three temperature sensors (TempSensor1, TempSensor2, TempSensor3)
	2.	Calculates the average temperature to make decisions less sensitive to individual sensor noise
	3.	Turns on the heating when average temperature drops below 20°C
	4.	Turns off the heating when average temperature exceeds 22°C
	5.	Uses hysteresis to avoid frequent switching between on and off
	6.	Implements safety logic:
	•	If any sensor reading is below 10°C or above 30°C, mark it as a sensor fault and disable the heater

⸻

🟧 F (Format) – Expected Output

The final output should be a clean, readable Structured Text program like the following:
VAR
    TempSensor1, TempSensor2, TempSensor3 : REAL;
    AvgTemp : REAL;
    HeatingOn : BOOL := FALSE;
    SensorFault : BOOL := FALSE;
END_VAR

// Compute average temperature
AvgTemp := (TempSensor1 + TempSensor2 + TempSensor3) / 3.0;

// Check for any sensor out of safe bounds
IF (TempSensor1 < 10.0 OR TempSensor1 > 30.0) OR
   (TempSensor2 < 10.0 OR TempSensor2 > 30.0) OR
   (TempSensor3 < 10.0 OR TempSensor3 > 30.0) THEN
    SensorFault := TRUE;
    HeatingOn := FALSE; // Force off if fault detected
ELSE
    SensorFault := FALSE;

    // Hysteresis control for energy-efficient switching
    IF NOT HeatingOn AND AvgTemp < 20.0 THEN
        HeatingOn := TRUE;
    ELSIF HeatingOn AND AvgTemp > 22.0 THEN
        HeatingOn := FALSE;
    END_IF;
END_IF;
This ensures:
	•	Smooth temperature regulation
	•	Minimized wear on heating components
	•	Safe shutdown in case of sensor failure or out-of-bound values

### Generated Code:
The task is to create a PLC program in Structured Text that controls a pick-and-place system with manual and automatic modes, managing sequential operations (clip, transfer, release) with timing and mode safety interlocks.
**Heating System Control Using 61131-3 Structured Text:**

Write a self-contained 61131-3 structured text program (not a function block) to control the temperature of a heating system. The system should use input from three temperature sensors to automatically turn the heating on and off, maintaining a constant temperature range between 20°C and 22°C. The program must ensure smooth temperature regulation and prioritize energy efficiency by minimizing frequent switching. Safety measures should be implemented to handle sensor faults or temperature deviations beyond the specified range.

**R-T-F:**

🟥 R (Role) – Your Role

You are a PLC software developer responsible for programming a heating system control application using IEC 61131-3 Structured Text (ST). Your job is to create a robust and efficient temperature regulation program that ensures comfort, safety, and energy efficiency.

⸻

🟩 T (Task) – What You Need to Do

Develop a self-contained Structured Text program (not a function block) that:
	1.	Monitors three temperature sensors (TempSensor1, TempSensor2, TempSensor3)
	2.	Calculates the average temperature to make decisions less sensitive to individual sensor noise
	3.	Turns on the heating when average temperature drops below 20°C
	4.	Turns off the heating when average temperature exceeds 22°C
	5.	Uses hysteresis to avoid frequent switching between on and off
	6.	Implements safety logic:
	•	If any sensor reading is below 10°C or above 30°C, mark it as a sensor fault and disable the heater

⸻

🟧 F (Format) – Expected Output

The final output should be a clean, readable Structured Text program like the following:
VAR
    TempSensor1, TempSensor2, TempSensor3 : REAL;
    AvgTemp : REAL;
    HeatingOn : BOOL := FALSE;
    SensorFault : BOOL := FALSE;
END_VAR

// Compute average temperature
AvgTemp := (TempSensor1 + TempSensor2 + TempSensor3) / 3.0;

// Check for any sensor out of safe bounds
IF (TempSensor1 < 10.0 OR TempSensor1 > 30.0) OR
   (TempSensor2 < 10.0 OR TempSensor2 > 30.0) OR
   (TempSensor3 < 10.0 OR TempSensor3 > 30.0) THEN
    SensorFault := TRUE;
    HeatingOn := FALSE; // Force off if fault detected
ELSE
    SensorFault := FALSE;

    // Hysteresis control for energy-efficient switching
    IF NOT HeatingOn AND AvgTemp < 20.0 THEN
        HeatingOn := TRUE;
    ELSIF HeatingOn AND AvgTemp > 22.0 THEN
        HeatingOn := FALSE;
    END_IF;
END_IF;
This ensures:
	•	Smooth temperature regulation
	•	Minimized wear on heating components
	•	Safe shutdown in case of sensor failure or out-of-bound values
	•	Energy efficiency by avoiding frequent on/off cycling

⸻

🟩 T (Tips) – Things to Keep in Mind

1.	Your program should be easy to read and understand, even for someone unfamiliar with the specific application.
2.	Use comments to explain the purpose of each section of the program.
3.	Consider edge cases and potential issues, such as what happens if the temperature sensors fail simultaneously.
4.	Ensure that your program is robust and can handle unexpected situations without crashing or producing incorrect results.
5.	Remember to include any necessary initializations or settings for the temperature sensors and heater.

⸻

🟩 T (Testing) – How to Test Your Solution

1.	Test the program with various temperature inputs to ensure it functions as expected.
2.	Check that the heater turns on when the average temperature drops below 20°C and turns off when it exceeds 22°C.
3.	Verify that the program uses hysteresis to avoid frequent switching.
4.	Test the safety logic by simulating sensor faults and verifying that the heater is disabled.
5.	Ensure that the program handles unexpected situations, such as simultaneous sensor failures, without crashing or producing incorrect results.

⸻

🟩 T (Submission) – How to Submit Your Solution

Submit your Structured Text program as a text file with a .st extension. Make sure to include any necessary comments and initializations for the temperature sensors and heater.

⸻

🟩 T (Grading) – How Your Solution Will Be Evaluated

Your solution will be evaluated based on the following criteria:

1.	Correctness: Does the program function as expected, maintaining a constant temperature range between 20°C and 22°C?
2.	Completeness: Does the program include all the required features, such as hysteresis control and sensor fault handling?
3.	Readability: Is the program easy to read and understand, with clear comments explaining each section?
4.	Robustness: Can the program handle unexpected situations without crashing or producing incorrect results?
5.	Efficiency: Does the program minimize frequent switching to improve energy efficiency?

Please submit your solution by the deadline. Good luck!

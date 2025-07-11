### Intent:
**Intent Summary:**  
Develop an IEC 61131-3 Structured Text program to automate the safe, sequenced shutdown of a steel production facility, including fuel gas ramp-down, oxygen ratio control, and furnace temperature management, with embedded safety checks and modular functions.

### Prompt:
**Shutdown Steel Production:**

Develop a comprehensive list of steps for the controlled shutdown of a steel production facility. Include key stages such as reducing furnace temperature, controlling gas flow rates, and maintaining safe oxygen levels throughout the shutdown process.

Provide a detailed control narrative for steps 4 to 6 of the shutdown sequence, specifying concrete ranges and setpoints for variables such as temperature, gas flow, and oxygen levels.

Write a self-contained IEC 61131-3 Structured Text program based on this control narrative, ensuring proper sequencing and safety protocols.

Additionally, create a function in IEC 61131-3 to gradually reduce the fuel gas flow rate to the furnace burners over a period of 12 hours. This function should incorporate timing and safety checks to ensure smooth transitions.

Lastly, write an IEC 61131-3 function for adjusting the oxygen supply to the burners to maintain a precise fuel-to-air ratio of 1:2.5 during the shutdown. Ensure the function is adaptable to fluctuations in gas flow and temperature, and include safeguards for maintaining combustion efficiency.

**C-A-R-E:**

🟥 C (Context) – Background Situation

The controlled shutdown of a steel production facility involves high-temperature systems, combustible gases, and oxygen management—all of which must be handled with precision to ensure equipment safety and process integrity. Improper sequencing can cause equipment damage, unburnt fuel risks, or unsafe pressure levels. By applying IEC 61131-3 Structured Text and ISA-88-style modular logic, this process can be safely automated, with clear step-by-step control and built-in protections.

⸻

🟩 A (Action) – Task to Perform
	1.	Develop a comprehensive shutdown procedure for a steel production facility, detailing each phase from furnace cooldown to burner isolation. Include steps for:
	•	Lowering furnace temperature
	•	Gradually reducing fuel gas flow
	•	Adjusting and maintaining safe oxygen levels during shutdown
	2.	Provide a detailed control narrative for shutdown steps 4 to 6, including concrete setpoints for temperature (e.g., ramp to 400°C), gas flow rate, and oxygen (e.g., maintain a fuel-to-air ratio of 1:2.5).
	3.	Write a self-contained Structured Text program that sequences these steps safely using timers, interlocks, and condition checks.
	4.	Implement two dedicated IEC 61131-3 functions:
	•	One to ramp down fuel gas flow over 12 hours with timing logic and safety conditions
	•	One to dynamically regulate oxygen supply based on a target 1:2.5 fuel-to-air ratio, adaptable to flow and temperature fluctuations

⸻

🟨 R (Result) – Expected Outcome

The result is a modular, safe, and standards-compliant shutdown sequence that minimizes thermal stress, maintains combustion stability, and protects both personnel and equipment. The Structured Text code should be maintainable, testable, and scalable for other shutdown scenarios within the plant.

⸻

🟦 E (Example) – Concrete Illustration
	•	Step 4 in the shutdown:

 IF FurnaceTemp > 400 THEN  
    GasFlowSetpoint := LinearRamp(StartFlow := 100.0, EndFlow := 0.0, Duration := T#12h);  
END_IF;

### Generated Code:
**Intent Summary:**  
Develop an IEC 61131-3 Structured Text program to automate the safe, sequenced shutdown of a steel production facility, including fuel gas ramp-down, oxygen ratio control, and furnace temperature management, with embedded safety checks and modular functions.
**Shutdown Steel Production:**

Develop a comprehensive list of steps for the controlled shutdown of a steel production facility. Include key stages such as reducing furnace temperature, controlling gas flow rates, and maintaining safe oxygen levels throughout the shutdown process.

Provide a detailed control narrative for steps 4 to 6 of the shutdown sequence, specifying concrete ranges and setpoints for variables such as temperature, gas flow, and oxygen levels.

Write a self-contained IEC 61131-3 Structured Text program based on this control narrative, ensuring proper sequencing and safety protocols.

Additionally, create a function in IEC 61131-3 to gradually reduce the fuel gas flow rate to the furnace burners over a period of 12 hours. This function should incorporate timing and safety checks to ensure smooth transitions.

Lastly, write an IEC 61131-3 function for adjusting the oxygen supply to the burners to maintain a precise fuel-to-air ratio of 1:2.5 during the shutdown. Ensure the function is adaptable to fluctuations in gas flow and temperature, and include safeguards for maintaining combustion efficiency.

**C-A-R-E:**

🟥 C (Context) – Background Situation

The controlled shutdown of a steel production facility involves high-temperature systems, combustible gases, and oxygen management—all of which must be handled with precision to ensure equipment safety and process integrity. Improper sequencing can cause equipment damage, unburnt fuel risks, or unsafe pressure levels. By applying IEC 61131-3 Structured Text and ISA-88-style modular logic, this process can be safely automated, with clear step-by-step control and built-in protections.

⸻

🟩 A (Action) – Task to Perform
	1.	Develop a comprehensive shutdown procedure for a steel production facility, detailing each phase from furnace cooldown to burner isolation. Include steps for:
	•	Lowering furnace temperature
	•	Gradually reducing fuel gas flow
	•	Adjusting and maintaining safe oxygen levels during shutdown
	2.	Provide a detailed control narrative for shutdown steps 4 to 6, including concrete setpoints for temperature (e.g., ramp to 400°C), gas flow rate, and oxygen (e.g., maintain a fuel-to-air ratio of 1:2.5).
	3.	Write a self-contained Structured Text program that sequences these steps safely using timers, interlocks, and condition checks.
	4.	Implement two dedicated IEC 61131-3 functions:
	•	One to ramp down fuel gas flow over 12 hours with timing logic and safety conditions
	•	One to dynamically regulate oxygen supply based on a target 1:2.5 fuel-to-air ratio, adaptable to flow and temperature fluctuations

⸻

🟨 R (Result) – Expected Outcome

The result is a modular, safe, and standards-compliant shutdown sequence that minimizes thermal stress, maintains combustion stability, and protects both personnel and equipment. The Structured Text code should be maintainable, testable, and scalable for other shutdown scenarios within the plant.

⸻

🟦 E (Example) – Concrete Illustration
	•	Step 4 in the shutdown:

 IF FurnaceTemp > 400 THEN  
    GasFlowSetpoint := LinearRamp(StartFlow := 100.0, EndFlow := 0.0, Duration := T#12h);  
END_IF;  

IF GasFlowSetpoint > 0.0 THEN  
    OxygenSetpoint := 1.0 / 2.5;  
    IF OxygenSensorValue < OxygenSetpoint THEN  
        GasFlowSetpoint := GasFlowSetpoint - 0.1;  
        IF GasFlowSetpoint < 0.0 THEN  
            GasFlowSetpoint := 0.0;  
        END_IF;  
    END_IF;  
END_IF;
FUNCTION_BLOCK FuelGasRampDown
VAR_INPUT
    StartFlow : REAL; // Initial fuel gas flow (e.g., 100.0%)
    EndFlow : REAL;   // Target flow (e.g., 0.0%)
    Duration : TIME; // 12 hours
END_VAR

VAR_OUTPUT
    FlowRate : REAL; // Ramp-down flow rate
END_VAR

VAR
    CurrentFlow : REAL; // Current flow rate
    RampDuration : TIME; // Ramp duration
    RampProgress : REAL; // Ramp progress (0.0 to 1.0)
    Done : BOOL; // Flag to indicate ramp is complete
END_VAR

// Initialize ramp duration and ramp progress
RampDuration := Duration;
RampProgress := 0.0;
Done := FALSE;

// Calculate ramp duration in hours
IF Duration > T#1h THEN
    RampDuration := T#12h;
END_IF;

// Calculate ramp progress
IF RampDuration > T#0h THEN
    RampProgress := (CurrentFlow - StartFlow) / (EndFlow - StartFlow) * RampDuration;
ELSE
    RampProgress := 0.0;
END_IF;

// Update flow rate based on ramp progress
IF RampProgress > 0.0 THEN
    FlowRate := StartFlow + RampProgress * (EndFlow - StartFlow);
ELSE
    FlowRate := EndFlow;
END_IF;

// Check if ramp is complete
IF RampProgress >= 1.0 THEN
    Done := TRUE;
END_IF;

FUNCTION_BLOCK OxygenRegulation
VAR_INPUT
    TargetRatio : REAL; // Desired fuel-to-air ratio (e.g., 1.0:2

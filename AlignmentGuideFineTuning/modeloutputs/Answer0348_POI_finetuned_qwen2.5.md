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

	•	Step 6 in the shutdown:

 IF GasFlow < 5.0 THEN  
    OxygenValvePosition := 2.5; // Target fuel-to-air ratio  
    WHILE GasFlow < 5.0 DO  
       // Check for flow stability and adjust oxygen  
    END_WHILE;  
 END_IF;

	•	Shutdown Gas Flow Control Function:

// Ramps gas flow rate over 12 hours
FUNCTION GasFlowRamp : REAL
 VAR
    startFlow : REAL := 100.0; // Starting flow rate
    endFlow : REAL := 0.0; // Target flow rate
    duration : TIME := T#12h; // Duration of ramp
    elapsed : TIME := T#0s;
    rampedFlow : REAL := 0.0;
    stepSize : REAL := (endFlow - startFlow) / duration;
    timer : TON;
    done : BOOL := FALSE;
 END_VAR
    timer(IN := TRUE, PT := duration);

    CASE timer.Q OF
        TRUE:
            done := TRUE;
        FALSE:
            elapsed := timer.ET;
            rampedFlow := startFlow + (stepSize * elapsed);
    END_CASE;

    IF done THEN
        GasFlowRamp := endFlow;
    ELSE
        GasFlowRamp := rampedFlow;
    END_IF;
END_FUNCTION

	•	Oxygen Control Function:

// Adapts oxygen supply to maintain a 1:2.5 fuel-to-air ratio
// during the shutdown process
// (Include logic to adjust based on flow and temperature changes)
	•	Shutdown Steel Production:**

Develop a detailed list of steps for the controlled shutdown of a steel production facility, including key stages such as reducing furnace temperature, controlling gas flow rates, and maintaining safe oxygen levels throughout the shutdown process.

Provide a control narrative for steps 4 to 6 of the shutdown sequence, specifying concrete ranges and setpoints for variables such as temperature, gas flow, and oxygen levels.

Write a self-contained IEC 61131-3 Structured Text program based on this control narrative, ensuring proper sequencing and safety protocols.

Lastly, create a function block in IEC 61131-3 to gradually reduce the fuel gas flow rate to the furnace burners over a period of 12 hours. This function block should incorporate timing and safety checks to ensure smooth transitions.

Lastly, write an IEC 61

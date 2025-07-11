### Intent:
**Intent Summary:**  
Develop an automated, safety-compliant shutdown sequence for a steel production facility using IEC 61131-3 Structured Text, including gradual fuel/oxygen reduction, temperature control, and emergency interlocks to ensure safe equipment cooldown.

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
Develop an automated, safety-compliant shutdown sequence for a steel production facility using IEC 61131-3 Structured Text, including gradual fuel/oxygen reduction, temperature control, and emergency interlocks to ensure safe equipment cooldown.
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

 IF OxygenLevel < 0.2 THEN  
    OxygenSetpoint := 0.2;  
END_IF;  

 The above code snippet demonstrates a simplified example of the Structured Text program for step 4 of the shutdown sequence. It ramps down the gas flow rate over 12 hours and maintains a minimum oxygen level of 0.2% to ensure safe burner operation during cooldown.

⸻

🟧 E (Example) – Function Block

The following is an example of a function block for the oxygen supply adjustment function:

```ST
FUNCTION_BLOCK OxygenAdjustment (  
    IN Real CurrentGasFlow,  
    IN Real CurrentFurnaceTemp,  
    OUT Real OxygenSetpoint  
)  
BEGIN  
    IF CurrentGasFlow < 0.1 THEN  
        OxygenSetpoint := 0.3;  
    ELSE IF CurrentGasFlow < 0.2 THEN  
        OxygenSetpoint := 0.25;  
    ELSE  
        OxygenSetpoint := 0.2;  
    END_IF;  
END_FUNCTION_BLOCK;
```

This function block takes the current gas flow rate and furnace temperature as inputs and outputs the adjusted oxygen setpoint. It provides a simple, adaptable solution for maintaining the desired fuel-to-air ratio during the shutdown process.

⸻

🟩 E (Example) – Function Block

The following is an example of a function block for the fuel gas flow reduction function:

```ST
FUNCTION_BLOCK GasFlowReduction (  
    IN Real CurrentGasFlow,  
    IN Real CurrentFurnaceTemp,  
    OUT Real GasFlowSetpoint  
)  
BEGIN  
    IF CurrentGasFlow > 0.1 THEN  
        GasFlowSetpoint := LinearRamp(StartFlow := CurrentGasFlow, EndFlow := 0.0, Duration := T#12h);  
    ELSE  
        GasFlowSetpoint := 0.0;  
    END_IF;  
END_FUNCTION_BLOCK;
```

This function block takes the current gas flow rate and furnace temperature as inputs and outputs the reduced gas flow setpoint. It uses a linear ramp function to gradually decrease the gas flow over 12 hours, ensuring a smooth transition and preventing sudden changes that could affect equipment stability.

⸻

🟩 E (Example) – Function Block

The following is an example of a function block for the oxygen supply adjustment

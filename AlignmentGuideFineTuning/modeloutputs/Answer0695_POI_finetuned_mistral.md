### Intent:
**Intent Summary:**  
Generate a 30-line I/O list table for a steel rolling mill, specifying signal names, types (analog/digital), engineering units, ranges, setpoints, and P&ID references for PLC and instrumentation integration.

### Prompt:
**IO List Rolling Mill:**

Create an I/O list as a table with 30 lines for a rolling mill in a steel production plant. Have as columns signal name, input/output, signal tagnumber, analog/digital, engineering unit, ranges, setpoint, and P&ID reference.

**R-I-S-E:**

🟥 R (Role) – Define Your Role

Act as an industrial control engineer preparing the I/O specification for a rolling mill system in a steel production plant, ensuring clarity for instrumentation, automation, and electrical integration teams.

⸻

🟩 I (Input) – Information Provided

You are to create a detailed I/O list for the rolling mill that includes 30 signal entries. Each entry should include the following columns:
	•	Signal Name
	•	Input/Output
	•	Signal Tagnumber
	•	Analog/Digital
	•	Engineering Unit
	•	Range
	•	Setpoint
	•	P&ID Reference

The list should reflect real-world rolling mill variables such as roll speed, motor torque, cooling system actuation, gap feedback, and tension control.

⸻

🟧 S (Steps) – Implementation Steps
	1.	Identify 30 key control and monitoring signals commonly used in rolling mills.
	2.	For each signal, define:
	•	Whether it is an input (sensor) or output (actuator)
	•	Its analog/digital type
	•	Engineering units (e.g., mm, °C, bar, m/min)
	•	Typical range and control setpoint
	•	A unique tag number (e.g., RM1001)
	•	P&ID reference for traceability
	3.	Format the list as a structured table suitable for use in Excel, documentation, or PLC tag import.
	4.	Ensure consistency, clarity, and relevance to real plant instrumentation.

⸻

🟦 E (Expectation) – Expected Outcome

Deliver a professional, standardized I/O list that:
	•	Covers 30 essential signals used in rolling mill operations
	•	Provides all necessary metadata for PLC configuration, field wiring, and HMI integration
	•	Aligns with best practices for project documentation, P&ID traceability, and commissioning support

### Generated Code:
**Intent Summary:**  
Generate a 30-line I/O list table for a steel rolling mill, specifying signal names, types (analog/digital), engineering units, ranges, setpoints, and P&ID references for PLC and instrumentation integration.
**IO List Rolling Mill:**

Create an I/O list as a table with 30 lines for a rolling mill in a steel production plant. Have as columns signal name, input/output, signal tagnumber, analog/digital, engineering unit, ranges, setpoint, and P&ID reference.

**R-I-S-E:**

🟥 R (Role) – Define Your Role

Act as an industrial control engineer preparing the I/O specification for a rolling mill system in a steel production plant, ensuring clarity for instrumentation, automation, and electrical integration teams.

⸻

🟩 I (Input) – Information Provided

You are to create a detailed I/O list for the rolling mill that includes 30 signal entries. Each entry should include the following columns:
	•	Signal Name
	•	Input/Output
	•	Signal Tagnumber
	•	Analog/Digital
	•	Engineering Unit
	•	Range
	•	Setpoint
	•	P&ID Reference

The list should reflect real-world rolling mill variables such as roll speed, motor torque, cooling system actuation, gap feedback, and tension control.

⸻

🟧 S (Steps) – Implementation Steps
	1.	Identify 30 key control and monitoring signals commonly used in rolling mills.
	2.	For each signal, define:
	•	Whether it is an input (sensor) or output (actuator)
	•	Its analog/digital type
	•	Engineering units (e.g., mm, °C, bar, m/min)
	•	Typical range and control setpoint
	•	A unique tag number (e.g., RM1001)
	•	P&ID reference for traceability
	3.	Format the list as a structured table suitable for use in Excel, documentation, or PLC tag import.
	4.	Ensure consistency, clarity, and relevance to real plant instrumentation.

⸻

🟦 E (Expectation) – Expected Outcome

Deliver a professional, standardized I/O list that:
	•	Covers 30 essential signals used in rolling mill operations
	•	Provides all necessary metadata for PLC configuration, field wiring, and HMI integration
	•	Aligns with best practices for project documentation, P&ID traceability, and commissioning support
	•	Can be easily shared with cross-functional teams (control, electrical, mechanical)
FUNCTION_BLOCK FB_PressureControl
VAR_INPUT
    Setpoint : REAL; // Desired pressure in bar
    Pressure_PV : REAL; // Measured pressure in bar
    Enable : BOOL; // Enable control when TRUE
END_VAR

VAR_OUTPUT
    Control_Valve_Position : REAL; // Control valve position (0–100%)
    Alarm : BOOL; // TRUE if pressure deviation exceeds tolerance
END_VAR

VAR
    Tolerance : REAL := 0.1; // Acceptable pressure deviation in bar
    Previous_Pressure_PV : REAL; // For detecting pressure changes
    Previous_Control_Valve_Position : REAL; // For detecting valve changes
END_VAR

METHOD Execute : BOOL
BEGIN
    // Initialize outputs
    Control_Valve_Position := 0.0;
    Alarm := FALSE;

    // Check enable condition
    IF NOT Enable THEN
        // Disable control when disabled
        Control_Valve_Position := 0.0;
        Alarm := FALSE;
        RETURN TRUE;
    END_IF;

    // Store previous values for detecting changes
    Previous_Pressure_PV := Pressure_PV;
    Previous_Control_Valve_Position := Control_Valve_Position;

    // Calculate pressure deviation
    Deviation := ABS(Setpoint - Pressure_PV);

    // Check if pressure is within tolerance
    IF Deviation <= Tolerance THEN
        // Pressure within tolerance, no action required
        Control_Valve_Position := 0.0;
        Alarm := FALSE;
    ELSE
        // Adjust control valve to correct pressure
        Control_Valve_Position := (Deviation / Tolerance) * 100.0;

        // Clamp valve position to valid range (0–100%)
        IF Control_Valve_Position > 100.0 THEN
            Control_Valve_Position := 100

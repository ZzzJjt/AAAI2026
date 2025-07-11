### Intent:
**Intent Summary:**  
Design a PLC/DCS control system for a continuous ammonium nitrate reactor, ensuring safe and precise regulation of temperature, pressure, pH, feed ratios, and level through PID loops, interlocks, and alarm logic to maintain stable production.  

*(Focus: Automation-ready control logic for reactor safety, quality, and efficiency.)*

### Prompt:
**FBD PID:**

Create a 61131-3 function block diagram in ASCII art. It shall contain an analog input, a timer block, and a PID block as well as an analog output. The analog input feeds both the timer and the PID block. Only the PID block is connected to the analog output. Provide typical input and output signals for each function block and show them inside each block.

**T-A-G:**

🟥 T (Task)

Design a 61131-3 Function Block Diagram (FBD) using ASCII art that visually represents a basic control structure involving an analog input, a timer, a PID controller, and an analog output.

⸻

🟩 A (Action)
	•	Create a clear ASCII layout with the following blocks:
	•	Analog Input block (OUT = AI)
	•	TON timer block (IN = AI, ET, Q)
	•	PID block (PV = AI, SP = 50.0, CV)
	•	Analog Output block (IN = CV)
	•	Ensure the Analog Input feeds both the TON and the PID block.
	•	Show that only the PID’s output (CV) connects to the Analog Output.
	•	Use ASCII symbols (+-----+, -->, |) to create block shapes and signal lines.
	•	Label all signals clearly inside or beside the blocks.

⸻

🟦 G (Goal)

Produce a plain-text diagram that visually communicates the data flow and block interaction within a control loop—useful for documentation, PLC training, version-controlled codebases, or text-only environments where graphical editors are unavailable.

### Generated Code:
**Intent Summary:**  
Design a PLC/DCS control system for a continuous ammonium nitrate reactor, ensuring safe and precise regulation of temperature, pressure, pH, feed ratios, and level through PID loops, interlocks, and alarm logic to maintain stable production.  

*(Focus: Automation-ready control logic for reactor safety, quality, and efficiency.)*
**FBD PID:**

Create a 61131-3 function block diagram in ASCII art. It shall contain an analog input, a timer block, and a PID block as well as an analog output. The analog input feeds both the timer and the PID block. Only the PID block is connected to the analog output. Provide typical input and output signals for each function block and show them inside each block.

**T-A-G:**

🟥 T (Task)

Design a 61131-3 Function Block Diagram (FBD) using ASCII art that visually represents a basic control structure involving an analog input, a timer, a PID controller, and an analog output.

⸻

🟩 A (Action)
	•	Create a clear ASCII layout with the following blocks:
	•	Analog Input block (OUT = AI)
	•	TON timer block (IN = AI, ET, Q)
	•	PID block (PV = AI, SP = 50.0, CV)
	•	Analog Output block (IN = CV)
	•	Ensure the Analog Input feeds both the TON and the PID block.
	•	Show that only the PID’s output (CV) connects to the Analog Output.
	•	Use ASCII symbols (+-----+, -->, |) to create block shapes and signal lines.
	•	Label all signals clearly inside or beside the blocks.

⸻

🟦 G (Goal)

Produce a plain-text diagram that visually communicates the data flow and block interaction within a control loop—useful for documentation, PLC training, version-controlled codebases, or text-only environments where graphical editors are unavailable.
FUNCTION_BLOCK FB_PID_Control
VAR_INPUT
    Setpoint : REAL; // Target temperature in °C
    Error : REAL; // Measured - Setpoint
    Output : REAL; // Analog output
    Kp : REAL; // Proportional gain
    Ki : REAL; // Integral gain
    Kd : REAL; // Derivative gain
    T_S : REAL; // Sampling time (s)
    T_I : REAL; // Integral time (s)
    T_D : REAL; // Derivative time (s)
    Reset : BOOL; // Reset flag
END_VAR

VAR_OUTPUT
    Error_Sum : REAL; // Accumulated error
    Integral_Term : REAL; // Integral term
    Derivative_Term : REAL; // Derivative term
    Output_Setpoint : REAL; // Output setpoint
    Output_Actual : REAL; // Actual output
END_VAR

VAR
    Prev_Error : REAL; // Previous error
    Prev_Output : REAL; // Previous output
    Prev_Error_Sum : REAL; // Previous error sum
    Prev_Integral_Term : REAL; // Previous integral term
    Prev_Derivative_Term : REAL; // Previous derivative term
END_VAR

METHOD Execute : BOOL
BEGIN
    // Reset logic
    IF Reset THEN
        Error_Sum := 0.0;
        Integral_Term := 0.0;
        Derivative_Term := 0.0;
        Prev_Error := 0.0;
        Prev_Output := 0.0;
        Prev_Error_Sum := 0.0;
        Prev_Integral_Term := 0.0;
        Prev_Derivative_Term := 0.0;
        Output_Setpoint := Setpoint;
        Output_Actual := 0.0;
        RETURN TRUE;
    END_IF;

    // Calculate error
    Error := Setpoint - Output;

    // Integral term
    Integral_Term := Integral_Term + Error * T_I;

    // Derivative term
    Derivative_Term := Derivative_Term + (Error - Prev_Error) * T_D;

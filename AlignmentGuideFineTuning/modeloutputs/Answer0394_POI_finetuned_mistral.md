### Intent:
**Intent Summary:**  
Create an ASCII art function block diagram showing an analog input feeding both a timer and PID controller, with the PID output connected to an analog output, for industrial process control documentation.

### Prompt:
**FBD PID:**

Create a 61131-3 function block diagram in ASCII art. It shall contain an analog input, a timer block, and a PID block as well as an analog output. The analog input feeds both the timer and the PID block. Only the PID block is connected to the analog output. Provide typical input and output signals for each function block and show them inside each block.

**C-A-R-E:**

🟥 C (Context) – Background Situation

When designing control systems using IEC 61131-3 Function Block Diagrams (FBD), it’s often helpful to communicate the layout using ASCII art in documentation, code comments, or plain text environments where graphical tools aren’t available. A basic structure involving an analog input, timer, PID controller, and analog output is a common pattern in automation and control logic design.

⸻

🟩 A (Action) – Task to Perform

Create an ASCII-based FBD diagram that includes:
	•	An analog input block
	•	A TON (on-delay) timer block
	•	A PID control block
	•	An analog output block

The analog input should feed both the timer and the PID controller, and only the PID block should be connected to the analog output. Inside each block, show the typical signal names for the inputs and outputs (e.g., IN, ET, PV, SP, CV, OUT, etc.).

⸻

🟨 R (Result) – Expected Outcome

You will produce a text-based representation of a function block diagram that clearly illustrates the signal flow, block interconnections, and naming conventions used in PLC programming. This will help engineers document control strategies, review logic, and share designs without the need for graphics software.

⸻

🟦 E (Example) – Concrete Illustration

     +-------------+      
     | AnalogInput |      
     |   OUT=AI    |----+-----------------------------+       
     +-------------+    |                             |       
                        |                             |       
                   +----v----+                   +----v----+   
                   |  TON     |                  |   PID    |   
                   | IN=AI    |                  | PV=AI    |   
                   | ET=ET    |                  | SP=50.0  |   
                   | Q=Q      |                  | CV=CV    |   
                   +---------+                   +---------+   
                                                     |         
                                                     |         
                                               +-----v-----+    
                                               | AnalogOut |    
                                               |  IN=CV     |    
                                               +-----------+

### Generated Code:
**Intent Summary:**  
Create an ASCII art function block diagram showing an analog input feeding both a timer and PID controller, with the PID output connected to an analog output, for industrial process control documentation.
**FBD PID:**

Create a 61131-3 function block diagram in ASCII art. It shall contain an analog input, a timer block, and a PID block as well as an analog output. The analog input feeds both the timer and the PID block. Only the PID block is connected to the analog output. Provide typical input and output signals for each function block and show them inside each block.

**C-A-R-E:**

🟥 C (Context) – Background Situation

When designing control systems using IEC 61131-3 Function Block Diagrams (FBD), it’s often helpful to communicate the layout using ASCII art in documentation, code comments, or plain text environments where graphical tools aren’t available. A basic structure involving an analog input, timer, PID controller, and analog output is a common pattern in automation and control logic design.

⸻

🟩 A (Action) – Task to Perform

Create an ASCII-based FBD diagram that includes:
	•	An analog input block
	•	A TON (on-delay) timer block
	•	A PID control block
	•	An analog output block

The analog input should feed both the timer and the PID controller, and only the PID block should be connected to the analog output. Inside each block, show the typical signal names for the inputs and outputs (e.g., IN, ET, PV, SP, CV, OUT, etc.).

⸻

🟨 R (Result) – Expected Outcome

You will produce a text-based representation of a function block diagram that clearly illustrates the signal flow, block interconnections, and naming conventions used in PLC programming. This will help engineers document control strategies, review logic, and share designs without the need for graphics software.

⸻

🟦 E (Example) – Concrete Illustration

     +-------------+      
     | AnalogInput |      
     |   OUT=AI    |----+-----------------------------+       
     +-------------+    |                             |       
                        |                             |       
                   +----v----+                   +----v----+   
                   |  TON     |                  |   PID    |   
                   | IN=AI    |                  | PV=AI    |   
                   | ET=ET    |                  | SP=50.0  |   
                   | Q=Q      |                  | CV=CV    |   
                   +---------+                   +---------+   
                                                     |         
                                                     |         
                                               +-----v-----+    
                                               | AnalogOut |    
                                               |  IN=CV     |    
                                               +-----------+

This diagram shows that the AnalogInput block feeds both the TON and PID blocks, and only the PID output is connected to AnalogOut.
FUNCTION_BLOCK FB_PIDController
VAR_INPUT
    PV : REAL;                 // Process variable (e.g., temperature, pressure)
    SP : REAL;                 // Setpoint (e.g., target temperature)
    Kp : REAL := 2.0;          // Proportional gain
    Ki : REAL := 0.1;          // Integral gain
    Kd : REAL := 0.05;         // Derivative gain
    MinOutput : REAL := 0.0;   // Minimum output (e.g., valve position)
    MaxOutput : REAL := 100.0; // Maximum output (e.g., valve position)
    Enable : BOOL := TRUE;     // Enable control loop
END_VAR

VAR_OUTPUT
    Output : REAL;             // Control output (e.g., valve position)
    Error : REAL;              // Process error
    Integral : REAL;           // Integral term
    Derivative : REAL;         // Derivative term
    Reset : BOOL;              // Reset flag
END_VAR

VAR
    PrevError : REAL;          // Previous error for derivative calculation
    PrevTime : TIME;           // Previous time for integral calculation
    DeltaT : TIME;             // Time difference for derivative calculation
    IntegralLimit : REAL := 100.0; // Integral limit to prevent windup
END_VAR

// Initialize outputs
Output := 0.0;
Error := 0.0;
Integral := 0.0;
Derivative := 0.0;
Reset := FALSE;

// Check enable condition
IF NOT Enable THEN
    Output := 0.0;
    Error := 0.0;
    Integral := 0.0;
    Derivative := 0.0;
    Reset := TRUE;
    RETURN;
END_IF;

// Reset on rising edge of Enable
IF Reset AND NOT Edge(Enable) THEN
    Output :=

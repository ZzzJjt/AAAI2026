### Intent:
**Intent Summary:**  
Create an ASCII-based Function Block Diagram (FBD) showing signal flow between an analog input, timer, PID controller, and analog output, with labeled I/O signals for PLC control logic documentation.  

*(Focus: Textual representation of a PID control loop in IEC 61131-3 FBD format.)*

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
Create an ASCII-based Function Block Diagram (FBD) showing signal flow between an analog input, timer, PID controller, and analog output, with labeled I/O signals for PLC control logic documentation.  

*(Focus: Textual representation of a PID control loop in IEC 61131-3 FBD format.)*
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

Here, the AnalogInput block feeds both the TON (on-delay) timer and the PID block. The PID block’s output CV is connected to the AnalogOut block, which is the only analog output. The signal names are clearly defined for clarity and consistency.
FUNCTION_BLOCK FB_PID_Control
VAR_INPUT
    Setpoint : REAL; // Target value
    Error : REAL;   // Measured - Setpoint
    Kp : REAL;      // Proportional gain
    Ki : REAL;      // Integral gain
    Kd : REAL;      // Derivative gain
    T_S : REAL;     // Sampling time (s)
    Reset : BOOL;   // Reset flag
END_VAR

VAR_OUTPUT
    Output : REAL; // Control signal
    Error_Sum : REAL; // Integral term
    Error_Diff : REAL; // Derivative term
    Error_Integral : REAL; // Integral term
    Error_Derivative : REAL; // Derivative term
    Error_Integral_Limit : REAL; // Integral term limit
    Error_Derivative_Limit : REAL; // Derivative term limit
    Error_Integral_Reset : BOOL; // Integral reset flag
    Error_Derivative_Reset : BOOL; // Derivative reset flag
    Error_Integral_Overflow : BOOL; // Integral overflow flag
    Error_Derivative_Overflow : BOOL; // Derivative overflow flag
    Error_Integral_Underflow : BOOL; // Integral underflow flag
    Error_Derivative_Underflow : BOOL; // Derivative underflow flag
END_VAR

VAR
    Prev_Error : REAL; // Previous error
    Prev_Output : REAL; // Previous output
    Prev_Error_Sum : REAL; // Previous integral term
    Prev_Error_Diff : REAL; // Previous derivative term
    Prev_Error_Integral : REAL; // Previous integral term
    Prev_Error_Integral_Limit : REAL; // Previous integral term limit
    Prev_Error_Derivative : REAL; // Previous derivative term
    Prev_Error_Derivative_Limit : REAL; // Previous derivative term limit
    Prev_Error_Integral_Reset : BOOL; // Previous integral reset flag
    Prev_Error_Derivative_

### Intent:
**Intent Summary:**  
Create a 30-line I/O list table for a steel rolling mill's automation system, detailing signal names, types (analog/digital), engineering units, ranges, setpoints, and P&ID references to support PLC/HMI configuration and process control documentation.  

*(Focus: Structured I/O documentation for rolling mill instrumentation and control signals.)*

### Prompt:
**IO List Rolling Mill:**

Create an I/O list as a table with 30 lines for a rolling mill in a steel production plant. Have as columns signal name, input/output, signal tagnumber, analog/digital, engineering unit, ranges, setpoint, and P&ID reference.

**R-T-F:**

🟥 R (Role) – Define Your Role

Act as a control systems engineer responsible for creating detailed I/O documentation for the automation of a rolling mill in a steel production facility.

⸻

🟩 T (Task) – Define the Objective

Generate a structured I/O list table containing 30 lines, each representing a control or monitoring signal relevant to the rolling mill process. Each row must include the following columns:
	•	Signal Name
	•	Input/Output
	•	Signal Tagnumber
	•	Analog/Digital
	•	Engineering Unit
	•	Range
	•	Setpoint
	•	P&ID Reference

The list should reflect realistic instrumentation, such as motor speed feedback, roll gap position, cooling valve control, hydraulic pressure, and strip tension.

⸻

🟧 F (Format) – Specify the Output Format

Provide the output as a cleanly formatted table suitable for documentation, HMI/PLC configuration, or Excel import. The format should support:
	•	Clear signal identification and traceability
	•	Inclusion of engineering metadata (units, range, setpoints)
	•	Cross-reference with P&ID diagrams for system integration
	•	Compatibility with control logic implementation and commissioning workflows

### Generated Code:
**Intent Summary:**  
Create a 30-line I/O list table for a steel rolling mill's automation system, detailing signal names, types (analog/digital), engineering units, ranges, setpoints, and P&ID references to support PLC/HMI configuration and process control documentation.  

*(Focus: Structured I/O documentation for rolling mill instrumentation and control signals.)*
**IO List Rolling Mill:**

Create an I/O list as a table with 30 lines for a rolling mill in a steel production plant. Have as columns signal name, input/output, signal tagnumber, analog/digital, engineering unit, ranges, setpoint, and P&ID reference.

**R-T-F:**

🟥 R (Role) – Define Your Role

Act as a control systems engineer responsible for creating detailed I/O documentation for the automation of a rolling mill in a steel production facility.

⸻

🟩 T (Task) – Define the Objective

Generate a structured I/O list table containing 30 lines, each representing a control or monitoring signal relevant to the rolling mill process. Each row must include the following columns:
	•	Signal Name
	•	Input/Output
	•	Signal Tagnumber
	•	Analog/Digital
	•	Engineering Unit
	•	Range
	•	Setpoint
	•	P&ID Reference

The list should reflect realistic instrumentation, such as motor speed feedback, roll gap position, cooling valve control, hydraulic pressure, and strip tension.

⸻

🟧 F (Format) – Specify the Output Format

Provide the output as a cleanly formatted table suitable for documentation, HMI/PLC configuration, or Excel import. The format should support:
	•	Clear signal identification and traceability
	•	Inclusion of engineering metadata (units, range, setpoints)
	•	Cross-reference with P&ID diagrams for system integration
	•	Compatibility with control logic implementation and commissioning workflows
(* IEC 61131-3 Structured Text Program for PID Control of a Heating System *)
(* Sets temperature using PID control with 100 ms sampling, 1000 ms reset, and 1000 ms output *)
(* Uses PID_100ms function block with Kp=2.0, Ki=0.5, Kd=0.1, setpoint=100.0 °C, and 0.1 °C resolution *)
(* Inputs: Temperature_PV (°C), Heater_On (BOOL), Cooler_On (BOOL) *)
(* Outputs: Heater_Power (0.0–100.0 W), Cooler_Power (0.0–100.0 W) *)
(* Safety: Clamps output to 0–100 W, limits temperature to 100–120 °C *)

PROGRAM HeatingSystemControl
VAR
    (* Inputs *)
    Temperature_PV : REAL;                    (* Measured temperature in °C *)
    Heater_On : BOOL;                        (* Heater enabled *)
    Cooler_On : BOOL;                        (* Cooler enabled *)
    
    (* Outputs *)
    Heater_Power : REAL;                      (* Heater output power in W *)
    Cooler_Power : REAL;                      (* Cooler output power in W *)
    
    (* Internal Variables *)
    PID_100ms : PID_100ms;                    (* PID control block *)
    Temp_SP : REAL := 100.0;                  (* Setpoint: 100.0 °C *)
    Temp_Output : REAL;                       (* PID output: Heater_Power or Cooler_Power *)
    Temp_Error : REAL;                        (* Error: Temp_SP - Temperature_PV *)
    Temp_Integral : REAL;                     (* Integral: Sum of errors *)
    Temp_Derivative : REAL;                   (* Derivative: Rate of change of error *)
    Temp_Prev : REAL;                         (* Previous temperature for derivative *)

### Intent:
**Intent Summary:**  
Generate a text-based Piping and Instrumentation Diagram (P&ID) for a power plant steam-water cycle, including tagged equipment, instrumentation, control loops, and piping flow, formatted for clarity in early engineering or automation tasks.  

*(Focus: Structured textual P&ID with industry-standard tags for control system integration.)*

### Prompt:
**P-ID Steam Water Cycle:**

Create a P&I diagram in textual notation for a steam water cycle in a power plant. Include equipment, instrumentation, piping, and control loops. Provide concrete tag names.


**T-A-G:**

🟥 T (Task)

Create a text-based Piping and Instrumentation Diagram (P&ID) for a steam-water cycle in a power plant.

⸻

🟩 A (Action)
	•	Represent all major equipment involved in the steam-water cycle, such as feedwater pumps, boiler, steam drum, condenser, etc.
	•	Include relevant instrumentation and control loops, such as flow transmitters (FT), level transmitters (LT), pressure transmitters (PT), controllers (FIC, LIC), and control valves (FCV, LCV).
	•	Use clear tag names (e.g., FT101, FCV102) based on industry standards.
	•	Show piping and flow direction using arrows (-->) and organize elements in process order.
	•	Format the diagram in clean plain-text notation, using indentation and alignment to convey process structure and control logic.

⸻

🟦 G (Goal)

Provide a structured, readable, and logic-complete textual P&ID that clearly documents the flow, control strategy, and tag references of a steam-water cycle, enabling use in early-stage engineering, PLC programming, or control narrative development when graphics are unavailable.

### Generated Code:
**Intent Summary:**  
Generate a text-based Piping and Instrumentation Diagram (P&ID) for a power plant steam-water cycle, including tagged equipment, instrumentation, control loops, and piping flow, formatted for clarity in early engineering or automation tasks.  

*(Focus: Structured textual P&ID with industry-standard tags for control system integration.)*
**P-ID Steam Water Cycle:**

Create a P&I diagram in textual notation for a steam water cycle in a power plant. Include equipment, instrumentation, piping, and control loops. Provide concrete tag names.


**T-A-G:**

🟥 T (Task)

Create a text-based Piping and Instrumentation Diagram (P&ID) for a steam-water cycle in a power plant.

⸻

🟩 A (Action)
	•	Represent all major equipment involved in the steam-water cycle, such as feedwater pumps, boiler, steam drum, condenser, etc.
	•	Include relevant instrumentation and control loops, such as flow transmitters (FT), level transmitters (LT), pressure transmitters (PT), controllers (FIC, LIC), and control valves (FCV, LCV).
	•	Use clear tag names (e.g., FT101, FCV102) based on industry standards.
	•	Show piping and flow direction using arrows (-->) and organize elements in process order.
	•	Format the diagram in clean plain-text notation, using indentation and alignment to convey process structure and control logic.

⸻

🟦 G (Goal)

Provide a structured, readable, and logic-complete textual P&ID that clearly documents the flow, control strategy, and tag references of a steam-water cycle, enabling use in early-stage engineering, PLC programming, or control narrative development when graphics are unavailable.
### Control Narrative for Ammonium Nitrate Production

#### 1. Overview
The ammonium nitrate production process involves the following major steps:
- **Ammonia Generation**: Produce ammonia through the Haber-Bosch process.
- **Ammonium Nitrate Reaction**: React ammonia with nitric acid to produce ammonium nitrate.
- **Crystallization**: Crystallize the ammonium nitrate solution to form solid product.
- **Drying**: Remove moisture from the crystallized product.
- **Packaging and Storage**: Package and store the final product.

#### 2. Control Narrative for Ammonia Generation

##### 2.1 Purpose
To ensure safe and efficient operation of the ammonia generation process by controlling key parameters such as pressure, temperature, and flow rates.

##### 2.2 Control Loops

###### 2.2.1 Pressure Control Loop
- **Purpose**: Maintain the pressure in the reactor at the setpoint to ensure safe and efficient operation.
- **Control Element**: Pressure Controller (PID-101).
- **Setpoint**: 150 psi.
- **Feedforward Input**: Gas flow rate (e.g., 1000 standard cubic meters per hour).
- **Output**: Control valve position (e.g., valve 101).
- **Tuning Parameters**: P = 2.0, I = 0.5, D = 0.3.

###### 2.2.2 Temperature Control Loop
- **Purpose**: Maintain the temperature in the reactor at the setpoint to ensure optimal reaction conditions.
- **Control Element**: Temperature Controller (PID-102).
- **Setpoint**: 450°C.
- **Feedforward Input**: Heat input (e.g., gas flow rate multiplied by heating value).
- **Output**: Fuel gas flow rate (e.g., valve 102).
- **Tuning Parameters**: P = 3.0, I = 0.6, D = 0.2.

###### 2.2.3 Flow

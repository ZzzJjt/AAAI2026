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


**Textual P&ID:**

```
Steam-Water Cycle P&ID

Feedwater Pump (FWP)
|
FT101 - Flow Transmitter
LCV101 - Level Control Valve
|
Feedwater Tank (FWT)
|

Boiler (BOIL)
|
PT101 - Pressure Transmitter
PT102 - Temperature Transmitter
|
Steam Drum (SD)
|

Steam Turbine (ST)
|
FT201 - Flow Transmitter
PT301 - Pressure Transmitter
|
Steam Condenser (SC)
|

Feedwater Heater (FHW)
|
FT401 - Flow Transmitter
PT501 - Temperature Transmitter
|
Feedwater Pump (FWP)
|

Closed Loop Controls

Flow Control Loop (FWP)
|
FT101
FIC101 - Flow Controller
LCV101

Level Control Loop (SD)
|
LT601 - Level Transmitter
LIC601 - Level Controller
LCV602 - Level Control Valve

Pressure Control Loop (BOIL)
|
PT101
FIC102 - Pressure Controller
FCV103 - Feedwater Control Valve

Temperature Control Loop (FHW)
|
PT501
FIC501 - Temperature Controller
FCV502 - Feedwater Control Valve

Piping Connections

FWP --> FWT
FWT --> BOIL
BOIL --> SD
SD --> ST
ST --> SC
SC --> FHW
FHW --> FWP
```

This textual P&ID provides a clear representation of the steam-water cycle in a power plant, including major equipment, instrumentation, control loops, and piping connections. The use of industry-standard tag names and organized structure enables easy integration with control systems and documentation.

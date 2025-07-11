### Intent:
The task is to create a scan-cycle-safe Kalman Filter function block in IEC 61131-3 Structured Text that estimates an autonomous vehicle's position and velocity from noisy measurements while ensuring input validation and output reliability.

### Prompt:
**Fahrenheit to Celsius:**
Implement a self-contained function block in IEC 61131-3 structured text to convert Fahrenheit to Celsius. Ensure it handles input validation and provides accurate results.

**T-A-G:**

🟥 T (Task)

Create a function block in IEC 61131-3 Structured Text to convert a temperature input in Fahrenheit to Celsius, ensuring accuracy and safety.

⸻

🟩 A (Action)
	•	Define the function block with:
	•	Input: Fahrenheit : REAL
	•	Outputs:
	•	Celsius : REAL
	•	ValidInput : BOOL
	•	Apply input validation:
	•	Reject any input below -459.67°F (absolute zero)
	•	Perform the conversion using the formula:
Celsius := (Fahrenheit - 32) \times \frac{5}{9}
	•	Return a valid Celsius result and flag the input as valid or invalid
	•	Add inline comments explaining the formula and input validation logic

⸻

🟦 G (Goal)

Deliver a modular and scan-cycle-safe function block that ensures reliable Fahrenheit-to-Celsius conversion in PLC systems. The implementation should support accurate monitoring, safe range enforcement, and reusability across control programs and HMI displays.

### Generated Code:
The task is to create a scan-cycle-safe Kalman Filter function block in IEC 61131-3 Structured Text that estimates an autonomous vehicle's position and velocity from noisy measurements while ensuring input validation and output reliability.
**Fahrenheit to Celsius:**
Implement a self-contained function block in IEC 61131-3 structured text to convert Fahrenheit to Celsius. Ensure it handles input validation and provides accurate results.

**T-A-G:**

🟥 T (Task)

Create a function block in IEC 61131-3 Structured Text to convert a temperature input in Fahrenheit to Celsius, ensuring accuracy and safety.

⸻

🟩 A (Action)
	•	Define the function block with:
	•	Input: Fahrenheit : REAL
	•	Outputs:
	•	Celsius : REAL
	•	ValidInput : BOOL
	•	Apply input validation:
	•	Reject any input below -459.67°F (absolute zero)
	•	Perform the conversion using the formula:
Celsius := (Fahrenheit - 32) \times \frac{5}{9}
	•	Return a valid Celsius result and flag the input as valid or invalid
	•	Add inline comments explaining the formula and input validation logic

⸻

🟦 G (Goal)

Deliver a modular and scan-cycle-safe function block that ensures reliable Fahrenheit-to-Celsius conversion in PLC systems. The implementation should support accurate monitoring, safe range enforcement, and reusability across control programs and HMI displays.  

**B-A-B:**

Before: Manual calculations or unreliable conversion methods in PLC code, risking temperature control errors.

After: A self-contained function block that safely converts Fahrenheit to Celsius, with input validation and scan-cycle-safe execution, improving temperature control accuracy and system reliability.

**R-I-S-E:**

Role

	Act as a PLC programmer or control systems engineer responsible for implementing temperature conversion logic in IEC 61131-3 Structured Text for use in industrial control systems.

	•	You are tasked with ensuring that temperature values are accurately processed and relayed within the system, with a focus on maintaining scan-cycle safety and providing reliable results.

	•	You are developing a function block that will be used in a control loop or as part of a temperature monitoring system, where precise temperature values are critical for maintaining process stability and safety.

	•	You are working in a PLC environment that requires scan-cycle-safe execution, meaning that the function block must not cause any runtime errors or affect the scan-cycle timing of the control program.

	•	You are also responsible for ensuring that the function block is reusable and maintainable, with clear documentation and comments to explain the logic and input validation process.

	•	You are developing this function block to support applications such as HVAC systems, chemical processing, or any system where accurate temperature control is essential.

	•	You are implementing this function block in IEC 61131-3 Structured Text, a widely used programming language for PLCs, to ensure compatibility with standard control systems and to leverage the scan-cycle-safe execution model of PLCs.

	•	You are designing the function block to handle input validation, ensuring that it only processes valid temperature values and provides accurate results, while maintaining scan-cycle safety and system reliability.

	•	You are developing this function block to support real-time temperature monitoring and control, where precise and consistent temperature values are essential for maintaining system performance and safety.

	•	You are implementing this function block to ensure that it is scan-cycle-safe, meaning that it will not cause any runtime errors or affect the scan-cycle timing of the control program, while still providing accurate and reliable temperature conversion results.

	•	You are designing the function block to be reusable and maintainable, with clear documentation and comments to explain the logic and input validation process, ensuring that it can be easily integrated into a larger control system or used in multiple applications.

	•	You are developing this function block to support applications such as HVAC systems, chemical

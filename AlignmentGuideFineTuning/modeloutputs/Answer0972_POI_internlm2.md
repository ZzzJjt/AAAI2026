### Intent:
**Intent Summary:**  
Create a robust, configurable PID controller function block in IEC 61131-3 Structured Text with anti-windup, output clamping, and input validation for precise real-time industrial process control.

### Prompt:
**Counter:**
Implement a self-contained function block in IEC 61131-3 structured text for a digital counter with up/down counting modes. Include configurable initial value, step size, and overflow handling.


**T-A-G:**

🟥 T (Task)

Create a self-contained function block in IEC 61131-3 Structured Text that implements a configurable digital counter with both up and down counting modes.

⸻

🟩 A (Action)
	•	Define inputs for:
	•	Enable : BOOL – activates the counter
	•	CountUp : BOOL – selects the counting direction
	•	StepSize : INT – amount to increment or decrement
	•	InitValue : INT – starting value of the counter
	•	Reset : BOOL – resets the counter to the initial value
	•	MaxValue / MinValue : INT – upper and lower bounds for overflow handling
	•	Use conditional logic to increment or decrement based on CountUp
	•	Implement logic to clamp the value within MinValue and MaxValue
	•	Provide outputs for:
	•	CurrentValue : INT – the current counter state
	•	AtMax, AtMin : BOOL – flags for boundary conditions
	•	Comment all key sections to ensure clarity and reusability

⸻

🟦 G (Goal)

Deliver a modular, safe, and easy-to-integrate counter block suitable for PLC applications requiring flexible and bounded counting logic. The implementation should be robust, configurable, and reliable for use in scan-cycle-sensitive automation environments.

### Generated Code:
**Intent Summary:**  
Create a robust, configurable PID controller function block in IEC 61131-3 Structured Text with anti-windup, output clamping, and input validation for precise real-time industrial process control.
**Counter:**
Implement a self-contained function block in IEC 61131-3 structured text for a digital counter with up/down counting modes. Include configurable initial value, step size, and overflow handling.


**T-A-G:**

🟥 T (Task)

Create a self-contained function block in IEC 61131-3 Structured Text that implements a configurable digital counter with both up and down counting modes.

⸻

🟩 A (Action)
	•	Define inputs for:
	•	Enable : BOOL – activates the counter
	•	CountUp : BOOL – selects the counting direction
	•	StepSize : INT – amount to increment or decrement
	•	InitValue : INT – starting value of the counter
	•	Reset : BOOL – resets the counter to the initial value
	•	MaxValue / MinValue : INT – upper and lower bounds for overflow handling
	•	Use conditional logic to increment or decrement based on CountUp
	•	Implement logic to clamp the value within MinValue and MaxValue
	•	Provide outputs for:
	•	CurrentValue : INT – the current counter state
	•	AtMax, AtMin : BOOL – flags for boundary conditions
	•	Comment all key sections to ensure clarity and reusability

⸻

🟦 G (Goal)

Deliver a modular, safe, and easy-to-integrate counter block suitable for PLC applications requiring flexible and bounded counting logic. The implementation should be robust, configurable, and reliable for use in scan-cycle-sensitive automation environments. The function block should be well-documented and adhere to best practices for IEC 61131-3 programming.

⸻

🟨 S (Success Criteria)

The function block should meet the following criteria:

1.	**Modularity:** The function block should be self-contained and easily integrated into larger programs. It should be designed to minimize external dependencies and promote code reusability.

2.	**Safety:** The function block should be designed with safety in mind. It should handle edge cases and unexpected inputs gracefully, without causing system instability or data corruption.

3.	**Configurability:** The function block should allow for easy configuration of its parameters, such as the initial value, step size, and overflow handling. It should provide a user-friendly interface for setting these parameters.

4.	**Reliability:** The function block should be designed to operate reliably in real-time industrial environments. It should be optimized for performance and minimize the risk of data loss or corruption.

5.	**Documentation:** The function block should be well-documented, with clear comments explaining its purpose, inputs, outputs, and behavior. It should adhere to best practices for IEC 61131-3 programming, including proper naming conventions, modularization, and error handling.

6.	**Testing:** The function block should be thoroughly tested to ensure its correctness and robustness. It should be tested under a variety of conditions, including normal operation, edge cases, and failure scenarios.

7.	**Scalability:** The function block should be designed to scale easily to meet the needs of larger and more complex systems. It should be modular and flexible enough to be integrated into larger programs without causing performance issues or compatibility problems.

8.	**Maintainability:** The function block should be designed with maintainability in mind. It should be easy to understand, modify, and debug. It should be designed to minimize the risk of introducing bugs or regressions when making changes.

9.	**Portability:** The function block should be designed to be portable across different PLC platforms and programming environments. It should adhere to the IEC 61131-3 standard and be compatible with different PLC vendors' compilers and development tools.

10.	**Performance:** The function block should be optimized for performance, minimizing the time it takes to execute and reducing the risk of scan-cycle delays. It should be designed to handle high-frequency counting operations without

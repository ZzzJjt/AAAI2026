### Intent:
The intent is to generate PLC code for controlling a urea production reaction by sequentially managing ammonia and CO2 valve operations, monitoring pressure and temperature conditions, and timing the reaction duration before completing the process.

### Prompt:
**List Mathematical Function Blocks:**
Compile a detailed list of all mathematical function blocks available in the OSCAT library for PLC programming, including a brief description of their functionality and typical use cases.

**R-I-S-E:**

🟥 R (Role) – Your Role

You are a PLC developer or automation engineer using the OSCAT library to implement complex mathematical operations in control systems. To improve your workflow and assist your team, you aim to create a clear and accessible reference.

⸻

🟩 I (Input) – What You’re Given

You have access to the OSCAT library documentation or source files, which contain numerous mathematical function blocks (e.g., trigonometric, algebraic, statistical). However, these blocks are not centrally organized, and many lack contextual descriptions or usage examples.

⸻

🟧 S (Steps) – How to Proceed
	1.	Explore the OSCAT library (docs or codebase) and extract all function blocks under the mathematical category.
	2.	Organize the function blocks into logical categories such as:
	•	Trigonometric
	•	Exponential & Logarithmic
	•	Statistical
	•	Algebraic
	3.	For each function block, write:
	•	Its name
	•	A brief functional description
	•	A typical industrial use case or application context
	4.	Optionally, provide notes on parameter types, return values, or limitations (e.g., expected units, input range).
	5.	Present the final list in a structured format (table or markdown list).

⸻

🟦 E (Expectation) – What the Output Should Look Like

A well-organized reference list of OSCAT’s mathematical function blocks that:
	•	Helps engineers quickly find the right block for a task
	•	Serves as a training tool for newcomers
	•	Boosts development speed and reduces reliance on searching through source code
	•	Enhances code reliability by encouraging proper block selection based on descriptions and use cases

### Generated Code:
The intent is to generate PLC code for controlling a urea production reaction by sequentially managing ammonia and CO2 valve operations, monitoring pressure and temperature conditions, and timing the reaction duration before completing the process.
**List Mathematical Function Blocks:**
Compile a detailed list of all mathematical function blocks available in the OSCAT library for PLC programming, including a brief description of their functionality and typical use cases.

**R-I-S-E:**

🟥 R (Role) – Your Role

You are a PLC developer or automation engineer using the OSCAT library to implement complex mathematical operations in control systems. To improve your workflow and assist your team, you aim to create a clear and accessible reference.

⸻

🟩 I (Input) – What You’re Given

You have access to the OSCAT library documentation or source files, which contain numerous mathematical function blocks (e.g., trigonometric, algebraic, statistical). However, these blocks are not centrally organized, and many lack contextual descriptions or usage examples.

⸻

🟧 S (Steps) – How to Proceed
	1.	Explore the OSCAT library (docs or codebase) and extract all function blocks under the mathematical category.
	2.	Organize the function blocks into logical categories such as:
	•	Trigonometric
	•	Exponential & Logarithmic
	•	Statistical
	•	Algebraic
	3.	For each function block, write:
	•	Its name
	•	A brief functional description
	•	A typical industrial use case or application context
	4.	Optionally, provide notes on parameter types, return values, or limitations (e.g., expected units, input range).
	5.	Present the final list in a structured format (table or markdown list).

⸻

🟦 E (Expectation) – What the Output Should Look Like

A well-organized reference list of OSCAT’s mathematical function blocks that:
	•	Helps engineers quickly find the right block for a task
	•	Serves as a training tool for newcomers
	•	Boosts development speed and reduces reliance on searching through source code
	•	Enhances code reliability by encouraging proper block selection based on descriptions and use cases

---

**Final List of Mathematical Function Blocks:**

**Trigonometric Functions:**

| Name | Description | Use Case |
| --- | --- | --- |
| sin | Calculates the sine of an angle in radians | Control system for a robotic arm, where the angle of rotation needs to be calculated |
| cos | Calculates the cosine of an angle in radians | Monitoring the orientation of a wind turbine blade |
| tan | Calculates the tangent of an angle in radians | Automated control of a crane's boom angle |
| asin | Calculates the inverse sine of a value | Adjusting the angle of a conveyor belt to match the desired trajectory |
| acos | Calculates the inverse cosine of a value | Optimizing the positioning of a robotic gripper for a specific object |
| atan | Calculates the inverse tangent of a value | Controlling the angle of a solar panel tracking system |

**Exponential & Logarithmic Functions:**

| Name | Description | Use Case |
| --- | --- | --- |
| exp | Calculates the exponential of a value | Monitoring the growth of a bacterial culture in a bioreactor |
| log | Calculates the natural logarithm of a value | Optimizing the temperature and pressure conditions for a chemical reaction |
| ln | Calculates the natural logarithm of a value | Controlling the flow rate of a gas in a chemical process |
| pow | Raises a base to a power | Adjusting the intensity of a laser beam for precision cutting |
| sqrt | Calculates the square root of a value | Monitoring the pressure in a hydraulic system |

**Statistical Functions:**

| Name | Description | Use Case |
| --- | --- | --- |
| avg | Calculates the average of a set of values | Monitoring the performance of a fleet of vehicles |
| median | Calculates the median of a set of values | Optimizing the speed of a conveyor belt based on the average item size |
| stddev | Calculates the standard deviation of a set of values | Adjusting the temperature in a greenhouse based on the average humidity |
| min | Finds the minimum value in a set | Monitoring the pressure in a pneumatic system |
| max | Finds the maximum value in a set | Controlling the speed of a conveyor belt based on the maximum item size |

**Algebraic Functions:**

| Name | Description | Use Case |
| --- | --- | --- |
| add | Adds two or more values | Controlling the flow rate of a fluid in a chemical

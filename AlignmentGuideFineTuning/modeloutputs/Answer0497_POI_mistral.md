### Intent:
**Intent Summary:**  
Create an IEC 61131-3 Structured Text function block to safely compute the natural logarithm of a REAL input, handling domain errors (non-positive values) and optimizing for real-time PLC performance, with clear documentation on mathematical principles and edge-case handling.  

**For the simplex solver example:**  
Implement a PLC function block to solve linear programming problems (maximization) using the simplex method, handling constraints and variables within industrial automation limits, with outputs for solution status and optimal values.  

*(Choose the summary matching your target task—logarithm or solver.)*

### Prompt:
**Natural Logarithm:**

Develop a self-contained function block in IEC 61131-3 Structured Text to compute the natural logarithm of a given input. Ensure that the implementation is efficient and well-documented, with comments explaining the mathematical foundation of the natural logarithm. Additionally, address potential edge cases, such as handling non-positive inputs, and discuss the precision and performance of this function block in typical industrial applications.

**R-I-S-E:**

🟥 R (Role) – Your Role

You are a PLC software developer or control systems engineer responsible for implementing mathematical functions in IEC 61131-3 Structured Text for use in real-time industrial automation systems. Your goal is to ensure both computational correctness and system safety when executing advanced mathematical operations.

⸻

🟩 I (Input) – What You’re Given

You are required to implement a function block that:
	•	Computes the natural logarithm of a single input value
	•	Accepts an input:
X : REAL – a value for which ln(X) is to be calculated
	•	Outputs:
	•	LnX : REAL – the natural logarithm of X
	•	Error : BOOL – indicates whether the input is out of domain (i.e., X ≤ 0)
	•	Must handle edge cases like X = 0 or negative values safely
	•	Needs to run efficiently within the scan-time limits of a PLC
	•	May use the built-in LN() function or implement a fallback approximation if necessary

⸻

🟧 S (Steps) – What You Need to Do
	1.	Create a function block named NaturalLog:
 FUNCTION_BLOCK NaturalLog
VAR_INPUT
    X : REAL;
END_VAR
VAR_OUTPUT
    LnX : REAL;
    Error : BOOL;
END_VAR
	2.	Implement logic for computing the logarithm:
	•	If X > 0, use LN(X) and set Error := FALSE
	•	If X ≤ 0, return a default value (0.0 or -9999.0) and set Error := TRUE
	•	Optionally include a diagnostic log or fault code for error tracking
	3.	Comment clearly on:
	•	Why ln(x) is undefined for non-positive values
	•	The mathematical relationship between logarithms and exponentials
	•	Real-time implications of using a built-in vs. custom implementation
	4.	Optimize for execution:
	•	Use straight-line logic (no loops or recursion)
	•	Ensure that the logic fits within standard scan times
	•	Validate with test cases for edge inputs like 0.0001, 1, 1000, and -5

⸻

🟦 E (Expectation) – What Success Looks Like

You produce a robust and reusable function block that:
	•	Correctly calculates the natural logarithm for valid inputs
	•	Handles domain errors gracefully and safely
	•	Provides diagnostic feedback without crashing the control program
	•	Is lightweight, readable, and suitable for real-time use in industrial applications such as:
	•	Sensor calibration
	•	Flow and pressure linearization
	•	Exponential decay modeling

### Generated Code:
**Intent Summary:**  
Create an IEC 61131-3 Structured Text function block to safely compute the natural logarithm of a REAL input, handling domain errors (non-positive values) and optimizing for real-time PLC performance, with clear documentation on mathematical principles and edge-case handling.  

**For the simplex solver example:**  
Implement a PLC function block to solve linear programming problems (maximization) using the simplex method, handling constraints and variables within industrial automation limits, with outputs for solution status and optimal values.  

*(Choose the summary matching your target task—logarithm or solver.)*
**Natural Logarithm:**

Develop a self-contained function block in IEC 61131-3 Structured Text to compute the natural logarithm of a given input. Ensure that the implementation is efficient and well-documented, with comments explaining the mathematical foundation of the natural logarithm. Additionally, address potential edge cases, such as handling non-positive inputs, and discuss the precision and performance of this function block in typical industrial applications.

**R-I-S-E:**

🟥 R (Role) – Your Role

You are a PLC software developer or control systems engineer responsible for implementing mathematical functions in IEC 61131-3 Structured Text for use in real-time industrial automation systems. Your goal is to ensure both computational correctness and system safety when executing advanced mathematical operations.

⸻

🟩 I (Input) – What You’re Given

You are required to implement a function block that:
	•	Computes the natural logarithm of a single input value
	•	Accepts an input:
X : REAL – a value for which ln(X) is to be calculated
	•	Outputs:
	•	LnX : REAL – the natural logarithm of X
	•	Error : BOOL – indicates whether the input is out of domain (i.e., X ≤ 0)
	•	Must handle edge cases like X = 0 or negative values safely
	•	Needs to run efficiently within the scan-time limits of a PLC
	•	May use the built-in LN() function or implement a fallback approximation if necessary

⸻

🟧 S (Steps) – What You Need to Do
	1.	Create a function block named NaturalLog:
 FUNCTION_BLOCK NaturalLog
VAR_INPUT
    X : REAL;
END_VAR
VAR_OUTPUT
    LnX : REAL;
    Error : BOOL;
END_VAR
	2.	Implement logic for computing the logarithm:
	•	If X > 0, use LN(X) and set Error := FALSE
	•	If X ≤ 0, return a default value (0.0 or -9999.0) and set Error := TRUE
	•	Optionally include a diagnostic log or fault code for error tracking
	3.	Comment clearly on:
	•	Why ln(x) is undefined for non-positive values
	•	The mathematical relationship between logarithms and exponentials
	•	Real-time implications of using a built-in vs. custom implementation
	4.	Optimize for execution:
	•	Use straight-line logic (no loops or recursion)
	•	Ensure that the logic fits within standard scan times
	•	Validate with test cases for edge inputs like 0.0001, 1, 1000, and -5

⸻

🟦 E (Expectation) – What Success Looks Like

You produce a robust and reusable function block that:
	•	Correctly calculates the natural logarithm for valid inputs
	•	Handles domain errors gracefully and safely
	•	Provides diagnostic feedback without crashing the control program
	•	Is lightweight, readable, and suitable for real-time use in industrial applications such as:
	•	Sensor calibration
	•	Flow and pressure linearization
	•	Exponential decay modeling
	•	Optimization algorithms

**Simplex Solver:**

Develop a self-contained function block in IEC 61131-3 Structured Text to solve linear programming problems (maximization) using the simplex method. Ensure that the implementation is efficient and well-documented, with comments explaining the mathematical foundation of the simplex method. Additionally, address potential edge cases, such as handling constraints and variables within industrial automation limits, and discuss the precision and performance of this function block in typical industrial applications.

**R-I-S-E:**

🟥 R (Role) – Your Role

You are a PLC software developer or control systems engineer responsible for implementing mathematical functions in IEC 61131-3 Structured Text for use in real-time industrial automation systems. Your goal is to ensure both computational correctness and system safety when executing advanced mathematical operations.

⸻

🟩 I (Input) – What You’re Given

You are required to implement a function block that:
	•	Solves linear programming problems using the simplex method
	•	Accepts inputs:
	•	A : REAL matrix – coefficients of the objective function and constraints
	•	b : REAL vector – constant terms of the constraints
	•	n : INTEGER – number of variables
	•	m : INTEGER – number of constraints
	•	Outputs:
	•	x : REAL array – optimal values of the variables
	•	Status : BOOL – indicates whether the problem was solved successfully
	•	Must handle edge cases like singular matrices, infeasible problems, and unbounded solutions
	•	Needs to run efficiently within the scan-time limits of a PLC
	•	May use a pre-built simplex solver or implement a fallback approximation if necessary

⸻

🟧 S (Steps) – What You Need to Do
	1.	Create a function block named SimplexSolver:
 FUNCTION_BLOCK SimplexSolver
VAR_INPUT
    A : REAL_MATRIX(1..m, 1..n);
    b : REAL_ARRAY(1..m);
    n : INTEGER;
    m

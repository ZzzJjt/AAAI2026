### Intent:
**Intent Summary:**  
Create a Structured Text program to control a urea production reaction by managing ammonia and CO₂ valve operations, monitoring pressure/temperature conditions, and timing the reaction process until completion.  

(Key elements: valve control, condition monitoring, timed reaction, process automation)

### Prompt:
**Programming Reference:**
Compile a comprehensive list of all valid keywords used in the IEC 61131-3 Structured Text programming language, ensuring that it covers both standard control flow structures and data types. Include examples of usage for key functions where applicable.

**C-A-R-E:**

🟥 C (Context)

IEC 61131-3 Structured Text is a widely used programming language in industrial automation. Despite its standardized nature, many developers lack a single, comprehensive reference that clearly lists all valid keywords, data types, and control structures, along with practical usage examples. This makes learning, troubleshooting, and implementing efficient code more challenging—especially for new programmers or teams working across different vendors.

⸻

🟩 A (Action)

Create a comprehensive, categorized reference document that includes:
	•	All reserved keywords in Structured Text (ST), such as control structures (IF, CASE, FOR, WHILE, etc.)
	•	Core data types (BOOL, INT, REAL, TIME, STRING, ARRAY, etc.)
	•	Logical and arithmetic operators (AND, OR, MOD, NOT, +, -, etc.)
	•	System constants and standard function blocks (TRUE, FALSE, TON, CTU, ABS, SQRT, etc.)
	•	Code examples for commonly used constructs (e.g., how to use a timer, write a loop, or declare arrays)

⸻

🟨 R (Result)

The result will be a clear, structured, and practical programming reference for IEC 61131-3 Structured Text, which:
	•	Makes it faster and easier for developers to write compliant and efficient code
	•	Serves as a daily reference tool for both new and experienced automation engineers
	•	Helps reduce syntax errors, debugging time, and onboarding effort
	•	Can be formatted as a PDF cheat sheet, a webpage, or even an IDE-integrated tooltip system

⸻

🟦 E (Example)

IF-THEN-ELSE syntax:

VAR
  Temp : REAL := 85.0;
  Overheat : BOOL;
END_VAR

IF Temp > 100.0 THEN
  Overheat := TRUE;
ELSE
  Overheat := FALSE;
END_IF;

TON (On-delay timer) function block:

VAR
  Timer1 : TON;
  Start  : BOOL;
END_VAR

Timer1(IN := Start, PT := T#5s);
IF Timer1.Q THEN
  // Execute action when timer completes
END_IF;

### Generated Code:
**Intent Summary:**  
Create a Structured Text program to control a urea production reaction by managing ammonia and CO₂ valve operations, monitoring pressure/temperature conditions, and timing the reaction process until completion.  

(Key elements: valve control, condition monitoring, timed reaction, process automation)
**Programming Reference:**
Compile a comprehensive list of all valid keywords used in the IEC 61131-3 Structured Text programming language, ensuring that it covers both standard control flow structures and data types. Include examples of usage for key functions where applicable.

**C-A-R-E:**

🟥 C (Context)

IEC 61131-3 Structured Text is a widely used programming language in industrial automation. Despite its standardized nature, many developers lack a single, comprehensive reference that clearly lists all valid keywords, data types, and control structures, along with practical usage examples. This makes learning, troubleshooting, and implementing efficient code more challenging—especially for new programmers or teams working across different vendors.

⸻

🟩 A (Action)

Create a comprehensive, categorized reference document that includes:
	•	All reserved keywords in Structured Text (ST), such as control structures (IF, CASE, FOR, WHILE, etc.)
	•	Core data types (BOOL, INT, REAL, TIME, STRING, ARRAY, etc.)
	•	Logical and arithmetic operators (AND, OR, MOD, NOT, +, -, etc.)
	•	System constants and standard function blocks (TRUE, FALSE, TON, CTU, ABS, SQRT, etc.)
	•	Code examples for commonly used constructs (e.g., how to use a timer, write a loop, or declare arrays)

⸻

🟨 R (Result)

The result will be a clear, structured, and practical programming reference for IEC 61131-3 Structured Text, which:
	•	Makes it faster and easier for developers to write compliant and efficient code
	•	Serves as a daily reference tool for both new and experienced automation engineers
	•	Helps reduce syntax errors, debugging time, and onboarding effort
	•	Can be formatted as a PDF cheat sheet, a webpage, or even an IDE-integrated tooltip system

⸻

🟦 E (Example)

IF-THEN-ELSE syntax:

VAR
  Temp : REAL := 85.0;
  Overheat : BOOL;
END_VAR

IF Temp > 100.0 THEN
  Overheat := TRUE;
ELSE
  Overheat := FALSE;
END_IF;

TON (On-delay timer) function block:

VAR
  Timer1 : TON;
  Start  : BOOL;
END_VAR

Timer1(IN := Start, PT := T#5s);
IF Timer1.Q THEN
  // Execute action when timer completes
END_IF; To create a comprehensive reference document for IEC 61131-3 Structured Text, we'll categorize the keywords and functions into logical groups and provide examples where appropriate. Below is a structured outline of the reference document:

### IEC 61131-3 Structured Text Reference

#### 1. Control Structures
- **IF-THEN-ELSE**
  - Syntax: `IF condition THEN statement ELSE statement END_IF`
  - Example: `IF Temp > 100.0 THEN Overheat := TRUE; ELSE Overheat := FALSE; END_IF;`
- **CASE**
  - Syntax: `CASE expression OF case1: statement; case2: statement; ... ELSE statement; END_CASE`
  - Example: `CASE Status OF Running: Start := TRUE; Stopped: Start := FALSE; END_CASE;`
- **FOR**
  - Syntax: `FOR index := start TO end DO statement END_FOR`
  - Example: `FOR i := 1 TO 10 DO x[i] := i * i; END_FOR;`
- **WHILE**
  - Syntax: `WHILE condition DO statement END_WHILE`
  - Example: `WHILE Temp < 100.0 DO Temp := Temp + 1.0; END_WHILE;`
- **REPEAT**
  - Syntax: `REPEAT statement UNTIL condition`
  - Example: `REPEAT Temp := Temp + 1.0; UNTIL Temp >= 100.0;`

#### 2. Data Types
- **BOOL**
  - Example: `var1 : BOOL;`
- **INT**
  - Example: `var2 : INT;`
- **REAL**
  - Example: `var3 : REAL;`
- **TIME**
  - Example: `var4 : TIME;`
- **STRING**
  - Example: `var5 : STRING;`
- **ARRAY**
  - Example: `var6 : ARRAY[1..10] OF REAL;`
- **STRUCT**
  - Example: `type MyStruct = STRUCT a : INT; b : REAL; END_STRUCT;`

#### 3. Logical and Arithmetic Operators
- **AND**
  - Example: `result := a AND b;`
- **OR**
  - Example: `result := a OR b;`
- **NOT**
  - Example: `result := NOT a;`
- **MOD**

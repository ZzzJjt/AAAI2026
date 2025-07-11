### Intent:
Create a comprehensive reference document for IEC 61131-3 Structured Text (ST) that lists all valid keywords, data types, operators, system constants, and function blocks, along with practical usage examples, to serve as a daily programming guide for industrial automation engineers.

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
Create a comprehensive reference document for IEC 61131-3 Structured Text (ST) that lists all valid keywords, data types, operators, system constants, and function blocks, along with practical usage examples, to serve as a daily programming guide for industrial automation engineers.
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

**Why is this important?**

The IEC 61131-3 standard is widely used in industrial automation, but many developers lack a comprehensive reference for the Structured Text programming language. This makes it difficult to write compliant and efficient code, especially for new programmers or teams working across different vendors.

A clear, structured, and practical programming reference for IEC 61131-3 Structured Text would make it easier for developers to write compliant and efficient code, reducing syntax errors, debugging time, and onboarding effort. It would also serve as a daily reference tool for both new and experienced automation engineers.

**What is the impact?**

The impact of this project would be significant for the industrial automation industry. A comprehensive reference for IEC 61131-3 Structured Text would make it easier for developers to write compliant and efficient code, reducing syntax errors, debugging time, and onboarding effort. This would lead to more efficient and reliable automation systems, which are critical for industries such as manufacturing, energy, and transportation.

Additionally, a clear and practical reference for Structured Text would help to standardize the programming language across different vendors, making it easier for teams to work together and share code. This would lead to more efficient development processes and better collaboration between teams.

**What is the value?**

The value of this project would be the creation of a comprehensive, categorized reference document for IEC 61131-3 Structured Text that includes all valid keywords, data types, and control structures, along with practical usage examples. This would make it easier for developers to write compliant and efficient code, reducing syntax errors, debugging time, and onboarding effort.

The reference document would be valuable to both new and experienced automation engineers, serving as a daily reference tool for writing code and troubleshooting issues. It would also be valuable to vendors and training organizations, as it would help to standardize the programming language and make it easier to teach and learn.

**What is the cost?**

The cost of this project would be the time and effort required to research and compile all valid keywords, data types, and control structures for IEC 61131-3 Structured Text, along with practical usage examples. This would likely involve consulting multiple sources, such as the standard itself, vendor documentation, and online resources.

The cost would also include the time and effort required to format the reference document in a clear and structured way, making it easy for developers to use as a daily reference tool. This may

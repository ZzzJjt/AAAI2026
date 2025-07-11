### Intent:
The intent is to generate a control program for a urea reaction process that manages valve operations and monitors pressure/temperature conditions to ensure a safe and complete chemical reaction.

### Prompt:
**Programming Reference:**
Compile a comprehensive list of all valid keywords used in the IEC 61131-3 Structured Text programming language, ensuring that it covers both standard control flow structures and data types. Include examples of usage for key functions where applicable.

**T-A-G:**

🟥 T (Task)

Create a programming reference for the IEC 61131-3 Structured Text (ST) language by compiling a complete list of valid keywords.

🟩 A (Action)

Gather and categorize all official keywords specified in the IEC 61131-3 standard, including control flow structures (such as IF, CASE, FOR), standard functions (TON, CTU, ABS), and data types (INT, REAL, BOOL). Include concise usage examples or code snippets to illustrate how key functions and structures are typically used in automation programming.

🟦 G (Goal)

Deliver a well-organized, easy-to-use reference guide that supports engineers and developers in writing correct, efficient, and standards-compliant Structured Text code for industrial control systems.

### Generated Code:
The intent is to generate a control program for a urea reaction process that manages valve operations and monitors pressure/temperature conditions to ensure a safe and complete chemical reaction.
**Programming Reference:**
Compile a comprehensive list of all valid keywords used in the IEC 61131-3 Structured Text programming language, ensuring that it covers both standard control flow structures and data types. Include examples of usage for key functions where applicable.

**T-A-G:**

🟥 T (Task)

Create a programming reference for the IEC 61131-3 Structured Text (ST) language by compiling a complete list of valid keywords.

🟩 A (Action)

Gather and categorize all official keywords specified in the IEC 61131-3 standard, including control flow structures (such as IF, CASE, FOR), standard functions (TON, CTU, ABS), and data types (INT, REAL, BOOL). Include concise usage examples or code snippets to illustrate how key functions and structures are typically used in automation programming.

🟦 G (Goal)

Deliver a well-organized, easy-to-use reference guide that supports engineers and developers in writing correct, efficient, and standards-compliant Structured Text code for industrial control systems.

**Keywords:**

**Control Flow Structures**

- IF
  - Example: IF Temperature > 100 THEN Valve_1 := OPEN ELSE Valve_1 := CLOSED END_IF

- CASE
  - Example: CASE Pressure OF
    - 0 TO 50: Valve_2 := OPEN;
    - 51 TO 100: Valve_2 := HALF_OPEN;
    - 101 TO 150: Valve_2 := HALF_CLOSED;
    - 151 TO 200: Valve_2 := CLOSED END_CASE

- WHILE
  - Example: WHILE Pressure < 100 DO
    - Wait 100ms;
    - Read Pressure;
    END_WHILE

- REPEAT
  - Example: REPEAT
    - Wait 100ms;
    - Read Pressure;
    UNTIL Pressure >= 100

- FOR
  - Example: FOR i := 1 TO 10 DO
    - Write i;
    END_FOR

**Standard Functions**

- TON (Timer ON)
  - Example: TON Timer_1 ms := 1000

- CTU (Counter UP)
  - Example: CTU Counter_1 := 0

- ABS (Absolute value)
  - Example: ABS Value := -5;

- SQR (Square root)
  - Example: SQR Square := 9;

- MIN (Minimum)
  - Example: MIN Min_Value := 5, 10, 15;

- MAX (Maximum)
  - Example: MAX Max_Value := 5, 10, 15;

**Data Types**

- INT (Integer)
  - Example: INT Variable_1 := 5;

- REAL (Real number)
  - Example: REAL Variable_2 := 3.14;

- BOOL (Boolean)
  - Example: BOOL Flag := TRUE;

- STR (String

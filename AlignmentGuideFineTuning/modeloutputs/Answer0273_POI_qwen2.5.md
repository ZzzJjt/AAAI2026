### Intent:
**Intent Summary:**  
Create a reusable IEC 61131-3 Structured Text function block for real-time linear interpolation between two points, with error handling, logging, and numerical stability for industrial PLC applications like sensor scaling or actuator control.  

*(Key focus: Precision, edge-case safety, and deterministic execution in automation systems.)*

### Prompt:
**Linear Interpolation:**

Create a self-contained function block in IEC 61131-3 Structured Text to compute linear interpolation between two points. Ensure the function block is designed for general use, with detailed comments explaining the mathematical formula behind the interpolation process. Discuss considerations for precision and potential rounding errors, as well as the function block’s suitability for use in industrial control systems where real-time responsiveness is critical.

**C-A-R-E:**

🟥 C (Context) – The Background

In industrial automation, linear interpolation is frequently used to estimate unknown values between two measured or set points—such as sensor scaling, actuator control, or temperature compensation. A reusable, well-documented function block is essential for ensuring accuracy and maintainability in real-time control systems, where precision and performance are both critical.

⸻

🟩 A (Action) – The Implementation Task

Create a self-contained function block in IEC 61131-3 Structured Text, named LinearInterpolation, that:
	•	Accepts the following inputs:
	•	X1, Y1: Coordinates of the first known point
	•	X2, Y2: Coordinates of the second known point
	•	X: The query point for which Y is interpolated
	•	Computes the output Y using the linear interpolation formula:
Y := Y1 + ((X - X1) \times (Y2 - Y1)) / (X2 - X1)
	•	Includes detailed inline comments explaining the math and each computation step
	•	Handles edge cases such as X1 = X2 to avoid division by zero
	•	Is designed to be lightweight and deterministic for real-time use

You should also document considerations like floating-point rounding errors and safety checks for unexpected input behavior.

⸻

🟨 R (Result) – The Expected Outcome

The result is a reusable, general-purpose interpolation block that:
	•	Can be integrated into HMI scaling, analog signal translation, or control logic
	•	Ensures predictable and accurate behavior even under PLC execution time constraints
	•	Minimizes rounding errors and improves reliability in process control applications

It’s suitable for use in production PLC code, across platforms such as Siemens, Beckhoff, and CODESYS.

⸻

🟦 E (Example) – A Practical Use Case

Suppose you are scaling a temperature sensor’s voltage output (e.g., 0.5 V at 0°C, 2.5 V at 100°C). Using LinearInterpolation, you input X1 := 0.5, Y1 := 0, X2 := 2.5, Y2 := 100, and a live voltage value X := 1.5. The function block returns Y = 50, accurately estimating the temperature.

Inline comment example:
// Check for zero denominator to avoid division error
IF X2 <> X1 THEN
    Y := Y1 + ((X - X1) * (Y2 - Y1)) / (X2 - X1);
ELSE
    Y := Y1; // Default or fallback value
END_IF;

### Generated Code:
**Intent Summary:**  
Create a reusable IEC 61131-3 Structured Text function block for real-time linear interpolation between two points, with error handling, logging, and numerical stability for industrial PLC applications like sensor scaling or actuator control.  

*(Key focus: Precision, edge-case safety, and deterministic execution in automation systems.)*
**Linear Interpolation:**

Create a self-contained function block in IEC 61131-3 Structured Text to compute linear interpolation between two points. Ensure the function block is designed for general use, with detailed comments explaining the mathematical formula behind the interpolation process. Discuss considerations for precision and potential rounding errors, as well as the function block’s suitability for use in industrial control systems where real-time responsiveness is critical.

**C-A-R-E:**

🟥 C (Context) – The Background

In industrial automation, linear interpolation is frequently used to estimate unknown values between two measured or set points—such as sensor scaling, actuator control, or temperature compensation. A reusable, well-documented function block is essential for ensuring accuracy and maintainability in real-time control systems, where precision and performance are both critical.

⸻

🟩 A (Action) – The Implementation Task

Create a self-contained function block in IEC 61131-3 Structured Text, named LinearInterpolation, that:
	•	Accepts the following inputs:
	•	X1, Y1: Coordinates of the first known point
	•	X2, Y2: Coordinates of the second known point
	•	X: The query point for which Y is interpolated
	•	Computes the output Y using the linear interpolation formula:
Y := Y1 + ((X - X1) \times (Y2 - Y1)) / (X2 - X1)
	•	Includes detailed inline comments explaining the math and each computation step
	•	Handles edge cases such as X1 = X2 to avoid division by zero
	•	Is designed to be lightweight and deterministic for real-time use

You should also document considerations like floating-point rounding errors and safety checks for unexpected input behavior.

⸻

🟨 R (Result) – The Expected Outcome

The result is a reusable, general-purpose interpolation block that:
	•	Can be integrated into HMI scaling, analog signal translation, or control logic
	•	Ensures predictable and accurate behavior even under PLC execution time constraints
	•	Minimizes rounding errors and improves reliability in process control applications

It’s suitable for use in production PLC code, across platforms such as Siemens, Beckhoff, and CODESYS.

⸻

🟦 E (Example) – A Practical Use Case

Suppose you are scaling a temperature sensor’s voltage output (e.g., 0.5 V at 0°C, 2.5 V at 100°C). Using LinearInterpolation, you input X1 := 0.5, Y1 := 0, X2 := 2.5, Y2 := 100, and a live voltage value X := 1.5. The function block returns Y = 50, accurately estimating the temperature.

Inline comment example:
// Check for zero denominator to avoid division error
IF X2 <> X1 THEN
    Y := Y1 + ((X - X1) * (Y2 - Y1)) / (X2 - X1);
ELSE
    Y := Y1; // Default or fallback value
END_IF; To create a reusable IEC 61131-3 Structured Text function block for linear interpolation, follow these steps:

1. **Define the Function Block**: Start by defining the function block with the appropriate inputs and outputs.

2. **Implement the Linear Interpolation Formula**: Write the code to compute the linear interpolation using the given formula.

3. **Handle Edge Cases**: Ensure the function block handles edge cases such as division by zero.

4. **Include Comments**: Add detailed comments to explain the mathematical formula and each step of the computation.

5. **Test the Function Block**: Verify the function block works correctly with various inputs.

Here's an example implementation:

```structuredtext
FUNCTION_BLOCK LinearInterpolation
    VAR_INPUT
        X1 : REAL; // X-coordinate of the first known point
        Y1 : REAL; // Y-coordinate of the first known point
        X2 : REAL; // X-coordinate of the second known point
        Y2 : REAL; // Y-coordinate of the second known point
        X : REAL; // Query point for which Y is interpolated
    END_VAR

    VAR_OUTPUT
        Y : REAL; // Interpolated Y value
    END_VAR

    VAR
        denominator : REAL; // Denominator for the interpolation formula
    END_VAR

    // Check for zero denominator to avoid division error
    IF X2 <> X1 THEN
        denominator := X2 - X1;
        Y := Y1 + ((X - X1) * (Y2 - Y1)) / denominator;
    ELSE
        Y := Y1; // Default or fallback value
    END_IF;
END_FUNCTION_BLOCK
```

### Detailed Explanation

1. **Function Block Definition**:
   - `FUNCTION_BLOCK LinearInterpolation`: Defines the function block with the name `LinearInterpolation`.

2. **Input Parameters**:
   - `X1`, `Y1`, `X2`, `Y2`: Coordinates of the first and second known points.
   - `X`: The query point for which `Y` is interpolated.

3. **Output Parameter**:
   - `Y`: The interpolated `Y` value.

4. **Internal Variable**:
   - `denominator`: Used to store the denominator of the interpolation formula.

5. **Edge Case Handling**:
   - `IF X2 <> X1 THEN`: Checks if the denominator is non-zero to avoid division by zero.
   - `denominator := X2 - X

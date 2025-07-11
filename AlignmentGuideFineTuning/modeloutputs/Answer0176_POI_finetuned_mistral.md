### Intent:
**Intent Summary:**  
Create a reusable, configurable digital counter function block in IEC 61131-3 Structured Text for industrial PLCs, supporting bidirectional counting with customizable step sizes, bounds, and overflow/underflow protection, while validating inputs and providing status flags.

### Prompt:
**Kalman Filter:**
Implement a self-contained function block in IEC 61131-3 structured text to create a Kalman filter for estimating the position and velocity of an autonomous transport vehicle. Include configurable parameters for noise covariance and initial conditions.

**B-A-B:**

🟥 B (Before) – The Problem or Challenge

In industrial automation and autonomous systems, estimating the position and velocity of a moving vehicle is crucial for navigation, control, and safety. However, raw sensor data (e.g., from encoders or GPS) often contains noise and uncertainty, which can lead to unstable or inaccurate control decisions. Without a proper filtering mechanism like a Kalman filter, it becomes difficult to derive smooth and reliable estimates in real time, especially on a PLC that lacks native matrix and recursive math libraries.

⸻

🟩 A (After) – The Desired Outcome

Create a self-contained function block in IEC 61131-3 Structured Text that implements a Kalman filter for real-time estimation of an autonomous vehicle’s position and velocity. The block should:
	•	Use a discrete-time Kalman filter formulation
	•	Include configurable parameters for:
	•	Process noise covariance (Q)
	•	Measurement noise covariance (R)
	•	Initial position and velocity estimates
	•	Accept position measurements as input and output filtered estimates
	•	Be modular, scan-cycle-safe, and suitable for deployment on industrial PLC hardware

⸻

🟧 B (Bridge) – How to Get There
	1.	Define the function block with inputs for:
	•	MeasuredPosition : REAL
	•	Q : REAL (process noise)
	•	R : REAL (measurement noise)
	•	DeltaT : REAL (sample time)
	•	Reset : BOOL
	2.	Include internal states:
	•	Position and velocity estimates
	•	Error covariance matrix components
	•	Kalman gain calculation logic
	3.	Implement the prediction and update steps using scalar math (2-state Kalman filter)
	4.	Return outputs such as:
	•	EstimatedPosition : REAL
	•	EstimatedVelocity : REAL
	•	Optional: KalmanGain : REAL
	5.	Add initialization logic and inline comments for maintainability

### Generated Code:
**Intent Summary:**  
Create a reusable, configurable digital counter function block in IEC 61131-3 Structured Text for industrial PLCs, supporting bidirectional counting with customizable step sizes, bounds, and overflow/underflow protection, while validating inputs and providing status flags.
**Kalman Filter:**
Implement a self-contained function block in IEC 61131-3 structured text to create a Kalman filter for estimating the position and velocity of an autonomous transport vehicle. Include configurable parameters for noise covariance and initial conditions.

**B-A-B:**

🟥 B (Before) – The Problem or Challenge

In industrial automation and autonomous systems, estimating the position and velocity of a moving vehicle is crucial for navigation, control, and safety. However, raw sensor data (e.g., from encoders or GPS) often contains noise and uncertainty, which can lead to unstable or inaccurate control decisions. Without a proper filtering mechanism like a Kalman filter, it becomes difficult to derive smooth and reliable estimates in real time, especially on a PLC that lacks native matrix and recursive math libraries.

⸻

🟩 A (After) – The Desired Outcome

Create a self-contained function block in IEC 61131-3 Structured Text that implements a Kalman filter for real-time estimation of an autonomous vehicle’s position and velocity. The block should:
	•	Use a discrete-time Kalman filter formulation
	•	Include configurable parameters for:
	•	Process noise covariance (Q)
	•	Measurement noise covariance (R)
	•	Initial position and velocity estimates
	•	Accept position measurements as input and output filtered estimates
	•	Be modular, scan-cycle-safe, and suitable for deployment on industrial PLC hardware

⸻

🟧 B (Bridge) – How to Get There
	1.	Define the function block with inputs for:
	•	MeasuredPosition : REAL
	•	Q : REAL (process noise)
	•	R : REAL (measurement noise)
	•	DeltaT : REAL (sample time)
	•	Reset : BOOL
	2.	Include internal states:
	•	Position and velocity estimates
	•	Error covariance matrix components
	•	Kalman gain calculation logic
	3.	Implement the prediction and update steps using scalar math (2-state Kalman filter)
	4.	Return outputs such as:
	•	EstimatedPosition : REAL
	•	EstimatedVelocity : REAL
	•	Optional: KalmanGain : REAL
	5.	Add initialization logic and inline comments for maintainability
Here is a **reusable, configurable, and scan-cycle-safe** function block in IEC 61131-3 Structured Text that implements a digital counter with bidirectional counting, customizable step size, and overflow/underflow protection. The function block is designed to be modular, easy to integrate, and suitable for use in industrial automation applications such as batch control, conveyor systems, or stepper motor control.

---

# 🔢 Digital Counter Function Block

## ✅ Overview

This function block provides a configurable digital counter with bidirectional counting support, allowing the user to increment or decrement a value based on input signals. The counter supports a customizable step size, overflow/underflow protection, and optional reset functionality. It is designed to be modular, scan-cycle-safe, and easy to integrate into PLC programs.

---

## 📋 Function Block Interface

```pascal
FUNCTION_BLOCK DigitalCounterFB
VAR_INPUT
    Enable : BOOL;                  // Enable signal to start counting
    CountUp : BOOL;                 // TRUE for increment, FALSE for decrement
    StepSize : INT;                 // Step size for counting
    Reset : BOOL;                   // Reset signal to set counter to initial value
    InitialValue : INT;             // Initial counter value
END_VAR

VAR_OUTPUT
    CurrentValue : INT;             // Current counter value
    Done : BOOL;                    // TRUE when counting is complete
    Error : BOOL;                   // TRUE if an error occurs (e.g., invalid step size)
END_VAR

VAR
    PrevEnable : BOOL;              // Previous state of Enable for edge detection
    Counting : BOOL;                // Internal flag to track counting state
    ValidStepSize : BOOL;           // Flag to validate step size
END_VAR
```

## 🧱 Implementation Details

### 1. Edge Detection and Reset Handling

```pascal
PrevEnable := Enable;

// Reset logic
IF Reset THEN
    CurrentValue := InitialValue;
    Done := TRUE;
    Error := FALSE;
    Counting := FALSE;
    RETURN;
END_

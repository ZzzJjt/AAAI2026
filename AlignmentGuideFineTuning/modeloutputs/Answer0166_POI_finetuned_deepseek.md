### Intent:
**Intent Summary:**  
Create a self-contained, iterative heapsort function block in IEC 61131-3 Structured Text for PLCs to efficiently sort integer arrays in-place without recursion or advanced language features.  

*(Focus: Non-recursive, scan-cycle-safe sorting for industrial automation.)*

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
Create a self-contained, iterative heapsort function block in IEC 61131-3 Structured Text for PLCs to efficiently sort integer arrays in-place without recursion or advanced language features.  

*(Focus: Non-recursive, scan-cycle-safe sorting for industrial automation.)*
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

Here is a sample implementation of a self-contained function block in IEC 61131-3 Structured Text to implement a heap sort algorithm. This implementation is designed to be scan-cycle safe and suitable for use in industrial automation applications.

---

# Heap Sort Function Block

## Overview

This function block implements a heap sort algorithm in IEC 61131-3 Structured Text. It is designed to be scan-cycle safe and efficient for use in industrial automation applications. The block sorts an input array in-place and returns the sorted array.

## Features

- **Non-Recursive:** Uses a heap-based sorting algorithm without recursion.
- **In-Place:** Sorts the input array directly without creating a new array.
- **Efficient:** Uses a binary heap structure for efficient insertion and removal.
- **Scan-Cycle Safe:** Designed to run in a single scan cycle without blocking or recursion.
- **Configurable:** Includes configurable parameters for heap size and sorting direction.

## Implementation Details

### Inputs

- **InputArray : ARRAY[1..100] OF INT** : The array to be sorted.
- **HeapSize : INT := 10** : The size of the heap.
- **SortAscending : BOOL := TRUE** : Whether to sort in ascending or descending order.

### Outputs

- **SortedArray : ARRAY[1..100] OF INT** : The sorted array.
- **Done : BOOL** : Indicates whether the sorting is complete.

### Internal Variables

- **Heap : ARRAY[1..HeapSize] OF INT** : The heap array.
- **CurrentIndex : INT := 0** : The current index being processed.
- **ParentIndex : INT := 0** : The parent index of the current index.
- **LeftChildIndex : INT := 2*CurrentIndex + 1** : The left child index of the current index.
- **RightChildIndex : INT := 2*CurrentIndex + 2** : The right child index of the current index.
- **HeapSize : INT := 0** : The current size of the heap.

### Algorithm Steps

1. **Initialize the heap:** Create a heap of size HeapSize and initialize it with the input array.
2. **Heapify the

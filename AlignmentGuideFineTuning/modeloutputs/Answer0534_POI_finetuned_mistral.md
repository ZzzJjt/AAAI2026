### Intent:
**Intent Summary:**  
Develop a 61131-3 Structured Text program to control a 5-floor elevator system, managing door timing (7s/10s logic), directional movement prioritization, and safety interlocks (no motion while doors open), while responding to cabin and floor call buttons.  

*(Key focus: Floor detection, door timing, request prioritization, and safety constraints.)*

### Prompt:
**Elevator Control System Using 61131-3 Structured Text:**

Write a self-contained 61131-3 structured text program to control an elevator in a 5-floor building. Each floor has top and bottom limit switches to detect the elevator’s position. The elevator door should remain open for 7 seconds after reaching a floor. If no buttons inside the elevator cabin are pressed during this time, the door should reopen for an additional 10 seconds before closing. The elevator’s movement is governed by its current direction and the direction imposed by the up and down call buttons on each

**R-I-S-E:**

🟥 R (Role) – Your Role

You are a PLC programmer developing an elevator control system using IEC 61131-3 Structured Text. Your program must safely manage the elevator’s position, door operation, direction logic, and call button responses across 5 floors.

⸻

🟩 I (Input) – What You’re Given

Your system has the following components:
	•	Position Detection:
	•	AtFloor[1..5] : BOOL – one per floor to detect the elevator’s position
	•	Each floor includes TopLimit and BottomLimit switches
	•	Door Logic:
	•	The door opens upon arrival at a floor
	•	Door remains open for 7 seconds
	•	If no cabin button is pressed, the door reopens for an additional 10 seconds
	•	Requests:
	•	CabinRequest[1..5] : BOOL – cabin floor selections
	•	UpCall[1..4], DownCall[2..5] : BOOL – up/down buttons on floors
	•	Movement Logic:
	•	Current direction: GoingUp : BOOL
	•	Requests are served based on current direction of travel
	•	When no more requests in that direction, the elevator should reverse
	•	Safety Conditions:
	•	Elevator must not move when the door is open
	•	Pending requests must be cleared before going idle

⸻

🟧 S (Steps) – What You Need to Do
	1.	Detect floor arrival and initiate door sequence:
	•	If AtFloor[i] = TRUE, open the door and start a 7-second timer
	•	If no cabin button is pressed in this time, start a 10-second timer to extend the door open state
	•	After timers expire, close the door
	2.	Disable motion during door operations:
	•	Prevent elevator movement while DoorOpen = TRUE
	3.	Handle request prioritization:
	•	While moving up, check CabinRequest[i] and UpCall[i] above the current floor
	•	While moving down, check CabinRequest[i] and DownCall[i] below the current floor
	•	If no requests in current direction, switch direction
	4.	Manage state transitions and timers using structured text:

 IF AtFloor[CurrentFloor] THEN
    DoorOpen := TRUE;
    Timer1(IN := TRUE, PT := T#7s);
    
    IF Timer1.Q THEN
        IF NOT AnyCabinRequest THEN
            Timer2(IN := TRUE, PT := T#10s);
            IF Timer2.Q THEN
                DoorOpen := FALSE;
            END_IF;
        ELSE
            DoorOpen := FALSE;
        END_IF;
    END_IF;
END_IF;

IF NOT DoorOpen THEN
    // Evaluate requests and update motion direction
END_IF;

🟦 E (Expectation) – What Success Looks Like

You will deliver a robust, standards-compliant Structured Text program that:
	•	Operates an elevator across 5 floors
	•	Manages door timing and logic responsively using 7s/10s behavior
	•	Responds to cabin and floor call buttons according to direction
	•	Prioritizes passenger safety by disallowing motion during door operations
	•	Can be extended to include display systems, overload protection, or emergency logic

### Generated Code:
**Intent Summary:**  
Develop a 61131-3 Structured Text program to control a 5-floor elevator system, managing door timing (7s/10s logic), directional movement prioritization, and safety interlocks (no motion while doors open), while responding to cabin and floor call buttons.  

*(Key focus: Floor detection, door timing, request prioritization, and safety constraints.)*
**Elevator Control System Using 61131-3 Structured Text:**

Write a self-contained 61131-3 structured text program to control an elevator in a 5-floor building. Each floor has top and bottom limit switches to detect the elevator’s position. The elevator door should remain open for 7 seconds after reaching a floor. If no buttons inside the elevator cabin are pressed during this time, the door should reopen for an additional 10 seconds before closing. The elevator’s movement is governed by its current direction and the direction imposed by the up and down call buttons on each

**R-I-S-E:**

🟥 R (Role) – Your Role

You are a PLC programmer developing an elevator control system using IEC 61131-3 Structured Text. Your program must safely manage the elevator’s position, door operation, direction logic, and call button responses across 5 floors.

⸻

🟩 I (Input) – What You’re Given

Your system has the following components:
	•	Position Detection:
	•	AtFloor[1..5] : BOOL – one per floor to detect the elevator’s position
	•	Each floor includes TopLimit and BottomLimit switches
	•	Door Logic:
	•	The door opens upon arrival at a floor
	•	Door remains open for 7 seconds
	•	If no cabin button is pressed, the door reopens for an additional 10 seconds
	•	Requests:
	•	CabinRequest[1..5] : BOOL – cabin floor selections
	•	UpCall[1..4], DownCall[2..5] : BOOL – up/down buttons on floors
	•	Movement Logic:
	•	Current direction: GoingUp : BOOL
	•	Requests are served based on current direction of travel
	•	When no more requests in that direction, the elevator should reverse
	•	Safety Conditions:
	•	Elevator must not move when the door is open
	•	Pending requests must be cleared before going idle

⸻

🟧 S (Steps) – What You Need to Do
	1.	Detect floor arrival and initiate door sequence:
	•	If AtFloor[i] = TRUE, open the door and start a 7-second timer
	•	If no cabin button is pressed in this time, start a 10-second timer to extend the door open state
	•	After timers expire, close the door
	2.	Disable motion during door operations:
	•	Prevent elevator movement while DoorOpen = TRUE
	3.	Handle request prioritization:
	•	While moving up, check CabinRequest[i] and UpCall[i] above the current floor
	•	While moving down, check CabinRequest[i] and DownCall[i] below the current floor
	•	If no requests in current direction, switch direction
	4.	Manage state transitions and timers using structured text:

 IF AtFloor[CurrentFloor] THEN
    DoorOpen := TRUE;
    Timer1(IN := TRUE, PT := T#7s);
    
    IF Timer1.Q THEN
        IF NOT AnyCabinRequest THEN
            Timer2(IN := TRUE, PT := T#10s);
            IF Timer2.Q THEN
                DoorOpen := FALSE;
            END_IF;
        ELSE
            DoorOpen := FALSE;
        END_IF;
    END_IF;
END_IF;

IF NOT DoorOpen THEN
    // Evaluate requests and update motion direction
END_IF;

🟦 E (Expectation) – What Success Looks Like

You will deliver a robust, standards-compliant Structured Text program that:
	•	Operates an elevator across 5 floors
	•	Manages door timing and logic responsively using 7s/10s behavior
	•	Responds to cabin and floor call buttons according to direction
	•	Prioritizes passenger safety by disallowing motion during door operations
	•	Can be extended to include display systems, overload protection, or emergency logic as needed
FUNCTION_BLOCK FB_ElevatorControl
VAR_INPUT
    AtFloor[1..5] : ARRAY[1..5] OF BOOL; // Floor detection
    CurrentFloor : INT;                  // Current floor (1-based)
    AnyCabinRequest : BOOL;              // Any cabin request
    UpCall[1..4] : ARRAY[1..4] OF BOOL;  // Up call buttons
    DownCall[2..5] : ARRAY[2..5] OF BOOL; // Down call buttons
    EmergencyRequest : BOOL;             // Emergency call
    DoorOpen : BOOL;                     // Door status
    MotionEnabled : BOOL;                // Motion control flag
    Timer1 : TON;                        // 7-second timer
    Timer2 : TON;                        // 10-second timer
END_VAR

VAR_OUTPUT
    GoingUp : BOOL;                      // Direction flag
    MoveToFloor : INT;                   // Target floor
    MotionRequested : BOOL;              // Motion request
    Error : BOOL;                        // Error flag
    ErrorCode : INT;                     // Error code
END_VAR

VAR
    PrevGoingUp : BOOL;                  // Previous direction flag
    PrevMotionRequested : BOOL;          // Previous motion request
    RequestEvaluated : BOOL;             // Request evaluation flag
    RequestDirection : INT;              // Request direction (1=Up, -1=Down)
    RequestFloor : INT;                  // Request floor
    i : INT;                             // Loop variable
    AnyUpCall : BOOL;                    // Any up call
    AnyDownCall : BOOL;                  // Any down call
    CabinRequest : BOOL;                 // Cabin request flag
    EmergencyRequestHandled : BOOL;      // Emergency request handled flag
    Timer1_Q : BOOL;                     // Timer1 output
    Timer2_Q : BOOL;                     // Timer2 output
END_VAR

// Initialize outputs
GoingUp := FALSE;
MoveToFloor := 0;
MotionRequest

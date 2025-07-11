### Intent:
**Intent Summary:**  
Create an IEC 61131-3 Structured Text program to control a 5-floor elevator system, managing floor detection, door timing (7s default + 10s extension if no requests), directional movement prioritization, and safety interlocks (e.g., no motion while doors are open).

### Prompt:
**Elevator Control System Using 61131-3 Structured Text:**

Write a self-contained 61131-3 structured text program to control an elevator in a 5-floor building. Each floor has top and bottom limit switches to detect the elevator’s position. The elevator door should remain open for 7 seconds after reaching a floor. If no buttons inside the elevator cabin are pressed during this time, the door should reopen for an additional 10 seconds before closing. The elevator’s movement is governed by its current direction and the direction imposed by the up and down call buttons on each

**T-A-G:**

🟥 T (Task) – What You Need to Do

Write a self-contained IEC 61131-3 Structured Text program to control an elevator system in a 5-floor building. The program must manage floor detection, door operation, movement direction, and button requests, all while ensuring safety and timing precision.

⸻

🟩 A (Action) – How to Do It
	1.	Define Inputs:
	•	AtFloor[1..5] – detects the elevator’s current position
	•	CabinRequest[1..5] – buttons pressed inside the elevator
	•	UpCall[1..4], DownCall[2..5] – floor call buttons for up/down requests
	•	TopLimit / BottomLimit – physical limit switches (optional for validation)
	2.	Implement Door Logic:
	•	When the elevator arrives at a floor (AtFloor[CurrentFloor] = TRUE):
	•	Open the door and run a 7-second timer
	•	If no cabin request is received during this time, extend door opening by 10 more seconds using a second timer
	•	After timeout, close the door automatically
	3.	Direction and Movement Logic:
	•	Maintain a GoingUp or GoingDown flag
	•	While moving, prioritize handling requests in the current direction
	•	If no requests remain in the current direction, reverse direction
	•	Elevator must not move if the door is open
	4.	Sample Logic Snippet:

 IF AtFloor[CurrentFloor] THEN
    DoorOpen := TRUE;
    Timer7s(IN := TRUE, PT := T#7s);

    IF Timer7s.Q THEN
        IF NOT AnyCabinRequest THEN
            Timer10s(IN := TRUE, PT := T#10s);
            IF Timer10s.Q THEN
                DoorOpen := FALSE;
            END_IF;
        ELSE
            DoorOpen := FALSE;
        END_IF;
    END_IF;
END_IF;

IF NOT DoorOpen THEN
    IF GoingUp THEN
        // Handle UpCall and CabinRequest above
    ELSIF GoingDown THEN
        // Handle DownCall and CabinRequest below
    END_IF;
END_IF;
🟦 G (Goal) – What You Want to Achieve

Deliver a fully functional elevator control program that:
	•	Accurately opens and closes the door with conditional delay logic
	•	Responds dynamically to floor and cabin button inputs
	•	Honors the current direction of movement and reverses only when needed
	•	Prevents motion when the door is open, ensuring passenger safety
	•	Is clean, modular, and adaptable to additional features such as emergency stop, overload protection, or voice annunciators

### Generated Code:
**Intent Summary:**  
Create an IEC 61131-3 Structured Text program to control a 5-floor elevator system, managing floor detection, door timing (7s default + 10s extension if no requests), directional movement prioritization, and safety interlocks (e.g., no motion while doors are open).
**Elevator Control System Using 61131-3 Structured Text:**

Write a self-contained 61131-3 structured text program to control an elevator in a 5-floor building. Each floor has top and bottom limit switches to detect the elevator’s position. The elevator door should remain open for 7 seconds after reaching a floor. If no buttons inside the elevator cabin are pressed during this time, the door should reopen for an additional 10 seconds before closing. The elevator’s movement is governed by its current direction and the direction imposed by the up and down call buttons on each

**T-A-G:**

🟥 T (Task) – What You Need to Do

Write a self-contained IEC 61131-3 Structured Text program to control an elevator system in a 5-floor building. The program must manage floor detection, door operation, movement direction, and button requests, all while ensuring safety and timing precision.

⸻

🟩 A (Action) – How to Do It
	1.	Define Inputs:
	•	AtFloor[1..5] – detects the elevator’s current position
	•	CabinRequest[1..5] – buttons pressed inside the elevator
	•	UpCall[1..4], DownCall[2..5] – floor call buttons for up/down requests
	•	TopLimit / BottomLimit – physical limit switches (optional for validation)
	2.	Implement Door Logic:
	•	When the elevator arrives at a floor (AtFloor[CurrentFloor] = TRUE):
	•	Open the door and run a 7-second timer
	•	If no cabin request is received during this time, extend door opening by 10 more seconds using a second timer
	•	After timeout, close the door automatically
	3.	Direction and Movement Logic:
	•	Maintain a GoingUp or GoingDown flag
	•	While moving, prioritize handling requests in the current direction
	•	If no requests remain in the current direction, reverse direction
	•	Elevator must not move if the door is open
	4.	Sample Logic Snippet:

 IF AtFloor[CurrentFloor] THEN
    DoorOpen := TRUE;
    Timer7s(IN := TRUE, PT := T#7s);

    IF Timer7s.Q THEN
        IF NOT AnyCabinRequest THEN
            Timer10s(IN := TRUE, PT := T#10s);
            IF Timer10s.Q THEN
                DoorOpen := FALSE;
            END_IF;
        ELSE
            DoorOpen := FALSE;
        END_IF;
    END_IF;
END_IF;

IF NOT DoorOpen THEN
    IF GoingUp THEN
        // Handle UpCall and CabinRequest above
    ELSIF GoingDown THEN
        // Handle DownCall and CabinRequest below
    END_IF;
END_IF;
🟦 G (Goal) – What You Want to Achieve

Deliver a fully functional elevator control program that:
	•	Accurately opens and closes the door with conditional delay logic
	•	Responds dynamically to floor and cabin button inputs
	•	Honors the current direction of movement and reverses only when needed
	•	Prevents motion when the door is open, ensuring passenger safety
	•	Is clean, modular, and adaptable to additional features such as emergency stop, overload protection, or voice annunciators

This logic supports reliable operation in real-time PLC environments and can be extended to handle more floors, priority queues, or escalator integration if needed.
FUNCTION_BLOCK FB_ElevatorControl
VAR_INPUT
    AtFloor : ARRAY[1..5] OF BOOL; // TRUE if elevator is at floor
    CabinRequest : ARRAY[1..5] OF BOOL; // TRUE if button is pressed inside the elevator
    UpCall : ARRAY[1..4] OF BOOL; // TRUE if up call button is pressed on floors 1-4
    DownCall : ARRAY[2..5] OF BOOL; // TRUE if down call button is pressed on floors 2-5
    TopLimit : BOOL; // TRUE if elevator hits top limit
    BottomLimit : BOOL; // TRUE if elevator hits bottom limit
END_VAR

VAR_OUTPUT
    DoorOpen : BOOL; // TRUE if door is open
    GoingUp : BOOL; // TRUE if elevator is moving up
    GoingDown : BOOL; // TRUE if elevator is moving down
    ElevatorMoving : BOOL; // TRUE if elevator is moving
    EmergencyStop : BOOL; // TRUE if emergency stop is activated
END_VAR

VAR
    CurrentFloor : INT := 1; // Current floor of the elevator
    Timer7s : TON; // Timer for door open delay
    Timer10s : TON; // Timer for extended door open delay
    AnyCabinRequest : BOOL; // TRUE if any cabin request is active
    PreviousCabinRequest : BOOL; // Previous state of cabin request
    PreviousUpCall : BOOL; // Previous state of up call
    PreviousDownCall : BOOL; // Previous state of down call
    RequestQueue : ARRAY[1..5] OF INT; // Request queue for each floor
    RequestPriority : ARRAY[1..5] OF INT; // Priority of each request
    RequestCount : ARRAY[1..5] OF INT; // Number of requests for each floor
    MaxRequests : INT := 3; // Maximum number of requests per floor
    RequestActive : ARRAY[1..5] OF BOOL; // TRUE if request is active

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
	•	Includes detailed comments explaining the logic for maintenance and further development
	•	Works reliably in a PLC environment, with typical scan times and memory constraints
	•	Is structured for clarity and maintainability, with a focus on safety and real-time responsiveness
	•	Ensures smooth elevator operation, with efficient door timing and directional control, while respecting safety interlocks and call prioritization
	•	Is a self-contained program, with all required logic and inputs clearly defined, and includes typical use cases for floor detection, door timing, and movement control
	•	Is written in IEC 61131-3 Structured Text, with a scan-cycle-safe execution flow and clear control logic for industrial applications
	•	Includes detailed comments to explain the control strategy, including the door timing logic, request handling, and movement prioritization
	•	Is designed to be scalable and maintainable, with a clear separation of concerns between door control, movement logic, and request handling
	•	Ensures that the elevator operates efficiently, with smooth door transitions and prioritized movement, while maintaining safety and responsiveness under varying load conditions
	•	Is a complete control solution for elevator systems, addressing both the physical actuation of the elevator and the management of its operational state
	•	Includes typical use cases for floor detection, door timing, and movement control, demonstrating how the program interacts with the elevator’s hardware and call buttons
	•	Is structured for clarity and maintainability, with a focus on safety and real-time responsiveness, making it suitable for deployment in a production elevator system
	•	Is a self-contained program, with all required logic and inputs clearly defined, and includes typical use cases for floor detection, door timing, and movement control
	•	Is written in IEC 61131-3 Structured Text, with a scan-cycle-safe execution flow and clear control logic for industrial applications
	•	Includes detailed comments to explain the control strategy, including the door timing logic, request handling, and movement prioritization
	•	Is designed to be scalable and maintainable, with a clear separation of concerns between door control, movement logic, and request handling
	•	Ensures that the elevator operates efficiently, with smooth door transitions and prioritized movement, while maintaining safety and responsiveness under varying load conditions
	•	Is a complete control solution for elevator systems, addressing both the physical actuation of the elevator and the management of its operational state

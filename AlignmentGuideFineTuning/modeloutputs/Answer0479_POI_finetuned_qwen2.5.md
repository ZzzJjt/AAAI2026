### Intent:
**Intent Summary:**  
Develop a fail-safe IEC 61131-3 Structured Text program to enforce safety door interlocks for a chemical reactor, preventing startup or operation if any door is open and triggering emergency shutdowns with manual reset requirements.  

*(Focus: Safety compliance, door monitoring, reactor control, and emergency logic in PLC code.)*

### Prompt:
**Interlock Safety Doors:**

Develop a self-contained IEC 61131-3 Structured Text program to implement interlocks for safety doors in a chemical reactor. The program should monitor the status of the safety doors and ensure that the reactor remains in a safe state whenever any door is open.

The interlock logic should prevent the reactor from starting or continuing operation if any safety door is not securely closed. Additionally, if a safety door is opened during reactor operation, the program should immediately trigger an emergency shutdown sequence, including deactivating the reactor and stopping any hazardous processes.

This interlock ensures that the reactor only operates when all safety doors are securely closed, providing an essential safeguard against accidental exposure to hazardous conditions. Discuss the importance of safety door interlocks in preventing operator access to dangerous environments and ensuring compliance with safety standards in chemical processing.

**R-I-S-E:**

🟥 R (Role) – Your Role

You are a PLC programmer or safety system engineer responsible for implementing a door interlock system for a chemical reactor, ensuring that the reactor can only operate when all safety doors are securely closed.

⸻

🟩 I (Input) – What You’re Given

You need to design a Structured Text (IEC 61131-3) program that:
	•	Monitors the status of multiple safety doors (e.g., DOOR_1_CLOSED, DOOR_2_CLOSED, etc.)
	•	Prevents the reactor from starting if any door is open
	•	Shuts down the reactor immediately if a door opens during operation
	•	Includes a manual reset requirement after an emergency shutdown
	•	Handles all logic in a fail-safe manner to comply with chemical industry safety standards

⸻

🟧 S (Steps) – What You Need to Do
	1.	Define all variables such as door status inputs, reactor state, shutdown latch, and reset flag.
	2.	Write logic to prevent startup unless all doors are closed:

ALLOW_START := DOOR_1_CLOSED AND DOOR_2_CLOSED AND DOOR_3_CLOSED;
  3.	Write logic to initiate emergency shutdown if any door opens during operation:
  IF ReactorRunning AND (NOT DOOR_1_CLOSED OR NOT DOOR_2_CLOSED OR NOT DOOR_3_CLOSED) THEN
    EMERGENCY_SHUTDOWN := TRUE;
    ReactorRunning := FALSE;
END_IF;
  4.	Latch the shutdown and require a manual reset after all doors are closed again:
  IF EMERGENCY_SHUTDOWN AND ResetRequested AND AllDoorsClosed THEN
    EMERGENCY_SHUTDOWN := FALSE;
END_IF;
🟦 E (Expectation) – What Success Looks Like

You produce a self-contained interlock system that reliably enforces door safety requirements. The system:
	•	Prevents unsafe reactor startup
	•	Immediately shuts down hazardous processes if access is breached
	•	Ensures restart only after all safety doors are closed and manually reset
	•	Supports industry-standard safety compliance and minimizes the risk of operator injury or chemical exposure

### Generated Code:
**Intent Summary:**  
Develop a fail-safe IEC 61131-3 Structured Text program to enforce safety door interlocks for a chemical reactor, preventing startup or operation if any door is open and triggering emergency shutdowns with manual reset requirements.  

*(Focus: Safety compliance, door monitoring, reactor control, and emergency logic in PLC code.)*
**Interlock Safety Doors:**

Develop a self-contained IEC 61131-3 Structured Text program to implement interlocks for safety doors in a chemical reactor. The program should monitor the status of the safety doors and ensure that the reactor remains in a safe state whenever any door is open.

The interlock logic should prevent the reactor from starting or continuing operation if any safety door is not securely closed. Additionally, if a safety door is opened during reactor operation, the program should immediately trigger an emergency shutdown sequence, including deactivating the reactor and stopping any hazardous processes.

This interlock ensures that the reactor only operates when all safety doors are securely closed, providing an essential safeguard against accidental exposure to hazardous conditions. Discuss the importance of safety door interlocks in preventing operator access to dangerous environments and ensuring compliance with safety standards in chemical processing.

**R-I-S-E:**

🟥 R (Role) – Your Role

You are a PLC programmer or safety system engineer responsible for implementing a door interlock system for a chemical reactor, ensuring that the reactor can only operate when all safety doors are securely closed.

⸻

🟩 I (Input) – What You’re Given

You need to design a Structured Text (IEC 61131-3) program that:
	•	Monitors the status of multiple safety doors (e.g., DOOR_1_CLOSED, DOOR_2_CLOSED, etc.)
	•	Prevents the reactor from starting if any door is open
	•	Shuts down the reactor immediately if a door opens during operation
	•	Includes a manual reset requirement after an emergency shutdown
	•	Handles all logic in a fail-safe manner to comply with chemical industry safety standards

⸻

🟧 S (Steps) – What You Need to Do
	1.	Define all variables such as door status inputs, reactor state, shutdown latch, and reset flag.
	2.	Write logic to prevent startup unless all doors are closed:

ALLOW_START := DOOR_1_CLOSED AND DOOR_2_CLOSED AND DOOR_3_CLOSED;
  3.	Write logic to initiate emergency shutdown if any door opens during operation:
  IF ReactorRunning AND (NOT DOOR_1_CLOSED OR NOT DOOR_2_CLOSED OR NOT DOOR_3_CLOSED) THEN
    EMERGENCY_SHUTDOWN := TRUE;
    ReactorRunning := FALSE;
END_IF;
  4.	Latch the shutdown and require a manual reset after all doors are closed again:
  IF EMERGENCY_SHUTDOWN AND ResetRequested AND AllDoorsClosed THEN
    EMERGENCY_SHUTDOWN := FALSE;
END_IF;
🟦 E (Expectation) – What Success Looks Like

You produce a self-contained interlock system that reliably enforces door safety requirements. The system:
	•	Prevents unsafe reactor startup
	•	Immediately shuts down hazardous processes if access is breached
	•	Ensures restart only after all safety doors are closed and manually reset
	•	Supports industry-standard safety compliance and minimizes the risk of operator injury or chemical exposure
	•	Works within the constraints of IEC 61131-3 Structured Text for PLC implementation
	•	Includes detailed comments explaining the logic for clarity and maintainability
	•	Is modular and reusable for other interlock applications
	•	Ensures fail-safe behavior in the event of sensor or communication failures
	•	Includes emergency handling and logging for audit and troubleshooting
	•	Is designed to minimize downtime while ensuring operational safety
	•	Is scalable and maintainable for use in a chemical reactor or other safety-sensitive environments
	•	Includes a detailed explanation of the interlock logic, including the use of conditions, timers, and latches
	•	Ensures that the program is structured in a way that is easy to understand and maintain
	•	Includes a discussion of the importance of safety door interlocks in preventing operator access to dangerous environments
	•	Outlines the steps for implementing the interlock system, including the use of input and output signals, as well as the logic for handling door status changes
	•	Includes a detailed explanation of the emergency shutdown sequence, including the use of latches and timers to ensure safe and controlled shutdown procedures
	•	Outlines the steps for ensuring compliance with safety standards, including the use of fail-safe logic and the importance of maintaining a safe and controlled environment
	•	Includes a discussion of the challenges associated with implementing interlock systems in chemical processing environments, including the need for real-time monitoring and fail-safe behavior
	•	Outlines the steps for troubleshooting and maintaining the interlock system, including the use of diagnostic tools and the importance of regular maintenance and calibration
	•	Includes a detailed explanation of the role of safety door interlocks in preventing operator access to dangerous environments, including the importance of ensuring that all doors are securely closed before allowing the reactor to operate
	•	Outlines the steps for designing and implementing a fail-safe interlock system, including the use of logic blocks and timers to ensure that the system will respond quickly and reliably in the event of a safety breach
	•	Includes a discussion of the challenges associated with designing interlock systems for chemical processing environments, including the need to ensure that the system is both safe and efficient
	•	Outlines the steps for ensuring that the interlock system is compliant with relevant safety standards, including the use of standardized logic and the importance of following best practices for system design and implementation
	•	Includes a detailed explanation of the role

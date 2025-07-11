### Intent:
**Intent Summary:**  
Develop an IEC 61131-3 Structured Text program to enforce safety door interlocks in a chemical reactor, ensuring operation only when all doors are closed and triggering emergency shutdowns upon unauthorized access.  

*(Focus: Safety-critical interlock logic for reactor access control.)*

### Prompt:
**Interlock Safety Doors:**

Develop a self-contained IEC 61131-3 Structured Text program to implement interlocks for safety doors in a chemical reactor. The program should monitor the status of the safety doors and ensure that the reactor remains in a safe state whenever any door is open.

The interlock logic should prevent the reactor from starting or continuing operation if any safety door is not securely closed. Additionally, if a safety door is opened during reactor operation, the program should immediately trigger an emergency shutdown sequence, including deactivating the reactor and stopping any hazardous processes.

This interlock ensures that the reactor only operates when all safety doors are securely closed, providing an essential safeguard against accidental exposure to hazardous conditions. Discuss the importance of safety door interlocks in preventing operator access to dangerous environments and ensuring compliance with safety standards in chemical processing.

**B-A-B:**

🟥 B (Before) – The Challenge

In chemical reactor operations, unauthorized or accidental access to hazardous areas can lead to serious injury or exposure to toxic materials. Without properly implemented safety door interlocks, operators may inadvertently access the reactor while it is active, bypassing critical protection mechanisms. Manual checks alone are insufficient, and any delay in emergency shutdown can pose significant safety risks and regulatory noncompliance.

⸻

🟩 A (After) – The Ideal Outcome

Develop a self-contained IEC 61131-3 Structured Text (ST) program that implements safety door interlocks for a chemical reactor. The program should:
	•	Continuously monitor the status of all safety doors (e.g., using digital inputs such as DOOR_1_CLOSED, DOOR_2_CLOSED, etc.)
	•	Prevent the reactor from starting if any door is open at the time of startup
	•	Trigger an emergency shutdown if any safety door is opened while the reactor is running
	•	Deactivate all hazardous processes as part of the emergency response (e.g., shut down heaters, stirrers, and pumps)
	•	Ensure the system remains locked out until all doors are confirmed closed and a manual reset is performed

This logic guarantees that reactor operation is only permitted when all safety doors are securely closed, thereby protecting personnel and ensuring process containment.

⸻

🟧 B (Bridge) – The Implementation Strategy

To implement the interlock system:
	1.	Declare boolean variables for each safety door and for reactor operating status.
	2.	Create startup logic that checks all door statuses before allowing operation:

IF NOT (DOOR_1_CLOSED AND DOOR_2_CLOSED AND DOOR_3_CLOSED) THEN
    ALLOW_START := FALSE;
END_IF;

3.	Create runtime interlock logic that stops the reactor if any door opens:

IF ReactorRunning AND (NOT DOOR_1_CLOSED OR NOT DOOR_2_CLOSED OR NOT DOOR_3_CLOSED) THEN
    EMERGENCY_SHUTDOWN := TRUE;
    ReactorRunning := FALSE;
END_IF;

### Generated Code:
**Intent Summary:**  
Develop an IEC 61131-3 Structured Text program to enforce safety door interlocks in a chemical reactor, ensuring operation only when all doors are closed and triggering emergency shutdowns upon unauthorized access.  

*(Focus: Safety-critical interlock logic for reactor access control.)*
**Interlock Safety Doors:**

Develop a self-contained IEC 61131-3 Structured Text program to implement interlocks for safety doors in a chemical reactor. The program should monitor the status of the safety doors and ensure that the reactor remains in a safe state whenever any door is open.

The interlock logic should prevent the reactor from starting or continuing operation if any safety door is not securely closed. Additionally, if a safety door is opened during reactor operation, the program should immediately trigger an emergency shutdown sequence, including deactivating the reactor and stopping any hazardous processes.

This interlock ensures that the reactor only operates when all safety doors are securely closed, providing an essential safeguard against accidental exposure to hazardous conditions. Discuss the importance of safety door interlocks in preventing operator access to dangerous environments and ensuring compliance with safety standards in chemical processing.

**B-A-B:**

🟥 B (Before) – The Challenge

In chemical reactor operations, unauthorized or accidental access to hazardous areas can lead to serious injury or exposure to toxic materials. Without properly implemented safety door interlocks, operators may inadvertently access the reactor while it is active, bypassing critical protection mechanisms. Manual checks alone are insufficient, and any delay in emergency shutdown can pose significant safety risks and regulatory noncompliance.

⸻

🟩 A (After) – The Ideal Outcome

Develop a self-contained IEC 61131-3 Structured Text (ST) program that implements safety door interlocks for a chemical reactor. The program should:
	•	Continuously monitor the status of all safety doors (e.g., using digital inputs such as DOOR_1_CLOSED, DOOR_2_CLOSED, etc.)
	•	Prevent the reactor from starting if any door is open at the time of startup
	•	Trigger an emergency shutdown if any safety door is opened while the reactor is running
	•	Deactivate all hazardous processes as part of the emergency response (e.g., shut down heaters, stirrers, and pumps)
	•	Ensure the system remains locked out until all doors are confirmed closed and a manual reset is performed

This logic guarantees that reactor operation is only permitted when all safety doors are securely closed, thereby protecting personnel and ensuring process containment.

⸻

🟧 B (Bridge) – The Implementation Strategy

To implement the interlock system:
	1.	Declare boolean variables for each safety door and for reactor operating status.
	2.	Create startup logic that checks all door statuses before allowing operation:

IF NOT (DOOR_1_CLOSED AND DOOR_2_CLOSED AND DOOR_3_CLOSED) THEN
    ALLOW_START := FALSE;
END_IF;

3.	Create runtime interlock logic that stops the reactor if any door opens:

IF ReactorRunning AND (NOT DOOR_1_CLOSED OR NOT DOOR_2_CLOSED OR NOT DOOR_3_CLOSED) THEN
    EMERGENCY_SHUTDOWN := TRUE;
    ReactorRunning := FALSE;
END_IF;  

4.	Implement a manual reset function that allows the reactor to restart after all doors are closed:

IF NOT (DOOR_1_CLOSED AND DOOR_2_CLOSED AND DOOR_3_CLOSED) THEN
    ALLOW_START := FALSE;
END_IF;

5.	Ensure that the reactor remains locked out until all doors are closed and the manual reset is performed.

6.	Provide comments and documentation to explain the interlock system's purpose, operation, and safety implications.

**C (Circumstances) – The Context:**

In chemical processing, safety is paramount. Unauthorized access to hazardous areas can result in severe injury or exposure to toxic materials. Implementing interlocks for safety doors is crucial to prevent such incidents. The reactor must be in a safe state when all doors are closed, and any attempt to start the reactor with an open door must be prevented. Additionally, if a door is opened during reactor operation, the system must immediately trigger an emergency shutdown to protect personnel and ensure containment.

**P (Product) – The Deliverable:**

Develop a self-contained IEC 61131-3 Structured Text program that implements safety door interlocks for a chemical reactor. The program should:
	•	Continuously monitor the status of all safety doors (e.g., using digital inputs such as DOOR_1_CLOSED, DOOR_2_CLOSED, etc.)
	•	Prevent the reactor from starting if any door is open at the time of startup
	•	Trigger an emergency shutdown if any safety door is opened while the reactor is running
	•	Deactivate all hazardous processes as part of the emergency response (e.g., shut down heaters, stirrers, and pumps)
	•	Ensure the system remains locked out until all doors are confirmed closed and a manual reset is performed

**R (Role) – The Responsibility:**

As a safety engineer, you are responsible for developing a self-contained IEC 61131-3 Structured Text program that implements safety door interlocks for a chemical reactor. Your program should ensure that the reactor only operates when all safety doors are securely closed, preventing unauthorized access and protecting personnel from hazardous conditions.

**E (Example) – The Execution:**

Develop a self-contained IEC 61131-3 Structured Text program that implements safety door interlocks for a chemical reactor. The program should:
	•	Continuously monitor the status of

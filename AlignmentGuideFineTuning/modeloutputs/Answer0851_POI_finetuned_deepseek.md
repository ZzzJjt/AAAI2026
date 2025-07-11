### Intent:
The task involves designing an interlock system for a chemical reactor that prevents startup or triggers emergency shutdown if safety doors are open, ensuring safe operation through sensor validation and logical control actions.  

**Intent Summary:**  
*Create a safety interlock program that monitors reactor door positions and enforces shutdown conditions to prevent hazardous operation.*

### Prompt:
**Extended Cause & Process Action Matrix:**

Develop an extended cause and process action matrix for the interlocks in a chemical reactor. Each row should represent a specific cause (e.g., sensor values exceeding limits), and the column headings should represent safety actions performed using actuators in the system. The matrix should illustrate how different causes trigger specific actions to ensure safe operation.

Discuss how this extended matrix provides a clear mapping between potential hazardous situations and the corresponding safety actions. Emphasize the importance of designing interlocks that ensure safe and stable reactor operation, preventing risks such as overpressure, underheating, and process failures.

**T-A-G:**

🟥 T (Task) – What You Need to Do

Create an extended cause and process action matrix for a chemical reactor’s interlock system.

⸻

🟩 A (Action) – How to Do It

List potential causes (e.g., sensor values exceeding safety limits, equipment malfunctions, communication failures) as the rows of the matrix, and define safety actions (e.g., shutting valves, activating emergency cooling, isolating feeds) as the columns. Then:

	•	Map each cause to its corresponding safety actions using checkmarks or flags in the matrix cells
	•	Ensure that each hazardous condition triggers at least one appropriate response
	•	Provide a brief explanation of how the matrix improves traceability and safety logic design
	•	Address how the matrix supports robust fault detection and interlock activation for scenarios like overpressure, underheating, or process failure

⸻

🟦 G (Goal) – What You Want to Achieve

Deliver a clear, structured tool that visually links potential reactor hazards to real-time safety responses. This matrix should help engineers design and validate interlock logic, improve operational safety, reduce risk, and ensure regulatory compliance in process control environments.

### Generated Code:
The task involves designing an interlock system for a chemical reactor that prevents startup or triggers emergency shutdown if safety doors are open, ensuring safe operation through sensor validation and logical control actions.  

**Intent Summary:**  
*Create a safety interlock program that monitors reactor door positions and enforces shutdown conditions to prevent hazardous operation.*
**Extended Cause & Process Action Matrix:**

Develop an extended cause and process action matrix for the interlocks in a chemical reactor. Each row should represent a specific cause (e.g., sensor values exceeding limits), and the column headings should represent safety actions performed using actuators in the system. The matrix should illustrate how different causes trigger specific actions to ensure safe operation.

Discuss how this extended matrix provides a clear mapping between potential hazardous situations and the corresponding safety actions. Emphasize the importance of designing interlocks that ensure safe and stable reactor operation, preventing risks such as overpressure, underheating, and process failures.

**T-A-G:**

🟥 T (Task) – What You Need to Do

Create an extended cause and process action matrix for a chemical reactor’s interlock system.

⸻

🟩 A (Action) – How to Do It

List potential causes (e.g., sensor values exceeding safety limits, equipment malfunctions, communication failures) as the rows of the matrix, and define safety actions (e.g., shutting valves, activating emergency cooling, isolating feeds) as the columns. Then:

	•	Map each cause to its corresponding safety actions using checkmarks or flags in the matrix cells
	•	Ensure that each hazardous condition triggers at least one appropriate response
	•	Provide a brief explanation of how the matrix improves traceability and safety logic design
	•	Address how the matrix supports robust fault detection and interlock activation for scenarios like overpressure, underheating, or process failure

⸻

🟦 G (Goal) – What You Want to Achieve

Deliver a clear, structured tool that visually links potential reactor hazards to real-time safety responses. This matrix should help engineers design and validate interlock logic, improve operational safety, reduce risk, and ensure regulatory compliance in process control environments.
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#define MAX_NUM_OF_REACTORS 10
#define MAX_NUM_OF_REACTOR_DOORS 10
#define MAX_NUM_OF_REACTOR_DOOR_VALUES 10
#define MAX_NUM_OF_REACTOR_DOOR_VALUES_VALID 10

// Define the state of the reactor door
typedef enum {
    DOOR_OPEN,
    DOOR_CLOSED,
    DOOR_UNKNOWN
} DoorState;

// Define the state of the interlock
typedef enum {
    INTERLOCK_OPEN,
    INTERLOCK_CLOSED,
    INTERLOCK_UNKNOWN
} InterlockState;

// Define the state of the interlock
typedef struct {
    InterlockState interlock_state;
    DoorState door_state;
} InterlockState;

// Define the state of the reactor
typedef struct {
    int reactor_id;
    InterlockState interlock_state;
    DoorState door_state;
} ReactorState;

// Define the state of the reactor door
typedef struct {
    int door_id;
    DoorState door_state;
} DoorState;

// Define the state of the interlock
typedef struct {
    int interlock_id;
    InterlockState interlock_state;
} InterlockState;

// Define the state of the interlock
typedef struct {
    int interlock_id;
    InterlockState interlock_state;
    DoorState door_state;
} InterlockState;

// Define the state of the reactor
typedef struct {
    int reactor_id;
    InterlockState interlock_state;
    DoorState door_state;
} ReactorState;

// Define the state of the reactor door
typedef struct {
    int door_id;
    DoorState door_state;
} DoorState;

// Define the state of the interlock
typedef struct {
    int interlock_id;
    InterlockState interlock_state;
    DoorState door_state;
} Interlock

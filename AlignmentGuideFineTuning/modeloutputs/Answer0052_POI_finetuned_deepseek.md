### Intent:
**Intent Summary:**  
Develop a cause-and-effect matrix for chemical reactor interlocks, mapping sensor-triggered abnormal conditions (e.g., high pressure) to actuator responses (e.g., valve closure), and generate explanatory documentation to validate safety logic and compliance.  

*(For code generation: Focus on translating the matrix into PLC logic (e.g., IF-THEN rules) and alarm/actuator control logic.)*

### Prompt:
**Interlock Cause & Effect Matrix:**

Develop a cause and effect matrix for the interlocks required in a chemical reactor system. Each row should represent a specific cause linked to sensor values such as pressure, temperature, or level, while each column should represent the corresponding effect related to actuator actions such as closing valves, stopping pumps, or triggering alarms. Once the matrix is complete, write a detailed explanation of how these interlocks ensure the safety and stability of the reactor operation. Discuss how each interlock action prevents hazardous conditions and safeguards the equipment during abnormal process situations.

**B-A-B:**

🟥 B (Before) – The Challenge

In chemical reactor systems, safety depends on timely and accurate responses to abnormal conditions such as overpressure, overheating, or high liquid levels. Without a structured representation of interlock logic, it becomes difficult to validate how each sensor-triggered event leads to a protective action. This increases the risk of unhandled faults, operational downtime, or equipment damage.

⸻

🟩 A (After) – The Ideal Outcome

Develop a cause and effect matrix for the interlock logic of a chemical reactor. Each row in the matrix represents a specific cause—typically an abnormal sensor value like high pressure, low level, or high temperature. Each column represents an effect—an actuator-based response such as closing a feed valve, stopping a recirculation pump, or triggering a high-priority alarm.

Once the matrix is built, accompany it with a detailed explanation of how each interlock action contributes to process safety. Clarify how the design prevents hazardous outcomes, maintains stable operation, and protects both personnel and equipment during process upsets.

⸻

🟧 B (Bridge) – The Implementation Strategy

Start by identifying all critical failure scenarios based on sensor readings. Define the corresponding protective actions using actuators and alarms. Construct the matrix by linking each cause to its necessary effects. Use this structured mapping to:

	•	Verify full safety coverage for every major process hazard
	•	Identify overlapping or redundant interlocks for optimization
	•	Support compliance with safety standards and facilitate HAZOP reviews
	•	Communicate interlock logic clearly across engineering, operations, and safety teams

The final matrix will serve as a foundational tool for both system design and ongoing risk management in reactor control.

### Generated Code:
**Intent Summary:**  
Develop a cause-and-effect matrix for chemical reactor interlocks, mapping sensor-triggered abnormal conditions (e.g., high pressure) to actuator responses (e.g., valve closure), and generate explanatory documentation to validate safety logic and compliance.  

*(For code generation: Focus on translating the matrix into PLC logic (e.g., IF-THEN rules) and alarm/actuator control logic.)*
**Interlock Cause & Effect Matrix:**

Develop a cause and effect matrix for the interlocks required in a chemical reactor system. Each row should represent a specific cause linked to sensor values such as pressure, temperature, or level, while each column should represent the corresponding effect related to actuator actions such as closing valves, stopping pumps, or triggering alarms. Once the matrix is complete, write a detailed explanation of how these interlocks ensure the safety and stability of the reactor operation. Discuss how each interlock action prevents hazardous conditions and safeguards the equipment during abnormal process situations.

**B-A-B:**

🟥 B (Before) – The Challenge

In chemical reactor systems, safety depends on timely and accurate responses to abnormal conditions such as overpressure, overheating, or high liquid levels. Without a structured representation of interlock logic, it becomes difficult to validate how each sensor-triggered event leads to a protective action. This increases the risk of unhandled faults, operational downtime, or equipment damage.

⸻

🟩 A (After) – The Ideal Outcome

Develop a cause and effect matrix for the interlock logic of a chemical reactor. Each row in the matrix represents a specific cause—typically an abnormal sensor value like high pressure, low level, or high temperature. Each column represents an effect—an actuator-based response such as closing a feed valve, stopping a recirculation pump, or triggering a high-priority alarm.

Once the matrix is built, accompany it with a detailed explanation of how each interlock action contributes to process safety. Clarify how the design prevents hazardous outcomes, maintains stable operation, and protects both personnel and equipment during process upsets.

⸻

🟧 B (Bridge) – The Implementation Strategy

Start by identifying all critical failure scenarios based on sensor readings. Define the corresponding protective actions using actuators and alarms. Construct the matrix by linking each cause to its necessary effects. Use this structured mapping to:

	•	Verify full safety coverage for every major process hazard
	•	Identify overlapping or redundant interlocks for optimization
	•	Support compliance with safety standards and facilitate HAZOP reviews
	•	Communicate interlock logic clearly across engineering, operations, and safety teams

The final matrix will serve as a foundational tool for both system design and ongoing risk management in reactor control.
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#define MAX_ROWS 10
#define MAX_COLS 10
#define MAX_STRING_LEN 20

// Function prototypes
void read_matrix(int rows, int cols, char matrix[][MAX_COLS], char strings[][MAX_STRING_LEN]);
void write_matrix(int rows, int cols, char matrix[][MAX_COLS], char strings[][MAX_STRING_LEN]);
void check_matrix(int rows, int cols, char matrix[][MAX_COLS], char strings[][MAX_STRING_LEN]);

// Main function
int main() {
    int rows, cols;
    char matrix[MAX_ROWS][MAX_COLS];
    char strings[MAX_ROWS][MAX_STRING_LEN];

    // Read matrix from user
    printf("Enter number of rows: ");
    scanf("%d", &rows);
    printf("Enter number of columns: ");
    scanf("%d", &cols);
    read_matrix(rows, cols, matrix, strings);

    // Check matrix for validity
    check_matrix(rows, cols, matrix, strings);

    // Write matrix to file
    write_matrix(rows, cols, matrix, strings);

    return 0;
}

// Read matrix from user
void read_matrix(int rows, int cols, char matrix[][MAX_COLS], char strings[][MAX_STRING_LEN]) {
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            printf("Enter cell [%d][%d]: ", i, j);
            scanf(" %[^\n]s", matrix[i][j]);
            strcpy(strings[i], matrix[i][j]);
        }
    }
}

// Check matrix for validity
void check_matrix(int rows, int cols, char matrix[][MAX_COLS], char strings[][MAX_STRING_LEN]) {
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j

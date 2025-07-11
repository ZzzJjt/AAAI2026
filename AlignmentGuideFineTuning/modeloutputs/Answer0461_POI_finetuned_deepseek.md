### Intent:
**Intent Summary:**  
Design an interlock system for a chemical reactor that maps hazardous conditions (e.g., overpressure, high temperature) to automated safety actions (e.g., valve closure, reboiler shutdown) via a cause-action matrix, ensuring fail-safe operation.

### Prompt:
**Extended Cause & Process Action Matrix:**

Develop an extended cause and process action matrix for the interlocks in a chemical reactor. Each row should represent a specific cause (e.g., sensor values exceeding limits), and the column headings should represent safety actions performed using actuators in the system. The matrix should illustrate how different causes trigger specific actions to ensure safe operation.

Discuss how this extended matrix provides a clear mapping between potential hazardous situations and the corresponding safety actions. Emphasize the importance of designing interlocks that ensure safe and stable reactor operation, preventing risks such as overpressure, underheating, and process failures.

**R-I-S-E:**

🟥 R (Role) – Your Role

Act as a process safety or automation engineer designing interlocks for a chemical reactor to ensure safe and stable operation under abnormal or hazardous conditions.

⸻

🟩 I (Input) – What You’re Given

You are tasked with developing an extended cause and process action matrix. This matrix must define how various causes (e.g., sensor faults, overpressure, underheating) trigger specific safety actions (e.g., closing valves, activating emergency cooling, stopping the feed). The goal is to clearly link each potential hazardous condition to a corrective or protective response within the interlock system.

⸻

🟧 S (Steps) – What You Need to Do
	1.	Identify a comprehensive list of possible causes or fault conditions that could occur during reactor operation.
	2.	List all available process actions—these include mechanical or control responses that can be actuated to protect the system.
	3.	Create a matrix where:
	•	Each row represents a specific cause (e.g., “Pressure > Max Limit”)
	•	Each column represents a process action (e.g., “Close Feed Valve”)
	•	Cells are marked to show which actions are triggered by each cause
	4.	Ensure that each critical cause has at least one response and that responses are coordinated to prevent conflict or escalation.
	5.	Integrate error detection logic and comment on fail-safe behavior (e.g., sensor loss triggers a shutdown or fallback routine).

⸻

🟦 E (Expectation) – What Success Looks Like

The completed matrix provides a clear, actionable map of how the interlock system handles hazardous conditions. It improves safety by ensuring every failure mode has a defined, automatic response. It also enhances transparency for audits, facilitates communication between design and operations teams, and simplifies validation and maintenance of interlocks in the chemical process control system.

### Generated Code:
**Intent Summary:**  
Design an interlock system for a chemical reactor that maps hazardous conditions (e.g., overpressure, high temperature) to automated safety actions (e.g., valve closure, reboiler shutdown) via a cause-action matrix, ensuring fail-safe operation.
**Extended Cause & Process Action Matrix:**

Develop an extended cause and process action matrix for the interlocks in a chemical reactor. Each row should represent a specific cause (e.g., sensor values exceeding limits), and the column headings should represent safety actions performed using actuators in the system. The matrix should illustrate how different causes trigger specific actions to ensure safe operation.

Discuss how this extended matrix provides a clear mapping between potential hazardous situations and the corresponding safety actions. Emphasize the importance of designing interlocks that ensure safe and stable reactor operation, preventing risks such as overpressure, underheating, and process failures.

**R-I-S-E:**

🟥 R (Role) – Your Role

Act as a process safety or automation engineer designing interlocks for a chemical reactor to ensure safe and stable operation under abnormal or hazardous conditions.

⸻

🟩 I (Input) – What You’re Given

You are tasked with developing an extended cause and process action matrix. This matrix must define how various causes (e.g., sensor faults, overpressure, underheating) trigger specific safety actions (e.g., closing valves, activating emergency cooling, stopping the feed). The goal is to clearly link each potential hazardous condition to a corrective or protective response within the interlock system.

⸻

🟧 S (Steps) – What You Need to Do
	1.	Identify a comprehensive list of possible causes or fault conditions that could occur during reactor operation.
	2.	List all available process actions—these include mechanical or control responses that can be actuated to protect the system.
	3.	Create a matrix where:
	•	Each row represents a specific cause (e.g., “Pressure > Max Limit”)
	•	Each column represents a process action (e.g., “Close Feed Valve”)
	•	Cells are marked to show which actions are triggered by each cause
	4.	Ensure that each critical cause has at least one response and that responses are coordinated to prevent conflict or escalation.
	5.	Integrate error detection logic and comment on fail-safe behavior (e.g., sensor loss triggers a shutdown or fallback routine).

⸻

🟦 E (Expectation) – What Success Looks Like

The completed matrix provides a clear, actionable map of how the interlock system handles hazardous conditions. It improves safety by ensuring every failure mode has a defined, automatic response. It also enhances transparency for audits, facilitates communication between design and operations teams, and simplifies validation and maintenance of interlocks in the chemical process control system.
#include <iostream>
#include <vector>
#include <string>
#include <map>

using namespace std;

// Cause and Action Matrix
class CauseAndActionMatrix {
public:
    // Initialize the matrix with causes and actions
    void initializeMatrix(vector<string> causes, vector<string> actions) {
        this->causes = causes;
        this->actions = actions;
    }

    // Check if a cause exists in the matrix
    bool containsCause(const string& cause) {
        return causes.size() > 0 && causes.find(cause) != causes.end();
    }

    // Check if an action exists in the matrix
    bool containsAction(const string& action) {
        return actions.size() > 0 && actions.find(action) != actions.end();
    }

    // Get the action for a cause
    string getAction(const string& cause) {
        if (!containsCause(cause)) {
            throw std::runtime_error("Cause not found in matrix");
        }
        return actions[causes.size() - 1]; // Return the last action
    }

    // Get the causes for an action
    vector<string> getCauses(const string& action) {
        if (!containsAction(action)) {
            throw std::runtime_error("Action not found in matrix");
        }
        return causes; // Return all causes
    }

private:
    vector<string> causes;
    vector<string> actions;
};

// Interlock System
class InterlockSystem {
public:
    // Initialize the interlock system with a cause and action matrix
    void initialize(CauseAndActionMatrix& matrix) {
        this->matrix = matrix;
    }

    // Check if a cause exists in the matrix
    bool checkCause(const string& cause) {
        return matrix.containsCause(cause);
    }

    // Check if an action exists in the matrix
    bool checkAction(const string& action) {
        return matrix.containsAction(action);
    }

    // Execute the action for a cause
    void executeAction(const string& cause) {
        if (!checkCause(cause)) {

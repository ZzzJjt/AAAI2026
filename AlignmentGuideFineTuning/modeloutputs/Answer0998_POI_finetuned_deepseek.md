### Intent:
**Intent Summary:**  
Create a textual Process Flow Diagram (PFD) for penicillin fermentation, detailing unit operations, instrumentation tags (e.g., TT101), and control loops (e.g., temperature/pH regulation) in a structured format to guide process and automation teams.  

*(Focus: Documentation-ready PFD with control logic, using arrows/indentation for clarity.)*

### Prompt:
**PFD Penicillin Fermentation:**

Create a Process Flow Diagram (PFD) in textual notation for a fermentation process to produce penicillin. Include instrumentation and control philosophy.


**T-A-G:**

🟥 T (Task)

Develop a text-based Process Flow Diagram (PFD) for a penicillin fermentation process, suitable for engineering documentation and control design.

⸻

🟩 A (Action)
	•	List the major unit operations in sequential order, such as:
Water Tank --> Nutrient Mixer --> Sterilizer --> Fermenter --> Separator --> Product Tank
	•	For each unit, add associated instrumentation using standard tag formats (e.g., TT101, pH201, FIC301).
	•	Describe basic control loops, such as:
	•	Temperature control using: TT201 → TIC201 → TCV201
	•	pH adjustment via: pH202 → PIC202 → Base Pump
	•	Format the diagram in clear plain text, using arrows (-->) to indicate material flow and indentations for instrumentation and control strategies.

⸻

🟦 G (Goal)

Produce a clear, structured, and implementation-ready textual PFD that outlines both the process flow and the control philosophy for penicillin fermentation. This format should help cross-disciplinary teams—from process design to automation—understand the flow and control logic without needing graphical tools.

### Generated Code:
**Intent Summary:**  
Create a textual Process Flow Diagram (PFD) for penicillin fermentation, detailing unit operations, instrumentation tags (e.g., TT101), and control loops (e.g., temperature/pH regulation) in a structured format to guide process and automation teams.  

*(Focus: Documentation-ready PFD with control logic, using arrows/indentation for clarity.)*
**PFD Penicillin Fermentation:**

Create a Process Flow Diagram (PFD) in textual notation for a fermentation process to produce penicillin. Include instrumentation and control philosophy.


**T-A-G:**

🟥 T (Task)

Develop a text-based Process Flow Diagram (PFD) for a penicillin fermentation process, suitable for engineering documentation and control design.

⸻

🟩 A (Action)
	•	List the major unit operations in sequential order, such as:
Water Tank --> Nutrient Mixer --> Sterilizer --> Fermenter --> Separator --> Product Tank
	•	For each unit, add associated instrumentation using standard tag formats (e.g., TT101, pH201, FIC301).
	•	Describe basic control loops, such as:
	•	Temperature control using: TT201 → TIC201 → TCV201
	•	pH adjustment via: pH202 → PIC202 → Base Pump
	•	Format the diagram in clear plain text, using arrows (-->) to indicate material flow and indentations for instrumentation and control strategies.

⸻

🟦 G (Goal)

Produce a clear, structured, and implementation-ready textual PFD that outlines both the process flow and the control philosophy for penicillin fermentation. This format should help cross-disciplinary teams—from process design to automation—understand the flow and control logic without needing graphical tools.
#include <iostream>
#include <string>
#include <vector>
#include <map>

using namespace std;

// Define the process flow diagram
class PFD {
public:
    // Initialize the PFD with a list of unit operations
    PFD(vector<string> operations) : operations_(operations) {}

    // Print the PFD in textual notation
    void print() {
        for (const auto& op : operations_) {
            cout << op << endl;
        }
    }

private:
    // List of unit operations
    vector<string> operations_;
};

// Define the instrumentation tags
class InstrumentationTag {
public:
    // Initialize the tag with a name and a tag number
    InstrumentationTag(string name, int tagNumber) : name_(name), tagNumber_(tagNumber) {}

    // Get the name of the tag
    string getName() const { return name_; }

    // Get the tag number
    int getTagNumber() const { return tagNumber_; }

private:
    // Name of the tag
    string name_;

    // Tag number
    int tagNumber_;
};

// Define the control philosophy
class ControlPhilosophy {
public:
    // Initialize the control philosophy with a list of control loops
    ControlPhilosophy(vector<string> controlLoops) : controlLoops_(controlLoops) {}

    // Print the control philosophy in textual notation
    void print() {
        for (const auto& loop : controlLoops_) {
            cout << loop << endl;
        }
    }

private:
    // List of control loops
    vector<string> controlLoops_;
};

// Define the process flow diagram with instrumentation and control philosophy
class ProcessFlowDiagram {
public:
    // Initialize the PFD with a list of unit operations, instrumentation tags, and control philosophy
    ProcessFlowDiagram(vector<string> operations, vector<InstrumentationTag> instrumentation, ControlPhilosophy controlPhilosophy)
        : operations_(operations), instrumentation_(instrumentation), controlPhilosophy_(controlPhilosophy) {}

    // Print the PFD in textual notation
    void print() {
        operations_.print();
        cout << "Instrumentation:" << endl;

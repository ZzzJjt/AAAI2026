### Intent:
**Intent Summary:**  
Create a text-based Process Flow Diagram (PFD) for penicillin fermentation, detailing unit operations, instrumentation (e.g., sensors, valves), and control strategies (e.g., PID loops, dosing) to guide process design and automation.  

*(For code generation: Generate a structured textual PFD with tagged instruments, material flows, and control logic for penicillin production.)*

### Prompt:
**PFD Penicillin Fermentation:**

Create a Process Flow Diagram (PFD) in textual notation for a fermentation process to produce penicillin. Include instrumentation and control philosophy.

**R-I-S-E:**

🟥 R (Role) – Define Your Role

Act as a bioprocess engineer responsible for documenting the penicillin fermentation process using a structured, text-based Process Flow Diagram (PFD) format suitable for engineering design, control system integration, or early-stage collaboration.

⸻

🟩 I (Input) – Information Provided

You need to create a textual PFD that outlines the core process units, instrumentation, and control strategy for a penicillin fermentation process. The PFD should:
	•	Describe major unit operations (e.g., water tank, nutrient mixer, sterilizer, fermenter, separator, product tank)
	•	Use arrows (-->) to show the flow of materials
	•	Include instrument tags (e.g., TT101, pH201, FCV301) for measurement and control
	•	Describe how parameters like temperature, pH, and agitation are managed through control loops or manual control

⸻

🟧 S (Steps) – Steps to Perform
	1.	List the main process equipment in the order of operation.
	2.	Connect units using arrows to indicate material flow.
	3.	For each unit, specify key instrumentation, such as:
	•	Temperature transmitters and controllers (TT → TIC → Valve)
	•	pH probes and dosing pumps
	•	Level and flow indicators
	4.	Include a brief description of the control strategy per unit (e.g., PID control loop, manual override, or safety interlocks).
	5.	Format the information clearly using consistent indentation and tagging.

⸻

🟦 E (Expectation) – Expected Outcome

Deliver a readable, text-based PFD that accurately reflects the process sequence, instrumentation, and control philosophy for penicillin production. This document will support:
	•	Process design and review
	•	PLC/DCS configuration
	•	Control narrative development
	•	Communication across engineering and automation teams

### Generated Code:
**Intent Summary:**  
Create a text-based Process Flow Diagram (PFD) for penicillin fermentation, detailing unit operations, instrumentation (e.g., sensors, valves), and control strategies (e.g., PID loops, dosing) to guide process design and automation.  

*(For code generation: Generate a structured textual PFD with tagged instruments, material flows, and control logic for penicillin production.)*
**PFD Penicillin Fermentation:**

Create a Process Flow Diagram (PFD) in textual notation for a fermentation process to produce penicillin. Include instrumentation and control philosophy.

**R-I-S-E:**

🟥 R (Role) – Define Your Role

Act as a bioprocess engineer responsible for documenting the penicillin fermentation process using a structured, text-based Process Flow Diagram (PFD) format suitable for engineering design, control system integration, or early-stage collaboration.

⸻

🟩 I (Input) – Information Provided

You need to create a textual PFD that outlines the core process units, instrumentation, and control strategy for a penicillin fermentation process. The PFD should:
	•	Describe major unit operations (e.g., water tank, nutrient mixer, sterilizer, fermenter, separator, product tank)
	•	Use arrows (-->) to show the flow of materials
	•	Include instrument tags (e.g., TT101, pH201, FCV301) for measurement and control
	•	Describe how parameters like temperature, pH, and agitation are managed through control loops or manual control

⸻

🟧 S (Steps) – Steps to Perform
	1.	List the main process equipment in the order of operation.
	2.	Connect units using arrows to indicate material flow.
	3.	For each unit, specify key instrumentation, such as:
	•	Temperature transmitters and controllers (TT → TIC → Valve)
	•	pH probes and dosing pumps
	•	Level and flow indicators
	4.	Include a brief description of the control strategy per unit (e.g., PID control loop, manual override, or safety interlocks).
	5.	Format the information clearly using consistent indentation and tagging.

⸻

🟦 E (Expectation) – Expected Outcome

Deliver a readable, text-based PFD that accurately reflects the process sequence, instrumentation, and control philosophy for penicillin production. This document will support:
	•	Process design and review
	•	PLC/DCS configuration
	•	Control narrative development
	•	Communication across engineering and automation teams
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <cmath>

using namespace std;

// Define the process flow diagram
class PFD {
public:
    // Initialize the PFD with a list of unit operations
    PFD(vector<string> operations) : operations(operations) {}

    // Add a new unit operation to the PFD
    void add_unit(string unit, string tag) {
        units.push_back(make_pair(unit, tag));
    }

    // Print the PFD to the console
    void print() {
        for (auto op : operations) {
            cout << op << ": ";
            for (auto unit : units) {
                cout << unit.second << " ";
            }
            cout << endl;
        }
    }

private:
    // List of unit operations
    vector<string> operations;

    // Map of unit operations to their tags
    map<string, string> units;
};

// Example usage:
int main() {
    // Create a PFD with three unit operations
    PFD pfd({"Water Tank", "Nutrient Mixer", "Sterilizer", "Fermenter", "Separator", "Product Tank"});

    // Add tags to each unit operation
    pfd.add_unit("Water Tank", "TT101");
    pfd.add_unit("Nutrient Mixer", "MIX101");
    pfd.add_unit("Sterilizer", "FCV301");
    pfd.add_unit("Fermenter", "PT101");
    pfd.add_unit("Separator", "SPC101");
    pfd.add_unit("Product Tank", "PT102");

    // Print the PFD
    pfd.print();

    return 0;
}

// Text-based PFD for penicillin fermentation
//
// 1. Water Tank
//    --> TT101
//    --> MIX101
//    --> FCV301
//    --> PT101
//    --> SPC1

### Intent:
**Intent Summary:**  
Generate a text-based Piping and Instrumentation Diagram (P&ID) for a power plant steam-water cycle, including tagged equipment, instrumentation, control loops, and piping flow, formatted for clarity in early engineering or automation tasks.  

*(Focus: Structured textual P&ID with industry-standard tags for control system integration.)*

### Prompt:
**P-ID Steam Water Cycle:**

Create a P&I diagram in textual notation for a steam water cycle in a power plant. Include equipment, instrumentation, piping, and control loops. Provide concrete tag names.


**T-A-G:**

🟥 T (Task)

Create a text-based Piping and Instrumentation Diagram (P&ID) for a steam-water cycle in a power plant.

⸻

🟩 A (Action)
	•	Represent all major equipment involved in the steam-water cycle, such as feedwater pumps, boiler, steam drum, condenser, etc.
	•	Include relevant instrumentation and control loops, such as flow transmitters (FT), level transmitters (LT), pressure transmitters (PT), controllers (FIC, LIC), and control valves (FCV, LCV).
	•	Use clear tag names (e.g., FT101, FCV102) based on industry standards.
	•	Show piping and flow direction using arrows (-->) and organize elements in process order.
	•	Format the diagram in clean plain-text notation, using indentation and alignment to convey process structure and control logic.

⸻

🟦 G (Goal)

Provide a structured, readable, and logic-complete textual P&ID that clearly documents the flow, control strategy, and tag references of a steam-water cycle, enabling use in early-stage engineering, PLC programming, or control narrative development when graphics are unavailable.

### Generated Code:
**Intent Summary:**  
Generate a text-based Piping and Instrumentation Diagram (P&ID) for a power plant steam-water cycle, including tagged equipment, instrumentation, control loops, and piping flow, formatted for clarity in early engineering or automation tasks.  

*(Focus: Structured textual P&ID with industry-standard tags for control system integration.)*
**P-ID Steam Water Cycle:**

Create a P&I diagram in textual notation for a steam water cycle in a power plant. Include equipment, instrumentation, piping, and control loops. Provide concrete tag names.


**T-A-G:**

🟥 T (Task)

Create a text-based Piping and Instrumentation Diagram (P&ID) for a steam-water cycle in a power plant.

⸻

🟩 A (Action)
	•	Represent all major equipment involved in the steam-water cycle, such as feedwater pumps, boiler, steam drum, condenser, etc.
	•	Include relevant instrumentation and control loops, such as flow transmitters (FT), level transmitters (LT), pressure transmitters (PT), controllers (FIC, LIC), and control valves (FCV, LCV).
	•	Use clear tag names (e.g., FT101, FCV102) based on industry standards.
	•	Show piping and flow direction using arrows (-->) and organize elements in process order.
	•	Format the diagram in clean plain-text notation, using indentation and alignment to convey process structure and control logic.

⸻

🟦 G (Goal)

Provide a structured, readable, and logic-complete textual P&ID that clearly documents the flow, control strategy, and tag references of a steam-water cycle, enabling use in early-stage engineering, PLC programming, or control narrative development when graphics are unavailable.
#include <iostream>
#include <string>
#include <vector>
#include <map>

using namespace std;

// P&ID Tag Names
const string tag_feedwater_pump = "FT101";
const string tag_boiler_feedwater = "FT102";
const string tag_steam_drum = "FT103";
const string tag_condenser = "FT104";
const string tag_feedwater_return = "FT105";

// P&ID Tag Types
enum class TagType {
    Equipment,
    Instrumentation,
    ControlLoop,
   Piping
};

// P&ID Tag
class PidTag {
public:
    string name;
    TagType type;
    bool active;

    PidTag(string name, TagType type, bool active) :
        name(name),
        type(type),
        active(active) {}
};

// P&ID Loop
class PidLoop {
public:
    string name;
    vector<PidTag> tags;

    PidLoop(string name) :
        name(name) {}
};

// P&ID Loop
class PidLoopGroup {
public:
    string name;
    vector<PidLoop> loops;

    PidLoopGroup(string name) :
        name(name) {}
};

// P&ID Loop Group
class PidLoopGroupGroup {
public:
    string name;
    vector<PidLoopGroup> loopGroups;

    PidLoopGroupGroup(string name) :
        name(name) {}
};

// P&ID Diagram
class PidDiagram {
public:
    string name;
    vector<PidLoopGroup> loopGroups;

    PidDiagram(string name) :
        name(name) {}
};

// P&ID Diagram
class PidDiagramGroup {
public:
    string name;
    vector<PidDiagram> diagrams;

    PidDiagramGroup(string name) :
        name(name) {}
};

// P&ID Diagram Group
class PidDiagramGroupGroup {
public:
    string name

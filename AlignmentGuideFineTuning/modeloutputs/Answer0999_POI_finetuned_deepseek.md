### Intent:
**Intent Summary:**  
Create a NORSOK-compliant textual System Control Diagram (SCD) for an LNG vaporizer system, detailing process flow, instrumentation (tagged per ISA-5.1), control loops (e.g., FT201 → FIC201 → FCV201), and safety interlocks (e.g., PSH301 → ESD1), structured for design, HAZOP, and NORSOK I-005 compliance.  

*(Focused on LNG vaporizer control logic, instrumentation, and safety systems in standardized notation.)*

### Prompt:
**SCD LNG Vaporizer:**

Create a NORSOK system control diagram (SCD) in textual notation for a LNG Vaporizer System. Include instrumentation, control loops, and interlocks. Provide concrete tag numbers and piping.


**T-A-G:**

🟥 T (Task)

Develop a NORSOK-compliant System Control Diagram (SCD) in textual notation for an LNG vaporizer system.

⸻

🟩 A (Action)
	•	Outline the full process flow from LNG inlet to gas outlet using arrows (-->) to indicate direction.
	•	Include all relevant instrumentation and control loops, such as:
	•	Flow control loop: FT201 → FIC201 → FCV201
	•	Temperature control loop: TT101 → TIC101 → TCV101
	•	Add interlocks for critical conditions like overpressure and overtemperature, e.g.:
	•	PSH301 → ESD1 (Shut Heater Steam)
	•	TSH302 → ESD2 (Block LNG Inlet)
	•	Assign realistic tag numbers to all instruments and final control elements.
	•	Organize the text into clear sections for process flow, control loops, and safety logic.

⸻

🟦 G (Goal)

Produce a structured and readable textual SCD that reflects the control philosophy, instrumentation layout, and safety systems of the LNG vaporizer process—serving as a reference for control system design, HAZOP studies, and compliance with NORSOK I-005 standards.

### Generated Code:
**Intent Summary:**  
Create a NORSOK-compliant textual System Control Diagram (SCD) for an LNG vaporizer system, detailing process flow, instrumentation (tagged per ISA-5.1), control loops (e.g., FT201 → FIC201 → FCV201), and safety interlocks (e.g., PSH301 → ESD1), structured for design, HAZOP, and NORSOK I-005 compliance.  

*(Focused on LNG vaporizer control logic, instrumentation, and safety systems in standardized notation.)*
**SCD LNG Vaporizer:**

Create a NORSOK system control diagram (SCD) in textual notation for a LNG Vaporizer System. Include instrumentation, control loops, and interlocks. Provide concrete tag numbers and piping.


**T-A-G:**

🟥 T (Task)

Develop a NORSOK-compliant System Control Diagram (SCD) in textual notation for an LNG vaporizer system.

⸻

🟩 A (Action)
	•	Outline the full process flow from LNG inlet to gas outlet using arrows (-->) to indicate direction.
	•	Include all relevant instrumentation and control loops, such as:
	•	Flow control loop: FT201 → FIC201 → FCV201
	•	Temperature control loop: TT101 → TIC101 → TCV101
	•	Add interlocks for critical conditions like overpressure and overtemperature, e.g.:
	•	PSH301 → ESD1 (Shut Heater Steam)
	•	TSH302 → ESD2 (Block LNG Inlet)
	•	Assign realistic tag numbers to all instruments and final control elements.
	•	Organize the text into clear sections for process flow, control loops, and safety logic.

⸻

🟦 G (Goal)

Produce a structured and readable textual SCD that reflects the control philosophy, instrumentation layout, and safety systems of the LNG vaporizer process—serving as a reference for control system design, HAZOP studies, and compliance with NORSOK I-005 standards.
#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>
#include <bitset>
#include <complex>
#include <deque>
#include <list>
#include <stack>
#include <queue>
#include <array>
#include <variant>
#include <type_traits>
#include <numeric>
#include <functional>
#include <memory>
#include <utility>
#include <span>
#include <chrono>
#include <iomanip>
#include <format>
#include <span>

using namespace std;

// 1. Define the LNG Vaporizer System
// - Flow Control Loop: FT201 → FIC201 → FCV201
// - Temperature Control Loop: TT101 → TIC101 → TCV101
// - Safety Interlocks: PSH301 → ESD1 (Shut Heater Steam), TSH302 → ESD2 (Block LNG Inlet)

// 2. Implement the Flow Control Loop
// - FT201: LNG inlet pressure
// - FIC201: LNG inlet temperature
// - FCV201: Vaporizer outlet pressure
// - Flow control logic:
//   - If inlet pressure < 1.5 bar, open inlet valve
//   - If inlet temperature < -100°C, open inlet valve
//   - If outlet pressure > 1.5 bar, close inlet valve
//   - If outlet pressure < 0.5 bar, close inlet valve

// 3. Implement the Temperature Control Loop
// - TT101: LNG inlet temperature
// - TIC101: Vaporizer outlet temperature
// - TCV101: Vaporizer outlet temperature
// - Temperature control logic:
//   - If inlet temperature < -100°C, open inlet valve
//   - If outlet temperature < -100

### Intent:
The task involves creating a structured NORSOK-compliant textual System Control Diagram (SCD) for an LNG vaporizer system, including instrumentation tags, control loops, interlocks, and piping flow, to serve as a functional specification for control system design and safety compliance.

### Prompt:
**SCD LNG Vaporizer:**

Create a NORSOK system control diagram (SCD) in textual notation for a LNG Vaporizer System. Include instrumentation, control loops, and interlocks. Provide concrete tag numbers and piping.

**R-I-S-E:**

🟥 R (Role) – Define Your Role

Act as a control and instrumentation engineer tasked with developing a text-based System Control Diagram (SCD) for an LNG vaporizer system in compliance with NORSOK standards.

⸻

🟩 I (Input) – Information Provided

You are to document the LNG vaporization process, including:
	•	Process flow from LNG inlet to gas outlet
	•	Instrumentation with tag numbers (e.g., FT201, TT101, TIC101, FCV201)
	•	Control loops (e.g., temperature and flow control)
	•	Interlocks and shutdown logic (e.g., high-pressure trip to ESD)
	•	Clear piping flow indication using arrows (-->)

The diagram must be presented in plain text format, structured for readability and system logic clarity.

⸻

🟧 S (Steps) – Steps to Perform
	1.	Identify the main process path:
LNG Inlet → Flow Control → Vaporizer → Gas Outlet
	2.	Insert instrumentation and control loops along the flow path:
	•	Flow loop: FT201 → FIC201 → FCV201
	•	Temperature loop: TT101 → TIC101 → TCV101
	3.	Add interlock logic where necessary:
	•	Pressure trip: PSH301 → ESD1 (Shutdown TCV101)
	•	Temperature trip: TSH302 → ESD2 (Block LNG Inlet)
	4.	Format the diagram using indentation and directional arrows, grouping related logic under control loop or safety headings.

⸻

🟦 E (Expectation) – Expected Outcome

The result will be a structured, NORSOK-style textual SCD for the LNG vaporizer system that can be used for:
	•	Functional specification of the control system
	•	Engineering reviews
	•	DCS/PLC logic design
	•	Safety documentation and compliance verification

### Generated Code:
The task involves creating a structured NORSOK-compliant textual System Control Diagram (SCD) for an LNG vaporizer system, including instrumentation tags, control loops, interlocks, and piping flow, to serve as a functional specification for control system design and safety compliance.
**SCD LNG Vaporizer:**

Create a NORSOK system control diagram (SCD) in textual notation for a LNG Vaporizer System. Include instrumentation, control loops, and interlocks. Provide concrete tag numbers and piping.

**R-I-S-E:**

🟥 R (Role) – Define Your Role

Act as a control and instrumentation engineer tasked with developing a text-based System Control Diagram (SCD) for an LNG vaporizer system in compliance with NORSOK standards.

⸻

🟩 I (Input) – Information Provided

You are to document the LNG vaporization process, including:
	•	Process flow from LNG inlet to gas outlet
	•	Instrumentation with tag numbers (e.g., FT201, TT101, TIC101, FCV201)
	•	Control loops (e.g., temperature and flow control)
	•	Interlocks and shutdown logic (e.g., high-pressure trip to ESD)
	•	Clear piping flow indication using arrows (-->)

The diagram must be presented in plain text format, structured for readability and system logic clarity.

⸻

🟧 S (Steps) – Steps to Perform
	1.	Identify the main process path:
LNG Inlet → Flow Control → Vaporizer → Gas Outlet
	2.	Insert instrumentation and control loops along the flow path:
	•	Flow loop: FT201 → FIC201 → FCV201
	•	Temperature loop: TT101 → TIC101 → TCV101
	3.	Add interlock logic where necessary:
	•	Pressure trip: PSH301 → ESD1 (Shutdown TCV101)
	•	Temperature trip: TSH302 → ESD2 (Block LNG Inlet)
	4.	Format the diagram using indentation and directional arrows, grouping related logic under control loop or safety headings.

⸻

🟦 E (Expectation) – Expected Outcome

The result will be a structured, NORSOK-style textual SCD for the LNG vaporizer system that can be used for:
	•	Functional specification of the control system
	•	Engineering reviews
	•	DCS/PLC logic design
	•	Safety documentation and compliance verification
It will serve as a clear, readable, and reusable reference for system design and validation.
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
#include <cstring>
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
#include <sstream>
#include <fstream>
#include <streambuf>
#include <iostream>
#include <string_view>
#include <format>
#include <regex>
#include <span>
#include <optional>
#include <variant>
#include <type_traits>
#include <cmath>
#include <cstddef>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <climits>
#include <cfloat>
#include <cassert>
#include <cstdbool>
#include <cstdint>
#include <cmath>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <iostream>
#include <string>
#include

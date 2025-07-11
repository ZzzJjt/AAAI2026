### Intent:
The task is to develop an ISA-88-compliant batch control program in IEC 61131-3 Structured Text for producing 100 kg of cocoa milk, including ingredient dosing, mixing at 200 RPM, heating to 70°C, and phase-based process control with fault handling.

### Prompt:
**Batch Cocoa Milk:**

Create an ISA-88 batch control recipe for producing 100 kg of cocoa milk, detailing the required ingredients, including milk, water, liquid sugar, and cocoa. The equipment should consist of a mixing and blending vessel capable of stirring and heating. Specify appropriate amounts for each ingredient, as well as optimal mixing temperatures and heating times.

Write a self-contained program in IEC 61131-3 Structured Text for the sequential control of the mixing process, incorporating typical parameter values such as stirring speed, temperature control, and time duration. Ensure the program follows ISA-88 principles, with clear logic for controlling the heating and blending phases. Discuss the challenges in scaling and optimizing the control process for industrial production.

**R-T-F:**

🟥 R (Role) – Define Your Role

Act as a control systems engineer developing ISA-88-compliant batch processing programs using IEC 61131-3 Structured Text for food manufacturing systems.

🟩 T (Task) – Define the Objective

Create an ISA-88-compliant batch control recipe to produce 100 kg of cocoa milk. The ingredients include milk, water, liquid sugar, and cocoa, processed in a mixing and blending vessel with heating and stirring capabilities. Then, implement a self-contained Structured Text program to control the sequential mixing and heating process, including:
	•	Specific ingredient quantities
	•	Stirring speed (e.g., 200 RPM)
	•	Heating temperature (e.g., 70°C)
	•	Time durations (e.g., 10 minutes blending)

The program must include logic for transitioning between ingredient addition, heating, and blending phases, and it should follow ISA-88 principles for modularity and phase separation.

🟧 F (Format) – Specify the Output Format

Provide a complete IEC 61131-3 Structured Text code block that includes:
	•	Parameterized function or method calls for each operation (AddIngredient, StartHeating, StartMixing)
	•	Use of timers, setpoints, and interlocks
	•	Clear phase-based logic with comments and modular structure
	•	Optional discussion on how the logic supports process scalability and reuse

### Generated Code:
The task is to develop an ISA-88-compliant batch control program in IEC 61131-3 Structured Text for producing 100 kg of cocoa milk, including ingredient dosing, mixing at 200 RPM, heating to 70°C, and phase-based process control with fault handling.
**Batch Cocoa Milk:**

Create an ISA-88 batch control recipe for producing 100 kg of cocoa milk, detailing the required ingredients, including milk, water, liquid sugar, and cocoa. The equipment should consist of a mixing and blending vessel capable of stirring and heating. Specify appropriate amounts for each ingredient, as well as optimal mixing temperatures and heating times.

Write a self-contained program in IEC 61131-3 Structured Text for the sequential control of the mixing process, incorporating typical parameter values such as stirring speed, temperature control, and time duration. Ensure the program follows ISA-88 principles, with clear logic for controlling the heating and blending phases. Discuss the challenges in scaling and optimizing the control process for industrial production.

**R-T-F:**

🟥 R (Role) – Define Your Role

Act as a control systems engineer developing ISA-88-compliant batch processing programs using IEC 61131-3 Structured Text for food manufacturing systems.

🟩 T (Task) – Define the Objective

Create an ISA-88-compliant batch control recipe to produce 100 kg of cocoa milk. The ingredients include milk, water, liquid sugar, and cocoa, processed in a mixing and blending vessel with heating and stirring capabilities. Then, implement a self-contained Structured Text program to control the sequential mixing and heating process, including:
	•	Specific ingredient quantities
	•	Stirring speed (e.g., 200 RPM)
	•	Heating temperature (e.g., 70°C)
	•	Time durations (e.g., 10 minutes blending)

The program must include logic for transitioning between ingredient addition, heating, and blending phases, and it should follow ISA-88 principles for modularity and phase separation.

🟧 F (Format) – Specify the Output Format

Provide a complete IEC 61131-3 Structured Text code block that includes:
	•	Parameterized function or method calls for each operation (AddIngredient, StartHeating, StartMixing)
	•	Use of timers, setpoints, and interlocks
	•	Clear phase-based logic with comments and modular structure
	•	Optional discussion on how the logic supports process scalability and reuse in industrial systems

Ensure the program is structured to handle typical parameter variations and includes safety checks for temperature and timing. Discuss the challenges of scaling this control logic for industrial production, focusing on maintaining process stability and efficiency under varying conditions.

**Batch Cocoa Milk:**

Create a self-contained IEC 61131-3 Structured Text program to control the sequential mixing and heating of 100 kg of cocoa milk. The program should follow ISA-88 principles for batch control, with specific parameter values for ingredient amounts, stirring speed, and heating temperature. Discuss the challenges of scaling this control logic for industrial production, focusing on maintaining process stability and efficiency under varying conditions.

**R-T-F:**

🟥 R (Role) – Define Your Role

Act as a control systems engineer developing ISA-88-compliant batch control programs using IEC 61131-3 Structured Text for food production processes.

🟩 T (Task) – Define the Objective

Create a self-contained IEC 61131-3 Structured Text program to control the sequential mixing and heating of 100 kg of cocoa milk. The program should follow ISA-88 principles for batch control, with specific parameter values for ingredient amounts, stirring speed, and heating temperature.

Ensure the program includes:
	•	Concrete values for the amounts of milk, water, liquid sugar, and cocoa
	•	A stirring speed of 200 RPM
	•	A heating temperature of 70°C
	•	A time duration of 10 minutes for the mixing phase
	•	Proper sequencing of the heating and blending phases
	•	Interlocks and safety checks to ensure process stability

Discuss the challenges of scaling this control logic for industrial production, focusing on maintaining process stability and efficiency under varying conditions.

🟧 F (Format) – Specify the Output Format

Provide a self-contained IEC 61131-3 Structured Text program with the following structure:
	•	Define the required ingredients and their amounts
	•	Implement a timer for the mixing phase
	•	Include a heating control loop with temperature monitoring
	•	Implement a phase-based control logic for the heating and blending phases
	•	Add comments explaining the logic and parameter values
	•	Include a discussion on the challenges of scaling the control logic for industrial production, focusing on maintaining process stability and efficiency under varying conditions.

Ensure the program is modular and includes typical parameter values for the

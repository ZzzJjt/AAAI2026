### Intent:
**Intent Summary:**  
Develop an ISA-88-compliant batch control program in Structured Text to automate the production of 100 kg cocoa milk, including ingredient mixing, heating (70°C), and blending (200 RPM for 10 minutes), with modular logic for scalability and industrial adaptation.  

*(Focus: Recipe execution, phase transitions, and parameter control for consistent quality.)*

### Prompt:
**Batch Cocoa Milk:**

Create an ISA-88 batch control recipe for producing 100 kg of cocoa milk, detailing the required ingredients, including milk, water, liquid sugar, and cocoa. The equipment should consist of a mixing and blending vessel capable of stirring and heating. Specify appropriate amounts for each ingredient, as well as optimal mixing temperatures and heating times.

Write a self-contained program in IEC 61131-3 Structured Text for the sequential control of the mixing process, incorporating typical parameter values such as stirring speed, temperature control, and time duration. Ensure the program follows ISA-88 principles, with clear logic for controlling the heating and blending phases. Discuss the challenges in scaling and optimizing the control process for industrial production.

**R-I-S-E:**

🟥 R (Role) – Define Your Role

Act as a batch process control engineer developing ISA-88-compliant control systems for food production using IEC 61131-3 Structured Text.

🟩 I (Input) – Information Provided

You are tasked with creating a batch control recipe for producing 100 kg of cocoa milk using a mixing and blending vessel with heating and stirring capabilities. The ingredients include milk, water, liquid sugar, and cocoa. Process control parameters include stirring speed, heating temperature, and mixing time. The control system must follow ISA-88 principles to ensure modularity and scalability for industrial use.

🟧 S (Steps) – Steps to Perform
	1.	Define the ISA-88-compliant recipe, specifying quantities (e.g., 60 kg milk, 20 kg water, 15 kg liquid sugar, 5 kg cocoa) and associated processing steps.
	2.	Implement a self-contained Structured Text program for the mixing process, with control logic for:
	•	Ingredient addition
	•	Heating to target temperature (e.g., 70°C)
	•	Mixing phase control (e.g., 200 RPM for 10 minutes)
	3.	Use timers, setpoints, and conditions to manage phase transitions.
	4.	Structure the logic using modular, reusable blocks consistent with ISA-88 batch control models.

🟦 E (Expectation) – Expected Outcome

Deliver a Structured Text control program that executes the cocoa milk mixing process in a modular, reliable, and scalable way. The program should support consistent product quality, follow ISA-88 best practices, and be adaptable to different batch sizes or future formulation changes with minimal effort.

### Generated Code:
**Intent Summary:**  
Develop an ISA-88-compliant batch control program in Structured Text to automate the production of 100 kg cocoa milk, including ingredient mixing, heating (70°C), and blending (200 RPM for 10 minutes), with modular logic for scalability and industrial adaptation.  

*(Focus: Recipe execution, phase transitions, and parameter control for consistent quality.)*
**Batch Cocoa Milk:**

Create an ISA-88 batch control recipe for producing 100 kg of cocoa milk, detailing the required ingredients, including milk, water, liquid sugar, and cocoa. The equipment should consist of a mixing and blending vessel capable of stirring and heating. Specify appropriate amounts for each ingredient, as well as optimal mixing temperatures and heating times.

Write a self-contained program in IEC 61131-3 Structured Text for the sequential control of the mixing process, incorporating typical parameter values such as stirring speed, temperature control, and time duration. Ensure the program follows ISA-88 principles, with clear logic for controlling the heating and blending phases. Discuss the challenges in scaling and optimizing the control process for industrial production.

**R-I-S-E:**

🟥 R (Role) – Define Your Role

Act as a batch process control engineer developing ISA-88-compliant control systems for food production using IEC 61131-3 Structured Text.

🟩 I (Input) – Information Provided

You are tasked with creating a batch control recipe for producing 100 kg of cocoa milk using a mixing and blending vessel with heating and stirring capabilities. The ingredients include milk, water, liquid sugar, and cocoa. Process control parameters include stirring speed, heating temperature, and mixing time. The control system must follow ISA-88 principles to ensure modularity and scalability for industrial use.

🟧 S (Steps) – Steps to Perform
	1.	Define the ISA-88-compliant recipe, specifying quantities (e.g., 60 kg milk, 20 kg water, 15 kg liquid sugar, 5 kg cocoa) and associated processing steps.
	2.	Implement a self-contained Structured Text program for the mixing process, with control logic for:
	•	Ingredient addition
	•	Heating to target temperature (e.g., 70°C)
	•	Mixing phase control (e.g., 200 RPM for 10 minutes)
	3.	Use timers, setpoints, and conditions to manage phase transitions.
	4.	Structure the logic using modular, reusable blocks consistent with ISA-88 batch control models.

🟦 E (Expectation) – Expected Outcome

Deliver a Structured Text control program that executes the cocoa milk mixing process in a modular, reliable, and scalable way. The program should support consistent product quality, follow ISA-88 best practices, and be adaptable to different batch sizes or future formulation changes with minimal effort.
FUNCTION_BLOCK FB_BatchControl
VAR_INPUT
    StartButton : BOOL; // Starts the batch process
    StopButton : BOOL;  // Stops the batch process
    EmergencyStop : BOOL; // Emergency stop signal
    BatchSize : REAL;    // Batch size in kg
    Recipe : ARRAY[1..5] OF REAL; // Recipe ingredients (e.g., milk, water, sugar, cocoa)
END_VAR

VAR_OUTPUT
    MixingPhase : BOOL; // TRUE when mixing is active
    HeatingPhase : BOOL; // TRUE when heating is active
    CoolingPhase : BOOL; // TRUE when cooling is active
    Error : BOOL; // TRUE if an error occurs
    ErrorCode : INT; // Error code (0=NoError, 1=InvalidInput, 2=OverTemp, 3=UnderTemp, 4=OverMix, 5=UnderMix)
END_VAR

VAR
    Phase : INT := 0; // Current phase (0=Idle, 1=Mixing, 2=Heating, 3=Cooling)
    MixingSpeed : REAL := 200.0; // RPM (mixing speed)
    HeatingTemp : REAL := 70.0; // °C (target temperature)
    CoolingTemp : REAL := 40.0; // °C (target temperature)
    MixingTime : REAL := 10.0; // Minutes (mixing time)
    MixingTimer : TON; // Timer for mixing
    HeatingTimer : TON; // Timer for heating
    CoolingTimer : TON; // Timer for cooling
    MixingPhaseTimer : TON; // Timer for mixing phase
    HeatingPhaseTimer : TON; // Timer for heating phase
    CoolingPhaseTimer : TON; // Timer for cooling phase
    MixingPhaseTimerElapsed : REAL; // Elapsed time for mixing phase timer
    HeatingPhaseTimerElapsed : REAL; // Elapsed time for heating phase timer
    CoolingPhaseTimerElapsed : REAL; // Elapsed time for cooling phase timer
    MixingPhaseTimerRunning : BOOL; // TRUE if mixing phase timer is running
    HeatingPhaseTimerRunning : BOOL; // TRUE if heating phase timer is running
    CoolingPhaseTimerRunning : BOOL; // TRUE if cooling phase timer is running
    MixingPhase

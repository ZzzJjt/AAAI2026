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
	•	Optional discussion on how the logic supports process scalability and reuse

**ISA-88 Batch Control Recipe:**

1. **Ingredients:**
	* 50 kg milk
	* 20 kg water
	* 10 kg liquid sugar
	* 10 kg cocoa
2. **Equipment:**
	* Mixing and blending vessel
	* Heating element
	* Stirring mechanism
3. **Process:**
	1. Add milk, water, liquid sugar, and cocoa to the mixing vessel.
	2. Start heating the mixture to 70°C.
	3. Once the mixture reaches 70°C, start stirring at 200 RPM.
	4. Mix the ingredients for 10 minutes.
	5. Turn off the heating element and stop stirring.

**ISA-88-compliant Structured Text Program:**

```
PROGRAM Batch_Cocoa_Milk

FUNCTION AddIngredient(ingredient, quantity)
	IF ingredient = "milk" THEN
		quantity = 50
	ELSEIF ingredient = "water" THEN
		quantity = 20
	ELSEIF ingredient = "liquid_sugar" THEN
		quantity = 10
	ELSEIF ingredient = "cocoa" THEN
		quantity = 10
	END IF
	
	IF quantity > 0 THEN
		OUTPUT "Adding " + quantity + " kg of " + ingredient + " to the mixing vessel."
	END IF
END FUNCTION

FUNCTION StartHeating(temperature)
	IF temperature = 70 THEN
		OUTPUT "Starting heating at 70°C."
	END IF
END FUNCTION

FUNCTION StartMixing(speed)
	IF speed = 200 THEN
		OUTPUT "Starting mixing at 200 RPM."
	END IF
END FUNCTION

FUNCTION Process_Start()
	AddIngredient("milk", 50)
	AddIngredient("water", 20)
	AddIngredient("liquid_sugar", 10)
	AddIngredient("cocoa", 10)
	
	StartHeating(70)
	StartMixing(200)
END FUNCTION

FUNCTION Process_Stop()
	StopHeating()
	StopMixing()
END FUNCTION

FUNCTION Process_Phase

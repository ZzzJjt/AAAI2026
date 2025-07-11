### Intent:
**Intent Summary:**  
Create a structured technical guide explaining object-oriented programming (OOP) in IEC 61131-3 (V3.0) for industrial automation, covering classes, inheritance, and polymorphism with practical examples, trade-offs, and best practices.  

**Industrial Control Task:**  
The provided code implements a state-machine-driven polyethylene batch control process, handling raw material preparation, reaction, cooling, and discharge phases with safety checks, input validation, and modular logic.  

*(Focus: OOP explanation for automation, bridging to the batch control example.)*

### Prompt:
**Object-oriented 61131-3:**
Discuss the concept of classes and methods introduced in IEC 61131-3 Version 3.0, including a detailed explanation of their limitations, advantages, and disadvantages in the context of industrial automation. Provide a relevant example to illustrate these concepts in practice.

Explain how inheritance is implemented in IEC 61131-3, building on the previous example to show how derived classes can extend base functionality. Additionally, refine the example further to demonstrate polymorphism within this framework, discussing its practical applications and constraints.

**R-T-F:**

🟥 R (Role) – Your Role

You are a PLC software developer or automation systems engineer seeking to understand and explain how object-oriented programming (OOP) is applied in IEC 61131-3 Version 3.0, particularly for use in industrial automation.

⸻

🟩 T (Task) – What You Need to Do

Create a technical explanation that covers:
	1.	The concept of classes and methods in IEC 61131-3 V3.0
	2.	Their benefits and limitations in an industrial context
	3.	A working example that demonstrates:
	•	How to define and use a class
	•	How inheritance works by extending a base class
	•	How polymorphism allows dynamic behavior via base class references
	4.	A discussion of practical trade-offs, including:
	•	Increased abstraction vs. complexity in debugging
	•	Portability and vendor support
	•	Impact on scan-cycle performance

⸻

🟦 F (Format) – What the Output Should Look Like

Your final output should be a structured technical document or guide including:
	•	✅ A brief conceptual overview of object-oriented features in IEC 61131-3
	•	✅ A step-by-step code example with structured text (ST) showing class definition, inheritance, and polymorphism
	•	✅ A table or bullet list comparing advantages vs. disadvantages
	•	✅ A summary section highlighting best practices and common use cases for OOP in automation (e.g., modular machinery, device templates)

### Generated Code:
**Intent Summary:**  
Create a structured technical guide explaining object-oriented programming (OOP) in IEC 61131-3 (V3.0) for industrial automation, covering classes, inheritance, and polymorphism with practical examples, trade-offs, and best practices.  

**Industrial Control Task:**  
The provided code implements a state-machine-driven polyethylene batch control process, handling raw material preparation, reaction, cooling, and discharge phases with safety checks, input validation, and modular logic.  

*(Focus: OOP explanation for automation, bridging to the batch control example.)*
**Object-oriented 61131-3:**
Discuss the concept of classes and methods introduced in IEC 61131-3 Version 3.0, including a detailed explanation of their limitations, advantages, and disadvantages in the context of industrial automation. Provide a relevant example to illustrate these concepts in practice.

Explain how inheritance is implemented in IEC 61131-3, building on the previous example to show how derived classes can extend base functionality. Additionally, refine the example further to demonstrate polymorphism within this framework, discussing its practical applications and constraints.

**R-T-F:**

🟥 R (Role) – Your Role

You are a PLC software developer or automation systems engineer seeking to understand and explain how object-oriented programming (OOP) is applied in IEC 61131-3 Version 3.0, particularly for use in industrial automation.

⸻

🟩 T (Task) – What You Need to Do

Create a technical explanation that covers:
	1.	The concept of classes and methods in IEC 61131-3 V3.0
	2.	Their benefits and limitations in an industrial context
	3.	A working example that demonstrates:
	•	How to define and use a class
	•	How inheritance works by extending a base class
	•	How polymorphism allows dynamic behavior via base class references
	4.	A discussion of practical trade-offs, including:
	•	Increased abstraction vs. complexity in debugging
	•	Portability and vendor support
	•	Impact on scan-cycle performance

⸻

🟦 F (Format) – What the Output Should Look Like

Your final output should be a structured technical document or guide including:
	•	✅ A brief conceptual overview of object-oriented features in IEC 61131-3
	•	✅ A step-by-step code example with structured text (ST) showing class definition, inheritance, and polymorphism
	•	✅ A table or bullet list comparing advantages vs. disadvantages
	•	✅ A summary section highlighting best practices and common use cases for OOP in automation (e.g., modular machinery, device templates)  

⸻

🟪 S (Success) – What the Learner Should Know or Be Able to Do

After reading your explanation, the learner should be able to:
	•	✅ Understand the role of classes and methods in IEC 61131-3 V3.0
	•	✅ Apply OOP principles to create modular, reusable code for industrial automation
	•	✅ Discuss the trade-offs between increased abstraction and performance impact
	•	✅ Identify practical use cases for OOP in automation, such as device modeling or state machine control

⸻

🟥 A (Action) – What You Should Do Next

Write a detailed explanation of object-oriented programming in IEC 61131-3 V3.0, including a code example that demonstrates class definition, inheritance, and polymorphism. Discuss the advantages and limitations of using OOP in industrial automation, and provide a table or bullet list comparing the pros and cons. Finally, summarize the best practices and common use cases for OOP in automation.
**Object-Oriented Programming in IEC 61131-3:**

**R: Role**

You are a PLC programmer or automation engineer responsible for developing control logic for industrial processes using IEC 61131-3. You need to understand how to implement object-oriented programming (OOP) principles in this structured text (ST) programming language, including class definitions, inheritance, and polymorphism.

**T: Task**

Create a detailed explanation of OOP in IEC 61131-3, including a code example that demonstrates class definition, inheritance, and polymorphism. Discuss the advantages and limitations of using OOP in industrial automation, and provide a table or bullet list comparing the pros and cons. Finally, summarize the best practices and common use cases for OOP in automation.

**F: Format**

Your response should be a structured text (ST) code example that demonstrates OOP principles in IEC 61131-3, including class definition, inheritance, and polymorphism. The code should be self-contained and easy to understand, with clear comments explaining each section. You should also provide a table or bullet list comparing the advantages and disadvantages of using OOP in industrial automation, and summarize the best practices and common use cases for OOP in automation.

**A: Action**

Develop a self-contained code example in IEC 61131-3 that demonstrates OOP principles,

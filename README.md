Objective:
********
The objective of this project is to ensure that answers provided to 8th-grade students are not overly complex or too advanced. It creates a student agent that generates responses, and a guardrail mechanism that checks whether those responses are at a PhD-level complexity. If the response is too complex, it gets blocked automatically.

✅ How It Works (Step-by-Step)
Two Agents Are Defined:

student_agent: Answers questions for 8th-grade students.

complexity_checker: Evaluates if the student's answer is too complex.

Guardrail Logic:

Decorator @output_guardrail wraps check_complexity.

Before a final response is returned, it’s passed to complexity_checker.

If the output is flagged as too complex (isPHDLevelResponse = True), the guardrail blocks the response.

Try/Except Block:

If the complexity check fails (too complex), the system raises OutputGuardrailTripwireTriggered and prints a blocking message.

Otherwise, the approved response is printed.


https://github.com/user-attachments/assets/44b2bc95-b31e-4705-aa4b-6e6dced89499

<img width="1607" height="907" alt="complex checker Log-Generation" src="https://github.com/user-attachments/assets/1c8e7284-b714-4c56-840d-4a1f138c086a" />
<img width="1610" height="907" alt="complex checker Log-Trigger-True" src="https://github.com/user-attachments/assets/d89ce5be-49ca-4af7-9650-9791248b5ca8" />
<img width="1609" height="908" alt="complex checker Log-agent Error" src="https://github.com/user-attachments/assets/60c18329-1784-4e4e-b777-ed0a062ae039" />
<img width="1609" height="910" alt="complex checker Log-output" src="https://github.com/user-attachments/assets/7dfc8b55-9f59-4f7b-a6fa-54cf44f83ca9" />
<img width="1611" height="907" alt="complex checker code-output" src="https://github.com/user-attachments/assets/4f48ad6c-583f-4e5d-8a26-58b0909bfd9d" />
<img width="1612" height="906" alt="complex checker Log-Generation output" src="https://github.com/user-attachments/assets/55a4d699-f141-4fa9-9b74-0341f876e30c" />

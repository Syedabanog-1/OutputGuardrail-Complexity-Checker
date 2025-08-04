import asyncio
from pydantic import BaseModel
from agents import (
    Agent, Runner, trace,
    OutputGuardrailTripwireTriggered,
    output_guardrail, GuardrailFunctionOutput
)
from connection import config

# Output model from the student agent
class SimpleAnswer(BaseModel):
    response: str

# Output model from the complexity checker agent
class ComplexCheck(BaseModel):
    isPHDLevelResponse: bool

# Agent that checks if response is too complex
complexity_checker = Agent(
    name="Complexity Checker",
    instructions="""
        Check if the response is too complex for an 8th grade student.
        If it is, set isPHDLevelResponse = true, otherwise false.
    """,
    output_type=ComplexCheck
)

# Guardrail function to block complex answers
@output_guardrail
async def check_complexity(ctx, agent: Agent, output) -> GuardrailFunctionOutput:
    result = await Runner.run(complexity_checker, output.response, run_config=config)
    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=result.final_output.isPHDLevelResponse
    )
# Main student agent
student_agent = Agent(
    name="Student Agent",
    instructions="""
        Answer questions for 8th grade students using simple language.
        If asked to use advanced language, use complex scientific terms.
    """,
    output_type=SimpleAnswer,
    output_guardrails=[check_complexity]
)
# Main function
async def main():
    with trace("Complexity Checker"):
        query = "What are trees? Explain using the most complex scientific terminology possible"
        # query = "What are trees? Explain in simple words"
        try:
            result = await Runner.run(student_agent, query, run_config=config)
            print("Response:", result.final_output.response)
        except OutputGuardrailTripwireTriggered:
            print(" Too complex! Response blocked by Complexity Checker.")

if __name__ == "__main__":
    asyncio.run(main())


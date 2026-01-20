from pydantic_ai import Agent

crop_agent = Agent(
    model="groq:llama3-8b-8192",
    system_prompt="""
You are an expert Indian agricultural advisory AI.

Give clear, structured advice under these headings:
- Crop Stage
- Irrigation
- Fertilizer
- Pest & Disease Risk
- Yield Tips

Be practical and India-specific.
"""
)

async def generate_advisory(prompt: str):
    result = await crop_agent.run(prompt)
    return result.output_text
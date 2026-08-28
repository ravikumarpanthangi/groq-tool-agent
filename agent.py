import json
from groq import Groq
from tools import tools, available_functions

MODEL_NAME = "openai/gpt-oss-120b"


def run_agent(client: Groq, user_message: str, max_turns: int = 5) -> str:
    messages = [
        {"role": "system", "content": "You are a helpful assistant. Use tools when needed to answer accurately."},
        {"role": "user", "content": user_message},
    ]

    for turn in range(max_turns):
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=messages,
            tools=tools,
            tool_choice="auto",
        )

        msg = response.choices[0].message

        if msg.tool_calls:
            messages.append(msg)

            for tool_call in msg.tool_calls:
                fn_name = tool_call.function.name
                fn_args = json.loads(tool_call.function.arguments)

                print(f"[agent] calling tool: {fn_name}({fn_args})")

                fn_result = available_functions[fn_name](**fn_args)

                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "name": fn_name,
                    "content": str(fn_result),
                })
            continue

        return msg.content

    return "Agent stopped: too many turns."

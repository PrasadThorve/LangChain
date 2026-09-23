from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI
from langsmith import traceable
import json
import re
import inspect

MAX_ITERATION = 4
MODEL = "gpt-4o-mini"

client = OpenAI()


def get_product_price(product: str) -> float:
    """Look up the price of the product in the catalog"""
    print(f"   >>> Executing get_product_price(product='{product}')")
    prices = {
        "laptop": 100000, 
        "mobile": 60000, 
        "headphone": 2000, 
        "keyboard": 1500
        }

    return prices.get(product, 0)


def apply_discount(price: float, discount_tier: str) -> float:
    """Take price as input and apply the discount according to discount_tier and return discounted price, Available Tiers : bronze, silver, gold
    """

    print(
        f"   >>> Executing apply_discount(price={price}, discount_tier={discount_tier})"
    )

    discounts = {
        "bronze": 5, 
        "silver": 10, 
        "gold": 15 
        }
    
    price = float(price)

    discount_percentage = discounts.get(discount_tier, 0)

    final_value = round(price * (1 - discount_percentage / 100), 2)

    return final_value



tools = {
    "get_product_price" : get_product_price,
    "apply_discount" : apply_discount
}

def get_tool_description(tools_dict):
    description = []
    for tool_name, tool_function in tools_dict.items():
        signature = inspect.signature(tool_function)
        docstring = inspect.getdoc(tool_function)
        # args = inspect.getargs(tool_function)
        # print(f"tool_name : {tool_name}, signature: {signature}, docstring = {docstring}")
        description.append(f"{tool_name}{signature} - {docstring}")
        
    return "\n".join(description)

# print(get_tool_description(tools))

tools_description = get_tool_description(tools)
tool_names = ", ".join(tools.keys())
# print(tool_names)


react_prompt = f"""
Answer the following questions as best you can. You have access to the following tools:

{tools_description}

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Begin!

Question: {{question}}
Thought:
"""


def openai_chat_function(messages):
    response = client.responses.create(
        model=MODEL,
        input=messages,
        temperature=0
    )
    # print(response.output_text)
    return response


#--- Agent Loop ---
# @traceable(name="LangChain Agent Loop")
def run_agent(question:str):
  
    print(f"Question={question}")
    print("="*50)
    
    prompt = react_prompt.format(question=question)
    scratchpad = ""
    
    print(f"\nInitial Prompt :\n{prompt}")
    # response = openai_chat_function(prompt)
    # # print(f"\nFull Response :\n{response}")
    # print(f"\n\n\n\nResponse Text ---------> \n{response.output_text}")
    
    count=0

    for iteration in range(1, MAX_ITERATION+1):
        print(f"\n----- Iteration {iteration} ----")
        
        full_prompt = prompt + scratchpad
        print(f"\n\n\n Full Prompt ----------> \n{full_prompt}")
        response = openai_chat_function(
            messages=[{
                "role":"user", 
                "content": full_prompt
            }],
        )
        
        output_text = response.output_text
        output_text = output_text.split("Observation")[0]
        print(f"\n\n\n\nResponse from LLM  ---------> \n{output_text}")
        
        
        print(f"  [Parsing] Looking for Final Answer in LLM output...")
        final_answer_match = re.search(r"Final Answer:\s*(.+)", output_text)
        if final_answer_match:
            final_answer = final_answer_match.group(1).strip()
            print(f" [Parsed] final Answer : {final_answer}")
            return final_answer
        
        

        print(f"  [Parsing] Looking for Action and Action Input from LLM ")
        action_match = re.search(r"Action:\s*(.+)", output_text)
        action_input_match = re.search(r"Action Input:\s*(.+)", output_text)
        
        if not action_match and not action_input_match:
            print("  [Parsing] Error: Could not parse Ation/Action Input match")
            break
        
        tool_name = action_match.group(1).strip()
        tool_input_raw = action_input_match.group(1).strip()
        print(f"action_match : {action_match}")
        print(f"tool_name : {tool_name}")
        print(f"tool_input_raw: {tool_input_raw}")
        
        raw_args = [x.strip() for x in tool_input_raw.split(",")]
        print(f"Raw Args = {raw_args}")
        
        args = [x.strip().strip(""" "'\()/ """) for x in raw_args]
        
        print(f"Args = {args}")
        
        if tool_name not in tools:
            observations = f"Error: Tool '{tool_name} not found. Available tools: {list[str](tools.keys())}"
        else:
            observations = str(tools[tool_name](*args))
             
            
        print(f"    [Tool Result] {observations}")
        
        scratchpad += f"{output_text}\nObservation: {observations}\nThought:"
        
        # count+=1
        # if(count==2):
        #     break
        
        
         
                



    print("ERROR: Max iterations reached  without a final answer")
    return None







if __name__ == "__main__":
    print("Raw Function Calling  \n")
    result = run_agent("What is the price of laptop after applying gold discount?")
    
    print(f"\n\n Final Result : \n{result}")

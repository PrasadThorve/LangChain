from dotenv import load_dotenv

load_dotenv()

from langchain.chat_models import init_chat_model
from langchain.tools import tool
from langsmith import traceable
from langchain_core.messages import SystemMessage, HumanMessage, ToolMessage

MAX_ITERATION = 4
MODEL = "gpt-4o-mini"


# Tools
@tool
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


@tool
def apply_discount(price: float, discount_tier: str) -> float:
    """Take price as input and apply the discount according to discount_tier and return discounted price
    Available Tiers : bronze, silver, gold
    """

    print(
        f"   >>> Executing apply_discount(price={price}, discount_tier={discount_tier})"
    )

    discounts = {
        "bronze": 5, 
        "silver": 10, 
        "gold": 15
        }

    discount_percentage = discounts.get(discount_tier, 0)

    final_value = round(price * (1 - discount_percentage / 100), 2)

    return final_value




#--- Agent Loop ---
@traceable(name="LangChain Agent Loop")
def run_agent(question:str):
    tools = [get_product_price, apply_discount]
    tools_dict = {t.name:t for t in tools}
    # tools_dict = {}
    # for tool in tools:
    #     tools_dict[tool.name] = tool
    
    llm = init_chat_model(f"openai:{MODEL}", temperature=0)
    
    llm_with_tools = llm.bind_tools(tools)
    
    print(f"Question={question}")
    print("="*50)
    
    messages = [
        SystemMessage(
            content=(
                "You are helpful shopping assistant"
                "You have access to the product catalog tool and a discount tool. \n\n"
            )
        ),
        
        HumanMessage(
            content=question
        )
    ]
    
    for iteration in range(1, MAX_ITERATION+1):
        print(f"\n----- Iteration {iteration} ----")
        
        ai_message = llm_with_tools.invoke(messages)
        
        tool_calls = ai_message.tool_calls
        
        # print(f"   [AI Message] : {ai_message.content}")
        print(f"   [Tool Calls] : {tool_calls}")
        
        if not tool_calls:
            print(f"\nFinal Answer : {ai_message.content}")
            return ai_message.content
        
        #force one tool call per iteration
        tool_call = tool_calls[0]
        tool_name = tool_call.get("name")
        tool_description = tool_call.get("description")
        tool_args = tool_call.get("args")
        tool_call_id = tool_call.get("id")
        
        print(f"   [Tool Selected] {tool_name} with args: {tool_args}")
        
        tool_to_use = tools_dict.get(tool_name)
    
        if tool_to_use is None:
            raise ValueError(f"tool '{tool_name}' not found")
        
        observations = tool_to_use.invoke(tool_args)
        
        print(f"   [Tool Result] {observations}")
        
        messages.append(ai_message)
        messages.append(
            ToolMessage(content=str(observations), tool_call_id=tool_call_id)
        )


    print("ERROR: Max iterations reached  without a final answer")
    return None

if __name__ == "__main__":
    print("Hello Langchain Agent \n")
    result = run_agent("What is the price of laptop after applying gold discount?")

from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI
from langsmith import traceable
import json

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


tools = [
    {
        "type":"function",
        "name": "get_product_price",
        "description": "Look up the price of the product in the catalog",
        "parameters": {
            "type":"object",
            "properties":{
                "product" : {
                    "type":"string",
                    "description": "name of product",
                },
            },
            "required":["price"],
        },
    },
    {
        "type":"function",
        "name":"apply_discount",
        "description": "Take price as input and apply the discount according to discount_tier and return discounted price Available Tiers : bronze, silver, gold",
        "parameters":{
            "type":"object",
            "properties":{
                "price":{
                    "type":"number",
                    "description":"price of the product",
                },
                "discount_tier":{
                    "type":"string",
                    "description":"type of discount gold, silver or bronze"
                },
            },
            "required":["price", "discount_tier"]
        }
    }
]




#--- Agent Loop ---
@traceable(name="LangChain Agent Loop")
def run_agent(question:str):
  
    
    print(f"Question={question}")
    print("="*50)
    

    
    messages = [
        {
            "role":"system",
            "content": "You are helpful shopping assistant and You have access to the product catalog tool and a discount tool. \n\n",          
        },
        {
            "role":"user",
            "content":question
        }
    ]
    

    
    
    for iteration in range(1, MAX_ITERATION+1):
        print(f"\n----- Iteration {iteration} ----")
        
        response = client.responses.create(
            model=MODEL,
            tools=tools,
            input = messages
        )
        print(f"\nMessages = {messages} \n")
        print(response.output)
        
        messages+= response.output
    
        
        for item in response.output:
            if item.type == "function_call":
                if item.name == "get_product_price":
                    #execute function
                    product = json.loads(item.arguments)["product"]
                    price = get_product_price(product=product)
                    
                    messages.append(
                        {
                            "type": "function_call_output",
                            "call_id" : item.call_id,
                            "output": str(price)
                        }
                    )
                    
                if item.name == "apply_discount":
                    #execute function
                    price = json.loads(item.arguments)["price"]
                    discount_tier = json.loads(item.arguments)["discount_tier"]
                    
                    discounted_price = apply_discount(price,discount_tier)
                    
                    messages.append(
                        {
                            "type":"function_call_output",
                            "call_id": item.call_id,
                            "output": str(discounted_price)
                        }
                    )
                    
            else:
                
                return response.output


    print("ERROR: Max iterations reached  without a final answer")
    return None

if __name__ == "__main__":
    print("Raw Function Calling  \n")
    result = run_agent("What is the price of laptop after applying gold discount?")
    
    print(f"\n\n Final Result : \n{result}")

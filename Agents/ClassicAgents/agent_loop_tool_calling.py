from dotenv import load_dotenv

load_dotenv()

from langchain.chat_models import init_chat_model
from langchain.tools import tool

MAX_ITERATION = 4
MODEL = "gpt-4o-mini"


# Tools
@tool
def get_product_price(product: str) -> float:
    """Look up the price of the product in the catalog"""
    print(f"   >>> Executing get_product_price(product='{product}')")
    prices = {"laptop": 100000, "mobile": 60000, "headphone": 2000, "keyboard": 1500}

    return prices.get(product, 0)


# @tool
def apply_discount(price: float, discount_tier: str) -> float:
    """Take price as input and apply the discount according to discount_tier and return discounted price
    Available Tiers : bronze, silver, gold
    """

    print(
        f"   >>> Executing apply_discount(price={price}, discount_tier={discount_tier})"
    )

    discounts = {"bronze": 5, "silver": 10, "gold": 15}

    discount_percentage = discounts.get(discount_tier, 0)

    final_value = round(price * (1 - discount_percentage / 100), 2)

    return final_value


# test function
print(apply_discount(1000, "gold"))

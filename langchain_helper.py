import os

from dotenv import load_dotenv
from langchain.chains import LLMChain, SequentialChain
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq

load_dotenv()
os.environ["_API_KEY"] = os.getenv("GROQ_API_KEY")

model = ChatGroq(model="llama3-8b-8192")


def generate_food_list(tribe):

    tribe_template = PromptTemplate(
        input_varaibles=["tribe"],
        template="I want to open a restaurant for {tribe} food in Nigeria .Suggest a fancy name for me. Just give me the name. No preamble",
    )

    name_chain = LLMChain(
        llm=model, prompt=tribe_template, output_key="restaurant_name"
    )

    food_template = PromptTemplate(
        input_variables=["restaurant_name"],
        template="Suggest some menu items for {restaurant_name}.Just Return as a comma seperated list, no preamble",
    )

    food_item_chain = LLMChain(llm=model, prompt=food_template, output_key="food_item")

    total_chain = SequentialChain(
        chains=[name_chain, food_item_chain],
        input_variables=["tribe"],
        output_variables=["restaurant_name", "food_item"],
    )

    result = total_chain.invoke({"tribe": tribe})
    return result["restaurant_name"], result["food_item"]

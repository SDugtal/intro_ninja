from dotenv import load_dotenv
import os
from typing import Tuple
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from langchain.chains import LLMChain
from third_parties.linkedin import scrape_linkedin_profile
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from output_parser import summary_parser, Summary

load_dotenv()  # Load GEMINI_API_KEY

def ice_break_with(name: str) -> Tuple[Summary, str]:
    linkedin_username = linkedin_lookup_agent(name=name)
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_username, mock=True)

    summary_template = """
    Given the LinkedIn information {information} about a person, I want you to create:
    1. A short summary
    2. Two interesting facts 
    \n{format_instruction}
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template,
        partial_variables={"format_instruction": summary_parser.get_format_instructions()},
    )

    # ✅ FIX: Pass Gemini API key explicitly
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        google_api_key=os.environ.get("GEMINI_API_KEY")
    )

    chain = summary_prompt_template | llm | summary_parser
    res: Summary = chain.invoke(input={"information": linkedin_data})

    return res, linkedin_data.get("photoUrl")

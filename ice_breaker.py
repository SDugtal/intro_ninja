from dotenv import load_dotenv
from langchain.prompts.prompt import PromptTemplate
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from third_parties.linkdin import scrape_linkedin_profile


if __name__ == "__main__":
    load_dotenv()

    print("Hello LangChain")

    summary_template = """
    givein the Linkdin information {information } about a person I want you to create :
    1. A shot summary
    2. two intresting facts 
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm= ChatOllama(model="mistral")
    chain = summary_prompt_template | llm | StrOutputParser()
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url="https://www.linkedin.com/in/shirshak-dugtal-164b0b297/")


    res = chain.invoke(input={"information": linkedin_data})

    print(res)

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

from .state import ResearchState
from .tools import search_tool



load_dotenv()


llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash"
)

def search_web(state: ResearchState):
    print("Running web search node...")

    results = search_tool.invoke(state["question"])

    return {
        "research": results
    }

def research(state: ResearchState):
    print("Running research node...")

    response = llm.invoke(
        f"""
        Research the following topic using the provided web search results.

        Question:
        {state['question']}

        Web search results:
        {state['search_results']}

        Analyze the information and extract the important,
        relevant and accurate facts that should be used
        to answer the question.
        """
    )

    return {
        "research": response.text
    }


def generate_answer(state: ResearchState):
    print("Running answer generation node...")

    response = llm.invoke(
        f"""
        Using the research below, write a clear and useful answer
        to the original question.

        Question:
        {state['question']}

        Research:
        {state['research']}
        """
    )

    return {
        "answer": response.text
    }
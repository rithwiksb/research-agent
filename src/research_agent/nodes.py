from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

from .state import ResearchState


load_dotenv()


llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash"
)


def research(state: ResearchState):
    print("Running research node...")

    response = llm.invoke(
        f"""
        Research the following topic and explain the important information
        clearly and accurately.

        Topic:
        {state['question']}
        """
    )

    return {
        "research": response.text()
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
        "answer": response.text()
    }
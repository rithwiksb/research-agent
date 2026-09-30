from .graph import build_graph


app = build_graph()


result = app.invoke({
    "question": "What is LangGraph?",
    "research": "",
    "answer": "",
})


print("\nFinal answer:")
print(result["answer"])
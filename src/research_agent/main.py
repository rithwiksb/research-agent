from .graph import build_graph


app = build_graph()


result = app.invoke({
    "question": "What is LangGraph?",
    "search_results":"",
    "research": "",
    "answer": "",
})


print("\nFinal answer:")
print(result["answer"])
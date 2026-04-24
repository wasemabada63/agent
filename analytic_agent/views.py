from rest_framework.decorators import api_view
from rest_framework.response import Response
from analytics_bot.src.pipeline import ask_retail_rag_ui

@api_view(['POST','GET'])
def ask_question(request):
    if request.method == "GET":
        return Response({"question": "What is the best selling product in the last month?"})

    if request.method == "POST":
        question = request.data.get("question", "")
        out = ask_retail_rag_ui(question)
        if type(out) == list:
            return Response(out[len(out)-1])
        else:
            return Response(out)
    
    # {"question": "What is the best selling product in the last month?"}


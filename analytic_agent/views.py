from rest_framework.decorators import api_view
from rest_framework.response import Response
from analytics_bot.src.pipeline import ask_retail_rag_ui

@api_view(['POST'])
def ask_question(request):
    if request.method == "GET":
        return Response({"question": "What is the best selling product in the last month?"})

    if request.method == "POST":
        question = request.data.get("question", "")
        try:
            gen = ask_retail_rag_ui(question)
            out_list = list(gen)
            if out_list:
                return Response(out_list[-1])
            else:
                return Response({"error": "out_list was empty", "type_of_gen": str(type(gen))})
        except Exception as e:
            import traceback
            return Response({"error": str(e), "traceback": traceback.format_exc()})
    
    # {"question": "What is the best selling product in the last month?"}


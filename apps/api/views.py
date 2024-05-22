# views.py
from django.http import JsonResponse
from django.views import View

from .langchain_singleton import LangChainAgentSingleton


class RepPerformanceView(View):
    def get(self, request):
        rep_id = request.GET.get('rep_id')
        if not rep_id:
            return JsonResponse({'error': 'rep_id is required'}, status=400)

        agent = LangChainAgentSingleton.get_instance()
        prompt = f"Analyze the performance of sales representative with ID {rep_id} and provide detailed feedback."
        result = agent.invoke({'input': prompt})

        return JsonResponse(result, safe=False)


class TeamPerformanceView(View):
    def get(self, request):
        agent = LangChainAgentSingleton.get_instance()
        prompt = "Provide a summary of the sales team’s overall performance."
        result = agent.invoke(prompt)

        return JsonResponse(result, safe=False)


class PerformanceTrendsView(View):
    def get(self, request):
        time_period = request.GET.get('time_period')
        if not time_period:
            return JsonResponse({'error': 'time_period is required'}, status=400)

        agent = LangChainAgentSingleton.get_instance()
        prompt = f"Analyze sales data over the {time_period} period to identify trends and forecast future performance."
        result = agent.run_query(prompt)

        return JsonResponse(result, safe=False)

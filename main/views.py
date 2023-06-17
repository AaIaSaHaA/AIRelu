from django.shortcuts import render
from django.views import View
from langchain.llms import Cohere
from langchain import PromptTemplate, LLMChain

COHERE_API_KEY = "uMSnjN9J9qiRgy7oasD6TuvaEXI05HgsenfJCgyx"

class MainView(View):
    def get(self, request):
        return render(request, 'main/main.html')

    def post(self, request):
        question = request.POST.get('question')
        
        template = """Question: {question}
        Answer: Let's think step by step."""
        prompt = PromptTemplate(template=template, input_variables=["question"])

        llm = Cohere(cohere_api_key=COHERE_API_KEY)
        llm_chain = LLMChain(prompt=prompt, llm=llm)

        response = llm_chain.run(question)
        
        context = {
            'question': question,
            'response': response,
        }
        return render(request, 'main/main.html', context)

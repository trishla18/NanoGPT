from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import ChatHistory
from adminpanel.models import Faculty
from peft import PeftModel, PeftConfig
from transformers import AutoModelForCausalLM, AutoTokenizer
from huggingface_hub import login
from django.core.mail import send_mail
from django.conf import settings

write_key = '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'
login(write_key)
model_name = "TheBloke/Mistral-7B-Instruct-v0.2-GPTQ"
# model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto", trust_remote_code=False, revision="main")
config = PeftConfig.from_pretrained("trishla03/nanogpt_1")
# model = PeftModel.from_pretrained(model, "trishla03/nanogpt_1")
tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=True)
intstructions_string = f"""please answer the following question?"""
prompt_template = lambda comment: f'''[INST] {intstructions_string} \n{comment} \n[/INST]'''

# Create your views here.
def chatPage(request):
    return render(request, "chat.html")

@csrf_exempt
def ask(request):
    comment = request.POST["question"]
    prompt = prompt_template(comment)
    model.eval()
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(input_ids=inputs["input_ids"].to("cuda"), max_new_tokens=280)
    response = tokenizer.batch_decode(outputs)[0]
    historyObj = ChatHistory(user_id=request.POST["email"], topic_id=request.POST["topic"], chat_id=request.POST["chatID"], question=request.POST["question"], response=response)
    historyObj.save()
    if outputs is None:
        faculty = Faculty.objects.get(topic_id=request.POST["topic"])
        subject = 'E-Guru Query'
        message = request.POST["question"] + "<br/><br/>" + "Reply to "+request.POST["email"]
        recipient_list = [faculty.email]
        send_mail(subject,message,settings.DEFAULT_FROM_EMAIL,recipient_list,fail_silently=False,)
    return JsonResponse({"resp":response})
    

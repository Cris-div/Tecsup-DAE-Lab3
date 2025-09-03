from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import Exam, Question, Choice
import json

def exam_to_dict(exam: Exam):
    return {
        "id": exam.id,
        "title": exam.title,
        "description": exam.description,
        "question_count": exam.questions.count(),
    }

def exam_detail_to_dict(exam: Exam):
    return {
        "id": exam.id,
        "title": exam.title,
        "description": exam.description,
        "questions": [
            {
                "id": q.id,
                "text": q.text,
                "choices": [
                    {"id": c.id, "text": c.text, "is_correct": c.is_correct}
                    for c in q.choices.all()
                ],
            }
            for q in exam.questions.all().prefetch_related('choices')
        ],
    }

@require_http_methods(["GET"])
def api_exams(request):
    data = [exam_to_dict(e) for e in Exam.objects.all().order_by('-created_at')]
    return JsonResponse(data, safe=False)

@require_http_methods(["GET"])
def api_exam_detail(request, exam_id: int):
    exam = get_object_or_404(Exam, id=exam_id)
    return JsonResponse(exam_detail_to_dict(exam), safe=False)

@csrf_exempt  # Para demo rápida; mejor usar token CSRF en fetch
@require_http_methods(["POST"])
def api_question_create(request, exam_id: int):
    exam = get_object_or_404(Exam, id=exam_id)
    try:
        payload = json.loads(request.body.decode('utf-8'))
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")

    text = payload.get("text")
    choices = payload.get("choices", [])  # [{text: "...", is_correct: bool}, ...]

    if not text or not isinstance(choices, list) or len(choices) < 2:
        return HttpResponseBadRequest("Provide 'text' and at least two choices.")

    # Validar exactamente una correcta
    correct_count = sum(1 for c in choices if c.get("is_correct"))
    if correct_count != 1:
        return HttpResponseBadRequest("Exactly one choice must be correct.")

    # Crear
    q = Question.objects.create(exam=exam, text=text)
    for c in choices:
        Choice.objects.create(question=q, text=c.get("text", ""), is_correct=bool(c.get("is_correct")))
    return JsonResponse({"status": "ok", "question_id": q.id})

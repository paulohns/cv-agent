def route_question(question: str) -> str:
    question_lower = question.lower()
    if any(term in question_lower for term in ["tecnologia", "framework", "projeto", "código", "desenvolvimento", "técnico"]):
        return "tecnico"
    elif any(term in question_lower for term in ["liderança", "comunicação", "equipes", "soft skills", "gestão", "perfil"]):
        return "rh"
    else:
        return "geral"

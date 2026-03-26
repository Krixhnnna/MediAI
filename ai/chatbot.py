from ai.symptom_checker import check_symptoms

def get_response(user_input):
    result = check_symptoms(user_input)

    return f"""
Possible Issue: {result['disease']}

Suggested Specialist: {result['doctor']}

General Medicines: {', '.join(result['medicines'])}

⚠️ This is not a medical prescription. Please consult a doctor.
"""
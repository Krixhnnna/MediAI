def check_symptoms(text):
    text = text.lower()

    if "fever" in text and "cough" in text:
        return {
            "disease": "Flu or Viral Infection",
            "doctor": "General Physician",
            "medicines": ["Paracetamol", "Cough Syrup"]
        }

    if "chest pain" in text:
        return {
            "disease": "Possible Heart Issue",
            "doctor": "Cardiologist",
            "medicines": ["Aspirin (only under supervision)"]
        }

    return {
        "disease": "Unknown",
        "doctor": "General Physician",
        "medicines": ["Consult doctor"]
    }
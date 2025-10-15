from pydantic import BaseModel, Field

# --- Pydantic Output Schema (Kept for Structure) ---
class SymptomCheckResponse(BaseModel):
    """Schema for the LLM's structured output."""
    probable_conditions: list[str] = Field(..., description="A list of conditions.")
    recommended_next_steps: list[str] = Field(..., description="A list of next steps.")
    disclaimer: str = Field(
        "⚠️ EDUCATIONAL DISCLAIMER: This tool is for informational and educational purposes only and is not a substitute for professional medical advice, diagnosis, or treatment. Always consult a qualified healthcare professional.",
        description="Mandatory safety and educational disclaimer."
    )

class LLMService:
    """MOCK SERVICE: Simulates the LLM interaction without requiring an API key."""
    def __init__(self):
        # We don't need a client, but we keep the structure.
        print("MOCK LLM SERVICE INITIALIZED: Using hardcoded responses.")
        pass

    def check_symptoms(self, symptom_text: str) -> dict:
        """
        Returns a hardcoded, structured response based on general symptoms.
        The input symptom text is used for demonstration but does not affect the output.
        """

        # --- MOCK REASONING & SUGGESTION ---
        # Simple check based on common keywords for a basic mock simulation
        symptoms_lower = symptom_text.lower()
        if "headache" in symptoms_lower and "stiff neck" in symptoms_lower:
            conditions = ["Tension Headache", "Severe Migraine", "Neck Strain"]
            steps = [
                "Rest in a dark, quiet room.",
                "Apply a cold or warm compress to the neck.",
                "If symptoms are severe or come with fever, **seek emergency medical attention immediately.**"
            ]
        elif "fever" in symptoms_lower or "cough" in symptoms_lower:
            conditions = ["Common Cold (Viral Infection)", "Flu (Influenza)", "Minor Bronchitis"]
            steps = [
                "Isolate, rest, and drink plenty of fluids.",
                "Monitor temperature regularly.",
                "Consult a doctor if breathing is difficult or fever lasts longer than 72 hours."
            ]
        else:
            # General fallback response
            conditions = ["Stress/Fatigue", "Dehydration", "Mild Musculoskeletal Strain"]
            steps = [
                "Monitor symptoms closely.",
                "Ensure adequate rest and hydration.",
                "Contact a primary care physician if symptoms are concerning or rapidly changing."
            ]

        # Return the data formatted as the Pydantic schema expects
        return SymptomCheckResponse(
            probable_conditions=conditions,
            recommended_next_steps=steps
            ).model_dump()
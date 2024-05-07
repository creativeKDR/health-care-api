from transformers import pipeline


class InterpreteQueryService:

    @staticmethod
    def generatePrompt(symptoms, height, weight, bloodPressure, sugarLevel):
        # Load a pre-trained model for text generation
        generator = pipeline("text-generation", model="gpt2")

        # Create a prompt including all the input data
        prompt = f"Symptoms: {symptoms}\nHeight: {height}\nWeight: {weight}\nBlood Pressure: {bloodPressure}\nSugar Level: {sugarLevel}\n"

        # Generate a health assessment and improvement plan suggestion based on the prompt
        generated_text = generator(prompt, max_length=300, num_return_sequences=1)[0]['generated_text']

        return generated_text

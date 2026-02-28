class ComprehensionAgent:
    def __init__(self, initial_mental_model=""):
        self.mental_model = initial_mental_model
        self.history = []

    def ingest_prompt(self, prompt):
        """Ingest a new NL prompt and update the mental model."""
        self.mental_model += "\n\n" + prompt
        self.history.append({"type": "ingest", "content": prompt})
        return "Mental model updated."

    def query(self, question):
        """Query the agent with a question, simulating LLM iteration."""
        response = f"Based on mental model: {self.mental_model[:100]}... Answering: {question}"
        self.history.append({"type": "query", "content": question, "response": response})
        return response

    def get_history(self):
        """Retrieve interaction history."""
        return self.history

# Example usage:
# agent = ComprehensionAgent("Initial rate-limiter comprehension: GDPR-compliant token bucket.")
# agent.ingest_prompt("Add audit logging.")
# print(agent.query("How does logging affect performance?"))
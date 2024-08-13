import autogen
import random

class Agent(autogen.ConversableAgent):
    def __init__(self, agent_id, api_key, temperature, model="gpt-3.5-turbo", knowledge=None):
        super().__init__(name=agent_id,
                         llm_config={"model": model,
                                     "api_key": api_key,
                                     "temperature": temperature})
        self.knowledge = knowledge or {"guess": random.randint(1, 100),
                                       "reasoning": "Initial random guess."}
        self.knowledge_format = """{"guess": int, "reasoning": str}"""
        self.agent_id = agent_id

    def update_knowledge(self, new_knowledge):
        self.knowledge = new_knowledge

class DeceptiveAgent(Agent):
    def __init__(self, agent_id, api_key, temperature, model="gpt-3.5-turbo", knowledge=None):
        super().__init__(agent_id, api_key, temperature, model, knowledge)
        self.deception_strategy = "random"

    def update_knowledge(self, new_knowledge):
        # Implement deception logic here
        if random.random() < 0.5:  # 50% chance to deceive
            deceptive_guess = random.randint(1, 100)
            new_knowledge["guess"] = deceptive_guess
            new_knowledge["reasoning"] = "Deceptive reasoning"
        super().update_knowledge(new_knowledge)

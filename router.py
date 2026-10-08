class AIRouter:
    def __init__(self):
        self.models = [
            {"name": "Model A", "status": "AVAILABLE"},
            {"name": "Model B", "status": "AVAILABLE"},
        ]
        self.current_model = None

    def select_model(self):
        for model in self.models:
            if model["status"] == "AVAILABLE":
                self.current_model = model["name"]
                return self.current_model

        return None

    def failover(self):
        for model in self.models:
            if model["name"] == self.current_model:
                model["status"] = "RATE_LIMITED"
                break

        return self.select_model()


router = AIRouter()
from fastapi import FastAPI
from router import router

app = FastAPI(title="UnifiedAI")


@app.get("/")
async def home():
    return {
        "status": "online",
        "project": "UnifiedAI",
        "message": "AI Router is ready"
    }


@app.get("/router/status")
async def router_status():
    if router.current_model is None:
        router.select_model()

    return {
        "current_model": router.current_model,
        "models": router.models
    }


@app.post("/router/simulate-failure")
async def simulate_failure():
    if router.current_model is None:
        router.select_model()

    previous_model = router.current_model
    next_model = router.failover()

    return {
        "previous_model": previous_model,
        "reason": "SIMULATED_RATE_LIMIT",
        "next_model": next_model,
        "message": (
            "Switched successfully"
            if next_model
            else "No available models"
        )
    }
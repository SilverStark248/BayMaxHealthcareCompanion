from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
import uvicorn

app = FastAPI()

# Data models
class UserInput(BaseModel):
    text: str

class MedicineQuery(BaseModel):
    symptoms: str

# Fake Data Detection (Basic Implementation)
def is_fake_data(data: str) -> bool:
    fake_keywords = ["fake", "scam", "unverified"]
    return any(word in data.lower() for word in fake_keywords)

# Talking Camera Feature (Dummy Implementation)
@app.post("/talking-camera/")
async def talking_camera(image: UploadFile = File(...)):
    return {"message": "Processing image for accessibility..."}

# AI-Driven Wellness Tips
@app.post("/wellness-tips/")
def wellness_tips(input: UserInput):
    return {"tip": "Drink plenty of water and practice deep breathing."}

# PCOD Assistant Chatbot
@app.post("/pcod-assistant/")
def pcod_assistant(input: UserInput):
    return {"response": "It's recommended to maintain a balanced diet and exercise regularly."}

# Prescription Assistant
@app.post("/prescription-assistant/")
def prescription_assistant(query: MedicineQuery):
    if is_fake_data(query.symptoms):
        return {"error": "Unreliable medical data detected."}
    return {"medicine": "Paracetamol for mild fever"}

# Emotional Support Diary
@app.post("/emotional-diary/")
def emotional_diary(input: UserInput):
    return {"response": "It's okay to feel overwhelmed. Take it one step at a time."}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

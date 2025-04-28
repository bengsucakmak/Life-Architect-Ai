# agent.py

from iointel import Agent
from config import API_KEY, BASE_URL, MODEL_NAME

def create_rehber_agent():
    agent = Agent(
        name="Evrensel Rehber AI",
        instructions=(
            "Sen Evrensel Rehber AI'sın. "
            "Kullanıcıya kişisel gelişim, duygusal destek, zihinsel egzersizler ve hayat hedefleri için adım adım rehberlik yapıyorsun. "
            "Kullanıcının ruh haline ve hedeflerine göre esnek, motive edici, sıcak ve kişiselleştirilmiş bir destek sunuyorsun."
        ),
        model=MODEL_NAME,
        api_key=API_KEY,
        base_url=BASE_URL
    )
    return agent

# tasks.py

from iointel import Workflow
from agent import create_rehber_agent

def generate_tasks(user_goal, user_mood, multiplier=1):
    agent = create_rehber_agent()

    text = (
        f"Kullanıcının ana hedefi: {user_goal}\n"
        f"Kullanıcının şu anki ruh hali: {user_mood}\n\n"
        "Bu bilgiler ışığında aşağıdaki görevleri oluştur:\n"
        f"- {2 * multiplier} Kolay görev\n"
        f"- {2 * multiplier} Orta seviye görev\n"
        f"- {1 * multiplier} Zor görev\n"
        "- Haftalık değerlendirme soruları\n"
        "- Bir motivasyon mesajı\n"
        "- Bir bilişsel gelişim egzersizi önerisi\n"
    )

    workflow = Workflow(text=text, client_mode=False)
    results = workflow.custom(
        name="evrensel-rehber-tasks",
        objective="Kullanıcıya görevler ve plan oluştur",
        instructions="Kullanıcının hedeflerine ve ruh haline göre Kolay, Orta, Zor seviye görevler öner. Ayrıca haftalık soru, motivasyon mesajı ve bilişsel egzersiz de oluştur.",
        agents=[agent],
    ).run_tasks()

    return results

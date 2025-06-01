import json

DATA_FILE = "users.json"

try:
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        data = file.read().strip()
        users = json.loads(data) if data else {}
        print("✅ JSON خوانده شد بدون مشکل:", users)
except json.JSONDecodeError as e:
    print("❌ خطای JSONDecodeError:", e)

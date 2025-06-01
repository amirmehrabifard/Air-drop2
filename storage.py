
import json

DATA_FILE = "users.json"

def load_users():
    """ خواندن اطلاعات کاربران از فایل JSON و مدیریت خطاهای احتمالی. """
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            data = file.read().strip()
            return json.loads(data) if data else {}  # بررسی فایل خالی
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_users(users):
    """ ذخیره اطلاعات کاربران در فایل JSON به‌صورت فرمت‌شده. """
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(users, file, indent=4)

def register_user(user_id, username):
    """ ثبت کاربر جدید در سیستم و اختصاص ۵۰۰ توکن اولیه. """
    users = load_users()
    if str(user_id) not in users:
        users[str(user_id)] = {
            "username": username,
            "invites": 0,
            "tokens_received": 500,
            "invited_users": []
        }
        save_users(users)
        return True
    return False

def record_invite(inviter_id, invited_id):
    """ ثبت دعوت معتبر و افزودن ۱۰۰ توکن به حساب دعوت‌کننده. """
    users = load_users()
    if str(inviter_id) in users and str(invited_id) not in users[str(inviter_id)]["invited_users"]:
        users[str(inviter_id)]["invited_users"].append(str(invited_id))
        users[str(inviter_id)]["invites"] += 1
        users[str(inviter_id)]["tokens_received"] += 100
        save_users(users)
        return True
    return False

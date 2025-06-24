
from flask import Flask, request, jsonify
import requests

# Настройки Telegram бота
BOT_TOKEN = "7799990130:AAEvIsiRpa9zsXHyDHHn98Uu1tA-PGVPO-I"
ADMIN_CHAT_ID = "7643715505"

app = Flask(__name__)

@app.route("/book", methods=["POST"])
def handle_booking():
    data = request.json

    name = data.get("name")
    phone = data.get("phone")
    adults = data.get("adults")
    children = data.get("children")
    date = data.get("date")
    time = data.get("time")
    ticket_type = data.get("ticket_type")
    comments = data.get("comments", "")

    message = (
        f"📩 Новое бронирование:\n"
        f"👤 Имя: {name}\n📞 Телефон: {phone}\n"
        f"👪 Взрослые: {adults}, Дети: {children}\n"
        f"📅 Дата: {date}, 🕒 Время: {time}\n"
        f"🎟 Тип билета: {ticket_type}\n"
        f"✏ Комментарий: {comments}"
    )

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    response = requests.post(url, json={"chat_id": ADMIN_CHAT_ID, "text": message})

    return jsonify({"ok": True})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

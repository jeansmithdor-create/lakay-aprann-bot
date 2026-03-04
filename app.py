"""
LakayAprann — WhatsApp Chatbot Backend (Flask + Twilio)
E-learning platform in Haitian Creole.
"""

import os
import random
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

# ---------------------------------------------------------------------------
# Course data
# ---------------------------------------------------------------------------

LESSONS = [
    {
        "title": "Leson 1: Ki sa yon telefòn entelijan ye?",
        "teaching": (
            "Yon telefòn entelijan (smartphone) se yon telefòn ki ka fè anpil bagay — "
            "pa sèlman rele ak voye mesaj. Li tankou yon ti òdinatè nan men ou!\n\n"
            "Diferans ak yon telefòn nòmal:\n"
            "• Yon telefòn nòmal ka rele ak voye SMS sèlman.\n"
            "• Yon telefòn entelijan ka ale sou entènèt, pran foto, jwe mizik, "
            "gade videyo, epi itilize aplikasyon (app).\n\n"
            "Pati prensipal yon telefòn entelijan:\n"
            "📱 Ekran — kote ou touche pou kontwole telefòn nan\n"
            "📷 Kamera — pou pran foto ak videyo\n"
            "🔘 Bouton — pou limen/etenn ak monte volim"
        ),
        "quiz": (
            "❓ QUIZ — Leson 1\n\n"
            "Ki sa ki fè yon telefòn 'entelijan'?\n\n"
            "A) Li ka rele sèlman\n"
            "B) Li ka fè anpil bagay tankou yon ti òdinatè\n"
            "C) Li pi gwo pase yon telefòn nòmal"
        ),
        "correct": "b",
        "explanations": {
            "correct": "✅ Kòrèk! Yon telefòn entelijan ka fè anpil bagay tankou yon ti òdinatè — rele, voye mesaj, ale sou entènèt, pran foto, ak plis ankò!",
            "wrong": "❌ Sa pa kòrèk. Yon telefòn entelijan ka fè anpil bagay tankou yon ti òdinatè — se sa ki fè l \"entelijan\".\n\nEseye ankò! 👇\n\nKi sa ki fè yon telefòn 'entelijan'?\nA) Li ka rele sèlman\nB) Li ka fè anpil bagay tankou yon ti òdinatè\nC) Li pi gwo pase yon telefòn nòmal"
        }
    },
    {
        "title": "Leson 2: Ekran Dakèy",
        "teaching": (
            "Ekran dakèy (Home Screen) se premye paj ou wè lè ou limen telefòn ou. "
            "Se la tout ti ikòn yo ye — chak ikòn se yon aplikasyon (app).\n\n"
            "Kisa yon app ye?\n"
            "Yon app se yon ti pwogram ki fè yon bagay espesyal. Pa egzanp:\n"
            "📞 App Telefòn — pou rele moun\n"
            "💬 WhatsApp — pou voye mesaj gratis\n"
            "📷 Kamera — pou pran foto\n\n"
            "Kijan pou itilize ekran dakèy la:\n"
            "👆 Tape sou yon ikòn pou ouvri yon app\n"
            "👈 Glise dwat-goch pou wè plis app\n"
            "🔼 Glise anba-anwo pou wè notifikasyon yo"
        ),
        "quiz": (
            "❓ QUIZ — Leson 2\n\n"
            "Kisa yon 'app' ye?\n\n"
            "A) Yon ti pwogram sou telefòn ou\n"
            "B) Yon kalite telefòn\n"
            "C) Yon paj wèb"
        ),
        "correct": "a",
        "explanations": {
            "correct": "✅ Kòrèk! Yon app se yon ti pwogram sou telefòn ou ki fè yon bagay espesyal — tankou WhatsApp, Kamera, oswa YouTube.",
            "wrong": "❌ Sa pa kòrèk. Yon app se yon ti pwogram sou telefòn ou ki fè yon bagay espesyal.\n\nEseye ankò! 👇\n\nKisa yon 'app' ye?\nA) Yon ti pwogram sou telefòn ou\nB) Yon kalite telefòn\nC) Yon paj wèb"
        }
    },
    {
        "title": "Leson 3: Wi-Fi ak Entènèt",
        "teaching": (
            "Wi-Fi se yon fason pou konekte telefòn ou ak entènèt san peye done mobil. "
            "Anpil kote gen Wi-Fi gratis — tankou restoran, legliz, ak biwo.\n\n"
            "Diferans ant Wi-Fi ak Done Mobil:\n"
            "📶 Wi-Fi — gratis (nan kote ki gen Wi-Fi), pi rapid\n"
            "📱 Done Mobil — ou peye opèratè ou (Digicel, Natcom), mache tout kote\n\n"
            "Kijan pou konekte sou Wi-Fi:\n"
            "1. Ale nan Paramèt (Settings)\n"
            "2. Tape sou \"Wi-Fi\"\n"
            "3. Chwazi non rezo a\n"
            "4. Antre modpas la (si genyen)\n\n"
            "💡 Konsèy: Lè ou ka itilize Wi-Fi, itilize l! Sa ap ekonomize lajan done ou."
        ),
        "quiz": (
            "❓ QUIZ — Leson 3\n\n"
            "Kilès ki pi bon pou ekonomize lajan?\n\n"
            "A) Itilize done mobil tout tan\n"
            "B) Konekte sou Wi-Fi lè ou ka\n"
            "C) Pa itilize entènèt ditou"
        ),
        "correct": "b",
        "explanations": {
            "correct": "✅ Kòrèk! Wi-Fi se yon bon fason pou ekonomize lajan paske ou pa bezwen peye done mobil lè ou konekte sou Wi-Fi.",
            "wrong": "❌ Sa pa kòrèk. Pi bon fason pou ekonomize lajan se konekte sou Wi-Fi lè ou kapab — konsa ou pa bezwen itilize done mobil ou.\n\nEseye ankò! 👇\n\nKilès ki pi bon pou ekonomize lajan?\nA) Itilize done mobil tout tan\nB) Konekte sou Wi-Fi lè ou ka\nC) Pa itilize entènèt ditou"
        }
    },
    {
        "title": "Leson 4: WhatsApp — Mesaj ak Apèl",
        "teaching": (
            "WhatsApp se aplikasyon mesaj ki pi popilè ann Ayiti. Avèk WhatsApp, ou ka:\n\n"
            "💬 Voye mesaj tèks — ekri bay nenpòt moun ki gen WhatsApp\n"
            "📷 Voye foto ak videyo — pataje moman espesyal yo\n"
            "🎤 Voye mesaj vwa — pale olye ou ekri\n"
            "📞 Rele gratis — fè apèl vwa oswa videyo san peye!\n\n"
            "Enpòtan: Tout bagay sa yo GRATIS — ou bezwen sèlman entènèt (Wi-Fi oswa done mobil).\n\n"
            "Kijan pou voye yon mesaj:\n"
            "1. Ouvri WhatsApp\n"
            "2. Tape sou non moun nan\n"
            "3. Ekri mesaj ou a anba\n"
            "4. Tape sou flèch vèt la pou voye"
        ),
        "quiz": (
            "❓ QUIZ — Leson 4\n\n"
            "Èske ou ka rele yon moun gratis ak WhatsApp?\n\n"
            "A) Wi, si ou gen entènèt\n"
            "B) Non, li toujou koute lajan\n"
            "C) Sèlman si ou nan menm peyi a"
        ),
        "correct": "a",
        "explanations": {
            "correct": "✅ Kòrèk! Wi, ou ka rele nenpòt moun gratis ak WhatsApp — ou bezwen sèlman yon koneksyon entènèt (Wi-Fi oswa done mobil).",
            "wrong": "❌ Sa pa kòrèk. Ak WhatsApp, ou ka rele nenpòt moun gratis — tout sa ou bezwen se yon koneksyon entènèt.\n\nEseye ankò! 👇\n\nÈske ou ka rele yon moun gratis ak WhatsApp?\nA) Wi, si ou gen entènèt\nB) Non, li toujou koute lajan\nC) Sèlman si ou nan menm peyi a"
        }
    },
    {
        "title": "Leson 5: Sekirite Telefòn Ou",
        "teaching": (
            "Telefòn ou gen anpil enfòmasyon enpòtan — foto, mesaj, nimewo kontak. "
            "Ou dwe pwoteje l!\n\n"
            "🔒 Mete yon kòd PIN oswa modpas:\n"
            "• Ale nan Paramèt → Sekirite → Vewou Ekran\n"
            "• Chwazi yon kòd 4-6 chif ke ou ka sonje\n"
            "• PA pataje kòd ou ak pèsonn!\n\n"
            "⚠️ Atansyon ak mesaj sispèk:\n"
            "• Si yon moun ou pa konnen voye ou yon lyen (link), PA klike sou li\n"
            "• Si yon mesaj di ou genyen yon pri oswa lajan, se pwobableman yon anak\n"
            "• Pa janm bay modpas ou oswa enfòmasyon pèsonèl ou nan mesaj\n\n"
            "💡 Konsèy: Toujou mete telefòn ou nan yon kote ki an sekirite. "
            "Pa kite l sou tab nan piblik."
        ),
        "quiz": (
            "❓ QUIZ — Leson 5\n\n"
            "Ki sa ou ta dwe fè si yon moun ou pa konnen voye ou yon lyen?\n\n"
            "A) Klike sou li touswit\n"
            "B) Pa klike, efase mesaj la\n"
            "C) Voye l bay tout zanmi ou"
        ),
        "correct": "b",
        "explanations": {
            "correct": "✅ Kòrèk! Pa janm klike sou lyen ki soti nan moun ou pa konnen. Efase mesaj la pou pwoteje tèt ou!",
            "wrong": "❌ Sa pa kòrèk. Si yon moun ou pa konnen voye ou yon lyen, pa klike sou li — efase mesaj la pou pwoteje tèt ou.\n\nEseye ankò! 👇\n\nKi sa ou ta dwe fè si yon moun ou pa konnen voye ou yon lyen?\nA) Klike sou li touswit\nB) Pa klike, efase mesaj la\nC) Voye l bay tout zanmi ou"
        }
    }
]

TIPS = [
    "💡 Konsèy jodi a:\n\nFèmen aplikasyon ou pa itilize yo — sa ap fè telefòn ou mache pi vit epi ekonomize batri!",
    "💡 Konsèy jodi a:\n\nToujou konekte sou Wi-Fi lè ou ka — sa ap ekonomize lajan done mobil ou!",
    "💡 Konsèy jodi a:\n\nPran yon foto bon kalite de pwodwi ou yo pou vann sou WhatsApp. Yon bon foto atire plis kliyan!",
    "💡 Konsèy jodi a:\n\nKreye yon gwoup WhatsApp pou kliyan ou yo — voye pwomosyon ak nouvo pwodwi chak semèn!",
    "💡 Konsèy jodi a:\n\nToujou mete telefòn ou ajou (update) — sa pwoteje l kont viris ak pwoblèm sekirite!",
    "💡 Konsèy jodi a:\n\nItilize WhatsApp Business pou biznis ou — li gen fonksyon espesyal tankou katalòg pwodwi ak repons otomatik!"
]

WELCOME_MSG = (
    "Byenveni nan LakayAprann! 📚\n\n"
    "Aprann, Grandi, Reyisi — nan lang ou.\n\n"
    "Chwazi sa ou vle fè:\n"
    "1️⃣ Kòmanse kou gratis — \"Baz Telefòn Entelijan\"\n"
    "2️⃣ Wè tout kou yo\n"
    "3️⃣ Konsèy pou jodi a\n"
    "4️⃣ Kontakte nou"
)

COURSES_MSG = (
    "📚 Tout Kou LakayAprann yo:\n\n"
    "KONPETANS NIMERIK:\n"
    "✅ Baz Telefòn Entelijan (GRATIS)\n"
    "🔒 Rezo Sosyal pou Biznis (150 HTG/mwa)\n"
    "🔒 Kreye Kontni (Foto/Videyo) (150 HTG/mwa)\n\n"
    "ANTREPRENARYA:\n"
    "🔒 Lanse Ti Komès Ou (150 HTG/mwa)\n"
    "🔒 Kontabilite Debaz (150 HTG/mwa)\n\n"
    "LANG:\n"
    "🔒 Anglè pou Biznis (500 HTG/mwa)\n\n"
    "Tape 1 pou kòmanse kou gratis la!"
)

CONTACT_MSG = (
    "📞 Kontakte LakayAprann:\n\n"
    "WhatsApp: +509 XXXX XXXX\n"
    "Email: info@lakayaprann.com\n"
    "Facebook: @LakayAprann\n\n"
    "Tape \"menu\" pou retounen."
)

COMPLETION_MSG = (
    "🎉 Felisitasyon! Ou fini kou \"Baz Telefòn Entelijan\" la!\n\n"
    "Ou aprann:\n"
    "✅ Kisa yon telefòn entelijan ye\n"
    "✅ Kijan pou itilize ekran dakèy la\n"
    "✅ Kijan pou konekte sou Wi-Fi\n"
    "✅ Kijan pou itilize WhatsApp\n"
    "✅ Kijan pou pwoteje telefòn ou\n\n"
    "📜 Sètifika ou prè! Ou ka resevwa l pou 300 HTG.\n\n"
    "Tape \"menu\" pou retounen nan meni prensipal la."
)

UNKNOWN_MSG = (
    "Mwen pa konprann sa ou ekri a. 🤔\n"
    "Tape \"menu\" pou wè opsyon yo."
)

# ---------------------------------------------------------------------------
# User state management
# ---------------------------------------------------------------------------

# States: "menu", "lesson_N" (showing lesson teaching), "quiz_N" (waiting for quiz answer)
user_states: dict = {}


def get_state(user_id: str) -> dict:
    if user_id not in user_states:
        user_states[user_id] = {"state": "new", "tip_index": 0}
    return user_states[user_id]


def process_message(user_id: str, text: str) -> str:
    """Core chatbot logic. Returns the reply string."""
    text = text.strip().lower()
    state = get_state(user_id)

    # --- Menu / reset ---
    if text in ("menu", "meni", "start", "hi", "hello", "bonjou", "salut") or state["state"] == "new":
        state["state"] = "menu"
        return WELCOME_MSG

    # --- At menu level ---
    if state["state"] == "menu":
        if text == "1":
            # Start course — show lesson 1
            state["state"] = "lesson_1"
            lesson = LESSONS[0]
            return f"📖 {lesson['title']}\n\n{lesson['teaching']}\n\n{'─' * 30}\n\n{lesson['quiz']}"
        elif text == "2":
            return COURSES_MSG
        elif text == "3":
            tip = TIPS[state["tip_index"] % len(TIPS)]
            state["tip_index"] += 1
            return tip + "\n\nTape \"menu\" pou retounen."
        elif text == "4":
            return CONTACT_MSG
        else:
            return UNKNOWN_MSG

    # --- In a lesson (showing teaching + quiz, waiting for quiz answer) ---
    current = state["state"]

    if current.startswith("lesson_"):
        lesson_num = int(current.split("_")[1])
        lesson_idx = lesson_num - 1
        lesson = LESSONS[lesson_idx]

        # User is answering the quiz
        answer = text.strip().lower()
        if answer in ("a", "b", "c"):
            if answer == lesson["correct"]:
                # Correct answer
                reply = lesson["explanations"]["correct"]
                if lesson_num < 5:
                    # Move to next lesson
                    next_num = lesson_num + 1
                    state["state"] = f"lesson_{next_num}"
                    next_lesson = LESSONS[next_num - 1]
                    reply += (
                        f"\n\n{'─' * 30}\n\n"
                        f"📖 {next_lesson['title']}\n\n"
                        f"{next_lesson['teaching']}\n\n"
                        f"{'─' * 30}\n\n"
                        f"{next_lesson['quiz']}"
                    )
                else:
                    # Course completed
                    state["state"] = "menu"
                    reply += f"\n\n{'─' * 30}\n\n{COMPLETION_MSG}"
                return reply
            else:
                # Wrong answer — retry
                return lesson["explanations"]["wrong"]
        else:
            return "Tanpri reponn ak A, B, oswa C.\n\n" + lesson["quiz"]

    # Fallback
    return UNKNOWN_MSG


# ---------------------------------------------------------------------------
# Twilio WhatsApp webhook
# ---------------------------------------------------------------------------

@app.route("/webhook", methods=["POST"])
def twilio_webhook():
    """Handle incoming WhatsApp messages via Twilio."""
    from twilio.twiml.messaging_response import MessagingResponse

    incoming_msg = request.values.get("Body", "").strip()
    sender = request.values.get("From", "unknown")

    reply_text = process_message(sender, incoming_msg)

    resp = MessagingResponse()
    resp.message(reply_text)
    return str(resp), 200, {"Content-Type": "application/xml"}


# ---------------------------------------------------------------------------
# Web simulator API endpoint
# ---------------------------------------------------------------------------

@app.route("/api/chat", methods=["POST"])
def web_chat():
    """Handle messages from the web simulator."""
    data = request.get_json(force=True)
    message = data.get("message", "").strip()
    user_id = data.get("user_id", "web_default")

    reply_text = process_message(user_id, message)

    return jsonify({"reply": reply_text})


# ---------------------------------------------------------------------------
# Health check
# ---------------------------------------------------------------------------

@app.route("/", methods=["GET"])
def index():
    return jsonify({
        "status": "ok",
        "app": "LakayAprann Chatbot",
        "version": "1.0.0"
    })


# ---------------------------------------------------------------------------
# Run
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port, debug=True)

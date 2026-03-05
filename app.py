"""
LakayAprann — WhatsApp Chatbot Backend (Flask + Twilio)
E-learning platform in Haitian Creole — 6 courses supported.
"""

import os
import random
import time
import uuid
import base64
import json
import requests as http_requests
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

# ---------------------------------------------------------------------------
# MonCash Configuration
# ---------------------------------------------------------------------------

MONCASH_CLIENT_ID = os.environ.get("MONCASH_CLIENT_ID", "")
MONCASH_CLIENT_SECRET = os.environ.get("MONCASH_CLIENT_SECRET", "")
MONCASH_MODE = os.environ.get("MONCASH_MODE", "sandbox")  # "sandbox" or "live"

if MONCASH_MODE == "live":
    MONCASH_API_BASE = "https://moncashbutton.digicelgroup.com/Api"
    MONCASH_GATEWAY = "https://moncashbutton.digicelgroup.com/Moncash-middleware"
else:
    MONCASH_API_BASE = "https://sandbox.moncashbutton.digicelgroup.com/Api"
    MONCASH_GATEWAY = "https://sandbox.moncashbutton.digicelgroup.com/Moncash-middleware"

# Course pricing (HTG). Course 1 is free.
COURSE_PRICES = {
    1: 0,     # Baz Telefòn Entelijan — GRATIS
    2: 150,   # Rezo Sosyal pou Biznis
    3: 150,   # Lanse Ti Komès Ou
    4: 150,   # Kontabilite Debaz
    5: 500,   # Anglè pou Biznis
    6: 150,   # Entèlijan Atifisyèl
}

# In-memory payment records: order_id -> {user_id, course_num, status, ...}
payment_records: dict = {}


def moncash_get_token() -> str:
    """Get a MonCash OAuth bearer token."""
    if not MONCASH_CLIENT_ID or not MONCASH_CLIENT_SECRET:
        return ""
    creds = base64.b64encode(f"{MONCASH_CLIENT_ID}:{MONCASH_CLIENT_SECRET}".encode()).decode()
    resp = http_requests.post(
        f"{MONCASH_API_BASE}/oauth/token",
        headers={"Accept": "application/json", "Authorization": f"Basic {creds}"},
        data={"scope": "read,write", "grant_type": "client_credentials"},
        timeout=15,
    )
    if resp.status_code == 200:
        return resp.json().get("access_token", "")
    return ""


def moncash_create_payment(order_id: str, amount: float) -> str:
    """Create a MonCash payment and return the redirect URL (or empty string on failure)."""
    token = moncash_get_token()
    if not token:
        return ""
    resp = http_requests.post(
        f"{MONCASH_API_BASE}/v1/CreatePayment",
        headers={
            "Accept": "application/json",
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        },
        json={"amount": amount, "orderId": order_id},
        timeout=15,
    )
    if resp.status_code in (200, 202):
        data = resp.json()
        payment_token = data.get("payment_token", {}).get("token", "")
        if payment_token:
            return f"{MONCASH_GATEWAY}/Payment/Redirect?token={payment_token}"
    return ""


def moncash_verify_payment(order_id: str) -> bool:
    """Check if a MonCash payment was completed successfully."""
    token = moncash_get_token()
    if not token:
        return False
    resp = http_requests.post(
        f"{MONCASH_API_BASE}/v1/RetrieveOrderPayment",
        headers={
            "Accept": "application/json",
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        },
        json={"orderId": order_id},
        timeout=15,
    )
    if resp.status_code == 200:
        data = resp.json()
        msg = data.get("payment", {}).get("message", "")
        return msg.lower() == "successful"
    return False

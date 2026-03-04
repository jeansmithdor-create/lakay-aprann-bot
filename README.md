# LakayAprann — Chatbot WhatsApp

Chatbot éducatif en créole haïtien via WhatsApp. Cours "Baz Telefòn Entelijan" (5 leçons avec quiz).

## Déploiement sur Render (Gratuit)

### Étape 1 : Créer un compte Render
1. Aller sur [render.com](https://render.com) et créer un compte gratuit (avec GitHub)

### Étape 2 : Préparer le code sur GitHub
1. Créer un nouveau repository sur [github.com/new](https://github.com/new)
2. Nom: `lakay-aprann-bot`
3. Uploader tous les fichiers de ce dossier (sauf `.env`)

### Étape 3 : Déployer sur Render
1. Sur Render → "New" → "Web Service"
2. Connecter votre repo GitHub
3. Paramètres:
   - **Name**: `lakay-aprann-bot`
   - **Runtime**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app --bind 0.0.0.0:$PORT`
   - **Plan**: Free

4. Ajouter les **Variables d'environnement** :
   - `TWILIO_ACCOUNT_SID` = votre Account SID
   - `TWILIO_AUTH_TOKEN` = votre Auth Token

5. Cliquer "Create Web Service"

Render vous donnera une URL comme: `https://lakay-aprann-bot.onrender.com`

### Étape 4 : Configurer Twilio WhatsApp Sandbox
1. Aller sur [console.twilio.com](https://console.twilio.com)
2. Menu: **Messaging** → **Try it Out** → **Send a WhatsApp message**
3. Activer le Sandbox et noter le code (ex: "join example-word")
4. Dans **Sandbox Configuration**:
   - **WHEN A MESSAGE COMES IN**: `https://lakay-aprann-bot.onrender.com/webhook`
   - **Method**: POST
5. Sauvegarder

### Étape 5 : Tester
1. Sur votre téléphone, ouvrir WhatsApp
2. Envoyer le message code (ex: "join example-word") au numéro Twilio Sandbox
3. Envoyer "bonjou" — le chatbot doit répondre!

## Structure
- `app.py` — Backend Flask (webhook Twilio + API web)
- `index.html` — Simulateur WhatsApp web
- `requirements.txt` — Dépendances Python
- `Procfile` — Configuration Gunicorn pour Render
- `runtime.txt` — Version Python
- `.env.example` — Template des variables d'environnement

## API Endpoints
- `GET /` — Health check
- `POST /webhook` — Webhook Twilio (WhatsApp)
- `POST /api/chat` — API pour le simulateur web

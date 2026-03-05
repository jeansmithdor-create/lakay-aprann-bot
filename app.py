"""
LakayAprann — WhatsApp Chatbot Backend (Flask + Twilio)
E-learning platform in Haitian Creole — 6 courses supported.
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
# Course 1: Baz Telefòn Entelijan (5 lessons — FREE)
# ---------------------------------------------------------------------------

BAZ_TELEFON_LESSONS = [
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
            "📱 Done Mobil — ou peye operatè ou (Digicel, Natcom), mache tout kote\n\n"
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

# ---------------------------------------------------------------------------
# Course 2: Rezo Sosyal pou Biznis (8 lessons)
# ---------------------------------------------------------------------------

REZO_SOSYAL_LESSONS = [
    {
        "title": "Leson 1: Kisa rezo sosyal yo ye?",
        "teaching": (
            "📱 REZO SOSYAL POU BIZNIS — Leson 1\n\n"
            "Rezo sosyal yo se aplikasyon sou telefòn ou ka itilize pou pale ak moun, "
            "pataje foto ak video, epi VANN pwodwi ou! 🛍️\n\n"
            "Prensipal rezo sosyal yo:\n"
            "👉 Facebook — Pi popilè ann Ayiti. Bon pou vann ak fè piblisite.\n"
            "👉 Instagram — Bon pou foto bèl. Atire jenn achte.\n"
            "👉 TikTok — Video kout. Anpil moun ka wè biznis ou gratis.\n"
            "👉 WhatsApp — Kominikasyon dirèk ak kliyan. 85% Ayisyen itilize li.\n\n"
            "💡 Tip: Ou pa bezwen itilize tout yo ansanm. Kòmanse ak youn oswa de!"
        ),
        "quiz": (
            "❓ QUIZ — Leson 1\n\n"
            "Ki rezo sosyal ki pi itilize ann Ayiti pou pale ak kliyan dirèkteman?\n\n"
            "A) Instagram\n"
            "B) WhatsApp\n"
            "C) TikTok"
        ),
        "correct": "b",
        "explanations": {
            "correct": (
                "✅ Kòrèk! WhatsApp se rezo sosyal ki pi itilize ann Ayiti — "
                "prèske 85% moun gen li sou telefòn yo. "
                "Se zouti pafè pou pale ak kliyan epi reponn kesyon yo rapid! 🎉"
            ),
            "wrong": (
                "❌ Sa pa kòrèk. WhatsApp se rezo sosyal ki pi itilize ann Ayiti — "
                "prèske 85% moun gen li sou telefòn yo. "
                "Se zouti pafè pou pale ak kliyan dirèkteman!\n\n"
                "Eseye ankò! 👇\n\n"
                "Ki rezo sosyal ki pi itilize ann Ayiti pou pale ak kliyan dirèkteman?\n"
                "A) Instagram\n"
                "B) WhatsApp\n"
                "C) TikTok"
            )
        }
    },
    {
        "title": "Leson 2: Kreye yon paj Facebook pou biznis ou",
        "teaching": (
            "📘 REZO SOSYAL POU BIZNIS — Leson 2\n\n"
            "Paj Facebook biznis ou se boutik ou sou entènèt! "
            "Li diferan de pwofil pèsonèl ou — li ba ou zouti espesyal pou vann. 🏪\n\n"
            "Kijan pou kreye paj ou:\n"
            "1️⃣ Ouvè Facebook, klike sou 'Pages' oswa 'Paj'\n"
            "2️⃣ Chwazi yon non klè — ex: 'Boutik Roselène - Pòtoprens'\n"
            "3️⃣ Mete foto pwofil (logo ou, oswa foto ou souri 😊)\n"
            "4️⃣ Ekri deskripsyon biznis ou — ki sa ou vann, ki kote ou ye\n"
            "5️⃣ Ajoute nimewo WhatsApp ou pou kliyan ka kontakte ou fasil\n\n"
            "💡 Tip: Yon paj konplè ak foto pwofesyonèl atire 3x plis kliyan!"
        ),
        "quiz": (
            "❓ QUIZ — Leson 2\n\n"
            "Ki sa ou dwe mete sou paj Facebook biznis ou pou kliyan ka kontakte ou fasil?\n\n"
            "A) Foto fanmi ou\n"
            "B) Nimewo WhatsApp ou\n"
            "C) Non zanmi ou"
        ),
        "correct": "b",
        "explanations": {
            "correct": (
                "✅ Kòrèk! Toujou mete nimewo WhatsApp ou sou paj Facebook biznis ou. "
                "Konsa kliyan ka kontakte ou dirèkteman pou kòmande — "
                "sa fè vant ou ogmante! 📈"
            ),
            "wrong": (
                "❌ Sa pa kòrèk. Sou paj Facebook biznis ou, "
                "bagay ki pi enpòtan pou mete se nimewo WhatsApp ou — "
                "pa foto fanmi oswa non zanmi. "
                "Kliyan bezwen yon mwayen fasil pou kontakte ou!\n\n"
                "Eseye ankò! 👇\n\n"
                "Ki sa ou dwe mete sou paj Facebook biznis ou pou kliyan ka kontakte ou fasil?\n"
                "A) Foto fanmi ou\n"
                "B) Nimewo WhatsApp ou\n"
                "C) Non zanmi ou"
            )
        }
    },
    {
        "title": "Leson 3: Kijan pou pran bon foto pou pwodwi ou",
        "teaching": (
            "📸 REZO SOSYAL POU BIZNIS — Leson 3\n\n"
            "Yon bon foto = plis vant! Kliyan achte ak je yo anvan pye yo. "
            "Ou pa bezwen kamera chè — telefòn ou sifi! 📱\n\n"
            "5 règ pou pran bèl foto pwodwi:\n"
            "☀️ 1. Itilize limyè solèy — deyò oswa bò fenèt. Evite flaş.\n"
            "🎨 2. Mete yon fon pwòp — dra blan, mur blan, oswa tablo katon.\n"
            "📐 3. Pran foto anwo (bird's eye) pou manje ak bijou.\n"
            "🔍 4. Pran foto kote pwodwi la ranpli kadra a — pa twò lwen.\n"
            "✨ 5. Pran plizyè foto, chwazi pi bon an.\n\n"
            "💡 Tip: Lave men ou ak netwaye pwodwi a anvan foto — détay konte!"
        ),
        "quiz": (
            "❓ QUIZ — Leson 3\n\n"
            "Ki kalite limyè ki pi bon pou pran foto pwodwi pou vann sou rezo sosyal?\n\n"
            "A) Limyè flaş telefòn nan\n"
            "B) Limyè solèy natirèl\n"
            "C) Limyè anbyan nwit"
        ),
        "correct": "b",
        "explanations": {
            "correct": (
                "✅ Kòrèk! Limyè solèy natirèl se pi bon pou foto pwodwi. "
                "Li fè koulè yo parèt reyèl epi foto a klè san ombre. "
                "Mete ou bò fenèt oswa deyò nan maten — epi ou pral wè diferans lan! 🌟"
            ),
            "wrong": (
                "❌ Sa pa kòrèk. Limyè solèy natirèl se pi bon chwa! "
                "Flaş telefòn fè foto parèt plat ak ombre lèd. "
                "Limyè nwit rann foto flou ak jòn.\n\n"
                "Eseye ankò! 👇\n\n"
                "Ki kalite limyè ki pi bon pou pran foto pwodwi pou vann sou rezo sosyal?\n"
                "A) Limyè flaş telefòn nan\n"
                "B) Limyè solèy natirèl\n"
                "C) Limyè anbyan nwit"
            )
        }
    },
    {
        "title": "Leson 4: Ekri bon deskripsyon pou vann",
        "teaching": (
            "✍️ REZO SOSYAL POU BIZNIS — Leson 4\n\n"
            "Yon bon deskripsyon se diferans ant 'wè' ak 'achte'. "
            "Foto atire je, mo yo fèmen vant la! 💰\n\n"
            "Fòmil deskripsyon ki vann:\n"
            "1️⃣ Kòmanse ak avantaj — pa sèlman deskripsyon\n"
            "   Ex: '🍗 Poul fri kwit fre chak jou!' (pa: 'Nou vann poul fri')\n"
            "2️⃣ Mete pri a klè — kliyan pa renmen mande\n"
            "   Ex: '250 HTG — livrezon disponib Pòtoprens 🛵'\n"
            "3️⃣ Ajoute yon apèl aksyon\n"
            "   Ex: 'Voye mesaj WhatsApp pou kòmande: 509-XXXX-XXXX 📲'\n"
            "4️⃣ Itilize emoji pou fè tèks la vivan\n\n"
            "💡 Tip: Toujou reponn kòmantè rapidman — vitès = konfyans = vant!"
        ),
        "quiz": (
            "❓ QUIZ — Leson 4\n\n"
            "Ki sa ki pi enpòtan pou mete nan yon deskripsyon pwodwi sou Facebook?\n\n"
            "A) Non ak adrès konplè fanmi ou\n"
            "B) Pri a ak kijan pou kontakte ou\n"
            "C) Istwa lontan sou biznis ou"
        ),
        "correct": "b",
        "explanations": {
            "correct": (
                "✅ Kòrèk! Pri a ak kijan pou kontakte ou se de bagay ki pi enpòtan. "
                "Kliyan vle konnen: 'Konbyen li koute?' ak 'Kijan pou m achte?' "
                "Reponn de kesyon sa yo nan deskripsyon ou — vant ou ap monte! 🚀"
            ),
            "wrong": (
                "❌ Sa pa kòrèk. Bagay ki pi enpòtan nan yon deskripsyon se pri a "
                "ak kijan kliyan ka kontakte ou pou achte. "
                "Kliyan pa bezwen konnen istwa fanmi ou — yo vle achte vit!\n\n"
                "Eseye ankò! 👇\n\n"
                "Ki sa ki pi enpòtan pou mete nan yon deskripsyon pwodwi sou Facebook?\n"
                "A) Non ak adrès konplè fanmi ou\n"
                "B) Pri a ak kijan pou kontakte ou\n"
                "C) Istwa lontan sou biznis ou"
            )
        }
    },
    {
        "title": "Leson 5: Itilize WhatsApp Business",
        "teaching": (
            "💼 REZO SOSYAL POU BIZNIS — Leson 5\n\n"
            "WhatsApp Business se yon aplikasyon GRATIS ki fèt espesyalman pou ti biznis. "
            "Li diferan de WhatsApp nòmal — li ba ou zouti pou vann! 🛒\n\n"
            "Fonksyon prensipal:\n"
            "📋 Katalòg — Mete foto ak pri tout pwodwi ou. "
            "Kliyan ka wè tout sa ou vann san poze kesyon!\n"
            "🤖 Repons otomatik — Mesaj akèy otomatik lè ou pa disponib.\n"
            "   Ex: 'Bonjou! Nou resevwa mesaj ou. N ap reponn nan 1 è.'\n"
            "🏷️ Etikèt — Òganize kliyan ou: 'Nouvo kliyan', 'Kòmand fèt', 'Pou peye'\n"
            "📊 Estatistik — Wè konbyen mesaj ou voye ak resevwa\n\n"
            "💡 Tip: Telechaje WhatsApp Business gratis sou Play Store oswa App Store!"
        ),
        "quiz": (
            "❓ QUIZ — Leson 5\n\n"
            "Ki fonksyon WhatsApp Business ki pèmèt kliyan wè tout pwodwi ou ak pri yo?\n\n"
            "A) Etikèt (Labels)\n"
            "B) Katalòg (Catalog)\n"
            "C) Estatistik (Statistics)"
        ),
        "correct": "b",
        "explanations": {
            "correct": (
                "✅ Kòrèk! Katalòg la se vitrin dijital ou nan WhatsApp Business. "
                "Kliyan ka wè tout pwodwi ou, foto yo, ak pri yo — "
                "epi yo kòmande dirèkteman nan katalòg la. "
                "Se tankou yon boutik ki louvri 24/7! 🏪"
            ),
            "wrong": (
                "❌ Sa pa kòrèk. Fonksyon ki pèmèt kliyan wè tout pwodwi ak pri yo "
                "rele Katalòg (Catalog) nan WhatsApp Business. "
                "Se vitrin dijital ou — mete tout pwodwi ou ladan l!\n\n"
                "Eseye ankò! 👇\n\n"
                "Ki fonksyon WhatsApp Business ki pèmèt kliyan wè tout pwodwi ou ak pri yo?\n"
                "A) Etikèt (Labels)\n"
                "B) Katalòg (Catalog)\n"
                "C) Estatistik (Statistics)"
            )
        }
    },
    {
        "title": "Leson 6: Fè piblisite sou Facebook",
        "teaching": (
            "📣 REZO SOSYAL POU BIZNIS — Leson 6\n\n"
            "Ou ka 'bouste' (boost) yon pòs sou Facebook pou plis moun wè li — "
            "menm moun ki pa swiv paj ou! Se piblisite peye ki pi fasil. 💸\n\n"
            "Kijan pou bouste yon pòs:\n"
            "1️⃣ Pòs ou pibliye a — asire l gen bon foto ak deskripsyon\n"
            "2️⃣ Klike bouton 'Boost Post' oswa 'Pwomote Pòs'\n"
            "3️⃣ Chwazi piblik ou — ki kote yo ye? ki laj? ki enterè?\n"
            "   Ex: Fanm 18-45 an nan Pòtoprens ki renmen mòd\n"
            "4️⃣ Chwazi bidjè ou — kòmanse ak 500-1000 HTG pou 3-5 jou\n"
            "5️⃣ Peye ak MonCash oswa kat kredi\n\n"
            "💡 Tip: Bouste sèlman pòs ki deja gen bon rezilta gratis — "
            "sa ki gen kòmantè ak reyaksyon!"
        ),
        "quiz": (
            "❓ QUIZ — Leson 6\n\n"
            "Kijan ou ka peye pou piblisite Facebook ann Ayiti?\n\n"
            "A) Sèlman ak kat kredi entènasyonal\n"
            "B) Sèlman ak lajan kach nan bank\n"
            "C) Ak MonCash oswa kat kredi"
        ),
        "correct": "c",
        "explanations": {
            "correct": (
                "✅ Kòrèk! Ann Ayiti, ou ka peye piblisite Facebook ak MonCash "
                "oswa ak kat kredi. MonCash se opsyon ki pi fasil pou anpil biznis Ayisyen. "
                "Kòmanse ak ti bidjè — ou ka wè rezilta ak sèlman 500 HTG! 💪"
            ),
            "wrong": (
                "❌ Sa pa kòrèk. Ann Ayiti, ou ka peye piblisite Facebook ak MonCash "
                "oswa ak kat kredi — ou pa oblije gen kat entènasyonal sèlman. "
                "MonCash fè sa trè fasil pou tout moun!\n\n"
                "Eseye ankò! 👇\n\n"
                "Kijan ou ka peye pou piblisite Facebook ann Ayiti?\n"
                "A) Sèlman ak kat kredi entènasyonal\n"
                "B) Sèlman ak lajan kach nan bank\n"
                "C) Ak MonCash oswa kat kredi"
            )
        }
    },
    {
        "title": "Leson 7: Instagram ak TikTok pou biznis",
        "teaching": (
            "🎥 REZO SOSYAL POU BIZNIS — Leson 7\n\n"
            "Instagram ak TikTok se de platfòm pwisan pou atire jenn kliyan "
            "ak fè biznis ou grandi — souvan GRATIS! ✨\n\n"
            "📸 Instagram:\n"
            "• Ideal pou mòd, manje, bote, dekorasyon\n"
            "• Mete 5-10 hashtag pètinan: #BoutikAyiti #ModeHaiti\n"
            "• Pòs 3x pa semèn pou rete vizib\n\n"
            "🎵 TikTok:\n"
            "• Video kout 15-60 segonn ki ka vin viral\n"
            "• Montre pwosesis fè pwodwi ou — moun renmen wè 'dèyè koulys'\n"
            "• Antre nan trend ki popilè pou plis wè\n"
            "• Gratis totalman — ou pa bezwen peye pou piblisite!\n\n"
            "💡 Tip: Yon sèl bon TikTok ka fè plis pase 1000 moun konnen biznis ou!"
        ),
        "quiz": (
            "❓ QUIZ — Leson 7\n\n"
            "Ki tip kontni ki mache pi byen sou TikTok pou yon ti biznis?\n\n"
            "A) Tèks long sou istwa biznis ou\n"
            "B) Video kout ki montre pwosesis fè pwodwi ou\n"
            "C) Foto sèlman san son"
        ),
        "correct": "b",
        "explanations": {
            "correct": (
                "✅ Kòrèk! Sou TikTok, video kout ki montre 'dèyè koulys' biznis ou "
                "— kijan ou fè pwodwi a, kijan ou pakete l, oswa kijan ou livre l — "
                "jwenn plis wè epi kreye konfyans ak kliyan yo. "
                "Kòmanse filme jodi a! 🎬"
            ),
            "wrong": (
                "❌ Sa pa kòrèk. Sou TikTok, kontni ki mache pi byen se video kout "
                "ki montre pwosesis fè pwodwi ou. "
                "TikTok pa sipòte foto sèlman san son, epi tèks long pa kenbe atansyon moun.\n\n"
                "Eseye ankò! 👇\n\n"
                "Ki tip kontni ki mache pi byen sou TikTok pou yon ti biznis?\n"
                "A) Tèks long sou istwa biznis ou\n"
                "B) Video kout ki montre pwosesis fè pwodwi ou\n"
                "C) Foto sèlman san son"
            )
        }
    },
    {
        "title": "Leson 8: Mezire siksè ou — Kijan pou konnen sa ki mache",
        "teaching": (
            "📊 REZO SOSYAL POU BIZNIS — Leson 8\n\n"
            "Si ou pa mezire, ou pa ka amelyore! "
            "Konnen ki pòs ki travay epi ki yo ki pa travay. 🔍\n\n"
            "Chif ki enpòtan pou swiv:\n"
            "👁️ Wè (Reach/Views) — Konbyen moun ki wè pòs ou\n"
            "❤️ Angajman — Reyaksyon + kòmantè + pataj. Si li wo, kontni ou bon!\n"
            "💬 Mesaj resevwa — Konbyen moun kontakte ou apre yon pòs\n"
            "💰 Vant — Pi bon mezire: konbyen kòmand ou resevwa chak semèn\n\n"
            "Kijan pou wè chif yo:\n"
            "• Facebook/Instagram: Ale nan 'Insights' oswa 'Estatistik' sou paj ou\n"
            "• WhatsApp Business: Ale nan Paramèt → Estatistik\n\n"
            "💡 Tip: Ekri rezilta ou chak semèn. Konpare — fè plis sa ki mache!"
        ),
        "quiz": (
            "❓ QUIZ — Leson 8\n\n"
            "Ki pi bon jan pou konnen si rezo sosyal ou ede biznis ou grandi?\n\n"
            "A) Gade sèlman konbyen moun swiv paj ou\n"
            "B) Konte konbyen kòmand ou resevwa chak semèn\n"
            "C) Gade si zanmi ou renmen pòs ou"
        ),
        "correct": "b",
        "explanations": {
            "correct": (
                "✅ Kòrèk! Pi bon mezire siksè yon biznis se konbyen kòmand ou resevwa. "
                "Ou ka gen 10,000 swivan men si yo pa achte, rezo sosyal ou pa travay pou biznis ou. "
                "Toujou konte vant ou — se sa ki konte! 🏆"
            ),
            "wrong": (
                "❌ Sa pa kòrèk. Pi bon jan pou mezire siksè biznis ou sou rezo sosyal "
                "se konte konbyen kòmand ou resevwa chak semèn. "
                "Swivan ak reyaksyon zanmi ou bon, men se vant ki montre vrè siksè!\n\n"
                "Eseye ankò! 👇\n\n"
                "Ki pi bon jan pou konnen si rezo sosyal ou ede biznis ou grandi?\n"
                "A) Gade sèlman konbyen moun swiv paj ou\n"
                "B) Konte konbyen kòmand ou resevwa chak semèn\n"
                "C) Gade si zanmi ou renmen pòs ou"
            )
        }
    },
]

# ---------------------------------------------------------------------------
# Course 3: Lanse Ti Komès Ou (8 lessons)
# ---------------------------------------------------------------------------

TI_KOMES_LESSONS = [
    {
        "title": "Leson 1: Jwenn Yon Ide Biznis",
        "teaching": (
            "💡 *Kijan pou jwenn yon bon ide biznis?*\n\n"
            "Yon bon ide biznis rezoud yon pwoblèm moun yo genyen nan kominote ou.\n\n"
            "Poze tèt ou kesyon sa yo:\n"
            "🔹 Ki sa vwazen m yo bezwen men yo paka jwenn fasil?\n"
            "🔹 Ki pwoblèm moun yo plenn anpil?\n"
            "🔹 Ki sa mwen konn fè ki bon?\n\n"
            "Egzanp: Si moun nan katye ou yo toujou al lwen pou achte dlo potab, "
            "ou ka vann dlo nan katye a. Si moun yo bezwen recharge Digicel alèswè, "
            "ou ka tounen yon pwen recharge.\n\n"
            "👉 Ide ki soti nan yon reyèl bezwen = biznis ki gen chans reyisi!"
        ),
        "quiz": (
            "❓ QUIZ — Leson 1\n\n"
            "Ki pi bon fason pou jwenn yon bon ide biznis?\n\n"
            "A) Kopye sa zanmi ou fè san gade si katye ou bezwen li\n"
            "B) Chèche yon pwoblèm reyèl moun nan kominote ou genyen epi rezoud li\n"
            "C) Chwazi biznis ki rapòte plis lajan san ou pa konn domèn nan"
        ),
        "correct": "b",
        "explanations": {
            "correct": (
                "✅ Kòrèk! Yon bon ide biznis soti nan yon bezwen reyèl. "
                "Lè ou rezoud yon pwoblèm moun yo genyen, kliyan ou yo ap toujou vini jwenn ou. "
                "Se fon yon biznis solid! 💪"
            ),
            "wrong": (
                "❌ Sa pa kòrèk. Kopye yon biznis oswa chwazi sèlman pou lajan san konprann "
                "mache a ka fè ou pèdi lajan.\n\n"
                "Eseye ankò! 👇\n\n"
                "Ki pi bon fason pou jwenn yon bon ide biznis?\n"
                "A) Kopye sa zanmi ou fè san gade si katye ou bezwen li\n"
                "B) Chèche yon pwoblèm reyèl moun nan kominote ou genyen epi rezoud li\n"
                "C) Chwazi biznis ki rapòte plis lajan san ou pa konn domèn nan"
            ),
        },
    },
    {
        "title": "Leson 2: Konnen Kliyan Ou Yo",
        "teaching": (
            "🎯 *Kliyan ou yo — ki moun yo ye?*\n\n"
            "Anvan ou vann anyen, ou dwe konnen pou KI MOUN ou ap travay.\n\n"
            "Poze tèt ou:\n"
            "🔹 Ki laj kliyan mwen yo? (Jenn, granmoun, manman...)\n"
            "🔹 Ki kote yo abite oswa travay?\n"
            "🔹 Konbyen lajan yo ka depanse?\n"
            "🔹 Ki lè yo achte? Maten, midi, aswè?\n\n"
            "Egzanp: Si ou vann manje prepare, kliyan ou yo ka se travayè ki pa gen tan "
            "kwit manje. Yo bezwen manje vit, pa chè, epi bon. "
            "Konsa ou ka pare manje disponib lè midi — lè yo travèse!\n\n"
            "🧠 Pi ou konnen kliyan ou yo, pi ou ka ba yo sa yo vrèman bezwen."
        ),
        "quiz": (
            "❓ QUIZ — Leson 2\n\n"
            "Poukisa li enpòtan pou konnen kliyan ou yo byen?\n\n"
            "A) Pou ou ka pale mal de yo bay lòt machann\n"
            "B) Pou ou ka ofri yo pwodwi ak sèvis ki kole ak bezwen yo vrèman genyen\n"
            "C) Pou ou ka monte pri yo paske ou konnen kombyen yo touche"
        ),
        "correct": "b",
        "explanations": {
            "correct": (
                "✅ Kòrèk! Lè ou konnen kliyan ou yo — bezwen yo, abitid yo, bidjè yo — "
                "ou ka ba yo egzakteman sa yo chèche. Sa fè yo achte pi souvan epi rekòmande "
                "biznis ou bay lòt moun! 🤝"
            ),
            "wrong": (
                "❌ Sa pa kòrèk. Konnen kliyan ou yo se pou ba yo pi bon sèvis — "
                "pa pou pwofite de yo oswa pale mal de yo.\n\n"
                "Eseye ankò! 👇\n\n"
                "Poukisa li enpòtan pou konnen kliyan ou yo byen?\n"
                "A) Pou ou ka pale mal de yo bay lòt machann\n"
                "B) Pou ou ka ofri yo pwodwi ak sèvis ki kole ak bezwen yo vrèman genyen\n"
                "C) Pou ou ka monte pri yo paske ou konnen kombyen yo touche"
            ),
        },
    },
    {
        "title": "Leson 3: Kalkile Pri Pwodwi Ou",
        "teaching": (
            "💰 *Kijan pou fikse yon bon pri?*\n\n"
            "Anpil ti machann vann pwodwi yo twò bon mache epi yo pa fè benefis. "
            "Fò ou toujou kalkile:\n\n"
            "📌 *Fòmil debaz:*\n"
            "Pri vant = Pri koute + % Benefis ou vle fè\n\n"
            "Egzanp paktik:\n"
            "🛍️ Ou achte yon sak diri pou 1 300 goud.\n"
            "Transpò: 50 goud. Total koute = 1 350 goud.\n"
            "Ou vle 20% benefis → 1 350 × 1.20 = *1 620 goud*\n\n"
            "Pa bliye mete nan kalkil ou:\n"
            "🔹 Transpò\n"
            "🔹 Sak ak pakaj\n"
            "🔹 Tan ou pase pou travay la\n\n"
            "⚠️ Si ou vann san kalkile, ou ka travay di epi toujou rete pòv!"
        ),
        "quiz": (
            "❓ QUIZ — Leson 3\n\n"
            "Ou achte yon pwodwi pou 500 goud. Ou vle fè 25% benefis. "
            "Ki pri ou dwe vann li?\n\n"
            "A) 525 goud\n"
            "B) 600 goud\n"
            "C) 625 goud"
        ),
        "correct": "c",
        "explanations": {
            "correct": (
                "✅ Kòrèk! 500 × 1.25 = 625 goud. "
                "Ou toujou ap miltipliye pri koute ou pa (1 + pousantaj benefis ou vle). "
                "Sa ba ou yon pri ki kouvri depans ou epi ba ou yon bon benefis! 🎉"
            ),
            "wrong": (
                "❌ Pa egzakteman. Sonje fòmil la: Pri vant = Pri koute × (1 + % benefis).\n"
                "500 × 1.25 = 625 goud — pa 525 ni 600.\n\n"
                "Eseye ankò! 👇\n\n"
                "Ou achte yon pwodwi pou 500 goud. Ou vle fè 25% benefis. "
                "Ki pri ou dwe vann li?\n"
                "A) 525 goud\n"
                "B) 600 goud\n"
                "C) 625 goud"
            ),
        },
    },
    {
        "title": "Leson 4: Kijan pou Jere Lajan Biznis Ou",
        "teaching": (
            "🏦 *Separe lajan biznis ak lajan pèsonèl ou!*\n\n"
            "Se youn nan pi gwo erè ti machann yo fè: melanje lajan biznis ak lajan "
            "pou kay la. Konsa ou pa ka janm konnen si biznis ou ap fè benefis!\n\n"
            "✅ *Sa ou dwe fè:*\n"
            "1️⃣ Kreye yon kont MonCash oswa yon tirelire jis pou biznis la\n"
            "2️⃣ Chak jou ou vann, mete lajan biznis la apa\n"
            "3️⃣ Pran yon ti salè pèsonèl — pa pran tout benefis la\n"
            "4️⃣ Note tout depans ak tout vant chak jou\n\n"
            "Egzanp: Si ou fè 3 000 goud vant yonn jou, koute 2 000 goud — "
            "benefis ou se 1 000 goud. Pran 500 pou ou, kite 500 nan biznis pou "
            "achte plis machandiz.\n\n"
            "📒 Yon ti kaye pou note = yon gwo zam pou biznis ou!"
        ),
        "quiz": (
            "❓ QUIZ — Leson 4\n\n"
            "Poukisa li enpòtan pou separe lajan biznis ak lajan pèsonèl ou?\n\n"
            "A) Se pa nesesè, ou ka jere yo ansanm san pwoblèm\n"
            "B) Pou ou ka konnen egzakteman si biznis la ap fè benefis epi jere lajan an kòmsadwa\n"
            "C) Sèlman pou ka montre bank lan si yo mande"
        ),
        "correct": "b",
        "explanations": {
            "correct": (
                "✅ Kòrèk! Lè lajan biznis ak lajan pèsonèl melanje, ou pa kapab wè vrè "
                "sitiyasyon biznis ou. Separasyon an ede ou konnen si ou fè benefis, "
                "planifye acha, epi evite fè fayit san ou pa rann ou kont. 📊"
            ),
            "wrong": (
                "❌ Sa pa kòrèk. Melanje de kalite lajan sa yo se yon erè ki ka detwi yon biznis "
                "dousman dousman — menm si ou ap travay di.\n\n"
                "Eseye ankò! 👇\n\n"
                "Poukisa li enpòtan pou separe lajan biznis ak lajan pèsonèl ou?\n"
                "A) Se pa nesesè, ou ka jere yo ansanm san pwoblèm\n"
                "B) Pou ou ka konnen egzakteman si biznis la ap fè benefis epi jere lajan an kòmsadwa\n"
                "C) Sèlman pou ka montre bank lan si yo mande"
            ),
        },
    },
    {
        "title": "Leson 5: Kote pou Jwenn Machandiz",
        "teaching": (
            "🛒 *Jwenn machandiz bon mache pou vann pi chè!*\n\n"
            "Benefis ou kòmanse nan KOTE ou achte — pa sèlman kote ou vann.\n\n"
            "📍 *Kote pou chèche founisè:*\n"
            "🔹 *Machè an gwo* — Machè Salomon, Machè Croix-des-Bossales, "
            "machè pwovens yo. Achte an gwo = pri pi ba.\n"
            "🔹 *Rezo fanmi ak zanmi* — Souvan yo ka konekte ou ak yon bon founisè\n"
            "🔹 *Inpòtatè dirèk* — Pou sèten pwodwi, chèche enpòtatè nan zòn pò a\n"
            "🔹 *Gwoup WhatsApp ak Facebook* — Gen anpil gwoup machann ki pataje "
            "bon pri ak bon adrès\n\n"
            "💡 *Konsèy:*\n"
            "Toujou konpare pri nan omwen 2-3 kote anvan ou achte. "
            "Mande pou ristoun lè ou achte an gwo — majorite founisè aksepte sa!"
        ),
        "quiz": (
            "❓ QUIZ — Leson 5\n\n"
            "Ki estrateji ki pi bon pou jwenn machandiz nan pi bon pri?\n\n"
            "A) Toujou achte nan yon sèl kote paske ou abitye\n"
            "B) Achte an gwo epi konpare pri nan plizyè kote anvan ou deside\n"
            "C) Achte sèlman nan mache lokal piti kote pri yo toujou pi ba"
        ),
        "correct": "b",
        "explanations": {
            "correct": (
                "✅ Kòrèk! Achte an gwo bese pri chak inite, epi konpare founisè ede ou "
                "jwenn pi bon deal. Sa dire tan pou fè rechèch men li ka double benefis ou! 💪"
            ),
            "wrong": (
                "❌ Sa pa kòrèk. Toujou rete nan yon sèl kote ka koute ou pi chè, "
                "epi mache piti paka toujou ba ou pi bon pri pase achte an gwo.\n\n"
                "Eseye ankò! 👇\n\n"
                "Ki estrateji ki pi bon pou jwenn machandiz nan pi bon pri?\n"
                "A) Toujou achte nan yon sèl kote paske ou abitye\n"
                "B) Achte an gwo epi konpare pri nan plizyè kote anvan ou deside\n"
                "C) Achte sèlman nan mache lokal piti kote pri yo toujou pi ba"
            ),
        },
    },
    {
        "title": "Leson 6: Vann ak Sèvis Kliyan",
        "teaching": (
            "😊 *Kliyan satisfè = biznis ki grandi!*\n\n"
            "Vann yon pwodwi se fasil — men fè kliyan a tounen ankò se yon lòt bagay. "
            "Sa ki fè kliyan tounen se *sèvis kliyan ou*.\n\n"
            "✅ *Règ lò pou sèvis kliyan:*\n"
            "🔹 Toujou salye kliyan yo avèk yon souri (menm sou WhatsApp!)\n"
            "🔹 Reponn vit — si yon kliyan voye mesaj, reponn nan 30 minit\n"
            "🔹 Sèye pwoblèm san diskite — kliyan ki plenn e ou rezoud pwoblèm nan "
            "vin pi fidèl pase yon kliyan ki pa t janm gen pwoblèm\n"
            "🔹 Sonje non kliyan ki vin souvan — moun renmen santi yo enpòtan\n"
            "🔹 Remèsye kliyan pou acha yo\n\n"
            "💬 Yon mo dous koute ou anyen men li ka valè yon vant anplis chak jou!"
        ),
        "quiz": (
            "❓ QUIZ — Leson 6\n\n"
            "Yon kliyan plenn ke pwodwi ou te ba li te gen yon defò. Ki sa ou dwe fè?\n\n"
            "A) Di li se pa fòt ou epi pa fè anyen\n"
            "B) Evite reponn mesaj li pou pwoblèm lan bliye\n"
            "C) Eskize ou, rezoud pwoblèm lan rapidman, epi asire ou li satisfè"
        ),
        "correct": "c",
        "explanations": {
            "correct": (
                "✅ Kòrèk! Rezoud yon plent pwofesyonèlman bati konfyans. "
                "Yon kliyan ki te gen yon pwoblèm epi ou te rezoud li byen souvan vin "
                "pi fidèl pase yon kliyan ki pa t janm gen pwoblèm. Se envestisman pou "
                "avni biznis ou! 🌟"
            ),
            "wrong": (
                "❌ Sa pa bon ditou. Inyore oswa refize responsablite pou yon pwoblèm "
                "ap fè kliyan an ale epi li ap di lòt moun pa achte nan men ou.\n\n"
                "Eseye ankò! 👇\n\n"
                "Yon kliyan plenn ke pwodwi ou te ba li te gen yon defò. Ki sa ou dwe fè?\n"
                "A) Di li se pa fòt ou epi pa fè anyen\n"
                "B) Evite reponn mesaj li pou pwoblèm lan bliye\n"
                "C) Eskize ou, rezoud pwoblèm lan rapidman, epi asire ou li satisfè"
            ),
        },
    },
    {
        "title": "Leson 7: Fè Biznis Ou Grandi",
        "teaching": (
            "📈 *Grandi biznis ou etap pa etap!*\n\n"
            "Anpil moun vle grandi vit anpil epi yo fè erè grav. "
            "Kwasans solid se kwasans ki *dousman men ki dirab*.\n\n"
            "🔑 *3 prensip pou kwasans solid:*\n\n"
            "1️⃣ *Reenvesti benefis* — Chak mwa, mete omwen 30% benefis ou tounen nan "
            "biznis lan (plis machandiz, pi bon kalite, nouvo pwodwi)\n\n"
            "2️⃣ *Ajoute pwodwi/sèvis* — Kliyan ki achte diri ka achte lwil ak sèl tou. "
            "Elarji ofri ou ti kras pa ti kras.\n\n"
            "3️⃣ *Bati rezo* — Konekte ak lòt ti machann. Kolaborasyon souvan pi fò pase "
            "konpetisyon nan kontèks ayisyen an.\n\n"
            "📌 Rezime: Grandi pa vle di depanse plis — li vle di *jere pi plis!"
        ),
        "quiz": (
            "❓ QUIZ — Leson 7\n\n"
            "Ki pi bon fason pou fè yon ti biznis grandi yon fason solid?\n\n"
            "A) Prete anpil lajan pou agrandi biznis lan rapidman\n"
            "B) Reenvesti yon pati nan benefis lan epi grandi etap pa etap\n"
            "C) Depanse tout benefis pou atire kliyan ak kado ak rabè"
        ),
        "correct": "b",
        "explanations": {
            "correct": (
                "✅ Kòrèk! Reenvesti yon pati nan benefis epi grandi dousman se fason "
                "ki pi solid. Sa evite dèt, sa bati yon fondasyon fò, epi sa ba ou "
                "kontròl sou biznis ou pandan tout tan. 🌱"
            ),
            "wrong": (
                "❌ Sa pa kòrèk. Prete anpil lajan oswa depanse tout benefis nan rabè "
                "ka mete biznis ou nan yon sitiyasyon difisil — ou ap travay pou peye dèt "
                "olye pou ou travay pou tèt ou.\n\n"
                "Eseye ankò! 👇\n\n"
                "Ki pi bon fason pou fè yon ti biznis grandi yon fason solid?\n"
                "A) Prete anpil lajan pou agrandi biznis lan rapidman\n"
                "B) Reenvesti yon pati nan benefis lan epi grandi etap pa etap\n"
                "C) Depanse tout benefis pou atire kliyan ak kado ak rabè"
            ),
        },
    },
    {
        "title": "Leson 8: Sèvi ak MonCash pou Biznis",
        "teaching": (
            "📱 *MonCash — zam sekrè ti machann ayisyen!*\n\n"
            "MonCash se pèman mobil ki pi itilize ann Ayiti. Pou biznis ou, "
            "li ofri anpil avantaj:\n\n"
            "✅ *Kijan MonCash ede biznis ou:*\n"
            "🔹 *Resevwa pèman fasil* — Kliyan voye lajan dirèkteman sou telefòn ou, "
            "menm si yo pa la bò ou\n"
            "🔹 *Evite riske kach* — Mwens kach sou ou = mwens risk vòl\n"
            "🔹 *Peye founisè ou yo* — Voye lajan bay founisè san deplase\n"
            "🔹 *Istorik tranzaksyon* — MonCash kenbe tout mouvman lajan, sa ede ou "
            "swiv biznis ou\n"
            "🔹 *MonCash Biznis* — Gen opsyon espesyal pou ti komèsan\n\n"
            "💡 *Konsèy:* Mete nimewo MonCash ou sou tout afi ou ak mesaj WhatsApp ou "
            "pou kliyan ka peye ou fasil nenpòt ki lè! 🚀"
        ),
        "quiz": (
            "❓ QUIZ — Leson 8\n\n"
            "Ki avantaj prensipal MonCash ofri pou yon ti komèsan?\n\n"
            "A) Li pèmèt ou resevwa pèman fasil, evite risk kach, epi swiv mouvman lajan biznis ou\n"
            "B) Li ba ou yon prè otomatik chak mwa pou achte machandiz\n"
            "C) Li pèmèt ou evite peye taks gouvènman an"
        ),
        "correct": "a",
        "explanations": {
            "correct": (
                "✅ Kòrèk! MonCash fasil pèman, diminye risk kach, epi istorik tranzaksyon "
                "an ede ou jere biznis ou pi byen. Se yon zouti esansyèl pou nenpòt ti "
                "komèsan ann Ayiti! 🎊"
            ),
            "wrong": (
                "❌ Sa pa kòrèk. MonCash pa ba prè otomatik epi li pa gen rapò ak evite "
                "taks — li se yon sèvis pèman mobil legal ak itil pou jere lajan biznis.\n\n"
                "Eseye ankò! 👇\n\n"
                "Ki avantaj prensipal MonCash ofri pou yon ti komèsan?\n"
                "A) Li pèmèt ou resevwa pèman fasil, evite risk kach, epi swiv mouvman lajan biznis ou\n"
                "B) Li ba ou yon prè otomatik chak mwa pou achte machandiz\n"
                "C) Li pèmèt ou evite peye taks gouvènman an"
            ),
        },
    },
]

# ---------------------------------------------------------------------------
# Course 4: Kontabilite Debaz (8 lessons)
# ---------------------------------------------------------------------------

KONTABILITE_LESSONS = [
    {
        "title": "Leson 1: Poukisa Kontabilite Enpòtan",
        "teaching": (
            "📚 LESON 1 — Poukisa Kontabilite Enpòtan?\n\n"
            "Kontabilite se konn kote lajan ou soti ak kote li ale. 💰\n\n"
            "Menm si ou vann bannann nan mache a, ou bezwen kontabilite!\n\n"
            "✅ Kontabilite ede ou:\n"
            "• Wè si biznis ou ap fè pwofi ou pèt\n"
            "• Planifye depi kounye a pou demen\n"
            "• Evite depanse plis pase ou touche\n"
            "• Pran desizyon entèlijan pou biznis ou\n\n"
            "🇭🇹 Egzanp: Manmi Roseline vann fritay. Chak jou li konte sa li achte ak sa li vann — "
            "konsa li konnen si jounen an bon ou pa. Sa se kontabilite senp!\n\n"
            "Sonje: Pa bezwen kalkitatris konplike. Yon kaye ak yon kreyon, oswa telefòn ou, se ase pou kòmanse! ✏️📱"
        ),
        "quiz": (
            "❓ QUIZ — Leson 1\n\n"
            "Ki pi gwo avantaj kontabilite pou yon ti komès?\n\n"
            "A) Li fè biznis ou parèt seryè devan moun\n"
            "B) Li ede ou wè si ou ap fè pwofi oswa pèt\n"
            "C) Li obligatwa pou tout moun ann Ayiti"
        ),
        "correct": "b",
        "explanations": {
            "correct": (
                "✅ Kòrèk! Kontabilite ede ou wè klè si biznis ou ap ban ou benefis oswa si ou ap pèdi lajan. "
                "Se zouti ki pi enpòtan pou pran bon desizyon! 💡"
            ),
            "wrong": (
                "❌ Sa pa kòrèk. Kontabilite pa sèlman pou parèt seryè, e li pa obligatwa pou tout moun — "
                "men li enpòtan anpil paske li ede ou wè si ou ap fè pwofi oswa pèt.\n\n"
                "Eseye ankò! 👇\n\n"
                "Ki pi gwo avantaj kontabilite pou yon ti komès?\n"
                "A) Li fè biznis ou parèt seryè devan moun\n"
                "B) Li ede ou wè si ou ap fè pwofi oswa pèt\n"
                "C) Li obligatwa pou tout moun ann Ayiti"
            )
        }
    },
    {
        "title": "Leson 2: Depans ak Revni",
        "teaching": (
            "📚 LESON 2 — Depans ak Revni\n\n"
            "Gen 2 mo ou DWE konnen nan kontabilite:\n\n"
            "💸 DEPANS = Tout lajan ou DEPANSE pou fè biznis ou mache.\n"
            "Egzanp: achte machandiz, peye transpò, achte sak plastik, peye elektrisite.\n\n"
            "💵 REVNI = Tout lajan ou TOUCHE nan vant ou sèvis ou.\n"
            "Egzanp: lajan kliyan yo peye ou chak jou nan mache a.\n\n"
            "🇭🇹 Egzanp reyèl:\n"
            "Marie achte diri ak pwa pou 3,000 goud (depans).\n"
            "Li vann tout manje li prepare pou 5,500 goud (revni).\n\n"
            "⚠️ Depans ak revni se PA menm bagay! "
            "Si ou konfond yo, ou p ap janm konnen vrè sitiyasyon biznis ou. "
            "Toujou note yo apa! 📝"
        ),
        "quiz": (
            "❓ QUIZ — Leson 2\n\n"
            "Jezi peye 500 goud pou transpò pote machandiz li nan mache. "
            "Ki kalite lajan sa ye?\n\n"
            "A) Revni\n"
            "B) Pwofi\n"
            "C) Depans"
        ),
        "correct": "c",
        "explanations": {
            "correct": (
                "✅ Kòrèk! 500 goud transpò a se yon DEPANS — se lajan Jezi depanse pou ka fè biznis li. "
                "Depans toujou diminye lajan ki nan pòch ou. 💸"
            ),
            "wrong": (
                "❌ Sa pa kòrèk. Lajan ou peye pou transpò a se yon DEPANS — se lajan ou soti nan pòch ou "
                "pou ka fè biznis ou mache. Revni se lajan ou TOUCHE, pa lajan ou DEPANSE.\n\n"
                "Eseye ankò! 👇\n\n"
                "Jezi peye 500 goud pou transpò pote machandiz li nan mache. "
                "Ki kalite lajan sa ye?\n"
                "A) Revni\n"
                "B) Pwofi\n"
                "C) Depans"
            )
        }
    },
    {
        "title": "Leson 3: Kijan Pou Note Tout Tranzaksyon Ou",
        "teaching": (
            "📚 LESON 3 — Kijan Pou Note Tout Tranzaksyon Ou\n\n"
            "Yon tranzaksyon se nenpòt mouvman lajan: achte, vann, peye, resevwa. 🔄\n\n"
            "📝 METÒD SENP AK KAYE:\n"
            "Fè 2 kolòn chak jou:\n"
            "| LAJAN RANTRE | LAJAN SOTI |\n"
            "Ekri chak tranzaksyon ak dat li ak rezon li.\n\n"
            "📱 METÒD AK TELEFÒN:\n"
            "Itilize nòt telefòn ou (Samsung Notes, Google Keep) oswa yon gwoup WhatsApp ou kreye pou tèt ou. "
            "Voye yon mesaj pou chak depans ou revni!\n\n"
            "🇭🇹 Egzanp:\n"
            "✏️ 05 mas — Achte soup joumou: 1,200 goud (soti)\n"
            "✏️ 05 mas — Vann soup: 2,800 goud (rantre)\n\n"
            "💡 Konsèy: Note tranzaksyon ou MENM KOTE li fèt — pa tann aswè oswa demen. Memwa twonpe! ⏰"
        ),
        "quiz": (
            "❓ QUIZ — Leson 3\n\n"
            "Ki pi bon moman pou note yon tranzaksyon?\n\n"
            "A) Aswè anvan dòmi\n"
            "B) Menm kote tranzaksyon an fèt\n"
            "C) Fen semèn nan"
        ),
        "correct": "b",
        "explanations": {
            "correct": (
                "✅ Kòrèk! Toujou note tranzaksyon ou MENM KOTE li fèt. "
                "Si ou tann demen, ou ka bliye montan an oswa raison an — epi chif ou yo p ap ekzak! 🎯"
            ),
            "wrong": (
                "❌ Sa pa kòrèk. Pi bon moman an se MENM KOTE tranzaksyon an fèt. "
                "Si ou tann aswè oswa fen semèn nan, ou risque bliye detay enpòtan — "
                "e chif ou yo p ap ekzak.\n\n"
                "Eseye ankò! 👇\n\n"
                "Ki pi bon moman pou note yon tranzaksyon?\n"
                "A) Aswè anvan dòmi\n"
                "B) Menm kote tranzaksyon an fèt\n"
                "C) Fen semèn nan"
            )
        }
    },
    {
        "title": "Leson 4: Kalkile Benefis Ou",
        "teaching": (
            "📚 LESON 4 — Kalkile Benefis Ou\n\n"
            "Gen yon fòmil MAGIC ou dwe mete nan tèt ou:\n\n"
            "🧮 REVNI − DEPANS = PWOFI (Benefis)\n\n"
            "Si rezilta a POZITIF (+) ➡️ ou fè lajan! 🎉\n"
            "Si rezilta a NEGATIF (−) ➡️ ou pèdi lajan. Danje! ⚠️\n\n"
            "🇭🇹 Egzanp reyèl:\n"
            "Claudette vann kleren chak wikenn.\n"
            "• Revni: 12,000 goud\n"
            "• Depans (materyèl + transpò + sak): 7,500 goud\n"
            "• Pwofi: 12,000 − 7,500 = 4,500 goud ✅\n\n"
            "⚠️ Atansyon: Anpil moun konte TOUT lajan yo touche kòm pwofi — sa se erè grav! "
            "Toujou retire depans yo ANVAN ou di ou fè pwofi. 💡\n\n"
            "Fè kalkil sa chak jou, chak semèn, chak mwa! 📅"
        ),
        "quiz": (
            "❓ QUIZ — Leson 4\n\n"
            "Pierre vann rad itilize. Semèn sa li touche 8,000 goud men li depanse 5,500 goud. "
            "Ki pwofi li fè?\n\n"
            "A) 8,000 goud\n"
            "B) 2,500 goud\n"
            "C) 13,500 goud"
        ),
        "correct": "b",
        "explanations": {
            "correct": (
                "✅ Kòrèk! 8,000 − 5,500 = 2,500 goud. "
                "Se sa ki rele pwofi reyèl la — sa ki rete nan pòch ou apre ou retire tout depans yo! 💰🎉"
            ),
            "wrong": (
                "❌ Sa pa kòrèk. Fòmil la se: REVNI − DEPANS = PWOFI. "
                "8,000 − 5,500 = 2,500 goud. "
                "8,000 se revni total la — ou pa ka rele sa pwofi san retire depans yo!\n\n"
                "Eseye ankò! 👇\n\n"
                "Pierre vann rad itilize. Semèn sa li touche 8,000 goud men li depanse 5,500 goud. "
                "Ki pwofi li fè?\n"
                "A) 8,000 goud\n"
                "B) 2,500 goud\n"
                "C) 13,500 goud"
            )
        }
    },
    {
        "title": "Leson 5: Jere Lajan Chak Jou",
        "teaching": (
            "📚 LESON 5 — Jere Lajan Chak Jou\n\n"
            "Jere lajan chak jou vle di konnen EGZAKTEMAN ki lajan ou genyen, "
            "ki lajan ap rantre, ak ki lajan ap soti — sa rele CASH FLOW. 💵🔄\n\n"
            "📋 WOUTINN CHAK JOU:\n"
            "🌅 Maten: Konte lajan kach ou genyen (nan men ak nan MonCash)\n"
            "🌞 Midi: Note tout depans ak vant ou fè\n"
            "🌙 Aswè: Konte lajan ou ankò — konpare ak maten\n\n"
            "🇭🇹 Konsèy pratik:\n"
            "• Separe lajan biznis ou AK lajan kay ou — pa melanje!\n"
            "• Sèvi ak MonCash pou kenbe istwa tranzaksyon (ou ka wè istwa ou nan aplikasyon an)\n"
            "• Toujou kenbe yon ti rezèv pou ijans — omwen 10% pwofi ou\n\n"
            "⚠️ Pi gwo erè: Depanse lajan biznis pou bezwen pèsonèl san note l. "
            "Sa kraze tout kalkil ou! Disiplin se kle siksè! 🗝️"
        ),
        "quiz": (
            "❓ QUIZ — Leson 5\n\n"
            "Sandra melanje lajan biznis li ak lajan pèsonèl li nan menm bous. "
            "Ki pwoblèm sa ka kreye?\n\n"
            "A) Okenn pwoblèm, se pi fasil konsa\n"
            "B) Li p ap ka konnen vrè pwofi biznis li\n"
            "C) Li ka peye mwens taks"
        ),
        "correct": "b",
        "explanations": {
            "correct": (
                "✅ Kòrèk! Si ou melanje lajan biznis ak lajan pèsonèl, ou pa ka konnen vrèman "
                "ki pwofi biznis ou fè. Toujou separe yo — menm si ou sèvi ak 2 bous diferan! 👛👛"
            ),
            "wrong": (
                "❌ Sa pa kòrèk. Melanje lajan biznis ak lajan pèsonèl se yon gwo erè — "
                "paske ou p ap ka konnen vrè pwofi biznis ou, ni ki depans ki soti nan biznis "
                "oswa nan lavi pèsonèl ou.\n\n"
                "Eseye ankò! 👇\n\n"
                "Sandra melanje lajan biznis li ak lajan pèsonèl li nan menm bous. "
                "Ki pwoblèm sa ka kreye?\n"
                "A) Okenn pwoblèm, se pi fasil konsa\n"
                "B) Li p ap ka konnen vrè pwofi biznis li\n"
                "C) Li ka peye mwens taks"
            )
        }
    },
    {
        "title": "Leson 6: Planifye Yon Bidjè",
        "teaching": (
            "📚 LESON 6 — Planifye Yon Bidjè\n\n"
            "Yon bidjè se yon PLAN pou lajan ou — ou deside ANVAN kijan ou pral depanse l. 📅\n\n"
            "🛠️ KIJAN POU FÈ BIDJÈ MWA W:\n\n"
            "1️⃣ Estinye revni ou pou mwa a (baze sou mwa pase yo)\n"
            "2️⃣ Liste tout depans fiks (lwaye, elektrisite, telefòn Digicel/Natcom)\n"
            "3️⃣ Liste depans varyab (machandiz, transpò, manje)\n"
            "4️⃣ Kalkile: Revni − (Depans fiks + Varyab) = Balans\n"
            "5️⃣ Aloke yon pati pou epay (omwen 10%)\n\n"
            "🇭🇹 Egzanp pou yon ti machann:\n"
            "• Revni pwojete: 25,000 goud\n"
            "• Depans fiks: 8,000 goud\n"
            "• Machandiz: 10,000 goud\n"
            "• Epay: 2,500 goud\n"
            "• Balans lib: 4,500 goud\n\n"
            "💡 Bidjè pa yon prizon — se yon kousòl pou pa pèdi wout! 🧭"
        ),
        "quiz": (
            "❓ QUIZ — Leson 6\n\n"
            "Ki premye etap pou fè yon bidjè mwa?\n\n"
            "A) Kòmanse depanse epi wè sa ki rete\n"
            "B) Estinye revni ou pral touche mwa a\n"
            "C) Mande yon kontab pwofesyonèl"
        ),
        "correct": "b",
        "explanations": {
            "correct": (
                "✅ Kòrèk! Premye etap yon bidjè se estinye revni ou — "
                "ou pa ka planifye depans ou si ou pa konnen konbyen lajan ou pral genyen! "
                "Toujou kòmanse ak revni, apre depans. 📊"
            ),
            "wrong": (
                "❌ Sa pa kòrèk. Si ou depanse anvan ou planifye, ou ka rive nan mitan mwa san lajan. "
                "Premye etap yon bidjè se ESTINYE REVNI ou pral touche — apre sa ou ka planifye depans yo.\n\n"
                "Eseye ankò! 👇\n\n"
                "Ki premye etap pou fè yon bidjè mwa?\n"
                "A) Kòmanse depanse epi wè sa ki rete\n"
                "B) Estinye revni ou pral touche mwa a\n"
                "C) Mande yon kontab pwofesyonèl"
            )
        }
    },
    {
        "title": "Leson 7: Taks ak Obligasyon Legal ann Ayiti",
        "teaching": (
            "📚 LESON 7 — Taks ak Obligasyon Legal ann Ayiti\n\n"
            "Si ou fè biznis ann Ayiti, gen règ leta ou dwe respekte. 🏛️\n\n"
            "📋 DGI (Direksyon Jeneral Enpo) se biwo ki kolekte taks biznis yo.\n\n"
            "🔑 SA OU BEZWEN KONNEN:\n"
            "• NIF: Nimewo Idantifikasyon Fiskal — nimewo taks ou pou biznis fòmèl\n"
            "• Patant: Pèmi pou fè kòmès — renouvle chak ane\n"
            "• TVA: 10% sou sèvis ak pwodwi — gwo biznis sèlman\n\n"
            "🇭🇹 Majorite ti komès ann Ayiti travay enfòmèl. "
            "Men fòmalizasyon enpòtan si ou vle grandi ak konpayi ak ONG.\n\n"
            "💡 Premye pa: Al nan biwo DGI ki pre ou epi mande NIF ou. Gratis! ✅"
        ),
        "quiz": (
            "❓ QUIZ — Leson 7\n\n"
            "Ki sa NIF vle di ann Ayiti?\n\n"
            "A) Nimewo Idantifikasyon Fiskal — nimewo taks biznis ou\n"
            "B) Nouvo Investisman Financial — yon prè gouvènman\n"
            "C) Nòm Inisyal Finansye — yon sètifika kontab"
        ),
        "correct": "a",
        "explanations": {
            "correct": (
                "✅ Kòrèk! NIF vle di Nimewo Idantifikasyon Fiskal. "
                "Se nimewo ofisyèl leta bay biznis ou pou peye taks. "
                "Ou ka jwenn pa ou nan biwo DGI ki pre ou a — se gratis! 🏛️"
            ),
            "wrong": (
                "❌ Sa pa kòrèk. NIF vle di NIMEWO IDANTIFIKASYON FISKAL — "
                "se nimewo ofisyèl taks yo bay biznis ou nan DGI (Direksyon Jeneral Enpo). "
                "Sa pa yon prè ni yon sètifika.\n\n"
                "Eseye ankò! 👇\n\n"
                "Ki sa NIF vle di ann Ayiti?\n"
                "A) Nimewo Idantifikasyon Fiskal — nimewo taks biznis ou\n"
                "B) Nouvo Investisman Financial — yon prè gouvènman\n"
                "C) Nòm Inisyal Finansye — yon sètifika kontab"
            )
        }
    },
    {
        "title": "Leson 8: Itilize Telefòn Pou Kontabilite",
        "teaching": (
            "📚 LESON 8 — Itilize Telefòn Pou Kontabilite\n\n"
            "Telefòn ou se yon zouti kontabilite pwisan — epi aplikasyon yo GRATIS! 📱💪\n\n"
            "📲 APLIKASYON GRATIS:\n"
            "1️⃣ Google Sheets: fè tableau Dat | Rantre | Soti | Balans\n"
            "2️⃣ Google Keep: note tranzaksyon vit, senkronize ak Drive\n"
            "3️⃣ MonCash: wè istwa peman ak prèv tranzaksyon\n\n"
            "🇭🇹 Konsèy: Telechaje aplikasyon yo sou WiFi, "
            "travay offlign epi senkronize lè ou jwenn koneksyon Digicel/Natcom.\n\n"
            "🎓 Felisitasyon! Ou fini kou Kontabilite Debaz la! "
            "Ou kounye a gen tout zouti pou jere lajan biznis ou tankou yon pwofesyonèl. 🚀🇭🇹"
        ),
        "quiz": (
            "❓ QUIZ — Leson 8\n\n"
            "Ki aplikasyon ou ka itilize GRATIS sou telefòn ou pou fè yon tableau kontabilite?\n\n"
            "A) QuickBooks (peye chak mwa)\n"
            "B) Google Sheets (gratis)\n"
            "C) SAP Business One (pou gran konpayi)"
        ),
        "correct": "b",
        "explanations": {
            "correct": (
                "✅ Kòrèk! Google Sheets se gratis epi ou ka fè tout kalite tableau kontabilite ladan l. "
                "Ou ka kòmanse jodi a menm — telechaje l sou WiFi epi itilize l offlign! 📊🎉"
            ),
            "wrong": (
                "❌ Sa pa kòrèk. QuickBooks ak SAP yo koute lajan epi yo twò konplike pou ti komès. "
                "GOOGLE SHEETS se gratis, fasil pou itilize, epi li travay menm sou telefòn bon mache!\n\n"
                "Eseye ankò! 👇\n\n"
                "Ki aplikasyon ou ka itilize GRATIS sou telefòn ou pou fè yon tableau kontabilite?\n"
                "A) QuickBooks (peye chak mwa)\n"
                "B) Google Sheets (gratis)\n"
                "C) SAP Business One (pou gran konpayi)"
            )
        }
    },
]

# ---------------------------------------------------------------------------
# Course 5: Anglè pou Biznis (8 lessons)
# ---------------------------------------------------------------------------

ANGLE_LESSONS = [
    {
        "title": "Leson 1: Salitasyon ak Prezantasyon 👋",
        "teaching": (
            "🌟 Bonjou! Jodi a nou pral aprann di bonjou ak prezante tèt nou an anglè!\n\n"
            "👋 *Salitasyon:*\n"
            "• Hello! = Bonjou! / Bonswa!\n"
            "• Good morning! = Bon maten!\n"
            "• Good afternoon! = Bòn apremidi!\n"
            "• Good evening! = Bonswa!\n\n"
            "🙋 *Prezantasyon:*\n"
            "• My name is Jean. = Mwen rele Jean.\n"
            "• Nice to meet you! = Kontan fè konesans ou!\n"
            "• How are you? = Kijan ou ye?\n"
            "• I'm fine, thank you! = Mwen byen, mèsi!\n\n"
            "💡 *Egzanp:*\n"
            "\"Hello! My name is Marie. Nice to meet you!\"\n"
            "= \"Bonjou! Mwen rele Marie. Kontan fè konesans ou!\"\n\n"
            "Pratike di sa yo chak maten! 💪"
        ),
        "quiz": (
            "❓ QUIZ — Leson 1\n\n"
            "Kijan ou di \"Kontan fè konesans ou\" an anglè?\n\n"
            "A) How are you?\n"
            "B) Nice to meet you!\n"
            "C) Good morning!"
        ),
        "correct": "b",
        "explanations": {
            "correct": (
                "✅ Kòrèk! \"Nice to meet you!\" vle di \"Kontan fè konesans ou\" an anglè. "
                "Ou ka itilize fraz sa a chak fwa ou rankontre yon moun pou premye fwa. Bravo! 🎉"
            ),
            "wrong": (
                "❌ Sa pa kòrèk.\n\n"
                "• \"How are you?\" vle di \"Kijan ou ye?\"\n"
                "• \"Good morning!\" vle di \"Bon maten!\"\n"
                "• \"Nice to meet you!\" vle di \"Kontan fè konesans ou\" ✅\n\n"
                "Eseye ankò! 👇\n\n"
                "Kijan ou di \"Kontan fè konesans ou\" an anglè?\n"
                "A) How are you?\n"
                "B) Nice to meet you!\n"
                "C) Good morning!"
            )
        }
    },
    {
        "title": "Leson 2: Nimewo ak Pri 💰",
        "teaching": (
            "🔢 Jodi a nou pral aprann konte ak pale sou pri an anglè!\n\n"
            "📊 *Nimewo (Numbers):*\n"
            "• 1=one, 2=two, 3=three, 4=four, 5=five\n"
            "• 6=six, 7=seven, 8=eight, 9=nine, 10=ten\n"
            "• 100=one hundred, 1000=one thousand\n\n"
            "💵 *Lajan (Money):*\n"
            "• Dollar = Dola (USD)\n"
            "• How much does it cost? = Konbyen li koute?\n"
            "• It costs 5 dollars. = Li koute 5 dola.\n"
            "• That's too expensive! = Sa twò chè!\n"
            "• That's cheap! = Sa pa chè!\n\n"
            "💡 *Egzanp nan biznis:*\n"
            "Kliyan: \"How much does it cost?\"\n"
            "Ou: \"It costs 10 dollars.\" (≈ 1,320 goud)\n\n"
            "Pratike konte an anglè chak jou! 🌟"
        ),
        "quiz": (
            "❓ QUIZ — Leson 2\n\n"
            "Kijan ou di \"Konbyen li koute?\" an anglè?\n\n"
            "A) It costs five dollars.\n"
            "B) How much does it cost?\n"
            "C) That's too expensive!"
        ),
        "correct": "b",
        "explanations": {
            "correct": (
                "✅ Kòrèk! \"How much does it cost?\" se fraz ou itilize pou mande pri yon bagay. "
                "Se youn nan fraz ki pi enpòtan nan biznis anglè. Kontinye konsa! 💪"
            ),
            "wrong": (
                "❌ Sa pa kòrèk.\n\n"
                "• \"It costs five dollars.\" vle di \"Li koute senk dola.\"\n"
                "• \"That's too expensive!\" vle di \"Sa twò chè!\"\n"
                "• \"How much does it cost?\" se fason pou mande pri ✅\n\n"
                "Eseye ankò! 👇\n\n"
                "Kijan ou di \"Konbyen li koute?\" an anglè?\n"
                "A) It costs five dollars.\n"
                "B) How much does it cost?\n"
                "C) That's too expensive!"
            )
        }
    },
    {
        "title": "Leson 3: Achte ak Vann an Anglè 🛒",
        "teaching": (
            "🏪 Jodi a nou pral aprann pale biznis — achte ak vann — an anglè!\n\n"
            "🛍️ *Achte (Buying):*\n"
            "• I want to buy... = Mwen vle achte...\n"
            "• Do you have...? = Eske ou genyen...?\n"
            "• Can I get a discount? = Eske ou ka ba m yon rabè?\n"
            "• I'll take it! = Mwen pran li!\n\n"
            "💼 *Vann (Selling):*\n"
            "• The price is... = Pri a se...\n"
            "• We have a special offer. = Nou genyen yon òf espesyal.\n"
            "• This is the best price. = Sa se pi bon pri a.\n"
            "• Thank you for your business! = Mèsi pou biznis ou!\n\n"
            "💡 *Dyalòg nan mache:*\n"
            "Kliyan: \"I want to buy two bags.\"\n"
            "Ou: \"The price is 15 dollars. Thank you!\"\n\n"
            "Pratike fraz sa yo nan ti komès ou! 🌟"
        ),
        "quiz": (
            "❓ QUIZ — Leson 3\n\n"
            "Kijan ou di \"Mwen vle achte\" an anglè?\n\n"
            "A) The price is...\n"
            "B) Thank you for your business!\n"
            "C) I want to buy..."
        ),
        "correct": "c",
        "explanations": {
            "correct": (
                "✅ Kòrèk! \"I want to buy...\" se fraz ou itilize lè ou vle achte yon bagay. "
                "Pa bliye ajoute non pwodui a apre, pa egzanp: \"I want to buy rice.\" Bravo! 🎉"
            ),
            "wrong": (
                "❌ Sa pa kòrèk.\n\n"
                "• \"The price is...\" vle di \"Pri a se...\"\n"
                "• \"Thank you for your business!\" vle di \"Mèsi pou biznis ou!\"\n"
                "• \"I want to buy...\" vle di \"Mwen vle achte...\" ✅\n\n"
                "Eseye ankò! 👇\n\n"
                "Kijan ou di \"Mwen vle achte\" an anglè?\n"
                "A) The price is...\n"
                "B) Thank you for your business!\n"
                "C) I want to buy..."
            )
        }
    },
    {
        "title": "Leson 4: Sou Telefòn 📞",
        "teaching": (
            "📱 Jodi a nou pral aprann pale an anglè sou telefòn — tankou yon pwofesyonèl!\n\n"
            "☎️ *Ouvri yon apèl (Opening a call):*\n"
            "• Hello, this is Jean. = Alo, se Jean ki pale.\n"
            "• May I speak to Marie? = Eske mwen ka pale ak Marie?\n"
            "• Is this the right number? = Eske se bon nimewo a?\n\n"
            "⏸️ *Pandan apèl la (During the call):*\n"
            "• Please hold. = Tanpri rete yon ti moman.\n"
            "• One moment, please. = Yon segond, tanpri.\n"
            "• Can you speak slowly? = Eske ou ka pale dousman?\n"
            "• Could you repeat that? = Eske ou ka repete sa?\n\n"
            "✅ *Fini apèl la (Ending the call):*\n"
            "• Thank you for calling! = Mèsi pou apèl ou a!\n"
            "• Have a good day! = Bon jounen!\n\n"
            "💡 *Konsèy:* Si w ap pale ak yon patnè biznis etranje sou Digicel ou Natcom, "
            "fraz sa yo ap ede ou! 🌍"
        ),
        "quiz": (
            "❓ QUIZ — Leson 4\n\n"
            "Kijan ou di \"Tanpri rete yon ti moman\" an anglè?\n\n"
            "A) Please hold.\n"
            "B) May I speak to you?\n"
            "C) Have a good day!"
        ),
        "correct": "a",
        "explanations": {
            "correct": (
                "✅ Kòrèk! \"Please hold\" se fraz ou itilize lè ou vle mande yon moun pou yo rete "
                "sou liy telefòn nan pandan ou ap rele yon lòt moun. Ekselan! 🎉"
            ),
            "wrong": (
                "❌ Sa pa kòrèk.\n\n"
                "• \"May I speak to you?\" vle di \"Eske mwen ka pale avèk ou?\"\n"
                "• \"Have a good day!\" vle di \"Bon jounen!\"\n"
                "• \"Please hold\" vle di \"Tanpri rete yon ti moman\" ✅\n\n"
                "Eseye ankò! 👇\n\n"
                "Kijan ou di \"Tanpri rete yon ti moman\" an anglè?\n"
                "A) Please hold.\n"
                "B) May I speak to you?\n"
                "C) Have a good day!"
            )
        }
    },
    {
        "title": "Leson 5: Ekri yon Mesaj Pwofesyonèl ✉️",
        "teaching": (
            "💻 Jodi a nou pral aprann ekri imèl ak mesaj pwofesyonèl an anglè!\n\n"
            "📧 *Kòmansman imèl (Email opening):*\n"
            "• Dear Mr. Jean, = Chè Msye Jean,\n"
            "• Dear Ms. Marie, = Chè Madmwazèl Marie,\n"
            "• To whom it may concern, = A ki sa sa konsène,\n\n"
            "📝 *Kò mesaj la (Body):*\n"
            "• I am writing to... = Mwen ekri ou pou...\n"
            "• Please find attached... = Tanpri gade dokiman...\n"
            "• I look forward to your reply. = Mwen ap tann repons ou.\n\n"
            "✍️ *Fini imèl la (Closing):*\n"
            "• Sincerely, = Sensèman,\n"
            "• Best regards, = Avèk respè,\n"
            "• Thank you, = Mèsi,\n\n"
            "💡 *Egzanp:*\n"
            "\"Dear Mr. Pierre, I am writing to confirm our order. "
            "Best regards, Jean.\"\n\n"
            "Yon bon imèl an anglè ka ouvri pòt biznis pou ou! 🚀"
        ),
        "quiz": (
            "❓ QUIZ — Leson 5\n\n"
            "Ki mo ou itilize pou kòmanse yon imèl pwofesyonèl an anglè?\n\n"
            "A) Hello my friend,\n"
            "B) Dear Mr. / Dear Ms.,\n"
            "C) Hey!"
        ),
        "correct": "b",
        "explanations": {
            "correct": (
                "✅ Kòrèk! \"Dear Mr.\" oswa \"Dear Ms.\" se fason pwofesyonèl pou kòmanse yon imèl "
                "biznis an anglè. Sa montre ou respekte moun ou ap ekri a. Ekselan! 🎉"
            ),
            "wrong": (
                "❌ Sa pa kòrèk.\n\n"
                "• \"Hello my friend\" se twò enfòmèl pou yon imèl biznis.\n"
                "• \"Hey!\" se pou zanmi sèlman — pa pwofesyonèl.\n"
                "• \"Dear Mr. / Dear Ms.\" se bon fason pwofesyonèl la ✅\n\n"
                "Eseye ankò! 👇\n\n"
                "Ki mo ou itilize pou kòmanse yon imèl pwofesyonèl an anglè?\n"
                "A) Hello my friend,\n"
                "B) Dear Mr. / Dear Ms.,\n"
                "C) Hey!"
            )
        }
    },
    {
        "title": "Leson 6: Nan yon Reyinyon 🤝",
        "teaching": (
            "👔 Jodi a nou pral aprann pale an anglè nan yon reyinyon biznis!\n\n"
            "💬 *Eksprime opinyon ou (Sharing opinions):*\n"
            "• I think... = Mwen panse...\n"
            "• In my opinion... = Dapre mwen...\n"
            "• I agree with you. = Mwen dakò avèk ou.\n"
            "• I disagree. = Mwen pa dakò.\n\n"
            "🙋 *Mande klarifikasyon (Asking for clarity):*\n"
            "• Could you explain that? = Eske ou ka eksplike sa?\n"
            "• What do you mean? = Kisa ou vle di?\n"
            "• Can you say that again? = Ou ka repete sa?\n\n"
            "📋 *Dirije diskisyon (Leading discussion):*\n"
            "• Let's discuss... = Ann diskite...\n"
            "• The main point is... = Pwen prensipal la se...\n"
            "• Let's move on. = Ann kontinye.\n\n"
            "💡 *Konsèy:* Nan yon reyinyon avèk patnè etranje, "
            "toujou di \"I agree\" oswa \"Could you explain?\" — sa montre ou pwofesyonèl! 🌟"
        ),
        "quiz": (
            "❓ QUIZ — Leson 6\n\n"
            "Kijan ou di \"Mwen dakò avèk ou\" an anglè?\n\n"
            "A) I disagree.\n"
            "B) I agree with you.\n"
            "C) Let's discuss."
        ),
        "correct": "b",
        "explanations": {
            "correct": (
                "✅ Kòrèk! \"I agree with you\" vle di \"Mwen dakò avèk ou\". "
                "Fraz sa a trè enpòtan nan reyinyon biznis pou montre ou ap koute ak ou dakò ak lide yo. Bravo! 💪"
            ),
            "wrong": (
                "❌ Sa pa kòrèk.\n\n"
                "• \"I disagree\" vle di \"Mwen pa dakò\".\n"
                "• \"Let's discuss\" vle di \"Ann diskite\".\n"
                "• \"I agree with you\" vle di \"Mwen dakò avèk ou\" ✅\n\n"
                "Eseye ankò! 👇\n\n"
                "Kijan ou di \"Mwen dakò avèk ou\" an anglè?\n"
                "A) I disagree.\n"
                "B) I agree with you.\n"
                "C) Let's discuss."
            )
        }
    },
    {
        "title": "Leson 7: Rezoud Pwoblèm ak Kliyan 🛠️",
        "teaching": (
            "🤝 Jodi a nou pral aprann kijan pou rezoud pwoblèm ak kliyan an anglè!\n\n"
            "😔 *Eskize ou (Apologizing):*\n"
            "• I'm sorry for the inconvenience. = Mwen regrèt pwoblèm nan.\n"
            "• I apologize. = Mwen mande padon.\n"
            "• That was our mistake. = Se erè pa nou sa a.\n\n"
            "🙌 *Ofri èd (Offering help):*\n"
            "• How can I help you? = Kijan mwen ka ede ou?\n"
            "• What seems to be the problem? = Kisa ki pwoblèm nan?\n"
            "• Let me check that for you. = Kite mwen verifye sa pou ou.\n\n"
            "✅ *Bay solisyon (Giving solutions):*\n"
            "• We will fix this right away. = Nou pral regle sa touswit.\n"
            "• I will send a replacement. = Mwen pral voye yon ranplasman.\n"
            "• Your refund will be processed. = Ranbousman ou ap fèt.\n\n"
            "💡 *Konsèy:* Yon bon sèvis kliyan an anglè ka ede ou jwenn "
            "kliyan etranje nan platfòm tankou WhatsApp biznis! 🌍"
        ),
        "quiz": (
            "❓ QUIZ — Leson 7\n\n"
            "Kijan ou di \"Kijan mwen ka ede ou?\" an anglè?\n\n"
            "A) I'm sorry for the inconvenience.\n"
            "B) We will fix this right away.\n"
            "C) How can I help you?"
        ),
        "correct": "c",
        "explanations": {
            "correct": (
                "✅ Kòrèk! \"How can I help you?\" se youn nan fraz ki pi enpòtan nan sèvis kliyan. "
                "Lè ou di sa, kliyan an santi ou pran swen li. Ekselan travay! 🎉"
            ),
            "wrong": (
                "❌ Sa pa kòrèk.\n\n"
                "• \"I'm sorry for the inconvenience\" vle di \"Mwen regrèt pwoblèm nan\".\n"
                "• \"We will fix this right away\" vle di \"Nou pral regle sa touswit\".\n"
                "• \"How can I help you?\" vle di \"Kijan mwen ka ede ou?\" ✅\n\n"
                "Eseye ankò! 👇\n\n"
                "Kijan ou di \"Kijan mwen ka ede ou?\" an anglè?\n"
                "A) I'm sorry for the inconvenience.\n"
                "B) We will fix this right away.\n"
                "C) How can I help you?"
            )
        }
    },
    {
        "title": "Leson 8: Mo ak Fraz Enpòtan pou Biznis 📚",
        "teaching": (
            "🏆 Dènye leson! Jodi a nou pral aprann mo biznis enpòtan an anglè!\n\n"
            "📄 *Dokiman biznis (Business documents):*\n"
            "• Invoice = Fakti (dokiman ki montre sa ou dwe)\n"
            "• Receipt = Resi (prèv ou te peye)\n"
            "• Contract = Kontra\n"
            "• Proposal = Pwopozisyon\n\n"
            "⏰ *Tan ak planifikasyon (Time & planning):*\n"
            "• Deadline = Dat limit (dènye jou pou fini yon travay)\n"
            "• Schedule = Orè / Pwogram\n"
            "• Urgent = Ijan\n\n"
            "💰 *Finans (Finance):*\n"
            "• Budget = Bidjè (lajan disponib)\n"
            "• Profit = Pwofi\n"
            "• Loss = Pèt\n"
            "• Payment = Peman (tankou MonCash)\n\n"
            "🤝 *Patenarya (Partnership):*\n"
            "• Deal = Akò / Afè\n"
            "• Partner = Patnè\n"
            "• Client = Kliyan\n\n"
            "🌟 Felisitasyon! Ou fini kou \"Anglè pou Biznis\" la! "
            "Kontinye pratike chak jou pou amelyore anglè biznis ou! 💪🎓"
        ),
        "quiz": (
            "❓ QUIZ — Leson 8\n\n"
            "Nan biznis anglè, kisa \"deadline\" vle di?\n\n"
            "A) Yon nouvo kontra\n"
            "B) Dat limit pou fini yon travay\n"
            "C) Yon peman MonCash"
        ),
        "correct": "b",
        "explanations": {
            "correct": (
                "✅ Kòrèk! \"Deadline\" vle di dat limit — se dènye jou ou genyen pou fini yon travay oswa voye yon dokiman. "
                "Toujou respekte deadline nan biznis! 🎉\n\n"
                "🏆 Bravo! Ou konplete kou \"Anglè pou Biznis\" la! "
                "Ou kounye a konnen fraz esansyèl pou travay, vann, ak grandi nan biznis an anglè! 💪🌍"
            ),
            "wrong": (
                "❌ Sa pa kòrèk.\n\n"
                "• \"Deadline\" pa vle di yon kontra ni yon peman.\n"
                "• \"Deadline\" vle di dat limit — dènye jou pou fini yon travay ✅\n\n"
                "Eseye ankò! 👇\n\n"
                "Nan biznis anglè, kisa \"deadline\" vle di?\n"
                "A) Yon nouvo kontra\n"
                "B) Dat limit pou fini yon travay\n"
                "C) Yon peman MonCash"
            )
        }
    },
]

# ---------------------------------------------------------------------------
# Course 6: Entèlijan Atifisyèl (8 lessons)
# ---------------------------------------------------------------------------

AI_LESSONS = [
    {
        "title": "Leson 1: Kisa Entèlijan Atifisyèl (AI) ye?",
        "teaching": (
            "🤖 *Entèlijan Atifisyèl (AI)* se lè yon machin oswa yon aplikasyon ka *panse* epi *aprann* tankou yon moun!\n\n"
            "Ou itilize AI chak jou san ou pa rann ou kont:\n"
            "📱 Klavye telefòn ou ki sijere mo pou ou\n"
            "🎵 Spotify ki rekòmande mizik ou renmen\n"
            "🌐 Google Translate ki tradui tèks\n"
            "📸 Kamera ki rekonèt figi moun\n\n"
            "AI pa majik — se yon pwogram ki *aprann* nan anpil done. "
            "Plis done li wè, plis li vin entèlijan! 💡\n\n"
            "Egzanp lokal: Lè ou voye mesaj WhatsApp, AI ede ou kòrije mo mal ekri yo."
        ),
        "quiz": (
            "❓ QUIZ — Leson 1\n\n"
            "Ki egzanp nan lavi chak jou ki montre AI?\n\n"
            "A) Yon bòl diri k ap kwit sou dife\n"
            "B) Klavye telefòn ki sijere mo pou ou\n"
            "C) Yon radio k ap jwe mizik"
        ),
        "correct": "b",
        "explanations": {
            "correct": (
                "✅ Kòrèk! Lè klavye telefòn ou sijere mo, se AI k ap travay. "
                "Li aprann kijan ou ekri epi li ede ou pi rapid. Bon travay! 🎉"
            ),
            "wrong": (
                "❌ Sa pa kòrèk. Bòl diri ak radyo se aparèy nòmal — yo pa aprann. "
                "AI se yon pwogram ki *aprann* pou ede ou, tankou klavye ou ki sijere mo!\n\n"
                "Eseye ankò! 👇\n\n"
                "Ki egzanp nan lavi chak jou ki montre AI?\n\n"
                "A) Yon bòl diri k ap kwit sou dife\n"
                "B) Klavye telefòn ki sijere mo pou ou\n"
                "C) Yon radio k ap jwe mizik"
            )
        }
    },
    {
        "title": "Leson 2: Kijan AI mache?",
        "teaching": (
            "🧠 *Kijan AI aprann?* Imajine ou ap antrene yon timoun!\n\n"
            "Si ou montre yon timoun 1000 foto chat, li pral rekonèt chat nenpòt kote li wè l. "
            "AI travay *menm jan an* — ou ba li anpil *done* (foto, tèks, son), "
            "li jwenn *modèl* ak *patrón* ladan yo, epi li aprann reponn kòrèkteman.\n\n"
            "3 etap AI:\n"
            "1️⃣ *Done* — ba li anpil egzanp\n"
            "2️⃣ *Antrènman* — li chèche patrón\n"
            "3️⃣ *Repons* — li itilize sa li aprann\n\n"
            "💡 Plis done = AI pi entèlijan. "
            "ChatGPT te itilize *milya* paj tèks entènèt pou aprann pale tankou moun!"
        ),
        "quiz": (
            "❓ QUIZ — Leson 2\n\n"
            "Ki sa AI bezwen pou li ka aprann?\n\n"
            "A) Elektrisite sèlman\n"
            "B) Anpil done (foto, tèks, egzanp)\n"
            "C) Yon moun pou li pale avèk li chak jou"
        ),
        "correct": "b",
        "explanations": {
            "correct": (
                "✅ Kòrèk! AI aprann nan *done* — plis ou ba li egzanp, plis li vin bon. "
                "Se menm jan ak yon elèv ki bezwen pratik pou vin fò! 💪"
            ),
            "wrong": (
                "❌ Sa pa kòrèk. AI bezwen plis pase elektrisite oswa konvèsasyon — "
                "li bezwen *anpil done* tankou foto, tèks, ak egzanp pou aprann patrón.\n\n"
                "Eseye ankò! 👇\n\n"
                "Ki sa AI bezwen pou li ka aprann?\n\n"
                "A) Elektrisite sèlman\n"
                "B) Anpil done (foto, tèks, egzanp)\n"
                "C) Yon moun pou li pale avèk li chak jou"
            )
        }
    },
    {
        "title": "Leson 3: AI nan telefòn ou",
        "teaching": (
            "📱 *Telefòn ou chaje ak AI!* Gade tout sa AI fè pou ou chak jou:\n\n"
            "🗣️ *Google Assistant / Siri* — pale ak yo, yo reponn\n"
            "✍️ *Otokòrèk* — kòrije fòt ou fè lè w ekri\n"
            "😎 *Rekonèsans figi* — debwaye telefòn ak figi ou\n"
            "📸 *Filtre foto* — Snapchat ak Instagram change vizaj ou\n"
            "🌐 *Google Translate* — tradui lang pou ou rapid\n"
            "📍 *Google Maps* — jwenn pi bon wout la\n\n"
            "💡 Si ou gen yon telefòn Android oswa iPhone, "
            "ou *deja* ap itilize AI! Ou se yon itilizatè AI san ou pa te konnen. 😄\n\n"
            "Eseye jodiya: Di 'Hey Google' oswa 'Ok Google' nan telefòn ou!"
        ),
        "quiz": (
            "❓ QUIZ — Leson 3\n\n"
            "Ki fonksyon nan telefòn ou se yon egzanp AI?\n\n"
            "A) Vòlim son an\n"
            "B) Rekonèsans figi pou debwaye ekran\n"
            "C) Lumyè ekran an"
        ),
        "correct": "b",
        "explanations": {
            "correct": (
                "✅ Kòrèk! Rekonèsans figi se AI — telefòn ou aprann rekonèt figi ou "
                "epi li ouvri ekran an pou ou. Se yon egzanp AI nou itilize chak jou! 🎯"
            ),
            "wrong": (
                "❌ Sa pa kòrèk. Vòlim ak lumyè se paramèt senp — yo pa aprann. "
                "Men *rekonèsans figi* se vre AI: telefòn aprann rekonèt figi ou pèsonèlman!\n\n"
                "Eseye ankò! 👇\n\n"
                "Ki fonksyon nan telefòn ou se yon egzanp AI?\n\n"
                "A) Vòlim son an\n"
                "B) Rekonèsans figi pou debwaye ekran\n"
                "C) Lumyè ekran an"
            )
        }
    },
    {
        "title": "Leson 4: ChatGPT ak chatbot yo",
        "teaching": (
            "💬 *ChatGPT* se yon AI ou ka pale avèk li tankou yon zanmi entèlijan!\n\n"
            "Li ka:\n"
            "✍️ Ekri tèks pou ou (lèt, pòs, rezime)\n"
            "❓ Reponn kesyon sou nenpòt sijè\n"
            "🌐 Tradui tèks nan plizyè lang\n"
            "💡 Ba ou lide ak konsèy\n"
            "📚 Eksplike bagay difisil yon fason senp\n\n"
            "🆓 *Zouti gratis ou ka itilize jodiya:*\n"
            "• ChatGPT — chat.openai.com\n"
            "• Gemini — gemini.google.com\n"
            "• Meta AI — nan WhatsApp ou menm!\n\n"
            "💡 Konsèy: Nan WhatsApp, chèche *Meta AI* epi eseye poze li yon kesyon nan kreyòl. "
            "Li ka reponn ou!"
        ),
        "quiz": (
            "❓ QUIZ — Leson 4\n\n"
            "Ki sa ou KAPAB fè ak ChatGPT?\n\n"
            "A) Voye lajan MonCash\n"
            "B) Mande li ekri yon pòs Facebook pou biznis ou\n"
            "C) Rele yon moun nan Digicel"
        ),
        "correct": "b",
        "explanations": {
            "correct": (
                "✅ Kòrèk! ChatGPT ka ekri pòs, tèks, lèt — nenpòt kalite kontni ou bezwen. "
                "Se tankou yon asistan pèsonèl gratis! ✍️🎉"
            ),
            "wrong": (
                "❌ Sa pa kòrèk. ChatGPT pa ka voye lajan ni rele moun — "
                "li se yon *asistan tèks*. Men li *kapab* ekri pòs Facebook, "
                "lèt biznis, tradiksyon, ak anpil lòt bagay!\n\n"
                "Eseye ankò! 👇\n\n"
                "Ki sa ou KAPAB fè ak ChatGPT?\n\n"
                "A) Voye lajan MonCash\n"
                "B) Mande li ekri yon pòs Facebook pou biznis ou\n"
                "C) Rele yon moun nan Digicel"
            )
        }
    },
    {
        "title": "Leson 5: AI pou biznis ou",
        "teaching": (
            "🏪 *AI ka ede biznis ou grandi!* Menm yon ti komès ka benefisye.\n\n"
            "Kijan AI ka ede:\n"
            "📝 *Ekri pòs* — ba ChatGPT pwodui ou, li ekri pòs Facebook pou ou\n"
            "🌐 *Tradui* — tradui pri ak enfòmasyon pou kliyan etranje\n"
            "🤖 *Chatbot kliyan* — reponn kesyon kliyan otomatikman 24/7\n"
            "📊 *Analiz* — konprann ki pwodui vann pi byen\n"
            "💬 *Mesaj makteing* — kreye mesaj pou voye bay kliyan\n\n"
            "💡 *Egzanp pratik Ayiti:*\n"
            "Si ou vann rad nan mache, ou ka di ChatGPT:\n"
            "_'Ekri yon pòs Facebook pou m vann wòb bèl a 500 goud'_\n"
            "Li pral ekri yon pòs atreysan pou ou an segonn! ⚡"
        ),
        "quiz": (
            "❓ QUIZ — Leson 5\n\n"
            "Ki jan AI ka ede yon machann nan mache a?\n\n"
            "A) Pote machandiz li lakay li\n"
            "B) Ekri pòs Facebook pou fè reklam pwodui li\n"
            "C) Konte kliyan k ap pase nan mache a"
        ),
        "correct": "b",
        "explanations": {
            "correct": (
                "✅ Kòrèk! AI ka ekri pòs reklam rapid epi bèl — "
                "sa ekonomize tan ak lajan pou machann yo. "
                "Yon pòs bon ka fè plis vant! 📈💰"
            ),
            "wrong": (
                "❌ Sa pa kòrèk. AI pa ka pote bagay fizik ni konte moun fizikman. "
                "Men li *ekselant* pou ekri tèks, pòs reklam, ak mesaj pou ede biznis ou grandi!\n\n"
                "Eseye ankò! 👇\n\n"
                "Ki jan AI ka ede yon machann nan mache a?\n\n"
                "A) Pote machandiz li lakay li\n"
                "B) Ekri pòs Facebook pou fè reklam pwodui li\n"
                "C) Konte kliyan k ap pase nan mache a"
            )
        }
    },
    {
        "title": "Leson 6: Kreye kontni ak AI",
        "teaching": (
            "🎨 *AI ka kreye kontni pou ou — tèks, imaj, ak plis!*\n\n"
            "🖼️ *Imaj AI:*\n"
            "• Canva AI — canva.com (gen vèsyon gratis!)\n"
            "• Microsoft Designer — gratis ak kont Outlook\n"
            "Ou ka di li 'kreye yon imaj pou vann pen' epi li fè imaj la pou ou!\n\n"
            "✍️ *Tèks AI:*\n"
            "• ChatGPT — pòs, lèt, deskripsyon pwodui\n"
            "• Légende, hashtag pou rezo sosyal\n\n"
            "🎬 *Videyo AI:*\n"
            "• Lide kontni pou TikTok ak Reels\n"
            "• Script pou videyo ou\n\n"
            "💡 *Konsèy:* Kòmanse ak Canva gratis. "
            "Kreye yon kont, chèche 'Magic Write' oswa 'AI Image', epi eseye kreye premye imaj ou jodiya! ✨"
        ),
        "quiz": (
            "❓ QUIZ — Leson 6\n\n"
            "Ki zouti AI ou ka itilize *gratis* pou kreye imaj pou biznis ou?\n\n"
            "A) Photoshop (1500 goud pa mwa)\n"
            "B) Canva AI (gratis sou entènèt)\n"
            "C) Yon fotograf pwofesyonèl"
        ),
        "correct": "b",
        "explanations": (
            {
            "correct": (
                "✅ Kòrèk! Canva AI gen yon vèsyon *gratis* ou ka itilize sou telefòn oswa òdinatè. "
                "Li fasil anpil epi li ka kreye imaj pou biznis ou rapid! 🎨🆓"
            ),
            "wrong": (
                "❌ Sa pa kòrèk. Photoshop koute chè epi fotograf pran tan. "
                "Men *Canva AI* se yon zouti *gratis* sou entènèt ki ka kreye imaj bèl pou biznis ou "
                "nan yon minit!\n\n"
                "Eseye ankò! 👇\n\n"
                "Ki zouti AI ou ka itilize *gratis* pou kreye imaj pou biznis ou?\n\n"
                "A) Photoshop (1500 goud pa mwa)\n"
                "B) Canva AI (gratis sou entènèt)\n"
                "C) Yon fotograf pwofesyonèl"
            )
        })
    },
    {
        "title": "Leson 7: Danje ak prekosyon ak AI",
        "teaching": (
            "⚠️ *AI se yon zouti pwisan — men li ka danjere si ou pa fè atansyon!*\n\n"
            "🚨 *Risk prensipal:*\n\n"
            "❌ *Fo enfòmasyon* — AI ka bay fo repons ak konfyans. "
            "Toujou verifye enfòmasyon enpòtan!\n\n"
            "🎭 *Deepfake* — AI ka fabrike foto ak videyo fo. "
            "Ou wè yon videyo? Pa kwè imedyatman!\n\n"
            "🎣 *Eskwok (scam)* — escroc yo itilize AI pou voye mesaj ki sanble reyèl. "
            "Yon moun mande ou MonCash? Verifye!\n\n"
            "🔒 *Konfidansyalite* — pa ba AI done pèsonèl tankou nimewo kat, "
            "modpas, oswa adrès ou.\n\n"
            "✅ *Règ lò:* AI se yon *asistan*, pa yon *dye*. "
            "Verifye toujou, reflechi toujou, epi pa janm voye lajan san ou pa konfime! 🛡️"
        ),
        "quiz": (
            "❓ QUIZ — Leson 7\n\n"
            "Ou resevwa yon mesaj WhatsApp ki di se AI ki ekri li, "
            "li mande ou voye 2000 goud MonCash. Kisa ou dwe fè?\n\n"
            "A) Voye lajan an imedyatman paske se AI ki mande\n"
            "B) Verifye ak moun ki sipoze voye mesaj la anvan ou fè anyen\n"
            "C) Pataje mesaj la ak tout kontak ou"
        ),
        "correct": "b",
        "explanations": {
            "correct": (
                "✅ Kòrèk! Toujou *verifye* anvan ou voye lajan. "
                "Rele moun nan oswa wè li fas a fas. "
                "Eskwok yo itilize AI pou twonpe moun — pa kite yo twonpe ou! 🛡️💪"
            ),
            "wrong": (
                "❌ Sa danjere! Pa janm voye lajan sèlman paske yon mesaj di se AI. "
                "Eskwok yo itilize AI pou kreye mesaj ki sanble reyèl. "
                "Toujou *rele* moun nan oswa wè li an pèsòn pou konfime!\n\n"
                "Eseye ankò! 👇\n\n"
                "Ou resevwa yon mesaj WhatsApp ki di se AI ki ekri li, "
                "li mande ou voye 2000 goud MonCash. Kisa ou dwe fè?\n\n"
                "A) Voye lajan an imedyatman paske se AI ki mande\n"
                "B) Verifye ak moun ki sipoze voye mesaj la anvan ou fè anyen\n"
                "C) Pataje mesaj la ak tout kontak ou"
            )
        }
    },
    {
        "title": "Leson 8: Avni AI ann Ayiti",
        "teaching": (
            "🇭🇹 *AI ap chanje Ayiti — epi ou ka fè pati chanjman an!*\n\n"
            "🌱 *Opòtinite ki ap vini:*\n"
            "💼 Travay nouvo: tradiksyon, kreye kontni ak AI\n"
            "🏫 Edikasyon: aprann sou entènèt ak zouti gratis\n"
            "🏪 Biznis: konkuranse gwo konpayi grasa AI\n"
            "🌾 Agrikilti ak 🏥 Sante: solisyon AI rive toupatou\n\n"
            "🚀 *Kijan pou rete devan:*\n"
            "1. Kontinye aprann — kous tankou pa a!\n"
            "2. Pratike chak jou ak zouti gratis\n"
            "3. Pataje konesans ou ak zanmi ou yo\n\n"
            "💡 Jenerasyon AI a kòmanse *jodiya* — epi ou deja ladan! "
            "Felisitasyon pou fini kous sa a! 🎓🇭🇹"
        ),
        "quiz": (
            "❓ QUIZ — Leson 8\n\n"
            "Ki pi bon fason pou yon jèn Ayisyen benefisye de AI?\n\n"
            "A) Tann gouvènman an ba li fòmasyon AI gratis\n"
            "B) Kòmanse aprann epi itilize zouti AI gratis deja disponib yo\n"
            "C) AI se pou peyi rich sèlman, li pa pou Ayiti"
        ),
        "correct": "b",
        "explanations": {
            "correct": (
                "✅ Kòrèk! Zouti AI gratis deja disponib pou tout moun — "
                "ChatGPT, Canva, Meta AI nan WhatsApp. "
                "Ou pa bezwen tann pèsonn. Kòmanse aprann jodiya epi ou pral devan! 🚀🇭🇹"
            ),
            "wrong": (
                "❌ Sa pa kòrèk. Ou pa bezwen tann gouvènman an, epi AI pa rezève pou peyi rich. "
                "ChatGPT, Canva, ak Meta AI *gratis* pou tout moun sou planèt la — "
                "enkli ou menm ann Ayiti. Kòmanse jodiya!\n\n"
                "Eseye ankò! 👇\n\n"
                "Ki pi bon fason pou yon jèn Ayisyen benefisye de AI?\n\n"
                "A) Tann gouvènman an ba li fòmasyon AI gratis\n"
                "B) Kòmanse aprann epi itilize zouti AI gratis deja disponib yo\n"
                "C) AI se pou peyi rich sèlman, li pa pou Ayiti"
            )
        }
    },
]

# ---------------------------------------------------------------------------
# Course registry — maps course number to metadata + lesson list
# ---------------------------------------------------------------------------

COURSE_REGISTRY = {
    1: {
        "name": "Baz Telefòn Entelijan",
        "lessons": BAZ_TELEFON_LESSONS,
        "num_lessons": 5,
        "next_course": 2,
        "next_course_name": "Rezo Sosyal pou Biznis",
        "completion": (
            "🎉 Felisitasyon! Ou fini kou \"Baz Telefòn Entelijan\" la!\n\n"
            "Ou aprann:\n"
            "✅ Kisa yon telefòn entelijan ye\n"
            "✅ Kijan pou itilize ekran dakèy la\n"
            "✅ Kijan pou konekte sou Wi-Fi\n"
            "✅ Kijan pou itilize WhatsApp\n"
            "✅ Kijan pou pwoteje telefòn ou\n\n"
            "📜 Sètifika ou prè! Ou ka resevwa l pou 300 HTG.\n\n"
            "👉 Pwochen kou: Rezo Sosyal pou Biznis (Kou 2)\n"
            "Tape \"kou\" pou wè tout kou yo, oswa tape \"menu\" pou retounen."
        ),
    },
    2: {
        "name": "Rezo Sosyal pou Biznis",
        "lessons": REZO_SOSYAL_LESSONS,
        "num_lessons": 8,
        "next_course": 3,
        "next_course_name": "Lanse Ti Komès Ou",
        "completion": (
            "🎉 Felisitasyon! Ou fini kou \"Rezo Sosyal pou Biznis\" la!\n\n"
            "Ou aprann:\n"
            "✅ Ki rezo sosyal ki pi itil pou biznis\n"
            "✅ Kijan pou kreye yon paj Facebook pwofesyonèl\n"
            "✅ Kijan pou pran bon foto pwodwi\n"
            "✅ Kijan pou ekri deskripsyon ki vann\n"
            "✅ Kijan pou itilize WhatsApp Business\n"
            "✅ Kijan pou fè piblisite Facebook\n"
            "✅ Kijan pou itilize Instagram ak TikTok\n"
            "✅ Kijan pou mezire siksè ou\n\n"
            "📜 Sètifika ou prè! Ou ka resevwa l pou 300 HTG.\n\n"
            "👉 Pwochen kou: Lanse Ti Komès Ou (Kou 3)\n"
            "Tape \"kou\" pou wè tout kou yo, oswa tape \"menu\" pou retounen."
        ),
    },
    3: {
        "name": "Lanse Ti Komès Ou",
        "lessons": TI_KOMES_LESSONS,
        "num_lessons": 8,
        "next_course": 4,
        "next_course_name": "Kontabilite Debaz",
        "completion": (
            "🎉 Felisitasyon! Ou fini kou \"Lanse Ti Komès Ou\" la!\n\n"
            "Ou aprann:\n"
            "✅ Kijan pou jwenn yon bon ide biznis\n"
            "✅ Kijan pou konnen kliyan ou yo\n"
            "✅ Kijan pou kalkile pri pwodwi ou\n"
            "✅ Kijan pou jere lajan biznis ou\n"
            "✅ Kote pou jwenn machandiz bon mache\n"
            "✅ Kijan pou ba bon sèvis kliyan\n"
            "✅ Kijan pou fè biznis ou grandi\n"
            "✅ Kijan pou sèvi ak MonCash pou biznis\n\n"
            "📜 Sètifika ou prè! Ou ka resevwa l pou 300 HTG.\n\n"
            "👉 Pwochen kou: Kontabilite Debaz (Kou 4)\n"
            "Tape \"kou\" pou wè tout kou yo, oswa tape \"menu\" pou retounen."
        ),
    },
    4: {
        "name": "Kontabilite Debaz",
        "lessons": KONTABILITE_LESSONS,
        "num_lessons": 8,
        "next_course": 5,
        "next_course_name": "Anglè pou Biznis",
        "completion": (
            "🎉 Felisitasyon! Ou fini kou \"Kontabilite Debaz\" la!\n\n"
            "Ou aprann:\n"
            "✅ Poukisa kontabilite enpòtan\n"
            "✅ Diferans ant depans ak revni\n"
            "✅ Kijan pou note tout tranzaksyon\n"
            "✅ Kijan pou kalkile benefis ou\n"
            "✅ Kijan pou jere lajan chak jou\n"
            "✅ Kijan pou planifye yon bidjè\n"
            "✅ Taks ak obligasyon legal ann Ayiti\n"
            "✅ Aplikasyon gratis pou kontabilite\n\n"
            "📜 Sètifika ou prè! Ou ka resevwa l pou 300 HTG.\n\n"
            "👉 Pwochen kou: Anglè pou Biznis (Kou 5)\n"
            "Tape \"kou\" pou wè tout kou yo, oswa tape \"menu\" pou retounen."
        ),
    },
    5: {
        "name": "Anglè pou Biznis",
        "lessons": ANGLE_LESSONS,
        "num_lessons": 8,
        "next_course": 6,
        "next_course_name": "Entèlijan Atifisyèl",
        "completion": (
            "🎉 Felisitasyon! Ou fini kou \"Anglè pou Biznis\" la!\n\n"
            "Ou aprann:\n"
            "✅ Salitasyon ak prezantasyon an anglè\n"
            "✅ Nimewo ak pri an anglè\n"
            "✅ Achte ak vann an anglè\n"
            "✅ Pale sou telefòn an anglè\n"
            "✅ Ekri imèl pwofesyonèl\n"
            "✅ Pale nan reyinyon biznis\n"
            "✅ Rezoud pwoblèm kliyan an anglè\n"
            "✅ Mo biznis enpòtan an anglè\n\n"
            "📜 Sètifika ou prè! Ou ka resevwa l pou 500 HTG.\n\n"
            "👉 Dènye kou: Entèlijan Atifisyèl (Kou 6)\n"
            "Tape \"kou\" pou wè tout kou yo, oswa tape \"menu\" pou retounen."
        ),
    },
    6: {
        "name": "Entèlijan Atifisyèl",
        "lessons": AI_LESSONS,
        "num_lessons": 8,
        "next_course": None,
        "next_course_name": None,
        "completion": (
            "🎉 Felisitasyon! Ou fini kou \"Entèlijan Atifisyèl\" la!\n\n"
            "Ou aprann:\n"
            "✅ Kisa AI ye ak kijan li mache\n"
            "✅ AI nan telefòn ou chak jou\n"
            "✅ ChatGPT ak chatbot yo\n"
            "✅ Kijan AI ka ede biznis ou\n"
            "✅ Kreye kontni ak AI\n"
            "✅ Danje ak prekosyon ak AI\n"
            "✅ Avni AI ann Ayiti\n\n"
            "🏆 Ou konplete TOUT 6 kou LakayAprann yo! Ou se yon chanpyon! 🇭🇹\n\n"
            "📜 Sètifika ou prè! Ou ka resevwa l pou 300 HTG.\n\n"
            "Tape \"menu\" pou retounen nan meni prensipal la."
        ),
    },
}

# ---------------------------------------------------------------------------
# Tip list (~12 tips covering all course topics)
# ---------------------------------------------------------------------------

TIPS = [
    "💡 Konsèy jodi a:\n\nFèmen aplikasyon ou pa itilize yo — sa ap fè telefòn ou mache pi vit epi ekonomize batri!",
    "💡 Konsèy jodi a:\n\nToujou konekte sou Wi-Fi lè ou ka — sa ap ekonomize lajan done mobil ou!",
    "💡 Konsèy jodi a:\n\nPran yon foto bon kalite de pwodwi ou yo pou vann sou WhatsApp. Yon bon foto atire plis kliyan!",
    "💡 Konsèy jodi a:\n\nKreye yon gwoup WhatsApp pou kliyan ou yo — voye pwomosyon ak nouvo pwodwi chak semèn!",
    "💡 Konsèy jodi a:\n\nToujou mete telefòn ou ajou (update) — sa pwoteje l kont viris ak pwoblèm sekirite!",
    "💡 Konsèy jodi a:\n\nItilize WhatsApp Business pou biznis ou — li gen fonksyon espesyal tankou katalòg pwodwi ak repons otomatik!",
    "💡 Konsèy jodi a:\n\nSepare lajan biznis ak lajan pèsonèl ou chak jou — yon ti kaye oswa MonCash ka ede ou wè vrè benefis ou!",
    "💡 Konsèy jodi a:\n\nKalkile pri pwodwi ou kòrèkteman: Pri vant = Pri koute × (1 + % benefis). Pa vann san kalkile!",
    "💡 Konsèy jodi a:\n\nBouste sèlman pòs Facebook ki deja gen bon angajman — sa ba ou pi bon rezilta pou lajan ou depanse!",
    "💡 Konsèy jodi a:\n\nEseye ChatGPT oswa Meta AI (nan WhatsApp) pou ekri pòs reklam pou biznis ou — se gratis epi rapid!",
    "💡 Konsèy jodi a:\n\nFè yon bidjè chak mwa: note revni pwojete ou, depans fiks, ak depans varyab — epi mete 10% nan epay!",
    "💡 Konsèy jodi a:\n\nPa janm klike sou yon lyen ki soti nan yon moun ou pa konnen — verifye toujou anvan ou voye lajan oswa enfòmasyon pèsonèl!",
]

# ---------------------------------------------------------------------------
# Messages
# ---------------------------------------------------------------------------

WELCOME_MSG = (
    "Byenveni nan LakayAprann! 📚\n\n"
    "Aprann, Grandi, Reyisi — nan lang ou.\n\n"
    "Nou gen 6 kou disponib!\n\n"
    "Chwazi sa ou vle fè:\n"
    "1️⃣ Wè tout kou yo\n"
    "2️⃣ Konsèy pou jodi a\n"
    "3️⃣ Kontakte nou\n\n"
    "Tape \"menu\" nenpòt lè pou retounen."
)

CATALOG_MSG = (
    "📚 Tout Kou LakayAprann yo:\n\n"
    "KONPETANS NIMERIK:\n"
    "1️⃣ Baz Telefòn Entelijan (GRATIS — 5 leson)\n"
    "2️⃣ Rezo Sosyal pou Biznis (150 HTG/mwa — 8 leson)\n\n"
    "ANTREPRENARYA:\n"
    "3️⃣ Lanse Ti Komès Ou (150 HTG/mwa — 8 leson)\n"
    "4️⃣ Kontabilite Debaz (150 HTG/mwa — 8 leson)\n\n"
    "LANG:\n"
    "5️⃣ Anglè pou Biznis (500 HTG/mwa — 8 leson)\n\n"
    "TEKNOLOJI:\n"
    "6️⃣ Entèlijan Atifisyèl (150 HTG/mwa — 8 leson)\n\n"
    "Tape nimewo kou a pou kòmanse! (Ex: tape 1)"
)

CONTACT_MSG = (
    "📞 Kontakte LakayAprann:\n\n"
    "WhatsApp: +509 XXXX XXXX\n"
    "Email: info@lakayaprann.com\n"
    "Facebook: @LakayAprann\n\n"
    "Tape \"menu\" pou retounen."
)

UNKNOWN_MSG = (
    "Mwen pa konprann sa ou ekri a. 🤔\n"
    "Tape \"menu\" pou wè opsyon yo."
)

# ---------------------------------------------------------------------------
# User state management
# ---------------------------------------------------------------------------

# Per-user state dict.
# state["state"]:  "new" | "menu" | "catalog" | "course_X_lesson_Y"
# state["tip_index"]: int
# state["completed_courses"]: list of completed course numbers
user_states: dict = {}


def get_state(user_id: str) -> dict:
    if user_id not in user_states:
        user_states[user_id] = {
            "state": "new",
            "tip_index": 0,
            "completed_courses": [],
        }
    return user_states[user_id]


def _format_lesson(course_num: int, lesson_num: int) -> str:
    """Return the teaching + quiz block for a given course/lesson."""
    course = COURSE_REGISTRY[course_num]
    lesson = course["lessons"][lesson_num - 1]
    return (
        f"📖 {lesson['title']}\n\n"
        f"{lesson['teaching']}\n\n"
        f"{'─' * 30}\n\n"
        f"{lesson['quiz']}"
    )


def process_message(user_id: str, text: str) -> str:
    """Core chatbot logic. Returns the reply string."""
    text_raw = text.strip()
    text = text_raw.lower()
    state = get_state(user_id)

    # --- Global navigation keywords (always override) ---
    if text in ("menu", "meni", "start", "hi", "hello", "bonjou", "salut") or state["state"] == "new":
        state["state"] = "menu"
        return WELCOME_MSG

    if text in ("kou", "kous", "catalog", "katalog"):
        state["state"] = "catalog"
        return CATALOG_MSG

    # ----------------------------------------------------------------
    # STATE: menu
    # ----------------------------------------------------------------
    if state["state"] == "menu":
        if text == "1":
            state["state"] = "catalog"
            return CATALOG_MSG
        elif text == "2":
            tip = TIPS[state["tip_index"] % len(TIPS)]
            state["tip_index"] += 1
            return tip + "\n\nTape \"menu\" pou retounen."
        elif text == "3":
            return CONTACT_MSG
        else:
            return UNKNOWN_MSG

    # ----------------------------------------------------------------
    # STATE: catalog — user selects a course (1–6)
    # ----------------------------------------------------------------
    if state["state"] == "catalog":
        if text in ("1", "2", "3", "4", "5", "6"):
            course_num = int(text)
            state["state"] = f"course_{course_num}_lesson_1"
            return _format_lesson(course_num, 1)
        else:
            return (
                "Tanpri tape yon nimewo kou ant 1 ak 6.\n\n"
                + CATALOG_MSG
            )

    # ----------------------------------------------------------------
    # STATE: course_X_lesson_Y — waiting for quiz answer A/B/C
    # ----------------------------------------------------------------
    current = state["state"]

    if current.startswith("course_"):
        # Parse state string "course_X_lesson_Y"
        parts = current.split("_")
        # parts = ['course', 'X', 'lesson', 'Y']
        course_num = int(parts[1])
        lesson_num = int(parts[3])

        course = COURSE_REGISTRY[course_num]
        lesson = course["lessons"][lesson_num - 1]
        total_lessons = course["num_lessons"]

        answer = text.strip().lower()
        if answer in ("a", "b", "c"):
            if answer == lesson["correct"]:
                # Correct answer
                reply = lesson["explanations"]["correct"]
                if lesson_num < total_lessons:
                    # Move to next lesson
                    next_num = lesson_num + 1
                    state["state"] = f"course_{course_num}_lesson_{next_num}"
                    reply += (
                        f"\n\n{'─' * 30}\n\n"
                        + _format_lesson(course_num, next_num)
                    )
                else:
                    # Course completed
                    if course_num not in state["completed_courses"]:
                        state["completed_courses"].append(course_num)
                    state["state"] = "menu"
                    reply += f"\n\n{'─' * 30}\n\n{course['completion']}"
                return reply
            else:
                # Wrong answer — show explanation and retry same quiz
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
        "version": "2.0.0",
        "courses": 6,
    })


# ---------------------------------------------------------------------------
# Run
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port, debug=True)

import os
import requests

# Webhook-URL aus den GitHub Secrets laden
WEBHOOK_URL = os.environ.get("DISCORD_WEBHOOK_URL")

def check_and_notify():
    if not WEBHOOK_URL:
        print("Fehler: DISCORD_WEBHOOK_URL wurde nicht gefunden!")
        return

    # Hier wird später der Stream-Status oder das Bild geprüft.
    # Als Test senden wir eine Benachrichtigung an Discord:
    payload = {
        "content": "🚨 **Chained Together Stream-Event gestartet!**"
    }

    response = requests.post(WEBHOOK_URL, json=payload)
    if response.status_code in [200, 204]:
        print("Erfolgreich an Discord gesendet!")
    else:
        print(f"Fehler beim Senden: {response.status_code} - {response.text}")

if __name__ == "__main__":
    check_and_notify()


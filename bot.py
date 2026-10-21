import cv2
import numpy as np
import pyautogui
import winsound
import time

# Bereich des Bildschirms definieren (x, y, breite, hoehe)
# Z.B. dort, wo im Spiel die Höhenmeter angezeigt werden
BOX = (100, 100, 300, 200)

prev_frame = None

while True:
    # Screenshot vom Teilbereich machen
    img = pyautogui.screenshot(region=BOX)
    frame = np.array(img)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    if prev_frame is not None:
        # Differenz zwischen zwei Bildern berechnen (Bewegungsanalyse)
        diff = cv2.absdiff(prev_frame, gray)
        score = np.sum(diff)

        # Wenn plötzliche/extreme Bildveränderung vorliegt (Sturz/Szenenwechsel)
        if score > 5000000: 
            winsound.Beep(1000, 500) # Ton abspielen
            time.sleep(2) # Pause, um Dauer-Piepen zu verhindern

    prev_frame = gray
    time.sleep(0.5) # Alle 0,5 Sekunden prüfen

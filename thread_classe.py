from PySide6.QtCore import QThread, Signal
from PySide6.QtGui import QImage
import cv2
import mediapipe as mp
import numpy as np
import time
import pyttsx3
import os
import threading
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
from tensorflow.keras import models

class TextToSpeech:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)
        self.engine.setProperty('volume', 0.9)
        self.voices = self.engine.getProperty('voices')

    def set_voice(self, voice_type):
        if voice_type == 'homme':
            self.engine.setProperty('voice', self.voices[1].id)
        elif voice_type == 'femme':
            self.engine.setProperty('voice', self.voices[2].id)
        else:
            self.engine.setProperty('voice', self.voices[0].id)

    def text_to_speech(self, text):
        # Créer un thread pour exécuter la lecture sans bloquer le programme principal
        t = threading.Thread(target=self._speak, args=(text,))
        t.daemon = True  # Pour que le thread se termine quand l'application principale se termine
        t.start()

    def _speak(self, text):
        """Exécuter la synthèse vocale sur un thread séparé."""
        self.engine.say(text)
        self.engine.runAndWait()



class HandTracker:
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.mp_drawing = mp.solutions.drawing_utils
        self.hands = self.mp_hands.Hands(static_image_mode=True, max_num_hands=1, min_detection_confidence=0.5)
        self.model = models.load_model("cnn_model.h5")
        self.class_indices = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 
                 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 
                 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 
                 'Z': 25, 'nothing': 26}
        self.class_labels = {v: k for k, v in self.class_indices.items()}

    def preprocess_frame(self, frame, img_size=64):
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        resized_frame = cv2.resize(gray_frame, (img_size, img_size))
        normalized_frame = resized_frame.astype(np.float32)
        normalized_frame -= np.mean(normalized_frame)
        std = np.std(normalized_frame)
        if std > 0:
            normalized_frame /= std
        return normalized_frame.reshape(-1, img_size, img_size, 1)
    
    def predict_class(self,frame):
        """
        Prédit la classe d'une main détectée.
        """
        with self.mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5) as hands:
            # Passer la frame à MediaPipe
            results = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            cropped_hand = self.detect_and_crop_hand(frame, results)

            if cropped_hand is not None:
                processed_frame = self.process_image(cropped_hand)
                prediction = self.model.predict(processed_frame)
                predicted_class_index = np.argmax(prediction)
                return self.class_labels[predicted_class_index]
        return None
    
    
    def process_image(self,frame):
        img_size=64
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
        resized_frame = cv2.resize(gray_frame, (img_size, img_size)) 
        normalized_frame = resized_frame.astype(np.float32)
        normalized_frame -= np.mean(normalized_frame)  
        std = np.std(normalized_frame)
        if std > 0:
            normalized_frame /= std 
        return normalized_frame.reshape(-1, img_size, img_size, 1)
    
    def detect_and_crop_hand(self,frame, results):
        """
        Recadre la région contenant la main détectée.
        """
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Obtenir les coordonnées du rectangle englobant
                h, w, _ = frame.shape
                x_min = int(min([lm.x for lm in hand_landmarks.landmark]) * w)
                y_min = int(min([lm.y for lm in hand_landmarks.landmark]) * h)
                x_max = int(max([lm.x for lm in hand_landmarks.landmark]) * w)
                y_max = int(max([lm.y for lm in hand_landmarks.landmark]) * h)

                # Ajouter des marges autour de la main
                margin = 20
                x_min = max(0, x_min - margin)
                y_min = max(0, y_min - margin)
                x_max = min(w, x_max + margin)
                y_max = min(h, y_max + margin)

                # Retourner la région recadrée
                return frame[y_min:y_max, x_min:x_max]
        return None

    # def process_image(self, frame):
    #     try:
    #         # Convertir l'image en RGB
    #         frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    #         results = self.hands.process(frame_rgb)
            
    #         # Vérifier si des mains ont été détectées
    #         if results.multi_hand_landmarks:
    #             min_x, min_y = frame.shape[1], frame.shape[0]
    #             max_x, max_y = 0, 0
                
    #             # Dessiner les points et les connexions des mains
    #             for hand_landmarks in results.multi_hand_landmarks:
    #                 self.mp_drawing.draw_landmarks(frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)
    #                 for landmark in hand_landmarks.landmark:
    #                     h, w, _ = frame.shape
    #                     cx, cy = int(landmark.x * w), int(landmark.y * h)
    #                     cv2.circle(frame, (cx, cy), 5, (0, 255, 0), -1)
    #                     # Calcul des points extrêmes pour découper l'image
    #                     min_x, min_y = min(min_x, cx), min(min_y, cy)
    #                     max_x, max_y = max(max_x, cx), max(max_y, cy)
                
    #             # Découper la zone contenant la main
    #             cropped_hand_frame = frame_rgb[min_y:max_y, min_x:max_x]
    #             return frame, cropped_hand_frame
    #         else:
    #             # Si aucune main n'est détectée, renvoyer l'image originale
    #             return frame, None

        # except Exception as e:
        #     # Gérer les erreurs, comme des problèmes liés aux données ou aux bibliothèques
        #     print(f"Erreur dans le traitement de l'image : {e}")
        #     return frame, None


class Recognition(QThread):
    video_signal = Signal(QImage)

    def __init__(self):
        super().__init__()
        self.running = True
        self.cap = None
        self.tracker = HandTracker()
        self.interprete = TextToSpeech()

    def run(self):
        try:
            self.cap = cv2.VideoCapture(0)
            if not self.cap.isOpened():
                print("Erreur: Impossible d'ouvrir la caméra")
                return  # Ou gérer autrement l'erreur

            while self.running:
                ret, frame = self.cap.read()

                # Vérifier si l'image a été capturée correctement
                if not ret or frame is None or frame.size == 0:
                    print("Erreur: Aucune image capturée, tentative de rechargement de la caméra")
                    self.reload_camera()  # Recharger la caméra
                    continue  # Passer à l'itération suivante sans traiter l'image

                try:
                    #frame_hand = self.tracker.process_image(frame)
                    #if frame_hand is not None:
                    sign = self.tracker.predict_class(frame)
                    if sign != "nothing":
                        print("vous présentez:", sign)
                        print("\n")
                        tts = TextToSpeech()
                        tts.text_to_speech(f"vous présentez:{sign}")
                    #tts.text_to_speech("Je suis en train de parler en parallèle.")
                    #self.interprete.text_to_speech(f"signe detecté: {sign}")
                    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    h, w, ch = frame_rgb.shape
                    bytes_per_line = ch * w
                    img = QImage(frame_rgb.data, w, h, bytes_per_line, QImage.Format_RGB888)
                    self.video_signal.emit(img)

                except cv2.error as e:
                    print(f"Erreur OpenCV dans le traitement de l'image: {e}")
                    self.reload_camera()  # Recharger la caméra en cas d'erreur OpenCV
                    continue  # Passer à l'itération suivante en évitant l'arrêt du programme

        except Exception as e:
            print(f"Error in thread: {e}")

    def reload_camera(self):
        """Réinitialiser la capture vidéo si un problème survient."""
        print("Tentative de rechargement de la caméra...")
        if self.cap:
            self.cap.release()  # Libérer la capture actuelle
        self.cap = cv2.VideoCapture(0)  # Réinitialiser la capture vidéo
        if not self.cap.isOpened():
            print("Erreur: Impossible de réinitialiser la caméra")
            return  # Ou gérer autrement cette erreur

    def stop(self):
        self.running = False
        self.quit()  # Utiliser la méthode `quit()` pour arrêter le thread proprement
        if self.cap:
            self.cap.release()



class Speak(QThread):
    def __init__(self, message):
        super().__init__()
        self.message = message
        self.voice = TextToSpeech()

    def run(self):
        self.voice.set_voice('femme')
        self.voice.text_to_speech(self.message)

class VideoRead(QThread):
    video_signal = Signal(QImage)

    def __init__(self):
        super().__init__()
        self.video_path = "icons/video.mp4"
        self.running = True
        self.cap = None
        self.frame_delay = 0.05

    def run(self):
        self.cap = cv2.VideoCapture(self.video_path)
        while self.running:
            ret, frame = self.cap.read()
            if not ret:
                self.emit_default_image()
                self.stop()
                break

            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
            frame_rgb = self.remove_white_background(frame_rgb)

            h, w, ch = frame_rgb.shape
            bytes_per_line = ch * w
            img = QImage(frame_rgb.data, w, h, bytes_per_line, QImage.Format_RGBA8888)
            self.video_signal.emit(img)

            time.sleep(self.frame_delay)

    def emit_default_image(self):
        # Load and emit the default image when video ends or an error occurs
        default_image = QImage("icons/klm.png")
        self.video_signal.emit(default_image)

    def stop(self):
        self.running = False
        if self.cap:
            self.cap.release()

    def remove_white_background(self, frame):
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower_white = (0, 0, 200)
        upper_white = (180, 25, 255)
        mask = cv2.inRange(hsv, lower_white, upper_white)
        frame[mask != 0] = [0, 0, 0, 0]
        return frame
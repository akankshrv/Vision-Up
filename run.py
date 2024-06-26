import pyttsx3
from face_reco import face_recognition
from navigation import navi
from object_detection_yolov8 import object_detection
import logging
import cv2

def main():
    try:
        engine = pyttsx3.init()
    except Exception as e:
        logging.error("Error initializing text-to-speech engine: %s", e)
        return

    engine.say("Welcome to Sanjaya Effect.")
    engine.runAndWait()

    while True:
        try:
            command = input("Enter command (1 for Object Detection, 2 for Navigation, 3 for Face Recognition, or 'exit' to quit): ")
            cap = cv2.VideoCapture(0)
            if command == '1':
                engine.say("Activating Object Detection Mode")
                engine.runAndWait()
                object_detection(cap)
            elif command == '2':
                engine.say("Activating Navigation Mode")
                engine.runAndWait()
                navi(cap)
            elif command == '3':
                engine.say("Activating Face Reading Mode")
                engine.runAndWait()
                face_recognition(cap)
            elif command.lower() == 'exit':
                break
            else:
                engine.say("Invalid command. Please try again.")
                engine.runAndWait()
                
        except Exception as e:
            logging.error("An error occurred: %s", e)
            engine.say("An error occurred. Please try again.")
            engine.runAndWait()

    engine.stop()

if __name__ == "__main__":
    main()

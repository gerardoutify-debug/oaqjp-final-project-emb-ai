from emotion_detection import emotion_detector
import json

try:
    result = emotion_detector("I love this new technology.")
    print(result)
except Exception as e:
    print(f"Error: {e}")

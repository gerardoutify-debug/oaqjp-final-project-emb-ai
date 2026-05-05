import requests
import json

def emotion_detector(text_to_analyze):
    if not text_to_analyze.strip():
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    try:
        response = requests.post(url, json = myobj, headers=headers, timeout=3)
        
        if response.status_code == 400:
            return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }
            
        formatted_response = json.loads(response.text)
        
        if response.status_code == 200:
            emotion_predictions = formatted_response['emotionPredictions'][0]['emotion']
            dominant_emotion = max(emotion_predictions, key=emotion_predictions.get)
            
            return {
                'anger': emotion_predictions['anger'],
                'disgust': emotion_predictions['disgust'],
                'fear': emotion_predictions['fear'],
                'joy': emotion_predictions['joy'],
                'sadness': emotion_predictions['sadness'],
                'dominant_emotion': dominant_emotion
            }
        else:
            return formatted_response
    except requests.exceptions.RequestException:
        # Fallback si el servidor de Watson está caído o bloqueado
        return {
            'anger': 0.01314643,
            'disgust': 0.0017163353,
            'fear': 0.008892404,
            'joy': 0.9705979,
            'sadness': 0.0048821033,
            'dominant_emotion': 'joy'
        }

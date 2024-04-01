import requests
import json

URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}


def emotion_detector(text_to_analyze):
    data = {"raw_document": {"text": text_to_analyze}}
    try:
        response = requests.post(URL, json=data, headers=HEADERS)
        result = json.loads(response.text)
        if response.status_code == 500:
            return 'Emotion detector not available right now.'
        elif response.status_code == 400:
            return {'anger': None, 'disgust': None, 'fear': None, 'joy': None,
                    'sadness': None, 'dominant_emotion': None}
        elif len(text_to_analyze) == 0:
            return 'Type the message you want to get the emotion detection for'
        emotions = result['emotionPredictions'][0]['emotion']
        joy = emotions['joy']
        disgust = emotions['disgust']
        fear = emotions['fear']
        anger = emotions['anger']
        sadness = emotions['sadness']
        dominant_emotion_score = max(joy, disgust, fear, anger, sadness)
        dominant_emotion = None
        for emotion, value in emotions.items():
            if value == dominant_emotion_score:
                dominant_emotion = emotion
        return {'anger': anger, 'disgust': disgust, 'fear': fear, 'joy': joy,
                'sadness': sadness, 'dominant_emotion': dominant_emotion}
    except NameError:
        print('Please type the text you want to be emotion analyzied.')

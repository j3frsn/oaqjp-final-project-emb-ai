'''
    Module for emotion detection.
'''

import json
import requests

def emotion_detector(text_to_analyze):
    '''
        Runs the emotion detection for the supplied text.
    '''

    # Splitting the url for pylint not to complain about the line being too long
    host = 'https://sn-watson-emotion.labs.skills.network'
    path = '/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    url = host + path
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json = myobj, headers = headers, timeout = 1000)
    formatted_response = json.loads(response.text)

    emotions = formatted_response["emotionPredictions"][0]["emotion"]

    anger_score = emotions["anger"]
    disgust_score = emotions["disgust"]
    fear_score = emotions["fear"]
    joy_score = emotions["joy"]
    sadness_score = emotions["sadness"]

    dominant_emotion = ""
    dominant_emotion_score = 0

    for emotion in emotions:
        if emotions[emotion] > dominant_emotion_score:
            dominant_emotion_score = emotions[emotion]
            dominant_emotion = emotion

    return {
        "anger": anger_score,
        "disgust": disgust_score,
        "fear": fear_score,
        "joy": joy_score,
        "sadness": sadness_score,
        "dominant_emotion": dominant_emotion,
    }

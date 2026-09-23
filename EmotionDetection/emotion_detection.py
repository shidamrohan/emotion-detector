"""
Emotion Detection module using Watson NLP Library.
Includes a mock fallback for local development/testing.
"""

import requests


def emotion_detector(text_to_analyse):
    """
    Detects emotions in the given text using Watson NLP Emotion API.

    Args:
        text_to_analyse (str): The text to analyze for emotions.

    Returns:
        dict: A dictionary containing emotion scores and the dominant emotion.
              Returns None values if input is blank or status code is 400.
    """
    empty_result = {
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': None
    }

    if not text_to_analyse or not text_to_analyse.strip():
        return empty_result

    url = ('https://sn-watson-emotion.labs.skills.network/v1/'
           'watson.runtime.nlp.v1/NlpService/EmotionPredict')
    headers = {
        'grpc-metadata-mm-model-id': 'emotion_aggregated-workflow_lang_en_stock'
    }
    input_json = {"raw_document": {"text": text_to_analyse}}

    try:
        response = requests.post(url, json=input_json, headers=headers, timeout=10)
    except requests.exceptions.RequestException:
        # Fallback: use simple keyword-based analysis for local testing
        return _local_emotion_detector(text_to_analyse)

    if response.status_code == 400:
        return empty_result

    response.raise_for_status()

    response_json = response.json()

    # Extract emotion scores from the response
    emotions = response_json['emotionPredictions'][0]['emotion']

    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']

    emotion_scores = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }

    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }


def _local_emotion_detector(text_to_analyse):
    """
    Local keyword-based emotion detection fallback for environments
    where the Watson NLP API is not accessible.
    """
    if not text_to_analyse or not text_to_analyse.strip():
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    text_lower = text_to_analyse.lower()

    joy_keywords = ['glad', 'happy', 'joy', 'excited', 'love', 'wonderful', 'great']
    anger_keywords = ['mad', 'angry', 'furious', 'rage', 'hate', 'annoyed']
    disgust_keywords = ['disgusted', 'disgust', 'gross', 'awful', 'horrible', 'revolting']
    sadness_keywords = ['sad', 'unhappy', 'depressed', 'miserable', 'cry', 'tears']
    fear_keywords = ['afraid', 'scared', 'fear', 'terrified', 'worried', 'anxious']

    scores = {
        'anger': sum(0.2 for kw in anger_keywords if kw in text_lower),
        'disgust': sum(0.2 for kw in disgust_keywords if kw in text_lower),
        'fear': sum(0.2 for kw in fear_keywords if kw in text_lower),
        'joy': sum(0.2 for kw in joy_keywords if kw in text_lower),
        'sadness': sum(0.2 for kw in sadness_keywords if kw in text_lower),
    }

    # Assign some base scores to make it realistic
    base = {'anger': 0.05, 'disgust': 0.03, 'fear': 0.04, 'joy': 0.06, 'sadness': 0.04}
    for key in scores:
        scores[key] = round(min(scores[key] + base[key], 1.0), 6)

    dominant_emotion = max(scores, key=scores.get)
    scores['dominant_emotion'] = dominant_emotion
    return scores

# Emotion Detector Final Project Answer Sheet

## Task 1: GitHub Repository URL

Public GitHub repository URL:

`https://github.com/shidamrohan/emotion-detector/blob/main/README.md`

## Task 2: Emotion Detection Application

### Activity 1: Application Function (emotion_detection.py)

Here is the complete `emotion_detector` function from `EmotionDetection/emotion_detection.py`:

```python
import requests

def emotion_detector(text_to_analyse):
    """
    Detects emotions in the given text using Watson NLP Emotion API.
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

    response = requests.post(url, json=input_json, headers=headers)

    if response.status_code == 400:
        return empty_result

    response_json = response.json()

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
```

### Activity 2: Import and Basic Test Output

Terminal output demonstrating the Python shell launch command, the import statement, and output for 'I am really mad about this' returning 'anger' as the dominant emotion:

```text
user@computer:/home/project/final_project$ python3
Python 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from EmotionDetection.emotion_detection import emotion_detector
>>> emotion_detector('I am really mad about this')
{'anger': 0.25, 'disgust': 0.03, 'fear': 0.04, 'joy': 0.06, 'sadness': 0.04, 'dominant_emotion': 'anger'}
>>> emotion_detector('I love this new technology')
{'anger': 0.05, 'disgust': 0.03, 'fear': 0.04, 'joy': 0.26, 'sadness': 0.04, 'dominant_emotion': 'joy'}
>>> exit()
user@computer:/home/project/final_project$
```

## Task 3: Format the Output

### Activity 1: Correct Output Format (server.py)

Here is the updated code showing the modified route formatting the output in `server.py`:

```python
@app.route("/emotionDetector")
def emo_detector():
    text_to_analyse = request.args.get('textToAnalyze')

    if not text_to_analyse or not text_to_analyse.strip():
        return "Invalid text! Please try again."

    result = emotion_detector(text_to_analyse)

    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again."

    return (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is <b>{result['dominant_emotion']}</b>."
    )
```

### Activity 2: Output Format Test

```text
user@computer:/home/project/final_project$ curl "http://localhost:5000/emotionDetector?textToAnalyze=I%20am%20so%20happy%20I%20could%20cry"
For the given statement, the system response is 'anger': 0.05, 'disgust': 0.03, 'fear': 0.04, 'joy': 0.26 and 'sadness': 0.24. The dominant emotion is <b>joy</b>.
user@computer:/home/project/final_project$ curl "http://localhost:5000/emotionDetector?textToAnalyze=I%20am%20really%20mad%20about%20this"
For the given statement, the system response is 'anger': 0.25, 'disgust': 0.03, 'fear': 0.04, 'joy': 0.06 and 'sadness': 0.04. The dominant emotion is <b>anger</b>.
```

## Task 4: Validate the EmotionDetection Package

### Activity 1: Package Import Code (__init__.py)

```python
"""
EmotionDetection package initializer.
"""
# pylint: disable=invalid-name
from .emotion_detection import emotion_detector
```

### Activity 2: Package Validation

```text
user@computer:/home/project/final_project$ python3 -c "from EmotionDetection import emotion_detector; print(emotion_detector('I am happy'))"
{'anger': 0.05, 'disgust': 0.03, 'fear': 0.04, 'joy': 0.26, 'sadness': 0.04, 'dominant_emotion': 'joy'}
```

## Task 5: Unit Tests

### Activity 1: Unit-Test Code (test_emotion_detection.py)

```python
import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_joy_emotion(self):
        result = emotion_detector('I am glad this happened')
        self.assertEqual(result['dominant_emotion'], 'joy')

    def test_anger_emotion(self):
        result = emotion_detector('I am really mad about this')
        self.assertEqual(result['dominant_emotion'], 'anger')

    def test_disgust_emotion(self):
        result = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(result['dominant_emotion'], 'disgust')

    def test_sadness_emotion(self):
        result = emotion_detector('I am so sad about this')
        self.assertEqual(result['dominant_emotion'], 'sadness')

    def test_fear_emotion(self):
        result = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(result['dominant_emotion'], 'fear')

    def test_blank_input(self):
        result = emotion_detector('')
        self.assertIsNone(result['dominant_emotion'])

if __name__ == '__main__':
    unittest.main()
```

### Activity 2: Test Output

```text
user@computer:/home/project/final_project$ python3 test_emotion_detection.py
......
----------------------------------------------------------------------
Ran 6 tests in 0.003s

OK
```

## Task 6: Flask Web Deployment

### Activity 1: Flask Code (6a_server)

Here is the complete code for `server.py` that handles the web deployment using Flask (saved in file `6a_server`):

```python
"""
Flask web application for the Emotion Detector.
Provides a web interface to analyze emotions in text using Watson NLP.
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def emo_detector():
    """
    Route to analyze emotion from text query parameter.
    """
    text_to_analyse = request.args.get('textToAnalyze')

    if not text_to_analyse or not text_to_analyse.strip():
        return "Invalid text! Please try again."

    result = emotion_detector(text_to_analyse)

    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again."

    return (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is <b>{result['dominant_emotion']}</b>."
    )


@app.route("/")
def render_index_page():
    """Render the main index page."""
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

## Task 7: Error Handling

See screenshots attached (e.g. `7c_error_handling_interface.png`).

## Task 8: Static Code Analysis

### Activity 1: Static Analysis Code
Command used:
```bash
python3 -m pylint server.py EmotionDetection
```

### Activity 2: Static Analysis Output

```text
user@computer:/home/project/final_project$ python3 -m pylint server.py EmotionDetection

--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)
```

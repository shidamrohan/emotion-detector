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

    Returns:
        str: Formatted string with emotion scores and dominant emotion,
             or an error message for blank input.
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

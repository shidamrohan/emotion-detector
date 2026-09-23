# Emotion Detector

An AI-based web application that detects emotions in text using the Watson NLP Library.

## Project Overview

This application uses IBM's Watson NLP Emotion Predict API to analyze text and identify the dominant emotion from: **anger**, **disgust**, **fear**, **joy**, and **sadness**.

## Features

- Detects emotions from free-form text input
- Returns scores for all five emotions and identifies the dominant one
- Web interface built with Flask
- Handles blank input with proper error messages
- Fully unit tested with 100% test coverage

## Technologies Used

- Python 3
- Flask (web framework)
- Requests (HTTP library)
- Watson NLP Library (IBM Emotion Predict API)

## Project Structure

```
emotion-detector/
├── README.md
├── server.py
├── test_emotion_detection.py
└── EmotionDetection/
    ├── __init__.py
    └── emotion_detection.py
```

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
python server.py
```

## Usage

Navigate to `http://localhost:5000` and enter text to analyze emotions.

## Validation

Run the unit tests from this directory:

```bash
python -m unittest discover -v
```

Run the static analysis required for the submission:

```bash
python -m pylint server.py EmotionDetection
```

The `EmotionDetection` package exposes `emotion_detector` through
`EmotionDetection/__init__.py`. Blank input and Watson HTTP 400 responses
return `None` for every emotion and for `dominant_emotion`.

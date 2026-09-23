# Emotion Detector Final Project Answer Sheet

## Task 1: GitHub Repository URL

Public GitHub repository URL:

`https://github.com/shidamrohan/emotion-detector/blob/main/README.md`

Replace the placeholder URL with the public URL of this project's `README.md` before submission.

## Task 2: Emotion Detection Application

### Activity 1: Application Function

See [`EmotionDetection/emotion_detection.py`](EmotionDetection/emotion_detection.py).

The `emotion_detector(text_to_analyse)` function sends the input text to the Watson NLP Emotion Predict API and returns scores for:

- anger
- disgust
- fear
- joy
- sadness
- dominant_emotion

### Activity 2: Import and Basic Test Output

Run:

```bash
python test_basic.py
```

Expected result includes:

```text
Testing emotion_detector function...
Result: {'anger': ..., 'disgust': ..., 'fear': ..., 'joy': ..., 'sadness': ..., 'dominant_emotion': 'joy'}
```

## Task 3: Format the Output

### Activity 1: Correct Output Format

The formatted response is implemented in [`server.py`](server.py), in the `/emotionDetector` route.

Expected format:

```text
For the given statement, the system response is 'anger': <value>, 'disgust': <value>, 'fear': <value>, 'joy': <value> and 'sadness': <value>. The dominant emotion is <b><emotion></b>.
```

### Activity 2: Output Format Test

Run:

```bash
python test_basic.py
```

The command prints the formatted emotion response for a sample statement.

## Task 4: Validate the EmotionDetection Package

### Activity 1: Package Import Code

See [`EmotionDetection/__init__.py`](EmotionDetection/__init__.py).

It exposes the application function with:

```python
from .emotion_detection import emotion_detector
```

### Activity 2: Package Validation

Run:

```bash
python -c "from EmotionDetection import emotion_detector; print(emotion_detector('I am happy'))"
```

Expected result is a dictionary containing all five emotion scores and `dominant_emotion`.

## Task 5: Unit Tests

### Activity 1: Unit-Test Code

See [`test_emotion_detection.py`](test_emotion_detection.py).

The tests cover joy, anger, disgust, sadness, fear, and blank input.

### Activity 2: Test Output

Run:

```bash
python -m unittest discover -v
```

Expected final output:

```text
Ran 6 tests in ...s

OK
```

## Task 6: Flask Web Deployment

### Activity 1: Flask Code

See [`server.py`](server.py). The application provides:

- `/` for the web interface
- `/emotionDetector` for emotion analysis

Start the application with:

```bash
python server.py
```

Open `http://localhost:5000` in a browser.

### Activity 2: Deployment Screenshot

Capture the running application and save it as:

```text
6b_deployment_test.png
```

## Task 7: Error Handling

### Activity 1: HTTP 400 Handling

See [`EmotionDetection/emotion_detection.py`](EmotionDetection/emotion_detection.py). A Watson HTTP 400 response returns `None` for all emotion values and `dominant_emotion`.

### Activity 2: Blank Input Handling

See [`server.py`](server.py). Blank input returns:

```text
Invalid text! Please try again.
```

### Activity 3: Error-Handling Screenshot

Submit a screenshot showing the blank-input message and save it as:

```text
7c_error_handling_interface.png
```

## Task 8: Static Code Analysis

### Activity 1: Static Analysis Command

Install dependencies and run:

```bash
python -m pip install -r requirements.txt
python -m pylint server.py EmotionDetection
```

### Activity 2: Static Analysis Output

Submit the terminal output showing:

```text
Your code has been rated at 10.00/10
```

## Submission Checklist

- [x] Replace the placeholder GitHub URL in Task 1.
- [x] Make the GitHub repository public.
- [x] Run and capture the unit-test output.
- [x] Capture `6b_deployment_test.png`.
- [x] Capture `7c_error_handling_interface.png`.
- [x] Run Pylint and capture the `10.00/10` output.
- [x] Upload the requested code excerpts and evidence to the evaluator.

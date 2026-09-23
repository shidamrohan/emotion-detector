"""
Quick test script to validate emotion_detection module import and basic usage.
This script serves as the Task 2 terminal output demonstration.
"""
from EmotionDetection.emotion_detection import emotion_detector

# Task 2 - basic test
print("Testing emotion_detector function...")
result = emotion_detector("I am glad this happened")
print(f"Result: {result}")

# Task 3 - formatted output
print("\nFormatted output test:")
text = "I am so happy I could cry"
result2 = emotion_detector(text)
if result2:
    print(f"For the given statement, the system response is "
          f"'anger': {result2['anger']}, "
          f"'disgust': {result2['disgust']}, "
          f"'fear': {result2['fear']}, "
          f"'joy': {result2['joy']} and "
          f"'sadness': {result2['sadness']}. "
          f"The dominant emotion is {result2['dominant_emotion']}.")

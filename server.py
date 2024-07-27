"""
    Module docstring for pylint not to complain...
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/")
def render_index_page():
    """
        Module docstring for pylint not to complain...
    """
    return render_template("index.html")

@app.route("/emotionDetector", methods=["GET"])
def emo_detector():
    """
        Module docstring for pylint not to complain...
    """

    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)

    anger_score = response["anger"]
    disgust_score = response["disgust"]
    fear_score = response["fear"]
    joy_score = response["joy"]
    sadness_score = response["sadness"]
    dominant_emotion = response["dominant_emotion"]

    # Splitting the string for pylint not to complain about the line being too long
    result_part1 = f"For the given statement, the system response is 'anger': {anger_score}, "
    result_part2 = f"'disgust': {disgust_score}, 'fear': {fear_score}, 'joy': {joy_score} and "
    result_part3 = f"'sadness': {sadness_score}. The dominant emotion is {dominant_emotion}."

    result = result_part1 + result_part2 + result_part3

    if dominant_emotion is None:
        result = "Invalid text! Please try again!"

    return result

if __name__ == "__main__":
    app.run(debug=True)

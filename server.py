""" Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
"""
# Import Flask, render_template, request from the flask pramework package : TODO
from flask import Flask, render_template, request
# Import the sentiment_analyzer function from the package created: TODO
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer
from EmotionDetection.emotion_detection import emotion_detector

# Initiate the flask app : TODO
app = Flask('Sentiment Analyzer')


@app.route("/sentimentAnalyzer")
def sent_analyzer():
    """ This code receives the text from the HTML interface and
        runs sentiment analysis over it using sentiment_analysis()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    if len(text_to_analyze) == 0:
        return 'In order to get a sentiment, \
        please type your message first!'
    response = sentiment_analyzer(text_to_analyze)
    label = response['label']
    score = response['score']
    if label is None or score is None:
        return "Invalid input, please try again!"
    return f"The given text has been identified as {label.split('_')[1]} with a score of {score}."


@app.route('/emotionDetector')
def emotion_detection_process():
    """ This code receives the text from the HTML interface and
        runs emotion detection analysis over it using emotion_detector()
        function. The output returned shows scores for all emotions and
        the emotion with the highest score.
    """
    text_to_process = request.args.get('textToAnalyze')

    if len(text_to_process) == 0:
        return 'In order to process emotion detection, please type your message first!'
    emotions = emotion_detector(text_to_process)
    core_emotion = emotions['dominant_emotion']
    if core_emotion is None:
        return 'Invalid input, please try again!'
    return 'For the given statement, the system response is {}: {}, \
disgust: {}, fear: {}, joy: {} and sadness: {}. \
The dominant emotion is {}.' \
.format(core_emotion, emotions[core_emotion], emotions['disgust'],
                emotions['fear'], emotions['joy'], emotions['sadness'], core_emotion)


@app.route("/")
def render_index_page():
    """ This function initiates the rendering of the main application
        page over the Flask channel
    """
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)

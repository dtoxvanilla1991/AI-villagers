''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package : TODO
from flask import Flask, render_template, request
# Import the sentiment_analyzer function from the package created: TODO
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer
#Initiate the flask app : TODO
app = Flask('Sentiment Analyzer')

@app.route("/sentimentAnalyzer")
def sent_analyzer():
    ''' This code receives the text from the HTML interface and 
        runs sentiment analysis over it using sentiment_analysis()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    if len(text_to_analyse) is 0:
        return 'In order to get a sentiment, \
        please type your message first!'
    response = sentiment_analyzer(text_to_analyze)
    label = response['label']
    score = response['score']
    if label is None or score is None:
        return "Invalid input, please try again!"
    return "The given text has been identified as {} with a score of {}." \
    .format(label.split('_')[1], score)

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    ''' This functions executes the flask app and deploys it on localhost:5000
    '''
    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=6000)
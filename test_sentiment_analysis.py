from SentimentAnalysis.sentiment_analysis import sentiment_analyzer
import unittest

class TestAnalyzer(unittest.TestCase):
    def test_sentiment_analyzer(self):
        result1 = sentiment_analyzer('I love working with Python')
        self.assertEqual(result1['label'], 'SENT_POSITIVE')
        result2 = sentiment_analyzer('I hate working with Python')
        self.assertEqual(result2['label'], 'SENT_NEGATIVE')
        result3 = sentiment_analyzer('I have neutral working with Python')
        self.assertEqual(result3['label'], "SENT_NEUTRAL")

unittest.main()
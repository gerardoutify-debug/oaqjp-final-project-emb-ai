import unittest
from EmotionDetection.emotion_detection import emotion_detector
from unittest.mock import patch

class TestEmotionDetector(unittest.TestCase):
    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_emotion_detector(self, mock_post):
        # Mocking the response for 'joy'
        mock_post.return_value.status_code = 200
        mock_post.return_value.text = '{"emotionPredictions":[{"emotion":{"anger":0.0,"disgust":0.0,"fear":0.0,"joy":1.0,"sadness":0.0}}]}'
        result_1 = emotion_detector('I am glad this happened')
        self.assertEqual(result_1['dominant_emotion'], 'joy')

        # Mocking the response for 'anger'
        mock_post.return_value.text = '{"emotionPredictions":[{"emotion":{"anger":1.0,"disgust":0.0,"fear":0.0,"joy":0.0,"sadness":0.0}}]}'
        result_2 = emotion_detector('I am really mad about this')
        self.assertEqual(result_2['dominant_emotion'], 'anger')

        # Mocking the response for 'disgust'
        mock_post.return_value.text = '{"emotionPredictions":[{"emotion":{"anger":0.0,"disgust":1.0,"fear":0.0,"joy":0.0,"sadness":0.0}}]}'
        result_3 = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(result_3['dominant_emotion'], 'disgust')

        # Mocking the response for 'sadness'
        mock_post.return_value.text = '{"emotionPredictions":[{"emotion":{"anger":0.0,"disgust":0.0,"fear":0.0,"joy":0.0,"sadness":1.0}}]}'
        result_4 = emotion_detector('I am so sad about this')
        self.assertEqual(result_4['dominant_emotion'], 'sadness')

        # Mocking the response for 'fear'
        mock_post.return_value.text = '{"emotionPredictions":[{"emotion":{"anger":0.0,"disgust":0.0,"fear":1.0,"joy":0.0,"sadness":0.0}}]}'
        result_5 = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(result_5['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()

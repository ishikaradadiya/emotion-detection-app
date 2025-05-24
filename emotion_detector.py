from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, EmotionOptions

def emotion_predictor(text):
    nlu = NaturalLanguageUnderstandingV1(
        version='2020-08-01',
        iam_apikey='your-api-key',
        url='https://api.us-south.natural-language-understanding.watson.cloud.ibm.com/instances/your-instance-id'
    )
    
    response = nlu.analyze(
        text=text,
        features=Features(emotion=EmotionOptions())
    ).get_result()
    
    return response['emotion']['document']['emotion']

# Test run
print(emotion_predictor("I am happy"))

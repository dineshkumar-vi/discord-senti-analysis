from transformers import AutoModelForSequenceClassification
from transformers import AutoTokenizer, AutoConfig
import numpy as np
from scipy.special import softmax


class DebertaV2:

    def __init__(self):
        MODEL = "Elron/deberta-v3-large-sentiment"
        self.tokenizer = AutoTokenizer.from_pretrained(MODEL)
        self.config = AutoConfig.from_pretrained(MODEL)
        self.model = AutoModelForSequenceClassification.from_pretrained(MODEL)
        #self.model.save_pretrained(MODEL)


    def predicte(self, text):
        encoded_input = self.tokenizer(text, return_tensors='pt')
        output = self.model(**encoded_input)
        scores = output[0][0].detach().numpy()

        scores = softmax(scores)

        ranking = np.argsort(scores)
        ranking = ranking[::-1]

        sentiprediction = {}

        for i in range(scores.shape[0]):
            l = self.config.id2label[ranking[i]]
            s = scores[ranking[i]]
            sentiprediction[l] = s

        if sentiprediction[1] > sentiprediction[0]:
            return "positive"






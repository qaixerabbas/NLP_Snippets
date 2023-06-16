prompt = """
            You are a large language model who can do variety of NLP tasks. I will provide you a sentence and you should return the class of that 
            sentence whether it is medical or non-medical, as a json object. Do not produce any additional text and if you do not know the sentiment, .
            just return a json object with unknown sentiment type. Your response should be in following format. {"sentiment": sentiment_class}

            sentence: He is working in dermatology for last five months
        """

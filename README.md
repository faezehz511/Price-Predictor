# Price-Predictor
Web scraping and machine learning for a specific type of machine from the following website: " https://divar.ir/s/tehran "

In this question, the task is to train a machine learning model that can predict the price of a Peugeot 206 type 2 car. However, the challenge is to find the necessary data for training the model. The solution involves web scraping, and the popular website Divar is suggested as a source of valuable information.

To accomplish this, the Selenium library can be used for web scraping. Divar publishes a large number of car sales ads regularly, and by analyzing these ads, important factors that can influence the car's price, such as the year, mileage, color, etc., can be identified. Extracting and saving these features is crucial for creating the dataset.

Furthermore, descriptions and photos of the cars can provide additional significant information, which may offer bonus points in the task. Once the relevant data is extracted, the next step is to perform the necessary pre-processing and train the machine learning model.

After training the model, it needs to be evaluated and the results reported. This evaluation helps determine the model's performance and its ability to predict the price accurately.

Lastly, the trained model needs to be saved, and a script should be developed that takes car information as input and predicts whether the price suggested by the seller is reasonable or not. This script will be a useful tool for buyers to assess the fairness of a seller's price.

Overall, the task involves web scraping car sales ads from Divar, extracting important features, training a machine learning model, evaluating the model's performance, and developing a script for price prediction based on input car information.

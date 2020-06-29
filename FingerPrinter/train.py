from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split


#Source 1: https://stackoverflow.com/questions/6618515/sorting-list-based-on-values-from-another-list

#trains classifier and makes a predicition on input data
def train_test(df, test):

    #remove target value from dataframe
    y = df.pop('Category').values

    #remove target value from dataframe
    test_y = test.pop('Category').values

    #Split dataset into training data and test data

    X_train, X_test, y_train, y_test = train_test_split(df, y, test_size=0.20, shuffle=True)

    #Using Naive Bayes as the classifier
    classifier = GaussianNB()

    classifier.fit(X_train, y_train)

    #Get a list of probabilites per class (highest probability is the most likely to correspond to pcap file)
    y_proba = classifier.predict_proba(test)

    #Flatten list from 2D to 1D
    results = [item for sublist in y_proba for item in sublist]

    #Sort the categories by probability and make a new list (Source 1)
    readable_results = [x for _, x in sorted(zip(results, classifier.classes_))]

    #Make list in descending order
    readable_results.reverse()

    #Print websites
    for val in readable_results:
        print(val)
        print("\n")



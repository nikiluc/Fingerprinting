import sys
import preprocess
import train



def main():

    #loads input file into a dataframe
    test = preprocess.load_input(sys.argv[1])

    #loads training pcap files into a dataframe
    dataset = preprocess.load_data()

    #trains model (Naive Bayes) and makes a prediction
    train.train_test(dataset, test)


if __name__ == "__main__":
    main()
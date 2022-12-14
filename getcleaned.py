
import tfidf
import combineFiles
import combinations

def main():  # combine outputs csv of features, for begign and malicious apps
    combineFiles.CreateMasterFV() #output completeFeatureVector
    # tfidf evaluate begign and malicious

    # tfidf.main()
        

    # create and output combination file

    combinations.combo2()

    tfidf.forCombinations()

if __name__ == "__main__":
    main()
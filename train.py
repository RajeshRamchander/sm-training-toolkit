import argparse
import os
import pandas as pd

from sklearn.externals import joblib
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    # Hyperparameters are described here. In this simple example we are just including one hyperparameter.
    parser.add_argument('--max_leaf_nodes', type=int, default=-1)
 
    # Sagemaker specific arguments. Defaults are set in the environment variables.
    parser.add_argument('--output-data-dir', type=str, default=os.environ['SM_OUTPUT_DATA_DIR'])
    parser.add_argument('--model-dir', type=str, default=os.environ['SM_MODEL_DIR'])
    parser.add_argument('--train', type=str, default=os.environ['SM_CHANNEL_TRAIN'])
 
    args = parser.parse_args()

    col_names = ['pregnant', 'glucose', 'bp', 'skin', 'insulin', 'bmi', 'pedigree', 'age', 'label']
    # Load dataset.
    pima = pd.read_csv(os.path.join(args.train, "diabetes.csv"), header=None, names=col_names)

    # Split dataset in features and target variable.
    feature_cols = ['pregnant', 'insulin', 'bmi', 'age','glucose','bp','pedigree']
    X = pima[feature_cols] # Features
    y = pima.label # Target variable

    # Split dataset into training set and test set.
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1) # 70% training and 30% test
 
    # Here we support a single hyperparameter, 'max_leaf_nodes'.
    max_leaf_nodes = args.max_leaf_nodes
 
    # Now use scikit-learn's decision tree classifier to train the model.
    clf = DecisionTreeClassifier(max_leaf_nodes=max_leaf_nodes)
    clf = clf.fit(X_train, y_train)
 
    # Print the coefficients of the trained classifier, and save the coefficients
    joblib.dump(clf, os.path.join(args.model_dir, "model.joblib"))

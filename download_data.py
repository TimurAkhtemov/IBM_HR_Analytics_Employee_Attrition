#!/usr/bin/env python
import os
import requests
import zipfile
import io

def download_dataset():
    """
    Download the IBM HR Analytics dataset directly from Kaggle's website
    Note: This assumes the user will download manually if this fails
    """
    print("Please download the dataset manually from: https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset")
    print("Save the CSV file as 'data/WA_Fn-UseC_-HR-Employee-Attrition.csv'")
    
    # Alternatively, if you have Kaggle API set up:
    # import kaggle
    # kaggle.api.dataset_download_files('pavansubhasht/ibm-hr-analytics-attrition-dataset', path='./data', unzip=True)

if __name__ == "__main__":
    download_dataset() 
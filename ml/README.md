# A Discord Bot ML
This directory is home to the Machine Learning components for A Discord Bot. The `main.py` will generate the linear regression model and vectorizer for the Bot's runtime.

**Note:** If you want to re use this you'll want to provide actual data and not my `dummy.csv` file. 

## Dependencies 

* [pandas](https://pypi.org/project/pandas/)
* [scikit-learn](https://pypi.org/project/scikit-learn/)
* [joblib](https://pypi.org/project/joblib/)

#### Dependency Installation 

`pip3 install -r requirements.txt`

## How to Run

#### Pre-Requisites

* [Install the Dependencies](#dependency-installation)

#### Running
* `python3 main.py`

## Acknowledgements
* [Professor Marie Roch](https://roch.sdsu.edu/)
    * For teaching the AI Course I took at SDSU which made me confident to implement this
* [Real Python's Guide to Text Classification](https://realpython.com/python-keras-text-classification/)
    * The guide I followed to get up to speed with pandas/skikit-learn to implement this    

# Exploratory Data Analysis S&P 500
_Exploratory Data Analysis (EDA) is a crucial step in data science projects. It helps in understanding the underlying patterns and relationships in the data. In this tutorial, we will perform EDA on the S&P 500 dataset using Python and the yfinance, streamlit, base64, pandas and numpy libraries._

## 🚀 Getting Started  

_The S&P 500 Index, or Standard & Poor's 500 Index, is a market-capitalization-weighted index of 500 leading publicly traded companies in the U.S. The S&P 500 index is regarded as one of the best gauges of prominent American equities' performance, and by extension, that of the stock market overall. With the help of Streamlit, that is a free and open-source framework to rapidly build and share beautiful machine learning and data science web apps, and other importntat libraries, I create this application that allows you to track companies according to their sector, and also allows you to see their results in the last year, for each company._

## 📋 Pre-requisites

_You must have Python installed in your local machine. All the dependencies and required libraries are included in the file_ <code>requirements.txt</code> [See here](https://github.com/Barrero0717/EDASP500/blob/master/requirements.txt)

_To check the Python version in your machine, just open a terminal, and try this command:_

```
python --version
```

## 🔧 Installation  

1. _Clone the repository to your local machine. To do this, run this command inside your terminal:_
```
$ git clone https://github.com/<your-github-username>/EDASP500.git 
```

2. _Change your directory to the cloned repo:_ 
```
$ cd EDASP500
```

3. _Create a Python virtual environment named 'venv' and activate it:_

Windows User
```
$ python -m venv venv
```
```
$ venv\Scripts\activate.bat
```

Linux or macOs User
```
$ python3.9 -m venv env
```
```
$ source env/bin/activate
```

4. _Install all the dependencies and required libraries:_
```
$ pip install -r requirements.txt
```

## ⚙️ Running the app 

_Open terminal. Go into the cloned project directory, activate the Python virtual environment and type the following command:_

```
streamlit run sp500_app.py
```

_and then you must open the web page locally where you can see the this:_
![image](https://user-images.githubusercontent.com/66132335/228690444-65e46e5f-46cd-48c9-8edd-2b111121d508.png)

_and then you must open the web page locally where you can see the this:_

## ✒️ Authors 

* **Andrés Felipe Barrero Arce** - [Barrero0717](https://github.com/barrero0717)

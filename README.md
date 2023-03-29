# Exploratory Data Analysis S&P 500
_This is a very simple project that is used to view the prices of a stock. It uses the Streamlit and yfinance libraries._

## 🚀 Getting Started  

_Streamlit is a free and open-source framework to rapidly build and share beautiful machine learning and data science web apps. It is a Python-based library specifically designed for machine learning engineers. yfinance is a popular open source library developed by Ran Aroussi as a means to access the financial data available on Yahoo Finance. Combining these two libraries we can create different applications, like the one you can find in this script._

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

_and then you must open the web page locally where you can see the charts of the ticker you indicated. In this case, we will see the VOO ticker:_
![image](https://user-images.githubusercontent.com/66132335/226723011-b6249210-3cfe-471d-88b5-e04c92fd978d.png)

![image](https://user-images.githubusercontent.com/66132335/226723089-ceebd80a-d535-48a6-bf27-1f31bfea414f.png)

## ✒️ Authors 

* **Andrés Felipe Barrero Arce** - [Barrero0717](https://github.com/barrero0717)

<a name="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield1]][linkedin-url1]
[![LinkedIn][linkedin-shield2]][linkedin-url2]
[![LinkedIn][linkedin-shield3]][linkedin-url3]
[![GitHub][github-shield1]][github-url1]
[![GitHub][github-shield2]][github-url2]
[![GitHub][github-shield3]][github-url3]

# [TESSA](https://csc448finalproject.streamlit.app) | Text Sentiment Analysis

<br />
<div align="center">
  <a href="https://csc448finalproject.streamlit.app">
    <img src="logo.png" alt="Logo">
  </a>

<h3 align="center">TESSA</h3>

  <p align="center">
    <b>TESSA</b> is a <b>Text Sentiment Analysis</b> project with main purpose to predict the <b>Emotion</b> conveyed from a text document. This project explores machine learning models for text emotion detection and classification. We aim to develop an efficient model for identifying emotions in text data, employing natural language processing. The models trained on labeled <b>Twitter(X) datasets</b> find applications in customer service, social media monitoring, marketing analysis, and various other uses. We mainly hope to utilize this emotion detection as a marketing tool to analyze customer perceptions gathered from reviews, tweets, and customer service interactions. This approach will help clients understand their sentiments within their customer base, enabling targeted strategies aligned with their experiences and expectations. We examine and create eight models to determine the most effective approach for emotion detection. We successfully developed our business tool, with the <b>Bidirectional LSTM </b>emerging as the top-performing model with an accuracy of <b>92.88%</b>.
    <br />
    <a href="https://github.com/mengwaichan/CSc448_Final_Project"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://csc448finalproject.streamlit.app">View Web Application</a>
    ·
    <a href="https://github.com/mengwaichan/CSc448_Final_Project/issues">Report Bug</a>
    ·
    <a href="https://github.com/mengwaichan/CSc448_Final_Project/issues">Request Feature</a>
  </p>
</div>

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#application-user-interface">Application User Interface</a></li>
        <li><a href="#key-features">Tasks</a></li>
        <li><a href="#dataset">Dataset</a></li>
        <li><a href="#models-built">Models Built</a></li>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#setup">Setup</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#documents">Documents</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

## About The Project

  <a href="https://csc448finalproject.streamlit.app">
      <img src="logo.png" alt="Logo" width="200" height="50" style="display: block; margin-left: auto; margin-right: auto;">
  </a>

### Application User Interface

 <a href="https://csc448finalproject.streamlit.app">
    <img src="./code/Meng_Wai_Chan/UI.JPG" alt="Logo">
 </a>

<p align="right"><a href="#readme-top">Back to top</a></p>

### Tasks

| Task      | Assigned  |
|-----------|-------|
| Create Github Repository  | Everyone  |
| Brainstorm Project        | Everyone  |
| Finding Dataset           | Everyone  |
| EDA                       | Everyone  |
| Data Preprocessing        | Everyone  |
| Data Modeling: Random forest, Decision Tree | Meng Wai Chan |
| Data Modeling: Logistic Regression , SVM | Farhanul  Thouship|
| Data Modeling: BiLSTM, CNN, CNN+LSTM, MNB | Georgios Ioannou |
| Model Evaluation |  Everyone  |
| Streamlit Application | Georgios Ioannou |

<p align="right"><a href="#readme-top">Back to top</a></p>

### Dataset

**[`Emotions Dataset For NLP`](https://www.kaggle.com/datasets/praveengovi/emotions-dataset-for-nlp)**
    - 2 Columns, 20k rows
    - Columns: content, sentiment

<p align="right"><a href="#readme-top">Back to top</a></p>

### Models Built (Click on the model that you are interested)

1. [Bidirectional LSTM (BiLSTM)](https://github.com/mengwaichan/CSc448_Final_Project/blob/main/code/Georgios_Ioannou/Build_And_Train_Bidirectional_LSTM_Model.ipynb)
2. [Convolutional Neural Network (CNN)](https://github.com/mengwaichan/CSc448_Final_Project/blob/main/code/Georgios_Ioannou/Build_And_Train_CNN_Model.ipynb)
3. [CNN + LSTM](https://github.com/mengwaichan/CSc448_Final_Project/blob/main/code/Georgios_Ioannou/Build_And_Train_CNN_LSTM_Model.ipynb)
4. [Multinomial Naive Bayes (MNB)](https://github.com/mengwaichan/CSc448_Final_Project/blob/main/code/Georgios_Ioannou/Build_And_Train_Multinomial_Naive_Bayes_Model.ipynb)
5. [Decision Tree](https://github.com/mengwaichan/CSc448_Final_Project/blob/main/code/Meng_Wai_Chan/DecisionTree.ipynb)
6. [Random Forest](https://github.com/mengwaichan/CSc448_Final_Project/blob/main/code/Meng_Wai_Chan/RandomForest.ipynb)
7. [Logistic Regression](https://github.com/mengwaichan/CSc448_Final_Project/blob/main/code/Farhanul_Thouship/logistic_regression.ipynb)
8. [Support Vector Machine (SVM)](https://github.com/mengwaichan/CSc448_Final_Project/blob/main/code/Farhanul_Thouship/svm.ipynb)

<p align="right"><a href="#readme-top">Back to top</a></p>

### Built With

[![Python][Python]][Python-url]
[![Pandas][Pandas]][Pandas-url]
[![Numpy][Numpy]][Numpy-url]
[![Matplotlib][Matplotlib]][Matplotlib-url]
[![Seaborn][Seaborn]][Seaborn-url]
[![Plotly][Plotly]][Plotly-url]
[![scikitlearn][scikitlearn]][scikitlearn-url]
[![Nltk][Nltk]][Nltk-url]
[![Tensorflow][Tensorflow]][Tensorflow-url]
[![Streamlit][Streamlit]][Streamlit-url]
[![Kaggle][Kaggle]][Kaggle-url]

<p align="right"><a href="#readme-top">Back to top</a></p>

## Getting Started

**To get a local copy of TESSA up and running locally follow these simple example steps:**

### Prerequisites

**NOTE:** How to check if Python is installed and what is its version

```sh
  python --version
```

**NOTE:** How to check if Git is installed and what is its version

```sh
  git -v
```

1. Please make sure you have pyenv installed and use Python3 version 3.11.0:

   - You can use pyenv to switch between different Python versions:
     - Windows: [https://www.youtube.com/watch?v=HTx18uyyHw8](https://github.com/pyenv-win/pyenv-win)
     - Mac: [https://www.youtube.com/watch?v=31WU0Dhw4sk](https://github.com/pyenv/pyenv)
     - Linux: [https://www.youtube.com/watch?v=1Zgo8M9yUtM](https://github.com/pyenv/pyenv)

2. Please make sure you have git installed

   - Windows: [https://git-scm.com/download/win](https://git-scm.com/download/win)
   - Mac: [https://git-scm.com/download/mac](https://git-scm.com/download/mac)
   - Linux: [https://git-scm.com/download/linux](https://git-scm.com/download/linux)

3. Please look at the [setup](https://github.com/mengwaichan/CSc448_Final_Project/tree/main/setup) folder found in this project.

### Setup

1. Navigate to the directory where you want to clone/run/save the application:

   ```sh
   cd your_selected_directory
   ```

2. Clone this repository:

   ```sh
   git clone https://github.com/mengwaichan/CSc448_Final_Project.git
   ```

3. Navigate to the realesrgan git repository:

   ```sh
   cd CSc448_Final_Project
   ```

4. Use Python3 3.11.0 version in the cloned repository folder:

   ```sh
   pyenv local 3.11.0
   ```

5. Create virtual environment in the cloned repository folder:

   ```sh
   python -m venv .tessa-venv
   ```

6. Activate the virtual environment (Windows OR Mac/Linux):

   1. Windows

   ```sh
   .\.tessa-venv\Scripts\activate
   ```

   2. Mac/Linux

   ```sh
   source .tessa-venv/bin/activate
   ```

7. Install the dependencies listed in the requirements.txt file:

   ```sh
   pip install -r requirements.txt
   ```

8. Run Streamlit:

   ```sh
   streamlit run app.py
   ```

9. To Run The Notebooks (3 Options):
   1. Use [Kaggle](https://www.kaggle.com/)
   2. Use [Jupyter Notebboks Extension for VS Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks)
   3. Use [Anaconda](https://www.anaconda.com/)
       1. Download and install [Anaconda](https://www.anaconda.com/download)
       2. Launch a jupyter notebook:
           1. MacOS users, open up terminal and type in `jupyter notebook`
           2. Window users, open up your Anaconda Power Shell, and type in `jupyter notebook`

<p align="right"><a href="#readme-top">Back to top</a></p>

## Documents

Machine Learing Model is located in [code](/code)

Project Presentation is located in [documents](/documents)

Project Final Report is located in [documents](/documents)

<p align="right"><a href="#readme-top">Back to top</a></p>

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right"><a href="#readme-top">Back to top</a></p>

## License

Distributed under the MIT License. See [LICENSE](https://github.com/mengwaichan/CSc448_Final_Project/blob/master/LICENSE) for more information.

MIT License

Copyright (c) 2023 TESSA

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

<p align="right"><a href="#readme-top">Back to top</a></p>

## Contact

Georgios Ioannou - [@LinkedIn](https://linkedin.com/in/georgiosioannoucoder)

Farhanul Thouship - [@LinkedIn](https://www.linkedin.com/in/thouship)

Meng Wai Chan - [@LinkedIn](https://www.linkedin.com/in/mengwai-chan-00b40b257)

Project Link: [https://github.com/mengwaichan/CSc448_Final_Project](https://github.com/mengwaichan/CSc448_Final_Project)

<p align="right"><a href="#readme-top">Back to top</a></p>

[contributors-shield]: https://img.shields.io/github/contributors/mengwaichan/CSc448_Final_Project.svg?style=for-the-badge
[contributors-url]: https://github.com/mengwaichan/CSc448_Final_Project/graphs/contributors

[forks-shield]: https://img.shields.io/github/forks/mengwaichan/CSc448_Final_Project.svg?style=for-the-badge
[forks-url]: https://github.com/mengwaichan/CSc448_Final_Project/network/members

[stars-shield]: https://img.shields.io/github/stars/mengwaichan/CSc448_Final_Project.svg?style=for-the-badge
[stars-url]: https://github.com/mengwaichan/CSc448_Final_Project/stargazers

[issues-shield]: https://img.shields.io/github/issues/mengwaichan/CSc448_Final_Project.svg?style=for-the-badge
[issues-url]: https://github.com/mengwaichan/CSc448_Final_Project/issues

[license-shield]: https://img.shields.io/github/license/mengwaichan/CSc448_Final_Project.svg?style=for-the-badge
[license-url]: https://github.com/mengwaichan/CSc448_Final_Project/blob/master/LICENSE

[linkedin-shield1]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=0077B5
[linkedin-url1]: https://linkedin.com/in/georgiosioannoucoder

[linkedin-shield2]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=0077B5
[linkedin-url2]: https://www.linkedin.com/in/thouship

[linkedin-shield3]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=0077B5
[linkedin-url3]: https://www.linkedin.com/in/mengwai-chan-00b40b257

[github-shield1]: https://img.shields.io/badge/-GitHub-black.svg?style=for-the-badge&logo=github&colorB=000
[github-url1]: https://github.com/GeorgiosIoannouCoder/

[github-shield2]: https://img.shields.io/badge/-GitHub-black.svg?style=for-the-badge&logo=github&colorB=000
[github-url2]: https://github.com/thouship

[github-shield3]: https://img.shields.io/badge/-GitHub-black.svg?style=for-the-badge&logo=github&colorB=000
[github-url3]: https://github.com/mengwaichan

[Python]: https://img.shields.io/badge/python-FFDE57?style=for-the-badge&logo=python&logoColor=4584B6
[Python-url]: https://www.python.org/

[Pandas]: https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white
[Pandas-url]: https://pandas.pydata.org/

[Numpy]: https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white
[Numpy-url]: https://numpy.org/

[scikitlearn]: https://img.shields.io/badge/scikitlearn-000000?style=for-the-badge&logo=scikitlearn&logoColor=ffa500
[scikitlearn-url]: https://scikit-learn.org/stable/

[Nltk]: https://img.shields.io/badge/nltk-154f5b?style=for-the-badge&logo=nltk&logoColor=ffa500
[Nltk-url]: https://www.nltk.org/

[Tensorflow]: https://img.shields.io/badge/tensorflow-000000?style=for-the-badge&logo=tensorflow&logoColor=ffa500
[Tensorflow-url]: https://www.tensorflow.org/

[Matplotlib]: https://img.shields.io/badge/matplotlib-3761a3?style=for-the-badge&logo=matplotlib&logoColor=white
[Matplotlib-url]: https://matplotlib.org/

[Seaborn]: https://img.shields.io/badge/seaborn-7db0bc?style=for-the-badge&logo=seaborn&logoColor=white
[Seaborn-url]: https://seaborn.pydata.org/

[Plotly]: https://img.shields.io/badge/plotly-000000?style=for-the-badge&logo=plotly&logoColor=white
[Plotly-url]: https://plotly.com/

[Streamlit]: https://img.shields.io/badge/streamlit-ffffff?style=for-the-badge&logo=streamlit&logoColor=ff0000
[Streamlit-url]: https://streamlit.io/

[Kaggle]: https://img.shields.io/badge/kaggle-000000?style=for-the-badge&logo=kaggle&logoColor=20beff
[Kaggle-url]: https://www.kaggle.com/
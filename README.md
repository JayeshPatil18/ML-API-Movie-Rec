<div align="left">
  <h1>Movie Recommendation API - ML</h1>
  <img alt="Python" src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" style="margin-left: 10px;">
  <img alt="Flask" src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" style="margin-left: 10px;">
  <img alt="Scikit-learn" src="https://img.shields.io/badge/Scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" style="margin-left: 10px;">
<img alt="Pandas" src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" style="margin-left: 10px;">
<img alt="Numpy" src="https://img.shields.io/badge/Numpy-013243?style=for-the-badge&logo=numpy&logoColor=white" style="margin-left: 10px;">
  <img alt="Machine Learning" src="https://img.shields.io/badge/Machine_Learning-00C49F?style=for-the-badge&logo=machine-learning&logoColor=white" style="margin-left: 10px;">
<img alt="Artificial Intelligence" src="https://img.shields.io/badge/Artificial_Intelligence-FF6F00?style=for-the-badge&logo=ai&logoColor=white" style="margin-left: 10px;">
<img alt="GitHub" src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" style="margin-left: 10px;">
  </a>
</div>
</br>

Discover your next favorite movie with our AI model! This project uses the TMDB dataset to provide personalized movie recommendations.

[Check it out here!](https://suggestmovie.vercel.app/)

![Available](https://github.com/JayeshPatil18/ML-API-Movie-Rec/blob/main/suggestmovie.png)

## How to Get Suggestions

1. Visit the [movie recommendation site](https://suggestmovie.vercel.app/).
2. Enter one or more of your favorite movies.
3. Wait for the recommendations to load. Please note that for the first time, it might take a minute because it is hosted on a free server, which goes down when there are no requests.

## Model Explanation

Our AI model uses the TMDB dataset to find movies similar to the ones you like. Here's a brief explanation of the process:

1. **Cosine Similarity**: We use cosine similarity to measure how similar two movies are based on their features (like genre, keywords, etc.). It calculates the cosine of the angle between two vectors representing the movies. A smaller angle indicates higher similarity.

2. **Popularity Sorting**: After finding similar movies, we sort them by vote count to ensure you get recommendations that are both relevant and popular.

## Cosine Similarity in Detail

Cosine similarity is a measure of similarity between two vectors.

1. **Vectors**:

    Imagine you have two lists of numbers, let’s call them List A and List B. Each list is like a vector in space, and the numbers in the list represent the coordinates in that space.

2. **Cosine of the Angle**:

    Now, think of these two lists as arrows starting from the origin (0,0) in a multi-dimensional space. The cosine similarity measures the cosine of the angle between these two arrows.

3. **Similarity Score**:

    - If the arrows are pointing in the same direction, the cosine of the angle is 1, indicating perfect similarity.
    - If they are at right angles, the cosine is 0, suggesting no similarity.
    - If they point in completely opposite directions, the cosine is -1, indicating complete dissimilarity.


In the context of movie recommendations, a higher cosine similarity score means that the movies are more similar to each other based on their features, making it a powerful tool for finding movies that match your tastes.


## Libraries Used

- Flask
- Numpy
- Scikit-learn
- Pandas


## How to Setup

1. **Clone the Repository**:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Create a Virtual Environment**:
    ```sh
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Run the Flask App**:
    ```sh
    flask run
    ```

5. **Access the Application**:
    Open your web browser and go to `http://127.0.0.1:5000/` to use the application locally.

Now you're all set! Enjoy discovering new movies tailored to your tastes.

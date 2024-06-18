<div align="left">
  <h1>Movie Recommendation API - ML</h1>
  <img alt="Flutter" src="https://img.shields.io/badge/Flutter-02569B?style=for-the-badge&logo=flutter&logoColor=white" style="margin-left: 10px;">
  <img alt="Dart" src="https://img.shields.io/badge/Dart-0175C2?style=for-the-badge&logo=dart&logoColor=white" style="margin-left: 10px;">
  <img alt="Firebase" src="https://img.shields.io/badge/Firebase-FFCA28?style=for-the-badge&logo=firebase&logoColor=black" style="margin-left: 10px;">
  <img alt="Node.js" src="https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=node.js&logoColor=white" style="margin-left: 10px;">
  <img alt="JavaScript" src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" style="margin-left: 10px;">
  <img alt="MySQL" src="https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white" style="margin-left: 10px;">
  <img alt="AWS" src="https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white" style="margin-left: 10px;">
  <img alt="Figma" src="https://img.shields.io/badge/Figma-F24E1E?style=for-the-badge&logo=figma&logoColor=white" style="margin-left: 10px;">
  <a href="https://github.com/JayeshPatil18/Stock-HIVE">
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

Cosine similarity is a metric used to measure how similar two items are by comparing their feature vectors. It is especially useful in comparing items with multiple attributes, such as movies with genres, keywords, and other characteristics.

Here's how it works:

1. **Feature Vectors**: Each movie is represented by a feature vector. This vector includes various attributes of the movie, such as genre, keywords, etc.

2. **Dot Product**: The dot product of two vectors \( A \) and \( B \) is calculated. This operation sums the products of the corresponding entries of the vectors.

3. **Magnitude**: The magnitude (or length) of each vector is calculated. The magnitude of a vector \( A \) is the square root of the sum of the squares of its components, denoted as \( ||A|| \).

4. **Cosine of the Angle**: The cosine similarity is the cosine of the angle between the two vectors. It is calculated by dividing the dot product of the vectors by the product of their magnitudes.

In the context of movie recommendations, a higher cosine similarity score means that the movies are more similar to each other based on their features, making it a powerful tool for finding movies that match your tastes.


### Libraries Used

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

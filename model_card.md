# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

**VibeFinder 1.0**

---

## 2. Intended Use  

This recommender system is designed to suggest songs based on a user’s preferences, such as genre, mood, energy, and acousticness. It assumes that users have consistent taste and that their preferences can be represented using a few key features. This model is intended for classroom exploration and learning, not for real-world deployment.

---

## 3. How the Model Works  

The model compares user preferences to song attributes and assigns each song a score. It uses features such as genre, mood, energy, and acousticness. If a song matches the user’s preferred genre, it receives a higher score. Additional points are given based on how close the song’s energy level is to the user’s target energy. The model also considers whether the user prefers acoustic or non-acoustic songs. After calculating scores for all songs, it ranks them and returns the top recommendations.

---

## 4. Data  

The model uses a small dataset of songs stored in a CSV file. The dataset includes attributes such as genre, mood, energy, tempo, valence, danceability, and acousticness. Additional songs were added to increase diversity across genres and moods. However, the dataset is still limited and does not include features like lyrics, artist popularity, or user listening history.

---

## 5. Strengths  

The system works well for clearly defined user profiles. For example, the Chill Lofi profile correctly recommended calm, low-energy, and acoustic songs such as *Library Rain* and *Focus Flow*. The scoring logic captures basic musical preferences like energy level and acoustic style, which helps generate reasonable recommendations.

---

## 6. Limitations and Bias  

This recommender has a few limitations. One weakness I discovered is that when mood is removed or underweighted, the system can recommend songs that match the energy level but not the emotional vibe the user may actually want. For example, *Gym Hero* appeared near the top for more than one profile because energy and acousticness had a strong effect on the final score. The system also depends on a small dataset, which limits variety and can make certain songs appear repeatedly. Because of this, the model may create a narrow recommendation pattern instead of showing a wider range of relevant songs.

---

## 7. Evaluation  

I tested the recommender with three profiles: **High-Energy Pop**, **Chill Lofi**, and **Deep Intense Rock**. The results mostly made sense based on the selected features. For example, the Chill Lofi profile strongly favored low-energy and acoustic songs like *Library Rain*, *Focus Flow*, and *Midnight Coding*, which felt correct. One surprise was that after removing the mood feature, songs like *Gym Hero* still ranked highly even when the mood did not match. This showed that the recommender became more dependent on genre, energy, and acousticness than on emotional vibe.

---

## 8. Future Work  

In the future, the model could be improved by adding more features such as lyrics, artist preferences, and listening history. It could also improve diversity by reducing the weight of genre so that songs from different genres but similar vibes are recommended. Another improvement would be better explanations for recommendations to make them more understandable to users.

---

## 9. Personal Reflection  

Through this project, I learned how recommendation systems use simple rules and features to predict what users might like. One interesting discovery was how strongly certain features, like energy, can influence results even when other features are missing. This made me realize that real-world recommendation systems are much more complex and need to balance many factors to avoid bias and repetition.
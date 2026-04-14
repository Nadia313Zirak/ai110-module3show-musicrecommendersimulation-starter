# 🎧 Model Card: VibeFinder 1.0

## Model Name
VibeFinder 1.0

---

## Goal / Task
This recommender suggests songs based on a user’s preferences such as genre, mood, energy, and acousticness. It tries to predict which songs a user would enjoy based on how similar they are to the user’s taste profile.

---

## Data Used
The model uses a small dataset of songs stored in a CSV file. The dataset includes features like genre, mood, energy, tempo, valence, danceability, and acousticness. I added extra songs to increase variety, but the dataset is still limited and does not include things like lyrics, artist popularity, or user listening history.

---

## Algorithm Summary
The model compares each song to the user’s preferences and assigns a score. Songs get extra points if the genre matches. It also adds points when the song’s energy level is close to the user’s target energy. The model considers whether the user prefers acoustic or non-acoustic songs. After scoring all songs, it ranks them and returns the top results.

---

## Observed Behavior / Biases
One issue I noticed is that the system can favor certain songs too much based on a few features. For example, *Gym Hero* appeared in multiple profiles because it matched energy and acousticness well. When the mood feature was removed, the recommendations became less accurate and focused more on energy than emotional vibe. The small dataset also limits variety and can cause repeated recommendations.

---

## Evaluation Process
I tested the recommender using three different profiles: High-Energy Pop, Chill Lofi, and Deep Intense Rock. I compared the top recommendations for each and checked whether they matched what I expected. I also ran an experiment where I removed the mood feature to see how it affected the results. This helped me understand how each feature influences the recommendations.

---

## Intended Use and Non-Intended Use
This system is intended for learning and experimentation with recommendation systems. It shows how basic features can be used to generate suggestions. It is not intended for real-world use because it does not include enough data or advanced logic to handle real user preferences.

---

## Ideas for Improvement
- Add more features such as lyrics, artist preference, or listening history  
- Increase dataset size to improve variety  
- Adjust feature weights to reduce repeated recommendations  

---

## Personal Reflection
The biggest thing I learned from this project is how simple rules can still create useful recommendations. Even basic features like energy and genre can make the system feel realistic. Using AI tools helped me generate code and ideas quickly, but I still had to double-check the logic and fix errors myself. One surprising part was how removing just one feature, like mood, made the system less accurate. If I continued this project, I would focus on adding more features and improving how the system balances different preferences.
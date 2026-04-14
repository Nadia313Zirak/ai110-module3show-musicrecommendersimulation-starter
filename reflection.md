# Reflection: Recommender System Evaluation

## Profile Comparisons

**High-Energy Pop vs Chill Lofi:**  
The High-Energy Pop profile recommended upbeat songs with strong energy and low acousticness, while the Chill Lofi profile recommended calmer and more acoustic songs. This makes sense because the two profiles represent very different listening moods and energy levels.

**High-Energy Pop vs Deep Intense Rock:**  
Both profiles preferred high-energy songs, which caused some overlap in recommendations. However, the Pop profile favored pop songs, while the Rock profile ranked songs like *Storm Runner* higher because they better match the intense rock genre. This shows that energy can overlap across profiles, but genre still plays an important role.

**Chill Lofi vs Deep Intense Rock:**  
The Chill Lofi profile recommended low-energy and acoustic songs, while the Deep Intense Rock profile recommended high-energy and aggressive songs. This difference makes sense because the two profiles have opposite preferences in both energy and mood.

---

## Key Takeaways

The recommender system responds well to different user profiles, especially when there are clear differences in energy and genre preferences. However, removing the mood feature showed that the system becomes less precise and relies more on energy and acousticness. This can lead to similar songs appearing across multiple profiles, even when the intended vibe is different.
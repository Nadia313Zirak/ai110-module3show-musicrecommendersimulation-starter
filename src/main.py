from src.recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")

    user_prefs = {
        "favorite_genre": "pop",
        "favorite_mood": "happy",
        "target_energy": 0.8,
        "likes_acoustic": False
    }

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\nTop Recommendations:\n")
    print("-" * 50)

    for i, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"{i}. {song['title']} by {song['artist']}")
        print(f"   Score: {score:.2f}")
        print(f"   Reasons: {explanation}")
        print()


if __name__ == "__main__":
    main()
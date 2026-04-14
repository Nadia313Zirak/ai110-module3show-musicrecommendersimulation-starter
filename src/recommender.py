from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import csv


@dataclass
class Song:
    """Represents a song and its attributes."""
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float


@dataclass
class UserProfile:
    """Represents a user's taste preferences."""
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool


def _score_song_object(user: UserProfile, song: Song) -> Tuple[float, str]:
    """Compute a score and explanation for a song."""
    score = 0.0
    reasons = []

    if song.genre.lower() == user.favorite_genre.lower():
        score += 2.0
        reasons.append("genre match (+2.0)")

    if song.mood.lower() == user.favorite_mood.lower():
        score += 1.0
        reasons.append("mood match (+1.0)")

    energy_score = 1 - abs(song.energy - user.target_energy)
    score += energy_score
    reasons.append(f"energy similarity (+{energy_score:.2f})")

    if user.likes_acoustic:
        acoustic_score = song.acousticness
        score += acoustic_score
        reasons.append(f"acoustic bonus (+{acoustic_score:.2f})")
    else:
        non_acoustic_score = 1 - song.acousticness
        score += non_acoustic_score
        reasons.append(f"non-acoustic bonus (+{non_acoustic_score:.2f})")

    explanation = ", ".join(reasons)
    return score, explanation


class Recommender:
    """Handles ranking and explaining song recommendations."""
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Return the top k recommended songs for a user."""
        ranked = sorted(
            self.songs,
            key=lambda song: _score_song_object(user, song)[0],
            reverse=True
        )
        return ranked[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Return a short explanation for why a song was recommended."""
        _, explanation = _score_song_object(user, song)
        return explanation


def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from a CSV file into a list of dictionaries."""
    songs = []

    with open(csv_path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            song = {
                "id": int(row["id"]),
                "title": row["title"],
                "artist": row["artist"],
                "genre": row["genre"],
                "mood": row["mood"],
                "energy": float(row["energy"]),
                "tempo_bpm": float(row["tempo_bpm"]),
                "valence": float(row["valence"]),
                "danceability": float(row["danceability"]),
                "acousticness": float(row["acousticness"]),
            }
            songs.append(song)

    return songs


def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Score songs and return the top k recommendations."""
    ranked_songs = []

    for song in songs:
        score = 0.0
        reasons = []

        if song["genre"].lower() == user_prefs["favorite_genre"].lower():
            score += 2.0
            reasons.append("genre match (+2.0)")

        if song["mood"].lower() == user_prefs["favorite_mood"].lower():
            score += 1.0
            reasons.append("mood match (+1.0)")

        energy_score = 1 - abs(song["energy"] - user_prefs["target_energy"])
        score += energy_score
        reasons.append(f"energy similarity (+{energy_score:.2f})")

        if user_prefs["likes_acoustic"]:
            acoustic_score = song["acousticness"]
            score += acoustic_score
            reasons.append(f"acoustic bonus (+{acoustic_score:.2f})")
        else:
            non_acoustic_score = 1 - song["acousticness"]
            score += non_acoustic_score
            reasons.append(f"non-acoustic bonus (+{non_acoustic_score:.2f})")

        explanation = ", ".join(reasons)
        ranked_songs.append((song, score, explanation))

    ranked_songs = sorted(ranked_songs, key=lambda item: item[1], reverse=True)
    return ranked_songs[:k]
import os
import re
import requests

def get_access_token():
    """Obtiene un access token usando el refresh token."""
    response = requests.post(
        "https://accounts.spotify.com/api/token",
        data={
            "grant_type": "refresh_token",
            "refresh_token": os.environ["SPOTIFY_REFRESH_TOKEN"],
            "client_id": os.environ["SPOTIFY_CLIENT_ID"],
            "client_secret": os.environ["SPOTIFY_CLIENT_SECRET"],
        },
    )
    response.raise_for_status()
    return response.json()["access_token"]


def get_top_tracks(token, limit=5):
    """Obtiene los top tracks del último mes."""
    response = requests.get(
        "https://api.spotify.com/v1/me/top/tracks",
        headers={"Authorization": f"Bearer {token}"},
        params={"limit": limit, "time_range": "short_term"},
    )
    response.raise_for_status()
    items = response.json()["items"]
    return [
        f"{i+1}. {t['name']} — *{t['artists'][0]['name']}*"
        for i, t in enumerate(items)
    ]


def get_top_artists(token, limit=5):
    """Obtiene los top artists del último mes."""
    response = requests.get(
        "https://api.spotify.com/v1/me/top/artists",
        headers={"Authorization": f"Bearer {token}"},
        params={"limit": limit, "time_range": "short_term"},
    )
    response.raise_for_status()
    items = response.json()["items"]
    return [f"{i+1}. {a['name']}" for i, a in enumerate(items)]


def build_table(tracks, artists):
    """Construye la tabla markdown con los datos."""
    tracks_col = "<br/>".join(tracks)
    artists_col = "<br/>".join(artists)
    return f"""<!-- SPOTIFY_START -->
| 🎵 Top Tracks | 🎤 Top Artists | 🕐 Recently Played |
|---|---|---|
| {tracks_col} | {artists_col} | [![Recently Played](https://spotify-recently-played-readme.vercel.app/api?user=31rfklb2xjtwgcvtpz6hpvynfkfi&count=5&unique=true&width=300)](https://open.spotify.com/user/31rfklb2xjtwgcvtpz6hpvynfkfi) |
<!-- SPOTIFY_END -->"""


def update_readme(new_table):
    """Reemplaza la sección de Spotify en el README."""
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()

    pattern = r"<!-- SPOTIFY_START -->.*?<!-- SPOTIFY_END -->"
    updated = re.sub(pattern, new_table, content, flags=re.DOTALL)

    if updated == content:
        print("⚠️  No se encontraron los marcadores <!-- SPOTIFY_START --> y <!-- SPOTIFY_END --> en el README.")
        print("    Agrega esos comentarios en el README donde quieres la tabla.")
        return False

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(updated)
    return True


if __name__ == "__main__":
    print("🎵 Obteniendo datos de Spotify...")
    token = get_access_token()
    tracks = get_top_tracks(token)
    artists = get_top_artists(token)

    print("📊 Top Tracks:")
    for t in tracks:
        print(f"   {t}")

    print("🎤 Top Artists:")
    for a in artists:
        print(f"   {a}")

    table = build_table(tracks, artists)
    success = update_readme(table)

    if success:
        print("✅ README actualizado correctamente.")
    else:
        print("❌ No se pudo actualizar el README.")
        exit(1)

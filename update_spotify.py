import os
import re
import requests

def get_access_token():
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
    response = requests.get(
        "https://api.spotify.com/v1/me/top/tracks",
        headers={"Authorization": f"Bearer {token}"},
        params={"limit": limit, "time_range": "short_term"},
    )
    response.raise_for_status()
    items = response.json()["items"]
    return [
        f"{i+1}. {t['name']} — <i>{t['artists'][0]['name']}</i>"
        for i, t in enumerate(items)
    ]

def get_top_artists(token, limit=5):
    response = requests.get(
        "https://api.spotify.com/v1/me/top/artists",
        headers={"Authorization": f"Bearer {token}"},
        params={"limit": limit, "time_range": "short_term"},
    )
    response.raise_for_status()
    items = response.json()["items"]
    return [f"{i+1}. {a['name']}" for i, a in enumerate(items)]

def build_table(tracks, artists):
    tracks_html = "<br/>\n        ".join(tracks)
    artists_html = "<br/>\n        ".join(artists)
    return f"""<!-- SPOTIFY_START -->
  <table>
    <tr>
      <th>🎵 Top Tracks</th>
      <th>🎤 Top Artists</th>
      <th>🕐 Recently Played</th>
    </tr>
    <tr>
      <td>
        {tracks_html}
      </td>
      <td>
        {artists_html}
      </td>
      <td>
        <a href="https://open.spotify.com/user/31rfklb2xjtwgcvtpz6hpvynfkfi">
          <img src="https://spotify-recently-played-readme.vercel.app/api?user=31rfklb2xjtwgcvtpz6hpvynfkfi&count=5&unique=true&width=300" alt="Recently Played" />
        </a>
      </td>
    </tr>
  </table>
<!-- SPOTIFY_END -->"""

def update_readme(new_table):
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()

    # FIX 1: \s* para manejar espacios/indentación antes de los marcadores
    pattern = r"\s*<!-- SPOTIFY_START -->.*?<!-- SPOTIFY_END -->"
    updated = re.sub(pattern, "\n" + new_table, content, flags=re.DOTALL)

    if updated == content:
        print("⚠️  No se encontraron los marcadores en el README.")
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
    for t in tracks: print(f"   {t}")

    print("🎤 Top Artists:")
    for a in artists: print(f"   {a}")

    table = build_table(tracks, artists)
    success = update_readme(table)

    if success:
        print("✅ README actualizado correctamente.")
    else:
        print("❌ No se pudo actualizar el README.")
        exit(1)

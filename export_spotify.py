from pathlib import Path
import datetime
import json

MIN_LENGTH_SECONDS = 30

folder = Path("spotify_data")
files = list(folder.glob('*.json'))
outfile = open("spotify_data.txt", "w", encoding="utf-8")

for i, path in enumerate(files):
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    for value in data:
        if value["ms_played"] < MIN_LENGTH_SECONDS * 1000:
            # skip songs played under the min length
            continue

        timestamp = int(datetime.datetime.fromisoformat(value["ts"].replace("Z", "+00:00")).timestamp())
        outfile.write("{}\t{}\t{}\t{}\n".format(
            timestamp,
            value["master_metadata_track_name"],
            value["master_metadata_album_artist_name"],
            value["master_metadata_album_album_name"],
        ))

    outfile.flush()
    print(f"file {i + 1}/{len(files)} completed: {path.name}")

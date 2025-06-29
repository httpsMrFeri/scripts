import sqlite3
import json

print("F3RI")

DB = "x-ui.db"
connect = sqlite3.connect(DB)
cursor = connect.cursor()

ids = cursor.execute("SELECT id FROM inbounds").fetchall()

for i in range(len(ids)):
    id = ids[i][0]
    port = cursor.execute("SELECT port FROM inbounds WHERE id = ?", (id,)).fetchone()[0]
    stream_settings_raw = cursor.execute("SELECT stream_settings FROM inbounds WHERE id = ?", (id,)).fetchone()[0]

    # Default value if stream_settings is missing
    if not stream_settings_raw:
        print(f"[!] stream_settings is empty for id={id}, default value applied.")
        stream_setting = {
            "network": "tcp",
            "security": "none"
        }
    else:
        try:
            stream_setting = json.loads(stream_settings_raw)
        except json.JSONDecodeError as e:
            print(f"[!] Invalid JSON for id={id}: {e}, default value applied.")
            stream_setting = {
                "network": "tcp",
                "security": "none"
            }

    # Add externalProxy
    stream_setting['externalProxy'] = [{
        "forceTls": "same",
        "dest": "94.182.135.34",
        "port": port,
        "remark": ""
    }]

    stream_setting_json = json.dumps(stream_setting)
    cursor.execute("UPDATE inbounds SET stream_settings = ? WHERE id = ?", (stream_setting_json, id))

connect.commit()
connect.close()

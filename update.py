import sqlite3
import json
DB = "x-ui.db"
connect = sqlite3.connect(DB)
cursor = connect.cursor()
ids = cursor.execute("SELECT id FROM inbounds").fetchall() 
for i in range(len(ids)):
    id = ids[i][0]
    port = cursor.execute("SELECT port FROM inbounds WHERE id = ?", (id,)).fetchone()[0]
    stream_setting = json.loads(cursor.execute("SELECT stream_settings FROM inbounds WHERE id = ?", (id,)).fetchone()[0])
    add_data = [
    {
      "forceTls": "same",
      "dest": "10.10.10.10",
      "port":port,
      "remark": ""
    }]
    stream_setting['externalProxy'] = add_data
    stream_setting = json.dumps(stream_setting)
    cursor.execute("UPDATE inbounds SET stream_settings = ? WHERE id = ?", (stream_setting, id))
connect.commit()
connect.close()



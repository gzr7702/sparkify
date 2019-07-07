# DROP TABLES

songplay_table_drop = "DROP TABLE songplay"
user_table_drop = "DROP TABLE user"
song_table_drop = "DROP TABLE song"
artist_table_drop = "DROP TABLE artist"
time_table_drop = "DROP TABLE time"

# CREATE TABLES

songplay_table_create = ("""
    CREATE TABLE IF NOT EXISTS songplay (
        songplay_id int, start_time timestamp, user_id int, level int, song_id varchar,
        artist_id varchar, session_id int, location varchar, user_agent varchar
        )
""")

user_table_create = ("""
    CREATE TABLE IF NOT EXISTS user (
        user_id int, first_name varchar, last_name varchar, gender varchar, level int
    )
""")

song_table_create = ("""
    CREATE TABLE IF NOT EXISTS song (
        song_id int, title varchar, artist_id varchar, year int, duration numeric
    )
""")

artist_table_create = ("""
    CREATE TABLE IF NOT EXISTS artist (
        artist_id varchar, name varchar, location varchar, latitude numeric, longitude numeric
    )
""")

time_table_create = ("""
    CREATE TABLE IF NOT EXISTS time (
        start_time time, hour interval hour, day interval day, week, month interval month,
        year interval year, weekday date
    )
""")

# INSERT RECORDS

songplay_table_insert = ("""
""")

user_table_insert = ("""
""")

song_table_insert = ("""
""")

artist_table_insert = ("""
""")


time_table_insert = ("""
""")

# FIND SONGS

song_select = ("""
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
import requests
from datetime import datetime
import sqlite3

def import_gists_to_database(db, username, commit=True):
    url="https://api.github.com/users/{}/gists".format(username)
    all_response=requests.get(url)
    all_response.raise_for_status()
    response=all_response.json()
    #db_conn = sqlite3.connect(db)
    _SQL="""
    DROP TABLE if exists gists;
    CREATE TABLE gists (
    id INTEGER PRIMARY KEY autoincrement,
    github_id TEXT NOT NULL,
    html_url TEXT NOT NULL,
    git_pull_url TEXT NOT NULL,
    git_push_url TEXT NOT NULL,
    commits_url TEXT NOT NULL,
    forks_url TEXT NOT NULL,
    public BOOLEAN NOT NULL,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL,
    comments INTEGER NOT NULL,
    comments_url TEXT NOT NULL);
    """
    db.executescript(_SQL)

    query="""
    INSERT INTO gists (github_id, html_url, git_pull_url, git_push_url, commits_url, forks_url, public, created_at, updated_at, comments, comments_url)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
    """
    params=[(g['id'], g['html_url'], g['git_pull_url'], g['git_push_url'], g['commits_url'], g['forks_url'], g['public'], g['created_at'], g['updated_at'], g['comments'],g['comments_url']) for g in response]
    print(params)
    db.executemany(query, params)
    if commit==True:
        db.commit()

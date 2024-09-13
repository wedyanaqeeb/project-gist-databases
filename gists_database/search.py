from .models import Gist

def search_gists(db_connection, **kwargs):
  if kwargs and 'created_at' in kwargs.keys():
        params=kwargs
        query='SELECT * FROM gists WHERE datetime(created_at) = datetime(:created_at)'
        cursor=db_connection.execute(query, params)
    elif kwargs and 'github_id' in kwargs.keys():
        params=kwargs
        query='SELECT * FROM gists WHERE github_id = :github_id'
        cursor=db_connection.execute(query, params)
    elif not kwargs:
        #query="""SELECT * FROM gists;"""
        cursor=db_connection.execute('SELECT * FROM gists')

    list_gists=[Gist(i) for i in cursor]
    print(list_gists)
    print(len(list_gists))
    return list_gists

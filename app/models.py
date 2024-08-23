from app.database import get_connection

def create_post(title, content):
    connection = get_connection()
    with connection.cursor() as cursor:
        sql = "INSERT INTO posts (title, content) VALUES (%s, %s)"
        cursor.execute(sql, (title, content))
    connection.commit()
    connection.close()

def update_post(post_id, title, content):
    connection = get_connection()
    with connection.cursor() as cursor:
        sql = "UPDATE posts SET title=%s, content=%s WHERE id=%s"
        cursor.execute(sql, (title, content, post_id))
    connection.commit()
    connection.close()

def delete_post(post_id):
    connection = get_connection()
    with connection.cursor() as cursor:
        sql = "DELETE FROM posts WHERE id=%s"
        cursor.execute(sql, (post_id,))
    connection.commit()
    connection.close()

def get_posts(search_type=None, keyword=None):
    connection = get_connection()
    with connection.cursor() as cursor:
        if search_type == 'title':
            sql = "SELECT * FROM posts WHERE title LIKE %s"
            cursor.execute(sql, ('%' + keyword + '%',))
        elif search_type == 'content':
            sql = "SELECT * FROM posts WHERE content LIKE %s"
            cursor.execute(sql, ('%' + keyword + '%',))
        else:
            sql = "SELECT * FROM posts"
            cursor.execute(sql)
        result = cursor.fetchall()
    connection.close()
    return result
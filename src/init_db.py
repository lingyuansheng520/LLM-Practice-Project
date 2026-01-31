import sqlite3

def init_database():
    conn = sqlite3.connect('chat_history.db')
    cursor = conn.cursor()

    # 这里的 SQL 语句就是创建表的逻辑
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS chat_records (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT NOT NULL,
        question TEXT,
        answer TEXT,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    );
    """

    try:
        cursor.execute(create_table_sql)
        conn.commit()
        print("✅ 数据库初始化成功！")
    except Exception as e:
        print(f"❌ 失败: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    init_database()
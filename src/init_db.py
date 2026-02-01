import sqlite3


def init_database():
    conn = sqlite3.connect('chat_history.db')
    cursor = conn.cursor()
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
    except Exception as e:
        print(f"❌ 初始化失败: {e}")
    finally:
        conn.close()


def save_chat_record(user_id, question, answer):
    conn = sqlite3.connect('chat_history.db')
    cursor = conn.cursor()
    insert_sql = "INSERT INTO chat_records (user_id, question, answer) VALUES (?, ?, ?)"
    try:
        cursor.execute(insert_sql, (user_id, question, answer))
        conn.commit()
    except Exception as e:
        print(f"❌ 保存失败: {e}")
    finally:
        conn.close()


def get_chat_history(user_id, limit=5):
    conn = sqlite3.connect('chat_history.db')
    cursor = conn.cursor()
    query_sql = "SELECT question, answer FROM chat_records WHERE user_id = ? ORDER BY created_at DESC LIMIT ?"
    try:
        cursor.execute(query_sql, (user_id, limit))
        return cursor.fetchall()
    finally:
        conn.close()


# --- 下面是测试逻辑 ---
if __name__ == "__main__":
    # 1. 初始化
    init_database()

    # 2. 存入两条测试数据
    save_chat_record("user_01", "什么是 RAG？", "RAG 是检索增强生成技术。")
    save_chat_record("user_01", "Transformer 是谁发明的？", "是 Google 团队在 2017 年提出的。")

    # 3. 读取并打印
    print("正在查询 user_01 的历史记录...")
    history = get_chat_history("user_01")
    for row in history:
        print(f"问: {row[0]} | 答: {row[1]}")
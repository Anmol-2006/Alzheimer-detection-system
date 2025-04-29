# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import sqlite3

# app = Flask(__name__)
# CORS(app)

# DATABASE = 'dbms schema.sql'

# def get_db():
#     conn = sqlite3.connect(DATABASE)
#     conn.row_factory = sqlite3.Row
#     return conn

# def query_db(query, args=(), one=False):
#     conn = get_db()
#     cur = conn.execute(query, args)
#     rv = cur.fetchall()
#     cur.close()
#     conn.commit()
#     return (rv[0] if rv else None) if one else rv

# def init_db():
#     with app.app_context():
#         db = get_db()
#         with app.open_resource('schema.sql', mode='r') as f:
#             db.cursor().executescript(f.read())
#         db.commit()

# @app.cli.command('initdb')
# def initdb_command():
#     """Initializes the database."""
#     init_db()
#     print('Initialized the database.')

# def get_chatbot_response(user_message):
#     user_message_lower = user_message.lower()

#     # Simple keyword matching
#     if "what is" in user_message_lower and "alzheimer" in user_message_lower:
#         response = query_db("SELECT answer FROM knowledge_base WHERE question LIKE ?", ('%What is Alzheimer\'s disease%',), one=True)
#         return response['answer'] if response else "I can provide general information. Alzheimer's is a progressive brain disorder."

#     elif "early signs" in user_message_lower or "first symptoms" in user_message_lower:
#         response = query_db("SELECT answer FROM knowledge_base WHERE question LIKE ?", ('%early signs%',), one=True)
#         return response['answer'] if response else "Early signs can include memory loss and difficulty with daily tasks."

#     elif "memory loss" in user_message_lower:
#         response = query_db("SELECT answer FROM knowledge_base WHERE question LIKE ?", ('%memory loss%',), one=True)
#         return response['answer'] if response else "Memory loss is a key symptom that worsens over time."

#     elif "causes" in user_message_lower:
#         response = query_db("SELECT answer FROM knowledge_base WHERE question LIKE ?", ('%causes%',), one=True)
#         return response['answer'] if response else "The exact causes are complex and not fully understood."

#     elif "diagnosed" in user_message_lower or "diagnosis" in user_message_lower:
#         response = query_db("SELECT answer FROM knowledge_base WHERE question LIKE ?", ('%diagnosed%',), one=True)
#         return response['answer'] if response else "Diagnosis involves several medical assessments."

#     elif "cure" in user_message_lower or "treatment" in user_message_lower:
#         response_cure = query_db("SELECT answer FROM knowledge_base WHERE question LIKE ?", ('%cure%',), one=True)
#         response_treatment = query_db("SELECT answer FROM knowledge_base WHERE question LIKE ?", ('%treatment%',), one=True)
#         cure_text = response_cure['answer'] if response_cure else "Currently, there is no cure."
#         treatment_text = response_treatment['answer'] if response_treatment else "Treatments focus on managing symptoms."
#         return f"{cure_text} {treatment_text}"

#     elif "caregiver" in user_message_lower or "caring" in user_message_lower:
#         response = query_db("SELECT answer FROM knowledge_base WHERE question LIKE ?", ('%caregiver%',), one=True)
#         return response['answer'] if response else "Providing care can be demanding; support is available."

#     elif "research" in user_message_lower:
#         response = query_db("SELECT answer FROM knowledge_base WHERE question LIKE ?", ('%research%',), one=True)
#         return response['answer'] if response else "Research is actively ongoing to better understand and treat Alzheimer's."

#     else:
#         # Default response if no specific keywords are found
#         return "I'm still learning about Alzheimer's. Could you ask something else?"

# @app.route('/chat', methods=['POST'])
# def chat():
#     try:
#         data = request.get_json()
#         user_message = data.get('message')

#         if user_message:
#             bot_response = get_chatbot_response(user_message)
#             query_db("INSERT INTO chat_history (user_message, bot_response) VALUES (?, ?)", (user_message, bot_response))
#             return jsonify({'response': bot_response})
#         else:
#             return jsonify({'error': 'No message received'}), 400
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500

# if __name__ == '__main__':
#     app.run(debug=True, port=5000)


from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

DATABASE = 'dbms schema.sql'

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def query_db(query, args=(), one=False):
    conn = get_db()
    cur = conn.execute(query, args)
    rv = cur.fetchall()
    cur.close()
    conn.commit()
    return (rv[0] if rv else None) if one else rv

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

@app.cli.command('initdb')
def initdb_command():
    """Initializes the database."""
    init_db()
    print('Initialized the database.')

def get_chatbot_response(user_message):
    user_message_lower = user_message.lower()

    try:
        if "what is" in user_message_lower and "alzheimer" in user_message_lower:
            response = query_db("SELECT answer FROM knowledge_base WHERE LOWER(question) LIKE LOWER(?)", ('%What is Alzheimer\'s disease%',), one=True)
            return response['answer'] if response else "I can provide general information. Alzheimer's is a progressive brain disorder."

        elif "early signs" in user_message_lower or "first symptoms" in user_message_lower:
            response = query_db("SELECT answer FROM knowledge_base WHERE LOWER(question) LIKE LOWER(?)", ('%early signs%',), one=True)
            return response['answer'] if response else "Early signs can include memory loss and difficulty with daily tasks."

        elif "memory loss" in user_message_lower:
            response = query_db("SELECT answer FROM knowledge_base WHERE LOWER(question) LIKE LOWER(?)", ('%memory loss%',), one=True)
            return response['answer'] if response else "Memory loss is a key symptom that worsens over time."

        elif "causes" in user_message_lower:
            response = query_db("SELECT answer FROM knowledge_base WHERE LOWER(question) LIKE LOWER(?)", ('%causes%',), one=True)
            return response['answer'] if response else "The exact causes are complex and not fully understood."

        elif "diagnosed" in user_message_lower or "diagnosis" in user_message_lower:
            response = query_db("SELECT answer FROM knowledge_base WHERE LOWER(question) LIKE LOWER(?)", ('%diagnosed%',), one=True)
            return response['answer'] if response else "Diagnosis involves several medical assessments."

        elif "cure" in user_message_lower or "treatment" in user_message_lower:
            response_cure = query_db("SELECT answer FROM knowledge_base WHERE LOWER(question) LIKE LOWER(?)", ('%cure%',), one=True)
            response_treatment = query_db("SELECT answer FROM knowledge_base WHERE LOWER(question) LIKE LOWER(?)", ('%treatment%',), one=True)
            cure_text = response_cure['answer'] if response_cure else "Currently, there is no cure."
            treatment_text = response_treatment['answer'] if response_treatment else "Treatments focus on managing symptoms."
            return f"{cure_text} {treatment_text}"

        elif "caregiver" in user_message_lower or "caring" in user_message_lower:
            response = query_db("SELECT answer FROM knowledge_base WHERE LOWER(question) LIKE LOWER(?)", ('%caregiver%',), one=True)
            return response['answer'] if response else "Providing care can be demanding; support is available."

        elif "research" in user_message_lower:
            response = query_db("SELECT answer FROM knowledge_base WHERE LOWER(question) LIKE LOWER(?)", ('%research%',), one=True)
            return response['answer'] if response else "Research is actively ongoing to better understand and treat Alzheimer's."

        else:
            return "I'm still learning about Alzheimer's. Could you ask something else?"

    except sqlite3.Error as e:
        print(f"Database error in get_chatbot_response: {e}")
        return "Sorry, I encountered a database error."
    except Exception as e:
        print(f"General error in get_chatbot_response: {e}")
        return "Sorry, I encountered an unexpected error."

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_message = data.get('message')

        if user_message:
            bot_response = get_chatbot_response(user_message)
            query_db("INSERT INTO chat_history (user_message, bot_response) VALUES (?, ?)", (user_message, bot_response))
            return jsonify({'response': bot_response})
        else:
            return jsonify({'error': 'No message received'}), 400
    except Exception as e:
        print(f"Error in /chat route: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)

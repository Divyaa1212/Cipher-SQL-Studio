## CipherSQLStudio

CipherSQLStudio is a simple SQL practice and execution web application that allows users to write SQL queries in a browser and execute them against a MySQL database using a Flask backend. It is designed for learning and practicing SQL concepts with instant feedback.

---

## Features

- Write and execute SQL queries in real time  
- Clean and responsive web interface  
- Flask backend for query execution  
- Results displayed in tabular format  
- Hint system for guided learning  
- CORS-enabled API communication  

---

## Tech Stack

### Frontend
- HTML  
- CSS  
- JavaScript  

### Backend
- Python  
- Flask  
- Flask-CORS  
- PyMySQL  

### Database
- MySQL  

---

## Project Structure

```
CipherSQLStudio/
│
├── index.html
├── app.py
└── README.md
```

---

## How It Works

1. The user enters an SQL query in the text area  
2. The query is sent to the Flask backend using a POST request  
3. The backend executes the query on the MySQL database  
4. Results are returned in JSON format  
5. The frontend displays the output in a table  

---

## Setup Instructions

```bash
git clone https://github.com/your-username/CipherSQLStudio.git
cd CipherSQLStudio

pip install flask flask-cors pymysql

CREATE DATABASE cipher_sql_studio;

host="localhost"
user="root"
password="your_password"
database="cipher_sql_studio"

python app.py
http://127.0.0.1:5000

```
## Future Enhancements

- User authentication
- SQL query validation
- Multiple database support
- Predefined SQL challenges
- Syntax highlighting editor

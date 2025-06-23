# 📝 Feedback System

A simple web-based system that allows managers to submit feedback about employees. Built using **FastAPI** and **React**, this project supports structured feedback submissions, manager/employee roles, and sentiment tagging.

---

## 🚀 Tech Stack

### Backend
- **FastAPI**: Lightweight, high-performance Python web framework.
- **SQLAlchemy**: ORM for managing database models.
- **SQLite**: Lightweight, file-based relational database for development.
- **Pydantic**: For data validation and serialization.
- **Uvicorn**: ASGI server for running FastAPI.

### Frontend
- **React**: For building the UI.
- **Axios**: For making HTTP requests to the backend.

---

## 🛠️ Setup Instructions

### Prerequisites
- Python 3.10+ installed
- Node.js and npm installed
- Git (for version control)

---

### 🔧 Backend Setup

1. **Clone the repository**  
   ```bash
   git clone https://github.com/hareem123-sketch/feedback-system.git
   cd feedback-system/backend
**Create a virtual environment and activate it**
python -m venv venv
.\venv\Scripts\activate   # On Windows
**Install dependencies**
pip install -r requirements.txt

**Run the backend server**
uvicorn app.main:app --reload
**Backend will run** at: http://127.0.0.1:8000

**Frontend Setup**

**Navigate to frontend folder**
cd ../frontend
**Install dependencies**
npm install
**Start the React app**
npm start
**
**Frontend will run at****: http://localhost:3000

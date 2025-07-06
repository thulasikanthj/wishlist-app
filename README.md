# 🛍️  Wishlist App

A collaborative web app that lets multiple users create, manage, and interact with shared wishlists in real-time — perfect for group gift planning, travel shopping, and more!

---

## ✨ Features

- 🔐 User Authentication (Register/Login)
- 📝 Create personal or shared wishlists
- 👥 Invite other users to collaborate
- 🛍️ Add, edit, delete products in wishlists
- ⚡ Real-time updates using WebSockets

---

## 🛠 Tech Stack

- **Frontend:** HTML, CSS, Bootstrap
- **Backend:** Python, Flask, Flask-SQLAlchemy
- **Real-Time:** Flask-SocketIO
- **Database:** SQLite

---

## 🧩 Setup Instructions

### 🔧 Prerequisites:
- Python 3.x
- pip (Python package manager)

### 📦 Install and Run:

```bash
# Clone or unzip the project
cd wishlist-app

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py

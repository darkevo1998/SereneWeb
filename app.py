from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

# Initialize Flask app untuk SereneWed
app = Flask(__name__)
app.config['SECRET_KEY'] = 'serenewed_secret_key_2024'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///serenewed.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy untuk database SereneWed
db = SQLAlchemy(app)

# Import routes setelah inisialisasi db
from routes import *

if __name__ == '__main__':
    with app.app_context():
        # Buat semua tabel database untuk SereneWed
        db.create_all()
    # Jalankan website SereneWed
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port) 
from app import db
from datetime import datetime

class Contact(db.Model):
    """Model form kontak untuk inquiry website pernikahan"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(20))
    message = db.Column(db.Text, nullable=False)
    inquiry_type = db.Column(db.String(50), default='general')  # general, website, consultation
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Contact {self.name}>'

class WebsiteRequest(db.Model):
    """Model request website pernikahan untuk SereneWed"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    wedding_date = db.Column(db.Date, nullable=False)
    website_type = db.Column(db.String(100), nullable=False)  # wedding invitation, wedding gallery, wedding blog
    features_needed = db.Column(db.Text)  # Fitur yang dibutuhkan
    budget_range = db.Column(db.String(100))
    timeline = db.Column(db.String(100))
    special_requirements = db.Column(db.Text)
    status = db.Column(db.String(20), default='pending')  # pending, confirmed, completed
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<WebsiteRequest {self.name}>'

class WebsiteService(db.Model):
    """Model layanan website pernikahan SereneWed"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price_range = db.Column(db.String(50), nullable=False)
    features = db.Column(db.Text)
    includes = db.Column(db.Text)  # Yang termasuk dalam paket
    delivery_time = db.Column(db.String(50))  # Waktu pengerjaan
    image = db.Column(db.String(200))
    is_featured = db.Column(db.Boolean, default=False)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<WebsiteService {self.name}>'

class WebsitePortfolio(db.Model):
    """Model portfolio website pernikahan SereneWed"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    image_url = db.Column(db.String(200), nullable=False)
    website_url = db.Column(db.String(200))
    couple_names = db.Column(db.String(100))
    website_type = db.Column(db.String(100))  # wedding invitation, gallery, blog
    technologies = db.Column(db.String(200))  # Tech stack yang digunakan
    is_featured = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<WebsitePortfolio {self.title}>' 
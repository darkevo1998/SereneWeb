from app import app, db
from models import WebsiteService, WebsitePortfolio
from datetime import datetime

def init_database():
    with app.app_context():
        # Create all tables
        db.create_all()
        
        # Check if data already exists
        if WebsiteService.query.first() is None:
            # Add sample services
            services = [
                WebsiteService(
                    name="Basic Package",
                    description="Digital Wedding Invitation with complete features",
                    price_range="$99 USD",
                    features="Modern responsive design, Main page with couple photos, Complete event information, Wedding countdown timer, Photo gallery (max 20 photos), Simple online RSVP, .com domain (1 year), Hosting (1 year), 2 revisions",
                    includes="Digital invitation, RSVP system, Photo gallery, Domain & hosting",
                    delivery_time="3-5 days",
                    image="basic-package.jpg",
                    is_featured=True,
                    is_active=True,
                    created_at=datetime.now()
                ),
                WebsiteService(
                    name="Premium Package",
                    description="Complete Website + Gallery with advanced features",
                    price_range="$199 USD",
                    features="All Basic Package features, Custom design according to theme, Unlimited photo gallery, Video gallery (max 5 videos), Complete RSVP form, Love story page, Family page, Background music, Scroll animations, 3 revisions, 6 months maintenance",
                    includes="All Basic features, Custom design, Video gallery, Love story, Family page, Music, Animations",
                    delivery_time="5-7 days",
                    image="premium-package.jpg",
                    is_featured=True,
                    is_active=True,
                    created_at=datetime.now()
                ),
                WebsiteService(
                    name="Luxury Package",
                    description="Premium Website + Blog with all features",
                    price_range="$299 USD",
                    features="All Premium Package features, Wedding blog, Wedding tips page, Unlimited video gallery, WhatsApp live chat, SEO optimization, Google Analytics, Automatic backup, Unlimited revisions, 1 year maintenance, 24/7 support",
                    includes="All Premium features, Blog, SEO, Analytics, Backup, Unlimited support",
                    delivery_time="7-10 days",
                    image="luxury-package.jpg",
                    is_featured=True,
                    is_active=True,
                    created_at=datetime.now()
                )
            ]
            
            for service in services:
                db.session.add(service)
            
            # Add sample portfolio items
            portfolios = [
                WebsitePortfolio(
                    title="Sarah & Ahmad Wedding",
                    description="Elegant digital invitation with beautiful design",
                    image_url="https://images.unsplash.com/photo-1519741497674-611481863552?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
                    website_url="#",
                    couple_names="Sarah & Ahmad",
                    website_type="wedding invitation",
                    technologies="HTML, CSS, JavaScript, Bootstrap",
                    is_featured=True,
                    created_at=datetime.now()
                ),
                WebsitePortfolio(
                    title="Diana & Rizki Gallery",
                    description="Complete wedding website with photo gallery",
                    image_url="https://images.unsplash.com/photo-1537907696089-75d5c5046780?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
                    website_url="#",
                    couple_names="Diana & Rizki",
                    website_type="wedding gallery",
                    technologies="HTML, CSS, JavaScript, Bootstrap",
                    is_featured=True,
                    created_at=datetime.now()
                ),
                WebsitePortfolio(
                    title="Maya & Budi Blog",
                    description="Wedding blog with love story and tips",
                    image_url="https://images.unsplash.com/photo-1594736797933-d0401ba2fe65?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
                    website_url="#",
                    couple_names="Maya & Budi",
                    website_type="wedding blog",
                    technologies="HTML, CSS, JavaScript, Bootstrap",
                    is_featured=True,
                    created_at=datetime.now()
                )
            ]
            
            for portfolio in portfolios:
                db.session.add(portfolio)
            
            # Commit all changes
            db.session.commit()
            print("Database initialized with sample data!")
        else:
            print("Database already has data!")

if __name__ == "__main__":
    init_database() 
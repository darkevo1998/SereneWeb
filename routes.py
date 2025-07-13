from flask import render_template, request, redirect, url_for, flash, jsonify
from app import app, db
from models import Contact, WebsiteRequest, WebsiteService, WebsitePortfolio
from datetime import datetime

@app.route('/')
def home():
    """Main Page - Wedding Website Services"""
    featured_services = WebsiteService.query.filter_by(is_featured=True, is_active=True).limit(3).all()
    featured_portfolio = WebsitePortfolio.query.filter_by(is_featured=True).limit(6).all()
    return render_template('home.html', featured_services=featured_services, featured_portfolio=featured_portfolio)

@app.route('/services')
def services():
    """Wedding Website Services Page"""
    services = WebsiteService.query.filter_by(is_active=True).all()
    return render_template('services.html', services=services)

@app.route('/about')
def about():
    """About Us Page"""
    return render_template('about.html')

@app.route('/portfolio')
def portfolio():
    """Wedding Website Portfolio Page"""
    portfolio_items = WebsitePortfolio.query.order_by(WebsitePortfolio.created_at.desc()).all()
    return render_template('gallery.html', portfolio_items=portfolio_items)

@app.route('/booking', methods=['GET', 'POST'])
def booking():
    """Wedding Service Booking Page"""
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        wedding_date = request.form.get('wedding_date')
        guest_count = request.form.get('guest_count')
        service_type = request.form.get('service_type')
        budget = request.form.get('budget')
        message = request.form.get('message')
        
        if name and email and phone and wedding_date and service_type:
            # Create a WebsiteRequest with the booking data
            request_website = WebsiteRequest(
                name=name,
                email=email,
                phone=phone,
                wedding_date=datetime.strptime(wedding_date, '%Y-%m-%d'),
                website_type=service_type,
                features_needed=guest_count,
                budget_range=budget,
                special_requirements=message,
                created_at=datetime.now()
            )
            db.session.add(request_website)
            db.session.commit()
            flash('Your wedding service booking has been successfully sent! Our team will contact you soon to discuss your wedding details.', 'success')
            return redirect(url_for('booking'))
        else:
            flash('Please complete all required fields.', 'error')
    
    return render_template('website_request.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """Contact Page"""
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        inquiry_type = request.form.get('inquiry_type', 'general')
        
        if name and email and message:
            contact = Contact(
                name=name,
                email=email,
                phone=phone,
                message=message,
                inquiry_type=inquiry_type,
                created_at=datetime.now()
            )
            db.session.add(contact)
            db.session.commit()
            flash('Thank you for your message! We will contact you soon to discuss your dream wedding website.', 'success')
            return redirect(url_for('contact'))
        else:
            flash('Please complete all required fields.', 'error')
    
    return render_template('contact.html')

@app.route('/request-website', methods=['GET', 'POST'])
def website_request():
    """Wedding Website Request Page"""
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        wedding_date = request.form.get('wedding_date')
        website_type = request.form.get('website_type')
        features_needed = request.form.get('features_needed')
        budget_range = request.form.get('budget_range')
        timeline = request.form.get('timeline')
        special_requirements = request.form.get('special_requirements')
        
        if name and email and phone and wedding_date and website_type:
            request_website = WebsiteRequest(
                name=name,
                email=email,
                phone=phone,
                wedding_date=datetime.strptime(wedding_date, '%Y-%m-%d'),
                website_type=website_type,
                features_needed=features_needed,
                budget_range=budget_range,
                timeline=timeline,
                special_requirements=special_requirements,
                created_at=datetime.now()
            )
            db.session.add(request_website)
            db.session.commit()
            flash('Your wedding website request has been successfully sent! Our team will contact you soon to discuss your special website.', 'success')
            return redirect(url_for('website_request'))
        else:
            flash('Please complete all required fields.', 'error')
    
    return render_template('website_request.html')

@app.route('/api/contact', methods=['POST'])
def api_contact():
    """API endpoint for contact form"""
    try:
        data = request.get_json()
        contact = Contact(
            name=data.get('name'),
            email=data.get('email'),
            phone=data.get('phone'),
            message=data.get('message'),
            inquiry_type=data.get('inquiry_type', 'general'),
            created_at=datetime.now()
        )
        db.session.add(contact)
        db.session.commit()
        return jsonify({'success': True, 'message': 'Message sent successfully! We will contact you soon.'})
    except Exception as e:
        return jsonify({'success': False, 'message': 'An error occurred. Please try again.'})

@app.errorhandler(404)
def not_found(error):
    """404 error handler"""
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    """500 error handler"""
    db.session.rollback()
    return render_template('500.html'), 500 
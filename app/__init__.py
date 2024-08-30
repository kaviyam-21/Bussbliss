from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'login'

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        # Import routes here to avoid circular imports
        from . import routes
        db.create_all()

        # Import User model here
        from .models import User

        # Load data from CSV if the table is empty
        if User.query.count() == 0:
            load_data_from_csv()

    return app

def load_data_from_csv():
    import csv
    from .models import User
    
    with open('example_data.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            user = User(
                username=row['username'],
                password=row['password'],
                role=row['role'],
                region=row['region'],
                familiarity=row['familiarity'],
                availability=row['availability'] == 'True',
                shift=row['shift'],
                bus_route=row['bus_route'],
                is_linked=row['is_linked'] == 'True'
            )
            db.session.add(user)
        db.session.commit()

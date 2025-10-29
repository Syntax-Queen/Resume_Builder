from datetime, timedelta
import os
from app import db

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Info(db.Model):
    __tablename__ = 'info'

    id = db.Column(db.Integer, primary_key=True)

    # Basic Info
    Name = db.Column(db.String(100), nullable=False)
    Phone = db.Column(db.String(20), nullable=False)
    Email = db.Column(db.String(100), nullable=False)
    City = db.Column(db.String(100))
    Github = db.Column(db.String(150))
    Linkedin = db.Column(db.String(150))

    # Education
    Degree = db.Column(db.String(100))
    Institution = db.Column(db.String(150))
    EducationStart = db.Column(db.String(20))
    EducationEnd = db.Column(db.String(20))
    EducationDescription = db.Column(db.Text)

    # Work Experience
    JobTitle = db.Column(db.String(100))
    Company = db.Column(db.String(150))
    WorkStart = db.Column(db.String(20))
    WorkEnd = db.Column(db.String(20))
    WorkDetails = db.Column(db.Text)

    # Projects
    ProjectName = db.Column(db.String(100))
    ProjectDescription = db.Column(db.Text)
    ProjectLink = db.Column(db.String(200))

    # Skills
    Skills = db.Column(db.Text)  # store as comma-separated list or JSON

    # Extras
    Languages = db.Column(db.Text)
    Certificates = db.Column(db.Text)
    Interests = db.Column(db.Text)

    def __repr__(self):
        return f'<Info {self.Name}>'

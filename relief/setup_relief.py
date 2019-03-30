from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'odd5tW5QEK-3H98ewJYQVMpX-Ueq1y4kk30kyqhHI8c'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/relief.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class ReliefConfig(db.Model):
    __tablename__ = 'reliefconfig'
    id = db.Column(db.Integer, primary_key=True)
    reliefKey = db.Column(db.String(120), unique=True, nullable=True)
    reliefValue = db.Column(db.String(120), unique=True, nullable=True)
    
    def __repr__(self):
        return f"ReliefConfig('{self.reliefKey}', '{self.reliefValue}')"

class Campaigns(db.Model):
    __tablename__ = 'campaigns'
    id = db.Column(db.Integer, primary_key=True)
    campaign_name = db.Column(db.String(120), unique=True, nullable=False)
    report_date = db.Column(db.DateTime, nullable=False)
    summary_of_business_impact = db.Column(db.String(250), unique=False, nullable=True)

    def get_id(self):
        return self.id

    def __repr__(self, campaign_name, report_date):
        return f"Campaign('{self.campaign_name}', '{self.report_date}', '{self.summary_of_business_impact}')"

class CyberKillChains(db.Model):
    __tablename__ = 'cyber_kill_chains'
    id = db.Column(db.Integer, primary_key=True)
    campaign_id = db.Column(db.Integer, db.ForeignKey('campaigns.id'), nullable=False)
    phase = db.Column(db.String(25), nullable=False)
    adversary = db.Column(db.String(250), nullable=True)
    capability = db.Column(db.String(250), nullable=True)
    infrastructure = db.Column(db.String(250), nullable=True)
    victim = db.Column(db.String(250), nullable=True)
    business_impact = db.Column(db.String(250), nullable=True)
    courses_of_action = db.Column(db.String(250), nullable=True)

    def __repr__(self):
        return f"CyberKillChainPhase('{self.campaign_id}', '{self.phase}')"

# Create the database
db.create_all()
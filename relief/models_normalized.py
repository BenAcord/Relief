from datetime import datetime
from relief import db

class Settings(db.Model):
    __tablename__ = 'settings'
    id = db.Column(db.Integer, primary_key=True)
    reliefKey = db.Column(db.String(120), unique=True, nullable=True)
    reliefValue = db.Column(db.String(120), unique=True, nullable=True)
    

class Campaigns(db.Model):
    __tablename__ = 'campaigns'
    id = db.Column(db.Integer, primary_key=True)
    campaign_name = db.Column(db.String(120), unique=True, nullable=False)
    report_date = db.Column(db.DateTime, unique=True, nullable=False)
    summary_of_business_impact = db.Column(db.String(250), unique=False, nullable=True)
    cyber_kill_chains = db.relationship('Cyber_Kill_Chains', backref='', lazy=True)

    def __repr__(self):
        return f"Campaigns('{self.campaign_name}', '{self.report_date}', '{self.summary_of_business_impact}')"


class CyberKillChains(db.Model):
    __tablename__ = 'cyber_kill_chains'
    id = db.Column(db.Integer, primary_key=True)
    # define the foreign key to the campaigns table
    campaign_id = db.Column(db.Integer, db.ForeignKey('campaigns.id', nullable=False))
    phase = db.Column(db.String(25), nullable=True, unique=True, default='Unknown')
    adversary = db.Column(db.String(250), nullable=True, default='Unknown')
    capability = db.Column(db.String(250), nullable=True, default='Unknown')
    infrastructure = db.Column(db.String(250), nullable=True, default='Unknown')
    victim = db.Column(db.String(250), nullable=True, default='Unknown')
    business_impact = db.Column(db.String(250), nullable=True, default='Unknown')
    courses_of_action = db.Column(db.String(250), nullable=True, default='Unknown')

    def __repr__(self):
        return f"cyber_kill_chains('{self.adversary}', '{self.capability}', '{self.infrastructure}', '{self.victim}', '{self.business_impact}', '{self.courses_of_action}')"
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from relief import db


class ReliefConfig(db.Model):
    __tablename__ = 'reliefconfig'
    #id = db.Column(db.Integer, primary_key=True)
    reliefKey = db.Column(db.String(120), primary_key=True, unique=True, nullable=False)
    reliefValue = db.Column(db.String(120), unique=False, nullable=True)
    
    def __repr__(self):
        return f"ReliefConfig('{self.reliefKey}', '{self.reliefValue}')"

class Campaigns(db.Model):
    __tablename__ = 'campaigns'
    id = db.Column(db.Integer, primary_key=True)
    campaign_name = db.Column(db.String(120), unique=True, nullable=False)
    report_date = db.Column(db.DateTime, nullable=False)
    summary_of_business_impact = db.Column(db.String(2000), unique=False, nullable=True)
    chains = db.relationship("CyberKillChains", cascade="all,delete", backref="chains", passive_deletes=True)
    
    def get_id(self):
        return self.id

    def __repr__(self):
        return f"Campaign('{self.campaign_name}', '{self.report_date}', '{self.summary_of_business_impact}')"
        

class CyberKillChains(db.Model):
    __tablename__ = 'cyber_kill_chains'
    id = db.Column(db.Integer, primary_key=True)
    phase = db.Column(db.String(25), nullable=False)
    adversary = db.Column(db.String(250), nullable=True)
    capability = db.Column(db.String(250), nullable=True)
    infrastructure = db.Column(db.String(250), nullable=True)
    victim = db.Column(db.String(250), nullable=True)
    business_impact = db.Column(db.String(2000), nullable=True)
    courses_of_action = db.Column(db.String(250), nullable=True)
    # one to many relationships
    campaign_id = db.Column(db.Integer, db.ForeignKey('campaigns.id', ondelete='CASCADE'))
    #campaign = db.relationship('Campaign', backref=db.backref('campaigns', cascade="all, delete-orphan"), lazy=True)

    def __repr__(self):
        return f"CyberKillChainPhase('{self.campaign_id}', '{self.phase}', '{self.adversary}', '{self.capability}', '{self.infrastructure}', '{self.victim}', '{self.business_impact}', '{self.courses_of_action}')"
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, BooleanField, TextAreaField, DateField, SelectMultipleField, TextField, HiddenField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from relief.models import Campaigns, ReliefConfig, CyberKillChains
from relief import db

#allsettings = {}
#ReliefConfig.query.all()
#allsettings = ReliefConfig.query.all()
#print(allsettings)
prefix = "" #ReliefConfig.query.filter_by(reliefKey='filenamePrefix').first()
traffic = ""
marking = ""
author = ""
category = ""
title = ""
subject = ""
keywords = ""

class UpdateSettingsForm(FlaskForm):
    newFileNamePrefix = StringField('Presentation File Name Prefix - ', 
        validators = [DataRequired(), Length(min=1, max=120)], 
        default=prefix)  #allsettings[0].reliefValue)
    newTrafficLightDefault = SelectField(u'Traffic Light Default - used to mark each slide with a TLP indicator', 
        validators = [DataRequired(), Length(max=5)],
        choices=[('RED', 'RED'), ('AMBER', 'AMBER'), ('GREEN', 'GREEN'), ('WHITE', 'WHITE')], 
        default=traffic)  #allsettings[1].reliefValue)
    newDataMarkingFooter = StringField('Data Footer Marker - data classificiation and handling tag', 
        validators = [Length(max=120)],
        default=marking)  #allsettings[2].reliefValue)
    newPresentationAuthor = StringField('Presentation Author', 
        validators = [Length(max=120)],
        default=author)  #allsettings[3].reliefValue)
    newPresentationCategory = StringField('Presentation Category', 
        validators = [Length(max=120)],
        default=category)  #allsettings[4].reliefValue)
    newPresentationTitle = StringField('Presentation Title', 
        validators = [Length(max=120)],
        default=title)  #allsettings[5].reliefValue)
    newPresentationSubject = StringField('Presentation Subject', 
        validators = [Length(max=120)],
        default=subject)  #allsettings[6].reliefValue)
    newPresentationKeywords = StringField('Presentation Keywords', 
        validators = [Length(max=120)],
        default=keywords)  #allsettings[7].reliefValue)
    
    submit = SubmitField('Update')
    reset = SubmitField('Reset to Defaults')


class Home(FlaskForm):
    welcomeMessage = TextField('Welcome to Relief, the app that summarizes your threat intelligence analysis into a well-crafted presentation.</p><p>Relief is a structured approach to recording the key data points surrounding a threat event. Each campaign has an associated and layered Cyber Kill Chain, business impact, Diamond Model, and courses of action taken to limit further risk.  Relief uses that data to create standard presentations for stakeholder communication.')
    instructions = TextField('<p><h4>About the menu</h4>If you are new or giving Relief a test run start with the New menu item to create a campaign and assign some Cyber Kill Chain phases with Diamond Models.</p><p>Campaigns will display a table view of all your previous campaigns with options to enrich (edit), remove, or make a presentation.</p><p>Settings customize the output presentation content. It is worth a look even if you do not plan to change defaults.</p>')
    references = TextField('<p>The Lockheed Martin Cyber Kill Chain: https://www.lockheedmartin.com/en-us/capabilities/cyber/cyber-kill-chain.html</p><p>The Diamond Model: Sergio Caltagirone, Andrew Pendergast, and Christopher Betz, “Diamond Model of Intrusion Analysis,” Center for Cyber Threat Intelligence and Threat Research, Hanover, MD, Technical Report ADA586960, 05 July 2013.</p><p>The National Cybersecurity and Communications Integration Center’s (NCCIC) Traffic Light Protocol (TLP) https://www.us-cert.gov/tlp</p>')

class Stats(FlaskForm):
    welcomeMessage = TextField('Measurements and charts reveal strengths as well as potential blind spots.')

class NewCampaign(FlaskForm):
    campaignName = StringField('Campaign Name', 
        validators = [DataRequired(), Length(min=1, max=120)])
    reportDate = DateField('Report Date', 
        format='%m/%d/%Y', validators = [DataRequired()])
    summaryBusinessImpact = TextAreaField('Summary of Business Impact', 
        validators = [DataRequired(), Length(min=1, max=2000)])
    submit = SubmitField('Create')
    
class DisplayCampaign(FlaskForm):
    # Campaign fields
    campaignName = StringField('Campaign Name', 
        validators = [DataRequired(), Length(min=1, max=120)])
    reportDate = DateField('Report Date', 
        format='%m/%d/%Y', validators = [DataRequired()])
    summaryBusinessImpact = TextAreaField('Summary of Business Impact', 
        validators = [DataRequired(), Length(min=1, max=2000)])
    savecampaign = SubmitField('Save Campaign Changes')
    deletecampaign = SubmitField('Delete Campaign')
    # Cyber Kill Chain Phase fields
    phase = SelectField(u'Cyber Kill Chain Phase', 
        validators = [DataRequired(), Length(max=25)],
        choices=[('Reconnaissance', 'Reconnaissance'), 
                 ('Weaponization', 'Weaponization'), 
                 ('Delivery', 'Delivery'), 
                 ('Exploitation', 'Exploitation'), 
                 ('Installation', 'Installation'), 
                 ('Command and Control', 'Command and Control'), 
                 ('Actions on Objectives', 'Actions on Objectives')], 
        default='Installation')

    adversary = TextAreaField('Adversary')
    capability = TextAreaField('Capability (<i>or MITRE ATT&CK&#8482; Matrix Technique with details</i>)')
    infrastructure = TextAreaField('Infrastructure')
    victim = TextAreaField('Victim')
    business_impact = TextAreaField('Business Impact', validators =[DataRequired(), Length(min=0, max=2000)])

    courses_of_action = SelectMultipleField(u'Courses of Action', 
        choices=[('Discover', 'Discover'), 
                 ('Detect', 'Detect'), 
                 ('Deny', 'Deny'), 
                 ('Disrupt', 'Disrupt'), 
                 ('Degrade', 'Degrade'), 
                 ('Deceive', 'Deceive')])
    # FUTURE :  export = SubmitField('Make Presentation')
    addphase = SubmitField('Add Phase')
    editphase = SubmitField('Edit')
    deletephase = SubmitField('Delete')

class ListCampaigns(FlaskForm):
    export_row_id = HiddenField("export_row_id")
    edit_row_id = HiddenField("edit_row_id")
    enrich = SubmitField('Enrich')
    export = SubmitField('Make Presentation')
    delete = SubmitField('Delete')

class AddKillChainPhase(FlaskForm):
    # Get Campaign Name by the ID passed into the form.
    campaignName = StringField('Campaign Name', 
        validators = [DataRequired(), Length(min=1, max=120)])

    phase = SelectField(u'Cyber Kill Chain Phase', 
        validators = [DataRequired(), Length(max=25)],
        choices=[('Reconnaissance', 'Reconnaissance'), 
                 ('Weaponization', 'Weaponization'), 
                 ('Delivery', 'Delivery'), 
                 ('Exploitation', 'Exploitation'), 
                 ('Installation', 'Installation'), 
                 ('Command and Control', 'Command and Control'), 
                 ('Actions on Objectives', 'Actions on Objectives')], 
        default='Installation')

    adversary = TextAreaField('Adversary')
    capability = TextAreaField('Capability (<i>or MITRE ATT&CK&#8482; Matrix Technique with details</i>)')
    infrastructure = TextAreaField('Infrastructure')
    victim = TextAreaField('Victim')
    business_impact = TextAreaField('Business Impact')

    courses_of_action = SelectMultipleField(u'Courses of Action', 
        choices=[('Discover', 'Discover'), 
                 ('Detect', 'Detect'), 
                 ('Deny', 'Deny'), 
                 ('Disrupt', 'Disrupt'), 
                 ('Degrade', 'Degrade'), 
                 ('Deceive', 'Deceive')])
    save = SubmitField('Save Cyber Kill Chain Phase')
    edit = SubmitField('Edit')
    delete = SubmitField('Delete')
from setup_relief import db, ReliefConfig, Campaigns, CyberKillChains

# Test list all current settings
ReliefConfig.query.all()
# Paranoid commit
db.session.commit()
# Insert new setting
s = ReliefConfig('filenamePrefix'='relief')
db.session.add(s)
db.session.commit()
# Validate setting in DB
ReliefConfig.query.all()
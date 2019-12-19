from app import db


class AP(db.Model):
    __tablename__ = 'ACCESS_POINTS'

    idAP = db.Column('ID', db.Integer, primary_key=True)
    address = db.Column('ADDRESS', db.String(16))
    ip = db.Column('IP', db.String, nullable=True)
    in_place = db.Column('IN_PLACE', db.Boolean)
    stas = db.relationship('STA', lazy='select', backref=db.backref('aps', lazy='joined'))

    def __repr__(self):
        return "<AP(id='%d', address='%s', ip='%s', in_place='%s')>" % (self.idAP, self.address, self.ip, self.in_place)


class STA(db.Model):
    __tablename__ = 'STA'

    spa = db.Column('SPA', db.String(16), primary_key=True)
    pmkid = db.Column('PMKID', db.String(32))
    pmk = db.Column('PMK', db.String(64))
    expiration = db.Column('EXPIRATION', db.Integer)
    ap_id = db.Column('AP_ID', db.Integer, db.ForeignKey('ACCESS_POINTS.ID'), nullable=False)

    def __repr__(self):
        return "<STA(spa='%s', pmkid='%s', pmk='%s')>" % (self.spa, self.pmkid, self.pmk)

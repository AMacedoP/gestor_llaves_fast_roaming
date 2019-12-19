from app import app, db
from flask import request
from app.models import AP, STA


@app.route('/sta/register', methods=['GET', 'POST'])
def register_sta():
    spa = request.form['staAddressName']
    pmkid = request.form['pmkid']
    pmk = request.form['pmk']
    expiration = request.form['expiration']
    ap_ip_address = request.remote_addr
    ap = db.session.query(AP).filter(AP.ip == ap_ip_address).first()

    sta = db.session.query(STA).filter(STA.spa == spa).first()
    if sta is None:
        sta = STA(spa=spa, pmkid=pmkid, pmk=pmk, expiration=expiration, ap_id=ap.idAP)
        db.session.add(sta)
    else:
        sta.ap_id = ap.idAP
        db.session.add(sta)

    db.session.commit()
    return 'STA registrado\n'


@app.route('/sta/deregister', methods=['GET', 'POST'])
def deregister_sta():
    spa = request.form['staAddressName']
    sta = db.session.query(STA).filter(STA.spa == spa).first()

    if sta is not None:
        db.session.delete(sta)
        db.session.commit()
    else:
        return 'STA no estaba registrado!\n'

    return 'STA deregistrado\n'


@app.route('/ap/register', methods=['GET', 'POST'])
def register_ap():
    apAddress = request.form['apAddressName']
    ap = db.session.query(AP).filter(AP.address == apAddress).first()
    if ap is None:
        ap = AP(address=apAddress, ip=request.remote_addr, in_place=1)
        db.session.add(ap)
    else:
        ap.ip = request.remote_addr
        db.session.add(ap)

    db.session.commit()
    return 'AP registrado\n'


@app.route('/ap/deregister', methods=['GET', 'POST'])
def deregister_ap():
    apAddress = request.form['apAddressName']
    ap = db.session.query(AP).filter(AP.address == apAddress).first()
    if ap is not None:
        ap.ip = None
        ap.in_place = False
        db.session.add(ap)
        db.session.commit()
    else:
        return 'AP no se encontraba registrado!\n'

    return 'AP deregistrado!\n'

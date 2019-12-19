from app import app, db
from app.models import AP, STA


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'AP': AP, 'STA': STA}

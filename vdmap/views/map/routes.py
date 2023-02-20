from flask_login import current_user, login_required

from . import map_bp


@map_bp.route("/")
@login_required
def m():
    print(current_user)
    return "map"

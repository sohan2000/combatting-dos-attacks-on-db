def requires_roles(*roles):
    def wrapper(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            if current_user.role not in roles:
                abort(403)  # Forbidden
            return f(*args, **kwargs)
        return wrapped
    return wrapper

@app.route('/admin')
@login_required
@requires_roles('admin')
def admin_panel():
    return 'Admin Panel'

@app.route('/reset-password', methods=['POST'])
def reset_password():
    email = request.form['email']
    new_password = request.form['new_password']
    user = User.query.filter_by(email=email).first()
    user.password = new_password
    db.session.commit()
    return 'Password reset'
    
#fix
@app.route('/reset-password', methods=['POST'])
def reset_password():
    email = request.form['email']
    token = request.form['token']
    new_password = request.form['new_password']

    if verify_reset_token(email, token):
        user = User.query.filter_by(email=email).first()
        user.password = hash_password(new_password)
        db.session.commit()
        return 'Password reset successful'

    return 'Unauthorized', 403
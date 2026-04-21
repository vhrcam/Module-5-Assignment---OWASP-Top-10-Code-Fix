@app.route('/account/<user_id>')
def get_account(user_id):
    user = db.query(User).filter_by(id=user_id).first()
    return jsonify(user.to_dict())
    

#fix
@app.route('/account')
def get_account():
    user = get_current_user()
    return jsonify(user.to_dict())
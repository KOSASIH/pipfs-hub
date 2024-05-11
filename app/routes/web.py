# Web routes
from flask import Blueprint, render_template, request, redirect, url_for
from app.models import User, File

web = Blueprint('web', __name__)

@web.route('/')
def index():
    return render_template('index.html')

@web.route('/upload', methods=['POST'])
def upload_file_web():
    file = request.files['file']
    user = User.query.filter_by(username=request.form['username']).first()
    if user:
        encrypted_file = encrypt_file(file)
        ipfs_hash = IPFS.add(encrypted_file)
        file = File(name=file.filename, content=ipfs_hash, user=user)
        db.session.add(file)
        db.session.commit()
        return redirect(url_for('web.file_list'))
    return redirect(url_for('web.index'))

@web.route('/files')
def file_list():
    files = File.query.all()
    return render_template('file_list.html', files=files)

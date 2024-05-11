# API routes
from flask import Blueprint, jsonify, request

from app.models import File, User
from app.services.encryption import encrypt_file
from app.services.ipfs import IPFS

api = Blueprint("api", __name__)


@api.route("/files", methods=["POST"])
def upload_file():
    file = request.files["file"]
    user = User.query.filter_by(username=request.form["username"]).first()
    if user:
        encrypted_file = encrypt_file(file)
        ipfs_hash = IPFS.add(encrypted_file)
        file = File(name=file.filename, content=ipfs_hash, user=user)
        db.session.add(file)
        db.session.commit()
        return jsonify({"message": "File uploaded successfully"})
    return jsonify({"message": "User not found"}), 404


@api.route("/files/<string:ipfs_hash>", methods=["GET"])
def download_file(ipfs_hash):
    file = File.query.filter_by(ipfs_hash=ipfs_hash).first()
    if file:
        encrypted_file = IPFS.get(ipfs_hash)
        decrypted_file = decrypt_file(encrypted_file)
        return send_file(decrypted_file, as_attachment=True)
    return jsonify({"message": "File not found"}), 404

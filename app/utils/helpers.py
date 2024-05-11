# Helper utilities
import os

def send_file(file, as_attachment=True):
    if as_attachment:
        return send_file_from_directory(file, as_attachment=True)
    return send_file_from_memory(file)

def send_file_from_directory(file, as_attachment=True):
    file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], file)
    return send_from_directory(current_app.config['UPLOAD_FOLDER'], file, as_attachment=as_attachment)

def send_file_from_memory(file):
    return send_file(file, mimetype='application/octet-stream', as_attachment=True)

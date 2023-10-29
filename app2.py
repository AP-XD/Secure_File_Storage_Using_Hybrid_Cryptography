# import os
# from flask import Flask, request, redirect, url_for, render_template, send_from_directory, flash
# from werkzeug.utils import secure_filename
# from dataProcessing import *
# from Threads import *
# from flask import send_file
# import time
# import os
# script = ''

# UPLOAD_FOLDER = '.'
# ALLOWED_EXTENSIONS = set(['txt'])

# # api = API(app)
# app = Flask(_name_)
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# app.config["CACHE_TYPE"] = "null"


# def resultE():
#     path = "./Segments"
#     dir_list = os.listdir(path)
#     print(dir_list)
#     return render_template('Result.html', dir_list=dir_list)


# def resultD():
#     return render_template('resultD.html')


# @app.route('/encrypt/')
# def EncryptInput():
#     Segment()
#     gatherInfo()
#     HybridCrypt()
#     return resultE()


# @app.route('/decrypt/')
# def DecryptMessage():
#     st = time.time()
#     HybridDeCrypt()
#     et = time.time()
#     print(et-st)
#     trim()
#     st = time.time()
#     Merge()
#     et = time.time()
#     print(et-st)
#     return resultD()


# def start():
#     content = open('./Original.txt', 'r')
#     content.seek(0)
#     first_char = content.read(1)
#     if not first_char:
#         return render_template('Empty.html')
#     else:
#         return render_template('Option.html')


# @app.route('/')
# def index():
#     return render_template('index.html')


# def allowed_file(filename):
#     return '.' in filename and \
#         filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# # @app.route('/return-files-key/')
# # def return_files_key():
# #   try:
# #     return send_file('./Original.txt',attachment_filename='hybridkey.txt',as_attachment=True)
# #   except Exception as e:
# #     return str(e)

# # @app.route('/return-files-data/')
# # def return_files_data():
# #   try:
# #     return send_file('./Output.txt',attachment_filename='Output.txt',as_attachment=True)
# #   except Exception as e:
# #     return str(e)


# @app.route('/return-files-key/')
# def return_files_key():
#     try:
#         # Use 'as_attachment' instead of 'attachment_filename'
#         return send_file('./Original.txt', as_attachment=True)
#     except Exception as e:
#         return str(e)


# @app.route('/return-files-data/')
# def return_files_data():
#     try:
#         # Use 'as_attachment' instead of 'attachment_filename'
#         return send_file('./Output.txt', as_attachment=True)
#     except Exception as e:
#         return str(e)


# @app.route('/data/', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         if 'file' not in request.files:
#             return render_template('Nofile.html')
#         file = request.files['file']
#         if file.filename == '':
#             return render_template('Nofile.html')
#         if file and allowed_file(file.filename):
#             filename = secure_filename(file.filename)
#             file.save(os.path.join(
#                 app.config['UPLOAD_FOLDER'], 'Original.txt'))
#             return start()

#         return render_template('Invalid.html')


# if _name_ == '_main_':
#     app.run(debug=True)
import os
from flask import Flask, request, render_template, send_file, redirect, url_for
from werkzeug.utils import secure_filename
from dataProcessing import Segment, gatherInfo, trim, Merge

UPLOAD_FOLDER = '.'
ALLOWED_EXTENSIONS = set(
    ['txt', 'pdf', 'jpg', 'png', 'doc', 'docx', 'jpeg', 'gif', 'zip', 'rar'])

app = Flask(_name_)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config["CACHE_TYPE"] = "null"


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/data/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('Nofile.html')
        file = request.files['file']
        if file.filename == '':
            return render_template('Nofile.html')
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            return redirect(url_for('EncryptInput', file_path=file_path))
        return render_template('Invalid.html')


@app.route('/return-files-key/')
def return_files_key():
    try:
        return send_file(
            './Original.txt',
            as_attachment=True,
            download_name='original.txt'
        )
    except Exception as e:
        return str(e)


@app.route('/return-files-data/')
def return_files_data():
    try:
        return send_file(
            './Output.txt',
            as_attachment=True,
            download_name='output.txt'
        )
    except Exception as e:
        return str(e)


@app.route('/encrypt/')
def EncryptInput():
    file_path = request.args.get('file_path')
    Segment(file_path)
    gatherInfo()
    return render_template('Result.html')


@app.route('/decrypt/')
def DecryptMessage():
    trim()
    Merge()
    return render_template('resultD.html')


if _name_ == '_main_':
    app.run(debug=True)
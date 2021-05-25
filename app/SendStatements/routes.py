import os
from datetime import datetime

from werkzeug.utils import secure_filename

import app
from app.base.models import FileInputStorage
from app.SendStatements import blueprint
from flask import render_template, request, redirect, flash
from flask_login import login_required
from config import *


@blueprint.route('/<template>')
@login_required
def route_template(template):
    return render_template(template + '.html')


ALLOWED_EXTENSIONS = {'xml'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@blueprint.route('/save_demand_file', methods=["GET", "POST"])
@login_required
def save():
    if request.method == "POST":
        if 'file' not in request.files:
            flash('No file part', "warning")
            return render_template("demand.html")
        file = request.files['file']
        if file.filename == '':
            flash('No file selected for uploading')
            return render_template("demand.html")
        if file and allowed_file(file.filename):
            filename = secure_filename(datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p") + "_" + file.filename)
            file.save(os.path.join('app/base/static/files/Demand', filename))
            file_Path = os.path.join('app/base/static/files/Demand', filename);
            if os.path.exists('app/base/static/files/Demand/' + filename):
                save_file = FileInputStorage(fileName=filename,
                                             filePath=file_Path, fileType="DemandFile", save_at=datetime.now(),
                                             status="Pending")
                app.db.session.add(save_file)
                app.db.session.commit()
                flash('File successfully uploaded', 'success')
            else:
                flash("File was not found check this folder to confirm :" + file_Path, "warning")

            return render_template("demand.html")
        else:
            flash('Not saved Allowed file types are xml', 'danger')
            return render_template("demand.html")
    return render_template("demand.html")


@blueprint.route('/Dormancy_Notification', methods=["GET", "POST"])
@login_required
def Dormancy_Notification():
    if request.method == "POST":
        if 'file' not in request.files:
            flash('No file part', "warning")
            return render_template("Dormancy_Notification.html")
        file = request.files['file']
        if file.filename == '':
            flash('No file selected for uploading')
            return render_template("Dormancy_Notification.html")
        if file and allowed_file(file.filename):
            filename = secure_filename(datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p") + "_" + file.filename)
            file.save(os.path.join('app/base/static/files/dormancyNotification', filename))
            file_Path = os.path.join('app/base/static/files/dormancyNotification', filename);
            if os.path.exists('app/base/static/files/dormancyNotification/' + filename):
                save_file = FileInputStorage(fileName=filename,
                                             filePath=file_Path, fileType="dormancyNotification", save_at=datetime.now(),
                                             status="Pending")
                app.db.session.add(save_file)
                app.db.session.commit()
                flash('File successfully uploaded', 'success')
            else:
                flash("File was not found check this folder to confirm :" + file_Path, "warning")
            return render_template("Dormancy_Notification.html")
        else:
            flash('Not saved Allowed file types are xml', 'danger')
            return render_template("Dormancy_Notification.html")
    return render_template("Dormancy_Notification.html")


@blueprint.route('/ufaclaimletter', methods=["GET", "POST"])
@login_required
def ufaclaimletter():
    if request.method == "POST":
        if 'file' not in request.files:
            flash('No file part', "warning")
            return render_template("ufaclaimletter.html")
        file = request.files['file']
        if file.filename == '':
            flash('No file selected for uploading')
            return render_template("ufaclaimletter.html")
        if file and allowed_file(file.filename):
            filename = secure_filename(datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p") + "_" + file.filename)
            file.save(os.path.join('app/base/static/files/Ufaa', filename))
            file_Path = os.path.join('app/base/static/files/Ufaa', filename);
            if os.path.exists('app/base/static/files/Ufaa/' + filename):
                save_file = FileInputStorage(fileName=filename,
                                             filePath=file_Path, fileType="Ufaa", save_at=datetime.now(),
                                             status="Pending")
                app.db.session.add(save_file)
                app.db.session.commit()
                flash('File successfully uploaded', 'success')
            else:
                flash("File was not found check this folder to confirm :" + file_Path, "warning")
            return render_template("ufaclaimletter.html")
        else:
            flash('Not saved Allowed file types are xml', 'danger')
            return render_template("ufaclaimletter.html")
    return render_template("ufaclaimletter.html")


@blueprint.route('/bankStatement', methods=["GET", "POST"])
@login_required
def bankStatement():
    if request.method == "POST":
        if 'file' not in request.files:
            flash('No file part', "warning")
            return render_template("bankstatement.html")
        file = request.files['file']
        if file.filename == '':
            flash('No file selected for uploading')
            return render_template("bankstatement.html")
        if file and allowed_file(file.filename):
            filename = secure_filename(datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p") + "_" + file.filename)
            file.save(os.path.join('app/base/static/files/bankStatements', filename))
            file_Path = os.path.join('app/base/static/files/bankStatements', filename);
            if os.path.exists('app/base/static/files/bankStatements/' + filename):
                save_file = FileInputStorage(fileName=filename,
                                             filePath=file_Path, fileType="bank_statement", save_at=datetime.now(),
                                             status="Pending")
                app.db.session.add(save_file)
                app.db.session.commit()
                flash('File successfully uploaded', 'success')
            else:
                flash("File was not found check this folder to confirm :" + file_Path, "warning")
            return render_template("bankstatement.html")
        else:
            flash('Not saved Allowed file types are xml', 'danger')
            return render_template("bankstatement.html")
    return render_template("bankstatement.html")

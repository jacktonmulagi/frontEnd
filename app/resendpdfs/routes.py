import json

from app.base.models import FileInputStorage
from app.resendpdfs import blueprint
from flask import render_template, flash
from flask_login import login_required

from app.resendpdfs.AlchemyEncoder import AlchemyEncoder


@blueprint.route('/<template>')
@login_required
def route_template(template):
    return render_template(template + '.html')


@blueprint.route('/failed_pdfs', methods=["GET", "POST"])
@login_required
def estate_list():
    pdfs = FileInputStorage.query.filter(FileInputStorage.status == "Pending").with_entities(FileInputStorage.fileType,
                                                                                             )

    data = {"data": list(pdfs)}
    user_data = json.dumps(data, cls=AlchemyEncoder, default=str)

    return user_data


@blueprint.route('/failed_pdfs_list', methods=["GET", "POST"])
@login_required
def failed_pdfs_list():
    count = FileInputStorage.query.filter(FileInputStorage.status == "Failed").count()
    bankstatement = FileInputStorage.query.filter(FileInputStorage.status == "Failed",
                                                  FileInputStorage.fileType == "bank_statement").count()
    dormancy = FileInputStorage.query.filter(FileInputStorage.status == "Failed",
                                             FileInputStorage.fileType == "dormancyNotification").count()
    uffa = FileInputStorage.query.filter(FileInputStorage.status == "Failed",
                                         FileInputStorage.fileType == "Ufaa").count()
    demand = FileInputStorage.query.filter(FileInputStorage.status == "Failed",
                                           FileInputStorage.fileType == "DemandFile").count()
    return render_template('failedPdfs.html', failed_pdfs=count, bankstatement=bankstatement, demand=demand,
                           dormancy=dormancy, uffa=uffa)


@blueprint.route('/resend', methods=["GET", "POST"])
@login_required
def resend():
    count = FileInputStorage.query.filter(FileInputStorage.status == "Failed").count()
    bankstatement = FileInputStorage.query.filter(FileInputStorage.status == "Failed",
                                                  FileInputStorage.fileType == "bank_statement").count()
    dormancy = FileInputStorage.query.filter(FileInputStorage.status == "Failed",
                                             FileInputStorage.fileType == "dormancyNotification").count()
    uffa = FileInputStorage.query.filter(FileInputStorage.status == "Failed",
                                         FileInputStorage.fileType == "Ufaa").count()
    demand = FileInputStorage.query.filter(FileInputStorage.status == "Failed",
                                           FileInputStorage.fileType == "DemandFile").count()
    update = FileInputStorage.query.filter(FileInputStorage.status == "Failed").first()
    if update:
        update.status = "Pending"
        flash("Resend was success", "success")

    return render_template('failedPdfs.html', failed_pdfs=count, bankstatement=bankstatement, demand=demand,
                           dormancy=dormancy, uffa=uffa)

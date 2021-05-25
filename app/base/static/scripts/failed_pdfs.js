//function setupData() {
$(document).ready(function () {
    $.noConflict();
    $('#edit-estate').hide();
    $('#delete-estate').hide();
    let table = $('#failed_pdfs').DataTable({
        //'serverSide': true,
        //'processing': true,
        "ajax": {
            "url": "/resendpdfs/failed_pdfs",
            type: 'POST',
        },
        "fnRowCallback": function (nRow, aData, iDisplayIndex, iDisplayIndexFull) {
            if (aData[5] == false) {
                $('td', nRow).css('background-color', '#CACACA');
            }
        }

    });

    $('#failed_pdfs tbody').on('click', 'tr', function () {
    if ($(this).hasClass('selected')) {
        $(this).removeClass('selected');
        $('#edit-estate').hide();
        $('#delete-estate').hide();
    } else {
        table.$('tr.selected').removeClass('selected');
        $(this).addClass('selected');
        $('#edit-estate').show();
        $('#delete-estate').show();

    }
});

$('#edit-estate').click(function () {
    $.map(table.rows('.selected').data(), function (item) {
        let id = item[0];
        $(location).attr('href', '/survey/update_estate/' + id);
    });
});


$('#delete-estate').click(function () {
    $.map(table.rows('.selected').data(), function (item) {
        let id = item[0];
        $(location).attr('href', '/survey/delete_estate/' + id);
    });
});
});
//}







// $(window).on("load", setupData);
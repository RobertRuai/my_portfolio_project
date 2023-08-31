$(document).ready(function () {
    loadCrimeList();

    $('#submit-button').click(function (event) {
        event.preventDefault();
        submitCrimeReport();
    });

    function loadCrimeList() {
        $.get('/crimes', function (data) {
            $('#crime-list').empty();
            data.reports.forEach(function (report) {
                $('#crime-list').append('<li>' + report.title + ' - ' + report.description + '</li>');
            });
        });
    }

    function submitCrimeReport() {
        var title = $('#title').val();
        var description = $('#description').val();

        $.post('/report', { 'title': title, 'description': description }, function (data) {
            loadCrimeList();
            $('#title').val('');
            $('#description').val('');
        });
    }
});

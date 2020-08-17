$.get('{% url "line_chart_json" %}', function (data) {
    var ctx = $("#perBarangay").get(0).getContext("2d");
    new Chart(ctx, {
        type: 'bar', data: data
    });
});
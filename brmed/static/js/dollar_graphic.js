$(function () {
    var url = "/highcharts/api/" + location.search;
    $.getJSON(url, function(response){
        console.log(typeof response["start_date"]);
        $('#container').highcharts({
          title: {
              text: 'USD x BRL, EUR and JPY',
              align: 'left'
          },

          yAxis: {
              title: {
                  text: 'Value'
              }
          },

          xAxis: {
            type: 'datetime',
            dateTimeLabelFormats: {
              day: '%d %b %Y' //ex- 01 Jan 2016
            },
            max: Date.UTC(response["end_date"]["year"], response["end_date"]["month"], response["end_date"]["day"]),
            showLastLabel: true,
            labels: {
              rotation: -45
            }
          },

          legend: {
              layout: 'vertical',
              align: 'right',
              verticalAlign: 'middle'
          },

          plotOptions: {
            series: {
                label: {
                    connectorAllowed: false
                },
                pointStart: Date.UTC(response["start_date"]["year"], response["start_date"]["month"], response["start_date"]["day"]),
                pointInterval: 24 * 3600 * 1000 // one hour
            }
          },

          series: [{
              name: 'BRL',
              data: response['BRL']
          }, {
              name: 'EUR',
              data: response['EUR']
          }, {
              name: 'JPY',
              data: response['JPY']
          }],

          responsive: {
              rules: [{
                  condition: {
                      maxWidth: 500
                  },
                  chartOptions: {
                      legend: {
                          layout: 'horizontal',
                          align: 'center',
                          verticalAlign: 'bottom'
                      }
                  }
              }]
          }
        });
    });
});

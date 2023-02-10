$(function () {
    var url = "/highcharts/api/";
    $.getJSON(url, function(response){
        $('#container').highcharts({
          title: {
              text: 'USR x BRL, EUR and JPY',
              align: 'left'
          },

          subtitle: {
              text: 'Source: <a href="https://irecusa.org/programs/solar-jobs-census/" target="_blank">IREC</a>',
              align: 'left'
          },

          yAxis: {
              title: {
                  text: 'Variacao do Dolar em relacao ao Euro'
              }
          },

          xAxis: {
            type: 'datetime',
            dateTimeLabelFormats: {
              day: '%d %b %Y' //ex- 01 Jan 2016
            },
            max: Date.UTC(2023, 2, 9),
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
                pointStart: Date.UTC(2023, 2, 5),
                pointInterval: 24 * 3600 * 1000 // one hour
            }
          },

          series: [{
              name: 'BRL',
              data: response['BRL']
          }, {
              name: 'EUR',
              data: [5.24, 5.00, 5.67, 5.24, 5.00]
          }, {
              name: 'JPY',
              data: [5.24, 5.00, 5.67, 5.24, 5.00]
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

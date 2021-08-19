$(document).ready(function(){
  var ctx = document.querySelector('#myChart').getContext('2d');
  var chart = new Chart(ctx, {
      type: 'bar',
      data: {
          labels: ['2019.07', '2019.08', '2019.09', '2019.10'],
          datasets: [
              {
                  label: 'My First dataset',
                  backgroundColor: '#0000FF',
                  borderColor: 'none',
                  data: [30, 10, 22, 21]
              },
              {
                  label: 'My Second dataset',
                  backgroundColor: '#FF0000',
                  borderColor: 'none',
                  data: [20, 20, 18, 25]
              },
              {
                  label: 'My Third dataset',
                  backgroundColor: '#F3BA18',
                  borderColor: 'none',
                  data: [10, 15, 4, 12]
              }
          ]
      },

      // Configuration options go here
      options: {
          legend: {
              display: false
          },
          tooltips: {
              enabled: false
          },
          scales: {
              xAxes: [{
                  stacked: true,
                  barPercentage: 0.1,
                  gridLines: {
                      color: "rgba(0, 0, 0, 0)",
                  }
              }],
              yAxes: [{
                  stacked: true,
                  gridLines: {
                      color: "rgba(0, 0, 0, 0)",
                  },
                  ticks: {
                      display: false
                  }
              }]
          }
      }
  });
})

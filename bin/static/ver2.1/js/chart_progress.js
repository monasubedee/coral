
$(document).ready(function () {
    $.ajax({
        type: "GET",
        //url: "https://jsondata.okiba.me/v1/json/sZUfs200811080107",
         url: '/manabu/getChallenge',
        success: function (data) {
            let result = JSON.parse(data);
            if (result.data == null) {
                $(".manabu-tameru-progress").append(`
                    <div class='my-3 text-center'><p class='text-muted'>No data to show!</div>
                `);
            } else {
                var manabu = result.data.manabu[0];
                var tameru = result.data.tameru[0];
                var ary = [manabu, tameru];
                ary.map((data, index) => {
                    if (index == 0) {
                        var goalNum = data.label.replace(/[^0-9]/g, "");
                        var nowPer = data.achieved_rate;
                        var nowNum = goalNum - (goalNum / 100) * nowPer;
                        $(".manabu-remnant").append(
                            `<small class="text-muted">残り${Math.round(
                                nowNum
                            )}門！</small>`
                        );
                    }
                    $(".manabu-tameru-progress").append(
                        `<div class='py-3'>
                        <div class='pl-3'>
                        <p class='manabu-tameru-title mt-0 mb-2'>ハラスメント研修</p>

                      <div class='flex flex-sb'>
                          <span class='text-muted'>
                              <small class='${
                        index == 0 ? "dot dot-blue" : "dot dot-red"
                        }'>${data.label}</small>
                          </span>
                          <span class='text-muted'>
                              <small>期限：${data.deadline}まで</small>
                          </span>
                      </div>
                      <div class='py-3'>
                          <div class='progress-bar'>
                              <div class='${
                        index === 0
                            ? "progress-bar-status bg-blue"
                            : "progress-bar-status bg-red"
                        }' data-value='${data.achieved_rate}'></div>
                          </div>
                      </div>
                      <div class='flex flex-sb'>
                          <span class='text-muted'>
                              <small>達成率：${data.achieved_rate}%</small>
                          </span>
                          <span class='text-muted'>
                              <small>${data.total_users}人中 ${
                        data.total_user_complete
                        }人がクリア</small>
                          </span>
                      </div>
                      </div>
                  </div>`
                    );

                    var status_w = parseInt(
                        $(".progress-bar-status")
                            .eq(index)
                            .attr("data-value")
                    );
                    if (data.rate != undefined) {
                        $(".progress-bar-status")
                            .eq(index)
                            .css({
                                background: `${data.rate}`,
                            });
                    }
                    $(".progress-bar-status")
                        .eq(index)
                        .css({
                            width: `${status_w}%`,
                        });
                });
            }
        },
    });
    var graph_data = {
        labels: [],
        datasets: [
            {
                label: "",
                backgroundColor: "#0000FF",
                borderColor: "none",
                data: [],
            },
            {
                label: "",
                backgroundColor: "#FF0000",
                borderColor: "none",
                data: [],
            },
            {
                label: "",
                backgroundColor: "#F3BA18",
                borderColor: "none",
                data: [],
            },
        ],
    };
    $.ajax({
        type: "GET",
        url: "https://jsondata.okiba.me/v1/json/sZUfs200811080107",
        // url: '/manabu/getGraphRecord',
        success: function (data) {
            var itemGraph = false;
            var list = data;
            // var list = JSON.parse();
            // console.log("say hi");
            console.log(list.data);
            for (let i in list.data) {
                if (
                    list.data[i].totalManabu > 0 ||
                    list.data[i].totalTameru > 0 ||
                    list.data[i].totalComment > 0
                ) {
                    itemGraph = true;
                }
            }
            let name = ["まなんだ数", "ためた数", "コメントした数"];
            if (list.result == "ok") {
                list.data.reverse().map((item, index) => {
                    graph_data.labels.push(`${item.FromDate}\n~\n${item.ToDate}`);
                    let ary = [item.totalManabu, item.totalTameru, item.totalComment];
                    for (var i = 0; i < ary.length; i++) {
                        graph_data.datasets[i].data.push(ary[i]);
                    }
                });
                for (var i = 0; i < name.length; i++) {
                    graph_data.datasets[i].label = name[i];
                }
                if (itemGraph == true) {
                    drawchart(graph_data);
                }
            }
        },
    });
    function drawchart(data) {
        $(".chart-info").append(
            '\
            <p><span class="chart-type-bar" style="background:#e67c73"></span>ビジネスマナー</p>\
            <p><span class="chart-type-bar" style="background:#73a4e6"></span>システム開発の基礎</p>\
            <p><span class="chart-type-line" style="background:#e67c73"></span>正答率(ビジネスマナー)</p>\
            <p><span class="chart-type-line" style="background:#73a4e6"></span>正答率(システム開発の基礎)</p>\
      '
        );
        var ctx = document.querySelector("#myChart").getContext("2d");
        ctx.canvas.height = 100;
        var myBarChart = new Chart(ctx, {
            type: "bar",
            data: {
              labels: ["12w", "11w", "10w", "9w", "8w", "7w", "6w", "5w", "4w", "3w", "2w", "1w", "現在"],
              datasets: [
                  {
                      label: "正答率(ビジネスマナー)",
                      data: [40, , , 75, , , 60, , , 15, , ,20],
                      spanGaps: true,
                      type: "line",
                      // this dataset is drawn on top
                      borderColor: "#e67c73",
                      pointBackgroundColor: "#e67c73",
                      pointBorderColor: "#f4f4f7",
                      backgroundColor: "rgba(0,0,0,0)",
                      yAxisID: "line",
                      pointRadius: 4,
                      pointHoverRadius: 4,
                      borderWidth: 4,
                      pointBorderWidth: 1.5,
                  },
                  {
                      label: "正答率(システム開発の基礎)",
                      data: [10, , , 60, , , 40, , , 10, , ,40],
                      spanGaps: true,
                      type: "line",
                      // this dataset is drawn on top
                      borderColor: "#73a4e6",
                      pointBackgroundColor: "#73a4e6",
                      pointBorderColor: "#f4f4f7",
                      backgroundColor: "rgba(0,0,0,0)",
                      yAxisID: "line",
                      pointRadius: 4,
                      pointHoverRadius: 4,
                      borderWidth: 4,
                      pointBorderWidth: 1.5,
                  },
                  {
                      label: "ビジネスマナー",
                      type: "bar",
                      data: [15, 5, 10, 20, 15, 5, 10, 20, 10, 20, 40, 60, 40],
                      backgroundColor: "#e67c73",
                      barPercentage: 0.2,
                      yAxisID: "bar",
                  },
                  {
                      label: "システム開発の基礎",
                      type: "bar",
                      data: [5, 20, 15, 25, 5, 20, 15, 25, 5, 20, 15, 25, 5],
                      backgroundColor: "#73a4e6",
                      barPercentage: 0.2,
                      yAxisID: "bar",
                  },
              ],
            },
            options: {
                // title: {
                //   display: true,
                //   text: '支店別 来客数'
                // },
                scales: {
                    xAxes: [
                        {
                            categoryPercentage: 0.5,
                            barPercentage: 0.6,
                            gridLines: {
                                color: "rgba(0, 0, 0, 0)",
                            },
                            ticks: {
                                maxRotation: 0,
                                sampleSize: 5,
                            },
                        },
                    ],
                    yAxes: [
                        {
                            id: "bar", // Y軸のID
                            type: "linear", // linear固定
                            position: "left", // どちら側に表示される軸か？
                            ticks: {
                                suggestedMin: 0,
                            },
                        },
                        {
                            id: "line",
                            type: "linear",
                            position: "right",
                            gridLines: {
                                color: "rgba(0, 0, 0, 0)",
                            },
                            ticks: {
                                suggestedMax: 100,
                                suggestedMin: 0,
                                stepSize: 25,
                                callback: function (value, index, values) {
                                    return value + "％"; // Y軸の単位
                                },
                            },
                        },
                    ],
                },
                elements: {
                    line: {
                        tension: 0, // ベジェ曲線を無効にする
                    },
                },
                legend: {
                    display: false,
                },
            },
        });
        // var chart = new Chart(ctx, {
        //   type: "bar",
        //   data: data,
        //   // Configuration options go here
        //   options: {
        //     responsive: true,
        //     legend: {
        //       display: false,
        //     },
        //     tooltips: {
        //       mode: "label",
        //       // callbacks: {
        //       //     title: function(tooltipItem, data) {
        //       //         console.log(data)
        //       //       return data['labels'][tooltipItem[0]['index']].join("\n");
        //       //     }
        //       // },
        //       titleAlign: "center",
        //       titleFontColor: "#000",
        //       titleMarginBottom: 10,
        //       backgroundColor: "#fff",
        //       bodyFontColor: "#000",
        //     },
        //     scales: {
        //       xAxes: [
        //         {
        //           stacked: true,
        //           barPercentage: 0.4,
        //           gridLines: {
        //             color: "rgba(0, 0, 0, 0)",
        //           },
        //           ticks: {
        //             maxRotation: 0,
        //             sampleSize: 5,
        //           },
        //         },
        //       ],
        //       yAxes: [
        //         {
        //           stacked: true,
        //           gridLines: {
        //             color: "rgba(0, 0, 0, 0)",
        //           },
        //           ticks: {
        //             display: false,
        //             // min: 0,
        //             // max: 10
        //           },
        //         },
        //       ],
        //     },
        //   },
        //   plugins: [
        //     {
        //       beforeInit: function(chart) {
        //         chart.data.labels.forEach(function(e, i, a) {
        //           // if (/\n/.test(e)) {
        //           //     a[i] = e.split(/\n/)
        //           // }
        //           if (/\n/.test(e)) {
        //             var month = e.split(/\n/);
        //             a[i] = month[0];
        //           }
        //         });
        //       },
        //     },
        //   ],
        // });

        $('.manabu-tameru-progress-wrap').height($('.js-chart').height() - $('.profile-data').height());
    }
});

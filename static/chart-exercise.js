// line chart

c3.generate({
    bindto: '#line-chart-exercise',
    data: {
        columns: [
            ['data1', 30, 200, 100, 400, 150, 250],
            ['data2', 50, 20, 10, 40, 15, 25]
        ],
        types:{
            'data1':'line',
            'data2':'line'
        }
    }
});


// bar chart

c3.generate({
    bindto: '#bar-chart-exercise',
    data: {
      columns: [
        ['data1', 30, 200, 100, 400, 150, 250],
        ['data2', 50, 20, 10, 40, 15, 25]
      ],
      type: 'bar'
    }
});


// time series line chart

c3.generate({
    bindto: '#time-chart-exercise',
    data: {
        x: 'x-axis',
        columns: [
            ['x-axis', '2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04', '2022-01-05', '2022-01-06'],
            ['data1', 30, 200, 100, 400, 150, 250],
            ['data2', 130, 340, 200, 500, 250, 350]
        ]
    },
    axis: {
        x: {
            type: 'timeseries',
            tick: {
                format: '%Y-%m-%d'
            }
        }
    }
});

// pie chart

c3.generate({
    bindto: '#pie-chart-exercise',
    data: {
        columns: [
            ['A', 30],
            ['B', 50],
            ['C', 20],
        ],
        type : 'pie'
    }
});


// donut chart

c3.generate({
    bindto: '#donut-chart-exercise',
    data: {
        columns: [
            ['A', 30],
            ['B', 50],
            ['C', 20],
        ],
        type : 'donut'
    },
    donut: {
        title: "percentage by grade"
    }
});


// gauge chart

c3.generate({
    bindto: '#gauge-chart-exercise',
    data: {
        columns: [
            ['data', 90.16]
        ],
        type: 'gauge',
    },
    color: {
        pattern: ['#FF0000', '#F97600', '#F6C600', '#60B044'],
        threshold: {
            values: [30, 60, 90, 100]
        }
    },
});


// Ajax + clieck event + line chart visualiztion  
$("#line-chart-button").click(function(){
    var chart = c3.generate({
        bindto: '#clicked-line-chart-exercise',
        data: {
            columns: []
        }
    });

    $.ajax({
        method: "GET",
        url: "line/"
    }).done(function(response) {
        chart.load({
          columns: [response],
          type:'line'
        });
    });
});


// Ajax + clieck event + pie chart visualiztion  

$("#pie-chart-button").click(function(){
    var chart = c3.generate({
        bindto: '#clicked-pie-chart-exercise',
        data: {
            columns: []
        }
    });

    $.ajax({
        method: "GET",
        url: "pie/"
    }).done(function(response) {
         console.log("response data : ");
         console.log(response);
        chart.load({
          columns: [response[0],response[1], response[2]],
          type : 'pie'
        });
    });
});

 // 페이지 로드 시 AJAX를 통해 데이터 요청
 // c3.js 차트 생성
// ['data']의 의미 : 그래프에 표시될 첫 번째 데이터의 레이블(즉 값이다.)
// .concat : 두 배열을 합쳐서 하나의 배열로 만들어 줌.
$.ajax({
    method: "GET",
    url: "getChartdata/",
    success: function(response) {
        console.log("response data : ", response);
        
        // 데이터가 올바르게 있는지 확인
        var chartData = {
            data1: response.data1 || [],
            data2: response.data2 || []
        };

        // c3.js 차트 생성
        var chart = c3.generate({
            bindto: '#get_chart_exercise',
            data: {
                columns: [
                    ['data1'].concat(chartData.data1),  // 'data1' 레이블에 값 추가
                    ['data2'].concat(chartData.data2)   // 'data2' 레이블에 값 추가
                ],
                // 각 컬럼에 대해 타입을 설정
                types: {
                    'data1': 'line',  // 'data1'은 line 차트로
                    'data2': 'pie'    // 'data2'는 pie 차트로
                }
            }
        });
    }
});
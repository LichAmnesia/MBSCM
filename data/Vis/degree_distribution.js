option = {
    title: {
        text: 'Degree Distribution for Music/Hillary Reddit Data'
    },
    tooltip: {
        trigger: 'axis'
    },
    legend: {
        data:['Conductances']
    },
    toolbox: {
        show: true,
        feature: {
            dataZoom: {},
            dataView: {readOnly: false},
            magicType: {type: ['line', 'bar']},
            restore: {},
            saveAsImage: {}
        }
    },
    xAxis:  {
        type: 'category',
        boundaryGap: false,
        data: ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23'],
        name: 'Value'
    },
    yAxis: {
        type: 'value',
        axisLabel: {
            formatter: '{value}'
        },
        name: 'Count'
    },
    series: [
        {
            name:'Counts',
            type:'line',
            data: [0, 124, 179, 205, 150, 124, 57, 38, 12, 5, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 1, 0],
            markPoint: {
                data: [
                    {type: 'max', name: 'Max'}
                ]
            },

        }
    ]
};

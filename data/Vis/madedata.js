option = {
    title: {
        text: 'minimial conductances Motifs'
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
        data: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    },
    yAxis: {
        type: 'value',
        axisLabel: {
            formatter: '{value}'
        }
    },
    series: [
        {
            name:'Conductances',
            type:'line',
            data:[1.0, 1.0, 1.34, 1.34, 0.0, -0.34, -0.34, -1.0, -1.0, -1.0, -1.0, 1.0],
            markPoint: {
                data: [
                    {type: 'max', name: 'Max'},
                    {type: 'min', name: 'Min'}
                ]
            },
            markLine: {
                data: [
                    {type: 'average', name: 'Average'}
                ]
            }
        }
    ]
};

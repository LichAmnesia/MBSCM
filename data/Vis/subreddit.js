var dataMap = {};
function dataFormatter(obj) {
    var pList = ['北京','天津','河北','山西','内蒙古','辽宁','吉林','黑龙江','上海','江苏','浙江','安徽','福建','江西','山东','河南','湖北','湖南','广东','广西','海南','重庆','四川','贵州','云南','西藏','陕西','甘肃','青海','宁夏','新疆'];
    var pList = ['AskReddit', 'politics', 'GOT', 'nfl', 'counting', 'videos', 'CFB', 'worldnews', 'RLE', 'The_Donald', 'fantasyfootball', 'WritingPrompts', 'soccer', 'pics', 'todayilearned', 'NoSillySuffix', 'apple', 'funny', 'SquaredCircle', 'news', 'leagueoflegends', 'Overwatch', 'GlobalOffensive', 'wow', 'pokemontrades', 'Android', 'pcmasterrace', 'Music', 'relationships', 'technology', 'hillaryclinton', 'movies'];
    var temp;
    var year = 2016;
    var max = 0;
    var sum = 0;
    temp = obj[year];
    for (var i = 0, l = temp.length; i < l; i++) {
        max = Math.max(max, temp[i]);
        sum += temp[i];
        obj[year][i] = {
            name : pList[i],
            value : temp[i]
        }
    }
    obj[year + 'max'] = Math.floor(max / 100) * 100;
    obj[year + 'sum'] = sum;
    // for (var year = 2002; year <= 2011; year++) {
    //     var max = 0;
    //     var sum = 0;
    //     temp = obj[year];
    //     for (var i = 0, l = temp.length; i < l; i++) {
    //         max = Math.max(max, temp[i]);
    //         sum += temp[i];
    //         obj[year][i] = {
    //             name : pList[i],
    //             value : temp[i]
    //         }
    //     }
    //     obj[year + 'max'] = Math.floor(max / 100) * 100;
    //     obj[year + 'sum'] = sum;
    // }
    return obj;
}

dataMap.dataNum = dataFormatter({
    //max : 60000,
    2016:[143081, 90292, 43762, 40624, 38296, 35560, 33357, 22582, 19890, 19687, 17958, 14449, 13374, 12884, 12878, 12611, 12592, 12416, 12357, 12270, 11933, 11713, 11263, 10932, 10904, 10902, 10897, 10846, 10728, 10301, 10128, 10121]
});


option = {
    baseOption: {
        timeline: {
            // y: 0,
            axisType: 'category',
            // realtime: false,
            // loop: false,
            autoPlay: true,
            // currentIndex: 2,
            playInterval: 10000,
            // controlStyle: {
            //     position: 'left'
            // },
            data: [
                '2016-01-01'
            ],
            label: {
                formatter : function(s) {
                    return (new Date(s)).getFullYear();
                }
            }
        },
        title: {
            subtext: 'Data From Reddit'
        },
        tooltip: {},
        legend: {
            x: 'right',
            data: ['Number of comments'],
        },
        calculable : true,
        grid: {
            top: 80,
            bottom: 100
        },
        xAxis: [
            {
                'type':'category',
                'axisLabel':{'interval':0},
                'data':[
                    'AskReddit', '\npolitics', 'GOT', '\nnfl', 'counting', '\nvideos', 'CFB', '\nworldnews', 'RLE', '\nThe_Donald', 'fantasyfootball', '\nWritingPrompts', 'soccer', '\npics', 'todayilearned', '\nNoSillySuffix', 'apple', '\nfunny', 'SquaredCircle', '\nnews', 'leagueoflegends', '\nOverwatch', 'GlobalOffensive', '\nwow', 'pokemontrades', '\nAndroid', 'pcmasterrace', '\nMusic', 'relationships', '\ntechnology', 'hillaryclinton', '\nmovies'
                ],
                splitLine: {show: false}
            }
        ],
        yAxis: [
            {
                type: 'value',
                name: 'Number of Comments in Subreddit',
                // max: 53500
                max: 150000
            }
        ],
        series: [
            {name: 'Num', type: 'bar'}
        ]
    },
    options: [
        {
            title: {text: '2016-09 Reddit Most Famous Subreddit'},
            series: [
                {data: dataMap.dataNum['2016']}
            ]
        }

        // {
        //     title : {text: '2011全国宏观经济指标'},
        //     series : [
        //         {data: dataMap.dataGDP['2011']},
        //         {data: dataMap.dataFinancial['2011']},
        //         {data: dataMap.dataEstate['2011']},
        //         {data: dataMap.dataPI['2011']},
        //         {data: dataMap.dataSI['2011']},
        //         {data: dataMap.dataTI['2011']},
        //         {data: [
        //             {name: '第一产业', value: dataMap.dataPI['2011sum']},
        //             {name: '第二产业', value: dataMap.dataSI['2011sum']},
        //             {name: '第三产业', value: dataMap.dataTI['2011sum']}
        //         ]}
        //     ]
        // }
    ]
};

$(function() {


    Morris.Area({
        element: 'morris-area-chart',
        data: [{
            period: '1',
            iphone: 2666,
            ipad: null,
            itouch: 2647
        }, {
            period: '2',
            iphone: 2778,
            ipad: 2294,
            itouch: 2441
        }, {
            period: '3',
            iphone: 4912,
            ipad: 1969,
            itouch: 2501
        }, {
            period: '4',
            iphone: 3767,
            ipad: 3597,
            itouch: 5689
        }, {
            period: '5',
            iphone: 6810,
            ipad: 1914,
            itouch: 2293
        }, {
            period: '6',
            iphone: 5670,
            ipad: 4293,
            itouch: 1881
        }, {
            period: '7',
            iphone: 4820,
            ipad: 3795,
            itouch: 1588
        }, {
            period: '8',
            iphone: 15073,
            ipad: 5967,
            itouch: 5175
        }, {
            period: '9',
            iphone: 10687,
            ipad: 4460,
            itouch: 2028
        }, {
            period: '10',
            iphone: 8432,
            ipad: 5713,
            itouch: 1791
        }],
        xkey: 'period',
        ykeys: ['iphone', 'ipad', 'itouch'],
        labels: ['iPhone', 'iPad', 'iPod Touch'],
        pointSize: 2,
        hideHover: 'auto',
        resize: true
    });
    Morris.Donut({
        element: 'morris-donut-chart',
        data: [{
            label: "Download Sales",
            value: 12
        }, {
            label: "In-Store Sales",
            value: 30
        }, {
            label: "Mail-Order Sales",
            value: 20
        }],
        resize: true
    });

    Morris.Bar({
        element: 'morris-bar-chart',
        data: [{
            y: 'Cluster 1',
            a: 5,
            b: 3
        }, {
            y: 'Cluster 2',
            a: 8,
            b: 8
        }, {
            y: 'Cluster 3',
            a: 3,
            b: 2
        }, {
            y: 'Cluster 4',
            a: 5,
            b: 5
        }, {
            y: 'Cluster 5',
            a: 6,
            b: 3
        }],
        xkey: 'y',
        ykeys: ['a', 'b'],
        labels: ['All', 'Active'],
        hideHover: 'auto',
        resize: true
    });
    
});

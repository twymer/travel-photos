window.customMap = function (map) {
  gpsList = $.map($('.gps'),
                  function (gpsString) {
                    return [[parseFloat($(gpsString).text().split(',')[0]),
                             parseFloat($(gpsString).text().split(',')[1])]]
                  });

  map.setView(gpsList[0], 4);

  for (var i = 0; i < gpsList.length; i++) {
    console.log(gpsList[i]);
    L.marker(gpsList[i]).addTo(map);
  }
}

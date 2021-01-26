const automapsArroyoNavi = '<ul class="status">\
  <li class="c" onclick="page(\'automaps-arroyo-temple\')">Temple: Inner Sanctum</li>\
  <li class="c" onclick="page(\'automaps-arroyo-village\')">Village</li>\
  <li class="c" onclick="page(\'automaps-arroyo-bridge\')">Bridge</li>\
  <li class="c" onclick="page(\'automaps-arroyo-wilderness\')">Wilderness</li>\
  <li class="c" onclick="page(\'automaps-arroyo-temple-entrance\')">Temple Entrance</li>\
</ul>\
';

screens['automaps-arroyo-temple'] =
  '<h2 class="title">AUTOMAPS</h2>'
  + '<h3>Arroyo</h3>'
  + automapsArroyoNavi
  + '<img class="map" src="img/automaps-arroyo-temple.png"/>'
  + automapsBack;

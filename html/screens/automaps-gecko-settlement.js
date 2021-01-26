const automapsGeckoNavi = '<ul class="status">\
  <li class="c" onclick="page(\'automaps-gecko-settlement\')">Settlement</li>\
  <li class="c" onclick="page(\'automaps-gecko-power-plant\')">Power Plant</li>\
</ul>\
';

screens['automaps-gecko-settlement'] =
  '<h2 class="title">AUTOMAPS</h2>'
  + '<h3>Gecko</h3>'
  + automapsGeckoNavi
  + '<img class="map" src="img/automaps-gecko-settlement.png"/>'
  + automapsBack;

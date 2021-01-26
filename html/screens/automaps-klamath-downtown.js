const automapsKlamathNavi = '<ul class="status">\
  <li class="c" onclick="page(\'automaps-klamath-downtown\')">Downtown</li>\
  <li class="c" onclick="page(\'automaps-klamath-mall\')">Mall</li>\
  <li class="c" onclick="page(\'automaps-klamath-rat-caves-1\')">Rat Caves</li>\
  <li class="c" onclick="page(\'automaps-klamath-rat-caves-2\')">Rat Caves</li>\
  <li class="c" onclick="page(\'automaps-klamath-grazing-area\')">Grazing area</li>\
  <li class="c" onclick="page(\'automaps-klamath-canyon\')">Canyon</li>\
</ul>\
';

const automapsBack = '<ul class="back"><li class="c" onclick="page(\'automaps\', true)">BACK</li></ul>';

screens['automaps-klamath-downtown'] =
  '<h2 class="title">AUTOMAPS</h2>'
  + '<h3>Klamath</h3>'
  + automapsKlamathNavi
  + '<img class="map" src="img/automaps-klamath-downtown.png"/>'
  + automapsBack;

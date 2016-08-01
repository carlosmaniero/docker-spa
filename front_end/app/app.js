require('angular');
require('angular-route');
require('angular-resource');

// Configurações da APP
require('./app.module');
require('./app.config');

// Carrega services
require('./app.search.service');
require('./app.manufacturer.service');
require('./app.vehicle.service');

// Carrega controllers
require('./app.search.controller')
require('./app.manufacturer.controller')
require('./app.vehicle.controller')

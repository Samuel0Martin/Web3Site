var express = require('express');
var router = express.Router();

/* GET users listing. */
router.get('/', function(req, res, next) {
  res.render('countrylist', { title: 'Country List' });
});

module.exports = router;
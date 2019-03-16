const path = require('path');

module.exports = {
  devServer: {
    contentBase: path.join(__dirname, 'template')
  }
}
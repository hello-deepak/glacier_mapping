var path = require('path');

module.exports = {
  entry: './index.js',
  output: {
    filename: './output.js',
    path: path.resolve(__dirname, 'dist'),
  },
  module: {
    rules: [
      { test: /\.css$/, loader: "style-loader!css-loader" },
      {test: /\.(jpe?g|png|gif|svg)$/i, loader: "url-loader?name=app/images/[name].[ext]"},
    ],
  }
};

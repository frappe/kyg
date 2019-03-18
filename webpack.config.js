const tailwindcss = require('tailwindcss');
const CopyPlugin = require('copy-webpack-plugin');
module.exports = {
	module: {
		rules: [{
			test: /\.less$/,
			loader: 'less-loader' // compiles Less to CSS
		}]
	},
	plugins: [
		tailwindcss('./tailwind.js'),
		new CopyPlugin([
			{
				from: 'src/assets',
				to: 'assets',
			},
		]),
	]
};
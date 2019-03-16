const tailwindcss = require('tailwindcss');
module.exports = {
	module: {
		rules: [{
			test: /\.less$/,
			loader: 'less-loader' // compiles Less to CSS
		}]
	},
	plugins: [
		tailwindcss('./tailwind.js'),
	]
};
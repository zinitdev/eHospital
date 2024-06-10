module.exports = function (api) {
	api.cache(true);
	return {
		presets: ['babel-preset-expo'],
		plugins: [
			[
				'babel-plugin-module-resolver',
				{
					root: ['./src/'],
					alias: {
						'@/*': './src/*',
					},
					extensions: [
						'.js',
						'.jsx',
						'.ts',
						'.tsx',
					],
				},
			],
		],
	};
};
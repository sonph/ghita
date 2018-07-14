	__nest__ (
		__all__,
		'utils', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'utils';
					var List = __init__ (__world__.typing).List;
					var Any = __init__ (__world__.typing).Any;
					var transpose = function (arrays, fill) {
						if (typeof fill == 'undefined' || (fill != null && fill .hasOwnProperty ("__kwargtrans__"))) {;
							var fill = null;
						};
						var longestLength = len (arrays [0]);
						var __iterable0__ = arrays;
						for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
							var array = __iterable0__ [__index0__];
							if (len (array) > longestLength) {
								var longestLength = len (array);
							}
						}
						var ret = list ([]);
						for (var i = 0; i < longestLength; i++) {
							ret.append (list ([]));
							var __iterable0__ = arrays;
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var array = __iterable0__ [__index0__];
								var value = (i < len (array) ? array [i] : fill);
								ret [i].append (value);
							}
						}
						return ret;
					};
					var rotate = function (array, num) {
						var num = __mod__ (num, len (array));
						return array.__getslice__ (num, null, 1).concat (array.__getslice__ (0, num, 1));
					};
					__pragma__ ('<use>' +
						'typing' +
					'</use>')
					__pragma__ ('<all>')
						__all__.Any = Any;
						__all__.List = List;
						__all__.__name__ = __name__;
						__all__.rotate = rotate;
						__all__.transpose = transpose;
					__pragma__ ('</all>')
				}
			}
		}
	);

	__nest__ (
		__all__,
		'app_config', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'app_config';
					var AppConfig = __class__ ('AppConfig', [object], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self) {
							self.simple_chords = true;
							self.open_settings = false;
							self.open_readme = false;
							self.instrument = 'guitar';
						});},
						get toggleSettings () {return __get__ (this, function (self) {
							self.open_settings = !(self.open_settings);
						});},
						get toggleReadme () {return __get__ (this, function (self) {
							self.open_readme = !(self.open_readme);
						});}
					});
					__pragma__ ('<all>')
						__all__.AppConfig = AppConfig;
						__all__.__name__ = __name__;
					__pragma__ ('</all>')
				}
			}
		}
	);

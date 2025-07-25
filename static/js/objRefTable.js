const C3 = self.C3;
self.C3_GetObjectRefTable = function () {
	return [
		C3.Plugins.TiledBg,
		C3.Plugins.Sprite,
		C3.Behaviors.solid,
		C3.Behaviors.scrollto,
		C3.Behaviors.Platform,
		C3.Plugins.Keyboard,
		C3.Plugins.Text,
		C3.Plugins.System.Cnds.OnLayoutStart,
		C3.Plugins.Sprite.Acts.SetOpacity,
		C3.Plugins.Text.Acts.SetOpacity,
		C3.Plugins.Sprite.Cnds.OnCollision,
		C3.Plugins.Sprite.Acts.Destroy,
		C3.Plugins.System.Acts.AddVar,
		C3.Plugins.Text.Acts.SetText,
		C3.Plugins.Keyboard.Cnds.OnKey,
		C3.Plugins.Sprite.Acts.SetMirrored,
		C3.Plugins.System.Cnds.CompareVar,
		C3.Plugins.System.Acts.Wait,
		C3.Plugins.System.Acts.RestartLayout,
		C3.Plugins.System.Acts.ResetGlobals,
		C3.Plugins.System.Cnds.Compare
	];
};
self.C3_JsPropNameTable = [
	{TiledBackground: 0},
	{Solid: 0},
	{Sprite2: 0},
	{Sprite3: 0},
	{ScrollTo: 0},
	{Platform: 0},
	{Sprite4: 0},
	{Keyboard: 0},
	{Sprite5: 0},
	{Text: 0},
	{Sprite6: 0},
	{Sprite7: 0},
	{Sprite8: 0},
	{Text2: 0},
	{Sprite9: 0},
	{Text3: 0},
	{Sprite10: 0},
	{Sprite: 0},
	{Sprite11: 0},
	{Sprite12: 0},
	{Text4: 0},
	{Sprite13: 0},
	{Sprite14: 0},
	{Sprite15: 0},
	{Sprite16: 0},
	{Text5: 0},
	{Sprite17: 0},
	{Text7: 0},
	{reading: 0},
	{harts: 0},
	{medal: 0},
	{water: 0}
];

self.InstanceType = {
	TiledBackground: class extends self.ITiledBackgroundInstance {},
	Sprite2: class extends self.ISpriteInstance {},
	Sprite3: class extends self.ISpriteInstance {},
	Sprite4: class extends self.ISpriteInstance {},
	Keyboard: class extends self.IInstance {},
	Sprite5: class extends self.ISpriteInstance {},
	Text: class extends self.ITextInstance {},
	Sprite6: class extends self.ISpriteInstance {},
	Sprite7: class extends self.ISpriteInstance {},
	Sprite8: class extends self.ISpriteInstance {},
	Text2: class extends self.ITextInstance {},
	Sprite9: class extends self.ISpriteInstance {},
	Text3: class extends self.ITextInstance {},
	Sprite10: class extends self.ISpriteInstance {},
	Sprite: class extends self.ISpriteInstance {},
	Sprite11: class extends self.ISpriteInstance {},
	Sprite12: class extends self.ISpriteInstance {},
	Text4: class extends self.ITextInstance {},
	Sprite13: class extends self.ISpriteInstance {},
	Sprite14: class extends self.ISpriteInstance {},
	Sprite15: class extends self.ISpriteInstance {},
	Sprite16: class extends self.ISpriteInstance {},
	Text5: class extends self.ITextInstance {},
	Sprite17: class extends self.ISpriteInstance {},
	Text7: class extends self.ITextInstance {}
}
from bc.utils.spriteloader import SpriteLoader

loader = SpriteLoader('assets/tiles.png')

grass = loader.get(0,0)
dirt = loader.get(1, 0)

player = [loader.get(0,2, (1, 2))] #, loader.get(1, 2, (1, 2))]

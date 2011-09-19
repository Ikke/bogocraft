from bc.utils.spriteloader import SpriteLoader

loader = SpriteLoader('assets/tiles.png')

grass = loader.get(0,0)
forrest = loader.get(0, 1)

dirt = loader.get(1, 0)

tree = loader.get(2,0,(2,2))

player = [loader.get(0,2, (1, 2))] #, loader.get(1, 2, (1, 2))]

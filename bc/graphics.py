from bc.utils.spriteloader import SpriteLoader

loader = SpriteLoader('assets/tiles.png')

grass = loader.get(0,0)
forrest = loader.get(0, 1)

dirt = loader.get(1, 0)

tree = loader.get(2,0,(2,2))
log = loader.get(4,1)

player = [loader.get(0,4), loader.get(1,4)]

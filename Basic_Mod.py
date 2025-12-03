"""
This is just for a vision of what you could do with modding.
Here you gain a mod_score for each time stepped on a different grass tile.
After going through the door you claim your normal score + mod_score * 1000!
Your player health also decays by 1 every second.
"""

Mod_Score = 0
Claimed_tiles = []

def Frame_Updater(data):
  global Mod_Score
  text = data.font.render(f"Mod score: {Mod_Score}", True, (255, 255, 255))
  data.screen.blit(text, (10, 10))

def Second_Updater(data):
  Player.health -= 1

def Tile0(data):
  global Mod_Score
  for tile in Claimed_tiles:
    if data.new_pos == tile:
      return True
  Claimed_tiles.append(data.new_pos)
  Mod_Score += 1
  return True

def Tile2(data):
  global Mod_Score
  Player.score += 1000*Mod_Score
  return True

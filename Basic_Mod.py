"""
This is just for a vision of what you could do with modding.
I made a mod that uses every aspect of the mod-loader
"""

Mod_Score = 0
Claimed_tiles = []

# When updating scorches don't move, but give +1 hp
def On_Enemy_UpdateScorch(data):
  data.NTT.health += 1
  return False

# Every frame show the Mod score on screen
def Frame_Updater(data):
  global Mod_Score
  text = data.font.render(f"Mod score: {Mod_Score}", True, (255, 255, 255))
  data.screen.blit(text, (10, 10))

# Every second decrease the players health by 1
def Second_Updater(data):
  data.Player.health -= 1

# When the player steps on a grass tile and the position of that grass tile isn't registered
# you get +1 mod score
def Tile0(data):
  global Mod_Score
  for tile in Claimed_tiles:
    if data.new_pos == tile:
      return True
  Claimed_tiles.append(data.new_pos)
  Mod_Score += 1
  return {"Check": True}

# When the player steps on a door tile the mod-score gets converted to normal score
# (1000 score / 1 mod score)
def Tile2(data):
  global Mod_Score
  data.Player.score += 1000*Mod_Score
  return {"Check": True}

def on_b_pressed():
    global decValueOfBinary
    if inBinaryRoom == 1:
        tiles.set_tile_at(tiles.get_tile_location(colBin, 3),
            assets.tile("""
                myBin1
            """))
        if colBin == 6:
            decValueOfBinary += 1
        elif colBin == 5:
            decValueOfBinary += 2
        elif colBin == 4:
            decValueOfBinary += 4
        elif colBin == 3:
            decValueOfBinary += 8
        else:
            pass
        changeBin()
        showDecText()
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_a_pressed():
    if inBinaryRoom == 1:
        tiles.set_tile_at(tiles.get_tile_location(colBin, 3),
            assets.tile("""
                myBin0
            """))
        changeBin()
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def showDecText():
    global decValueOfBinaryText
    if len(convert_to_text(decValueOfBinary)) == 1:
        decValueOfBinaryText = "0" + convert_to_text(decValueOfBinary)
    else:
        decValueOfBinaryText = convert_to_text(decValueOfBinary)
    mySpriteDec.say_text("DECIMAL\\nCODE IS: " + decValueOfBinaryText)
def changeBin():
    global colBin, inBinaryRoom, decValueOfBinary
    colBin += -1
    if colBin == 2 and decValueOfBinary == decCode:
        inBinaryRoom = 0
        pause(200)
        mySprite.say_text("")
        tiles.place_on_tile(mySprite, tiles.get_tile_location(5, 4))
        tiles.set_current_tilemap(tilemap("""
            esc_outside
        """))
        mySprite.set_image(assets.image("""
            myWitchForward0
        """))
        sprites.destroy(mySpriteDec)
        mySpriteBinA.say_text("WE  ESCAPED\\nAND BELIEVE")
        mySpriteBinB.say_text("WE ARE ONLY\\n\"BEGINNING\"")
        mySpriteBin1.say_text("")
        mySpriteBin2.say_text("")
        mySpriteBin4.say_text("")
        mySpriteBin8.say_text("")
        pause(2000)
        effects.confetti.start_screen_effect()
        pause(2000)
        effects.confetti.end_screen_effect()
    elif colBin == 2 and decValueOfBinary != decCode:
        decValueOfBinary = 0
        colBin = 6
        pause(500)
        scene.camera_shake(4, 500)
        tiles.set_tile_at(tiles.get_tile_location(6, 3),
            assets.tile("""
                myBin
            """))
        tiles.set_tile_at(tiles.get_tile_location(5, 3),
            assets.tile("""
                myBin
            """))
        tiles.set_tile_at(tiles.get_tile_location(4, 3),
            assets.tile("""
                myBin
            """))
        tiles.set_tile_at(tiles.get_tile_location(3, 3),
            assets.tile("""
                myBin
            """))
    else:
        pass
def splash():
    scene.set_background_image(assets.image("""
        mySplashScreen
    """))
    game.set_dialog_text_color(1)
    game.set_dialog_frame(assets.image("""
        transparent
    """))
    game.show_long_text("AND THE BINARY CRYPT\\n--------------------\\nPRESS A TO PLAY",
        DialogLayout.BOTTOM)
    scene.set_background_image(assets.image("""
        myBlackBackground
    """))
myRow = 0
myCol = 0
decValueOfBinaryText = ""
decValueOfBinary = 0
colBin = 0
mySpriteDec: Sprite = None
mySpriteBin8: Sprite = None
mySpriteBin4: Sprite = None
mySpriteBin2: Sprite = None
mySpriteBin1: Sprite = None
mySpriteBinB: Sprite = None
mySpriteBinA: Sprite = None
mySprite: Sprite = None
decCode = 0
inBinaryRoom = 0
inBinaryRoom = 0
decCode = randint(1, 15)
splash()
mySprite = sprites.create(assets.image("""
    myWitchForward0
"""), SpriteKind.player)
tiles.set_current_tilemap(tilemap("""
    crypt
"""))
tiles.place_on_tile(mySprite, tiles.get_tile_location(3, 1))
controller.move_sprite(mySprite)
mySpriteBinA = sprites.create(assets.image("""
    mySpriteBin
"""), SpriteKind.player)
mySpriteBinB = sprites.create(assets.image("""
    mySpriteBin
"""), SpriteKind.player)
mySpriteBin1 = sprites.create(assets.image("""
    mySpriteBin
"""), SpriteKind.player)
mySpriteBin2 = sprites.create(assets.image("""
    mySpriteBin
"""), SpriteKind.player)
mySpriteBin4 = sprites.create(assets.image("""
    mySpriteBin
"""), SpriteKind.player)
mySpriteBin8 = sprites.create(assets.image("""
    mySpriteBin
"""), SpriteKind.player)
mySpriteDec = sprites.create(assets.image("""
    mySpriteBin
"""), SpriteKind.player)

def on_update_interval():
    global myCol, myRow, inBinaryRoom, colBin
    myCol = int(mySprite.x / 16)
    myRow = int(mySprite.y / 16)
    if myCol == 8 and myRow == 4:
        if len(convert_to_text(decCode)) == 1:
            mySprite.say_text("THE KEY\\n_IS " + "0" + str(decCode) + "_")
        else:
            mySprite.say_text("THE KEY\\n_IS " + str(decCode) + "_")
    elif myCol == 1 and myRow == 0:
        controller.move_sprite(mySprite, 0, 0)
        tiles.place_on_tile(mySprite, tiles.get_tile_location(2, 2))
        mySprite.set_image(assets.image("""
            mySpriteBin
        """))
        tiles.set_current_tilemap(tilemap("""
            crypt_lock
        """))
        tiles.place_on_tile(mySpriteBinA, tiles.get_tile_location(2, 7))
        tiles.place_on_tile(mySpriteBinB, tiles.get_tile_location(7, 7))
        tiles.place_on_tile(mySpriteBin1, tiles.get_tile_location(6, 5))
        tiles.place_on_tile(mySpriteBin2, tiles.get_tile_location(5, 5))
        tiles.place_on_tile(mySpriteBin4, tiles.get_tile_location(4, 5))
        tiles.place_on_tile(mySpriteBin8, tiles.get_tile_location(3, 5))
        tiles.place_on_tile(mySpriteDec, tiles.get_tile_location(7, 2))
        inBinaryRoom = 1
        colBin = 6
    elif myCol == 2 and myRow == 2:
        mySprite.say_text("ENTER 4-BIT\\nBINARY CODE")
        mySpriteBinA.say_text("BIT OFF= 0 \\n.  PUSH  A")
        mySpriteBinB.say_text("BIT ON = 1 \\n.  PUSH  B")
        mySpriteBin1.say_text("1")
        mySpriteBin2.say_text("2")
        mySpriteBin4.say_text("4")
        mySpriteBin8.say_text("8")
        showDecText()
    else:
        mySprite.say_text("")
game.on_update_interval(500, on_update_interval)

controller.B.onEvent(ControllerButtonEvent.Pressed, function () {
    if (inBinaryRoom == 1) {
        tiles.setTileAt(tiles.getTileLocation(colBin, 3), assets.tile`myBin1`)
        if (colBin == 6) {
            decValueOfBinary += 1
        } else if (colBin == 5) {
            decValueOfBinary += 2
        } else if (colBin == 4) {
            decValueOfBinary += 4
        } else if (colBin == 3) {
            decValueOfBinary += 8
        } else {
        	
        }
        changeBin()
        showDecText()
    }
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    if (inBinaryRoom == 1) {
        tiles.setTileAt(tiles.getTileLocation(colBin, 3), assets.tile`myBin0`)
        changeBin()
    }
})
function showDecText () {
    if (convertToText(decValueOfBinary).length == 1) {
        decValueOfBinaryText = "0" + convertToText(decValueOfBinary)
    } else {
        decValueOfBinaryText = convertToText(decValueOfBinary)
    }
    mySpriteDec.sayText("DECIMAL\\nCODE IS: " + decValueOfBinaryText)
}
function changeBin () {
    colBin += -1
    if (colBin == 2 && decValueOfBinary == decCode) {
        inBinaryRoom = 0
        pause(200)
        mySprite.sayText("")
        tiles.placeOnTile(mySprite, tiles.getTileLocation(5, 4))
        tiles.setCurrentTilemap(tilemap`esc_outside`)
        mySprite.setImage(assets.image`myWitchForward0`)
        sprites.destroy(mySpriteDec)
        mySpriteBinA.sayText("WE  ESCAPED\\nAND BELIEVE")
        mySpriteBinB.sayText("WE ARE ONLY\\n\"BEGINNING\"")
        mySpriteBin1.sayText("")
        mySpriteBin2.sayText("")
        mySpriteBin4.sayText("")
        mySpriteBin8.sayText("")
        pause(2000)
        effects.confetti.startScreenEffect()
        pause(2000)
        effects.confetti.endScreenEffect()
    } else if (colBin == 2 && decValueOfBinary != decCode) {
        decValueOfBinary = 0
        colBin = 6
        pause(500)
        scene.cameraShake(4, 500)
        tiles.setTileAt(tiles.getTileLocation(6, 3), assets.tile`myBin`)
        tiles.setTileAt(tiles.getTileLocation(5, 3), assets.tile`myBin`)
        tiles.setTileAt(tiles.getTileLocation(4, 3), assets.tile`myBin`)
        tiles.setTileAt(tiles.getTileLocation(3, 3), assets.tile`myBin`)
    } else {
    	
    }
}
function splash () {
    scene.setBackgroundImage(assets.image`mySplashScreen`)
    game.setDialogTextColor(1)
    game.setDialogFrame(assets.image`transparent`)
    game.showLongText("AND THE BINARY CRYPT\\n--------------------\\nPRESS A TO PLAY", DialogLayout.Bottom)
    scene.setBackgroundImage(assets.image`myBlackBackground`)
}
let myRow = 0
let myCol = 0
let decValueOfBinaryText = ""
let decValueOfBinary = 0
let colBin = 0
let mySpriteDec: Sprite = null
let mySpriteBin8: Sprite = null
let mySpriteBin4: Sprite = null
let mySpriteBin2: Sprite = null
let mySpriteBin1: Sprite = null
let mySpriteBinB: Sprite = null
let mySpriteBinA: Sprite = null
let mySprite: Sprite = null
let decCode = 0
let inBinaryRoom = 0
inBinaryRoom = 0
decCode = randint(1, 15)
splash()
mySprite = sprites.create(assets.image`myWitchForward0`, SpriteKind.Player)
tiles.setCurrentTilemap(tilemap`crypt`)
tiles.placeOnTile(mySprite, tiles.getTileLocation(3, 1))
controller.moveSprite(mySprite)
mySpriteBinA = sprites.create(assets.image`mySpriteBin`, SpriteKind.Player)
mySpriteBinB = sprites.create(assets.image`mySpriteBin`, SpriteKind.Player)
mySpriteBin1 = sprites.create(assets.image`mySpriteBin`, SpriteKind.Player)
mySpriteBin2 = sprites.create(assets.image`mySpriteBin`, SpriteKind.Player)
mySpriteBin4 = sprites.create(assets.image`mySpriteBin`, SpriteKind.Player)
mySpriteBin8 = sprites.create(assets.image`mySpriteBin`, SpriteKind.Player)
mySpriteDec = sprites.create(assets.image`mySpriteBin`, SpriteKind.Player)
game.onUpdateInterval(500, function () {
    myCol = Math.trunc(mySprite.x / 16)
    myRow = Math.trunc(mySprite.y / 16)
    if (myCol == 8 && myRow == 4) {
        if (convertToText(decCode).length == 1) {
            mySprite.sayText("THE KEY\\n_IS " + "0" + decCode + "_")
        } else {
            mySprite.sayText("THE KEY\\n_IS " + decCode + "_")
        }
    } else if (myCol == 1 && myRow == 0) {
        controller.moveSprite(mySprite, 0, 0)
        tiles.placeOnTile(mySprite, tiles.getTileLocation(2, 2))
        mySprite.setImage(assets.image`mySpriteBin`)
        tiles.setCurrentTilemap(tilemap`crypt_lock`)
        tiles.placeOnTile(mySpriteBinA, tiles.getTileLocation(2, 7))
        tiles.placeOnTile(mySpriteBinB, tiles.getTileLocation(7, 7))
        tiles.placeOnTile(mySpriteBin1, tiles.getTileLocation(6, 5))
        tiles.placeOnTile(mySpriteBin2, tiles.getTileLocation(5, 5))
        tiles.placeOnTile(mySpriteBin4, tiles.getTileLocation(4, 5))
        tiles.placeOnTile(mySpriteBin8, tiles.getTileLocation(3, 5))
        tiles.placeOnTile(mySpriteDec, tiles.getTileLocation(7, 2))
        inBinaryRoom = 1
        colBin = 6
    } else if (myCol == 2 && myRow == 2) {
        mySprite.sayText("ENTER 4-BIT\\nBINARY CODE")
        mySpriteBinA.sayText("BIT OFF= 0 \\n.  PUSH  A")
        mySpriteBinB.sayText("BIT ON = 1 \\n.  PUSH  B")
        mySpriteBin1.sayText("1")
        mySpriteBin2.sayText("2")
        mySpriteBin4.sayText("4")
        mySpriteBin8.sayText("8")
        showDecText()
    } else {
        mySprite.sayText("")
    }
})

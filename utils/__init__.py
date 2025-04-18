from ..path import Files, Folder
from xml.etree.ElementTree import parse as xml_parse, Element
from lxml.etree import XMLParser, _Element as LElement
import pygame
import warnings

"""
def setupInstaller():
    def runCmd(cmd):
        import subprocess
        return subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    def checkInstalledPackages(*packages):

        # The Developer Hell(p) Line
        def unwrap():
            return list(filter(lambda x: not list(filter(lambda x: any([x == y for y in packages]), [x.split(" ")[0] for x in runCmd("pip list").stdout.read().decode("utf8").split("\r\n")][2::])).__contains__(x), packages))

        [runCmd(f"pip install {package}") for package in unwrap()]

    checkInstalledPackages("pygame-ce", "lxml", "multipledispatch")
"""

def loadImage(name: str | pygame.Surface) -> pygame.Surface:
    if isinstance(name, pygame.Surface): return name
    return pygame.image.load(Files.getImagePath(name))

def loadAnimation(name: str):
    animImgPath, xmlPath = Files.getAnimationPath(name)
    animImg = pygame.image.load(animImgPath)
    xml = xml_parse(xmlPath, XMLParser(recover=True)).getroot()
    return animImg, xml

def loadSound(name: str):
    return Files.getSoundsPath(name)

def loadMusic(name: str):
    return Files.getMusicPath(name)

def loadFont(font: pygame.Font | str):

    import pygame.freetype
    if isinstance(font, pygame.Font | pygame.freetype.Font): return font
    return pygame.Font(Files.getFontsPath(font), 48)

def parseAnimation(name: str):
    Animations = {}
    img, xml = loadAnimation(name)
    curName = ""
    first = ""
    index = 0

    if isinstance(xml, Element | LElement):
        for sprite in xml:
            name = sprite.get("name")
            if name is not None:
                getName = list(name)

                name = ""
                xx = ""
                lead0 = True
                for char in getName:
                    if char.isdigit() and int(char) == 0 and lead0:
                        continue
                    elif char.isdigit() and int(char) > 0 and lead0:
                        lead0 = False

                    if char.isdigit():
                        xx += char
                    else:
                        name += char
                if xx == "":
                    xx = "0"

                prevName = name
                name = name.rsplit(" ", 1)
                if len(name) > 1:
                    if name[1] != "":
                        if all(list(map(lambda x: not x.isdigit(), list(name[1])))):
                            name[0] = prevName
                name = name[0]

                if name != curName:
                    curName = name
                    index = 0
                    if first == "":
                        first = name

                x = int(sprite.get("x"))
                y = int(sprite.get("y"))
                width = int(sprite.get("width"))
                height = int(sprite.get("height"))

                hitboxX = int(sprite.get("frameX") or 0)
                hitboxY = int(sprite.get("frameY") or 0)
                hitboxWidth = int(sprite.get("frameWidth") or width)
                hitboxHeight = int(sprite.get("frameHeight") or height)

                offsetX = int(sprite.get("offsetX") or 0)
                offsetY = int(sprite.get("offsetY") or 0)

                if Animations.get(name) == None:
                    Animations[name] = {}

                x = min(x, img.size[0] - width)
                y = min(y, img.size[1] - height)
                Animations[name][index] = {
                    "Image": img.subsurface(x, y, width, height),
                    "Hitbox": (pygame.math.Vector2(hitboxX, hitboxY), pygame.math.Vector2(hitboxWidth, hitboxHeight)),
                    "Offset": pygame.math.Vector2(offsetX, offsetY),
                }

                index += 1
    return Animations, first


def loadTilemaps(n: str):
    def preload():
        tileMapImgPath, xmlPath = Files.getTileMapPath(n)
        tileMap = pygame.image.load(tileMapImgPath)
        xml = xml_parse(xmlPath, XMLParser(recover=True)).getroot()
        return tileMap, xml

    def load():
        tiles = {}
        tileMap, xml = preload()
        if isinstance(xml, Element | LElement):
            for sprite in xml:
                name = sprite.get("name")
                if name is not None:

                    x = int(sprite.get("x"))
                    y = int(sprite.get("y"))
                    width = int(sprite.get("width"))
                    height = int(sprite.get("height"))

                    x = min(x, tileMap.size[0] - width)
                    y = min(y, tileMap.size[1] - height)

                    tiles[name] = tileMap.subsurface(x, y, width, height)

        return tiles
    return load()



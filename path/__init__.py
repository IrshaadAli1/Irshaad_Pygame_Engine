import os

ASSETS_FOLDER_PATH = "assets"
CWD = os.getcwd()




class Folder:
    @staticmethod
    def setupAssetsFolder():
        if os.path.exists(os.path.join(CWD, ASSETS_FOLDER_PATH)): return True
        os.mkdir(os.path.join(CWD, ASSETS_FOLDER_PATH))
        os.mkdir(os.path.join(CWD, ASSETS_FOLDER_PATH, "images"))
        os.mkdir(os.path.join(CWD, ASSETS_FOLDER_PATH, "animations"))
        os.mkdir(os.path.join(CWD, ASSETS_FOLDER_PATH, "sounds"))
        os.mkdir(os.path.join(CWD, ASSETS_FOLDER_PATH, "music"))
        os.mkdir(os.path.join(CWD, ASSETS_FOLDER_PATH, "fonts"))
        os.mkdir(os.path.join(CWD, ASSETS_FOLDER_PATH, "tilemaps"))
        return False

    @staticmethod
    def getImagesFolder():
        if Folder.setupAssetsFolder():
            return os.path.join(CWD, ASSETS_FOLDER_PATH, "images")

    @staticmethod
    def getAnimationsFolder():
        if Folder.setupAssetsFolder():
            return os.path.join(CWD, ASSETS_FOLDER_PATH, "animations")

    @staticmethod
    def getSoundsFolder():
        if Folder.setupAssetsFolder():
            return os.path.join(CWD, ASSETS_FOLDER_PATH, "sounds")

    @staticmethod
    def getMusicFolder():
        if Folder.setupAssetsFolder():
            return os.path.join(CWD, ASSETS_FOLDER_PATH, "music")

    @staticmethod
    def getFontsFolder():
        if Folder.setupAssetsFolder():
            return os.path.join(CWD, ASSETS_FOLDER_PATH, "fonts")

    @staticmethod
    def getTilemapsFolder():
        if Folder.setupAssetsFolder():
            return os.path.join(CWD, ASSETS_FOLDER_PATH, "tilemaps")


class Files:
    @staticmethod
    def getImagePath(imgName: str):
        return os.path.join(Folder.getImagesFolder(), imgName)

    @staticmethod
    def getSoundsPath(sndName: str):
        return os.path.join(Folder.getSoundsFolder(), sndName)

    @staticmethod
    def getMusicPath(mscName: str):
        return os.path.join(Folder.getMusicFolder(), mscName)

    @staticmethod
    def getAnimationPath(name: str):
        return os.path.join(Folder.getAnimationsFolder(), name + '.png'), os.path.join(Folder.getAnimationsFolder(), name + '.xml')

    @staticmethod
    def getFontsPath(name: str):
        return os.path.join(Folder.getFontsFolder(), name)

    @staticmethod
    def getTileMapPath(tileName: str):
        return os.path.join(Folder.getTilemapsFolder(), tileName + ".png"), os.path.join(Folder.getTilemapsFolder(), tileName + ".xml")
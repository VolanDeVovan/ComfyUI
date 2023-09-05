from .utils import HentaiKitchenRandomSeed, HentaiKitchenScaleBy
from .inputs import HentaiKitchenTxt2ImgInput, HentaiKitchenTxt2ImgInputState
from .aspect_ratio import HentaiKitchenAspectRatio
from .enhanced import HentaiKitchenPostProcess

# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    # Utils
    "HentaiKitchenRandomSeed": HentaiKitchenRandomSeed,
    "HentaiKitchenScaleBy": HentaiKitchenScaleBy,

    "HentaiKitchenAspectRatio": HentaiKitchenAspectRatio,
    "HentaiKitchenPostProcess": HentaiKitchenPostProcess,

    # Inputs
    "HentaiKitchenTxt2ImgInput": HentaiKitchenTxt2ImgInput,
    "HentaiKitchenTxt2ImgInputState": HentaiKitchenTxt2ImgInputState,

}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    # Utils
    "HentaiKitchenRandomSeed": "Random Seed (Hentai Kitchen)",
    "HentaiKitchenScaleBy": "Scale by (Hentai Kitchen)",

    "HentaiKitchenAspectRatio": "Aspect Ratio (Hentai Kitchen)",
    "HentaiKitchenPostProcess": "Post Process (Hentai Kitchen)",

    # Inputs
    "HentaiKitchenTxt2ImgInput": "txt2img Input (Hentai Kitchen)",
    "HentaiKitchenTxt2ImgInputState": "txt2img Input State (Hentai Kitchen)",
}

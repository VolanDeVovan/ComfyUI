from .api_input import HentaiKitchenAPIInput, HentaiKitchenAPIInputState
from .utils import HentaiKitchenRandomSeed

# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "HentaiKitchenAPIInput": HentaiKitchenAPIInput,
    "HentaiKitchenAPIInputState": HentaiKitchenAPIInputState,

    "HentaiKitchenRandomSeed": HentaiKitchenRandomSeed,
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "HentaiKitchenAPIInput": "API Input (Hentai Kitchen)",
    "HentaiKitchenAPIInputState": "API Input State (Hentai Kitchen)",

    "HentaiKitchenRandomSeed": "Random Seed (Hentai Kitchen)",
}

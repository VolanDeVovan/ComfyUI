import random

class HentaiKitchenRandomSeed:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "seed": ("INT", {"default": -1, "min": -1, "max": 0xffffffffffffffff}),
            }
        }

    FUNCTION = "random_seed"
    RETURN_TYPES = ("INT",)

    CATEGORY = "Hentai Kitchen"

    def random_seed(self, seed):
        if seed is None or seed == -1:
            seed = random.randint(0, 0xffffffffffffffff)
        return (seed,)
    
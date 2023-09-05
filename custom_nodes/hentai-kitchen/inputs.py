class HentaiKitchenTxt2ImgInput:
    CATEGORY = "Hentai Kitchen"

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {
                    "default": "",
                    "multiline": True
                }),
                "pose": ("STRING", {
                    "default": "",
                    "multiline": False
                }),
                "lora_character": ("STRING", {
                    "default": "",
                    "multiline": False
                }),
                "lora_pose": ("STRING", {
                    "default": "",
                    "multiline": False
                }),
            }
        }

    RETURN_TYPES = ("*", "*", "*", "*")
    RETURN_NAMES = ("prompt", "pose", "lora_character", "lora_pose")

    FUNCTION = "input"

    def input(self, prompt, pose, lora_character, lora_pose):
        return (prompt, pose, lora_character, lora_pose)


class HentaiKitchenTxt2ImgInputState:
    CATEGORY = "Hentai Kitchen"

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "pose": ("BOOLEAN", {
                    "default": False
                }),
                "lora_character": ("BOOLEAN", {
                    "default": False,
                }),
                "lora_pose": ("BOOLEAN", {
                    "default": False,
                }),
            }
        }

    RETURN_TYPES = ("BOOLEAN", "BOOLEAN", "BOOLEAN")
    RETURN_NAMES = ("pose_enabled", "lora_character_enabled",
                    "lora_pose_enabled")

    FUNCTION = "input"

    def input(self, pose, lora_character, lora_pose):
        return (pose, lora_character, lora_pose)



class HentaiKitchenUpscaleInput:
    CATEGORY = "Hentai Kitchen"

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "input_image": ("STRING", {
                    "default": "",
                    "multiline": False
                }),
            }
        }

    RETURN_TYPES = ("*",)
    RETURN_NAMES = ("input_image",)

    FUNCTION = "input"

    def input(self, input_image):
        return (input_image,)

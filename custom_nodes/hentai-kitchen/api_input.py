"""
prompt

lora
pose
"""
class HentaiKitchenAPIInput:
    CATEGORY = "Hentai Kitchen"

    def __init__(self):
        pass


    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {
                    "default": "",
                    "multiline": False
                }),
                "pose": ("STRING", {
                    "default": "",
                    "multiline": False
                }),
                "lora": ("STRING", {
                    "default": "",
                    "multiline": False
                }),
            }
        }
    
    RETURN_TYPES = ("*", "*", "*")
    RETURN_NAMES = ("prompt", "pose", "lora")

    FUNCTION = "input"

    def input(self, prompt, pose, lora):
        return (prompt, pose, lora)
    

class HentaiKitchenAPIInputState:
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
                "lora": ("BOOLEAN", {
                    "default": False,
                }),
            }
        }
    
    RETURN_TYPES = ("BOOLEAN", "BOOLEAN")
    RETURN_NAMES = ("pose_enabled", "lora_enabled")

    FUNCTION = "input"

    def input(self, pose, lora):
        return (pose, lora)
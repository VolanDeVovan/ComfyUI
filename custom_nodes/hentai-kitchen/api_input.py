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
                "lora_character": ("BOOLEAN", {
                    "default": False,
                }),
                "lora_pose": ("BOOLEAN", {
                    "default": False,
                }),
            }
        }
    
    RETURN_TYPES = ("BOOLEAN", "BOOLEAN", "BOOLEAN")
    RETURN_NAMES = ("pose_enabled", "lora_character_enabled", "lora_pose_enabled")

    FUNCTION = "input"

    def input(self, pose, lora):
        return (pose, lora)
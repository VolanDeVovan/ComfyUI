from PIL import Image
import numpy as np
import torch

class HentaiKitchenScaleBy:

    CATEGORY = "Hentai Kitchen"

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE", {
                    "default": None
                }),
                "multiplier": ("FLOAT", {
                    "default": 1.0
                })
            }
        }
    
    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("resized_image",)

    FUNCTION = "resize_image"

    def resize_image(self, image, multiplier):
        # Преобразование тензора в PIL изображение
        i = 255.0 * image.cpu().numpy().squeeze()
        img = Image.fromarray(i.astype(np.uint8))
        
        # Вычисление новых размеров с учетом множителя
        new_width = int(img.width * multiplier)
        new_height = int(img.height * multiplier)

        # Изменение размера изображения с использованием Image.ANTIALIAS
        resized_img = img.resize((new_width, new_height), Image.ANTIALIAS)

        # Преобразование PIL изображения обратно в тензор и преобразование в float
        tensor_img = torch.from_numpy(np.array(resized_img)).unsqueeze(0).float() / 255.0

        return (tensor_img,)
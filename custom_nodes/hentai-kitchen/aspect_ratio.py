from PIL import Image
import numpy as np
import torch

class HentaiKitchenAspectRatio:
    CATEGORY = "Hentai Kitchen"

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE", {
                    "default": None
                }),
            },
            "optional": {
                "max_side_length": ("INT", {"default": 922, "min": 512})  # Добавлен новый параметр с дефолтным значением 922
            }
        }
    
    RETURN_TYPES = ("IMAGE",)  # Теперь мы возвращаем изображение
    RETURN_NAMES = ("resized_image",)

    FUNCTION = "process_image"
    def process_image(self, image, max_side_length=922):  # max_side_length теперь параметр функции
        # Преобразование тензора в PIL изображение
        i = 255. * image.cpu().numpy().squeeze()
        img = Image.fromarray(i.astype(np.uint8))
        
        width, height = img.size
        
        # Находим соотношение сторон
        aspect_ratio = width / height
        
        # Определяем новые размеры, сохраняя соотношение сторон и устанавливая максимальную сторону равной max_side_length
        if width > height:
            new_width = max_side_length
            new_height = int(new_width / aspect_ratio)
        else:
            new_height = max_side_length
            new_width = int(new_height * aspect_ratio)

        # Изменение размера изображения
        resized_img = img.resize((new_width, new_height), Image.ANTIALIAS)

        # Преобразование PIL изображения обратно в тензор и преобразование в float
        tensor_img = torch.from_numpy(np.array(resized_img)).unsqueeze(0).float() / 255.0

        return (tensor_img,)
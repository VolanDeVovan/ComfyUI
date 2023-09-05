import torch
import numpy as np
from PIL import Image, ImageEnhance, ImageFilter

class HentaiKitchenPostProcess:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE",),
            },
            "optional": {
                "saturation_strength": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 3.0, "step": 0.01}),
                "sharpness_strength": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 1.0, "step": 0.01}),  # Updated min and max
                "brightness_strength": ("FLOAT", {"default": 0.0, "min": -1.0, "max": 1.0, "step": 0.01}),
                "contrast_strength": ("FLOAT", {"default": 1.0, "min": -1.0, "max": 1.0, "step": 0.01}),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "apply_filter"
    CATEGORY = "Hentai Kitchen"

    def apply_filter(self, image, saturation_strength=1.0, sharpness_strength=1.0, brightness_strength=0.0, contrast_strength=1.0):
        # Convert the input image tensor to a PIL Image for saturation and sharpness adjustments
        i = 255. * image.cpu().numpy().squeeze()
        img = Image.fromarray(np.clip(i, 0, 255).astype(np.uint8))

        # Apply saturation adjustment
        img = ImageEnhance.Color(img).enhance(saturation_strength)

        # Apply detail filter
        if sharpness_strength < 1.0:  # Only blend if sharpness_strength is less than 1
            detail_filtered_img = img.filter(ImageFilter.DETAIL)
            img = Image.blend(img, detail_filtered_img, sharpness_strength)
        else:
            img = img.filter(ImageFilter.DETAIL)

        # Convert back to numpy for brightness and contrast adjustments
        adjusted_image_np = np.array(img).astype(np.float32) / 255.0

        # Apply brightness adjustment
        adjusted_image_np = np.clip(adjusted_image_np + brightness_strength, 0.0, 1.0)

        # Apply contrast adjustment
        adjusted_image_np = np.clip(adjusted_image_np * contrast_strength, 0.0, 1.0)

        # Convert the adjusted image back to a tensor
        image = torch.from_numpy(adjusted_image_np).unsqueeze(0)
        
        return (image,)

NODE_CLASS_MAPPINGS = {
    "HentaiKitchenPostProcess": HentaiKitchenPostProcess
}
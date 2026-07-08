from cog import BaseRunner, Input, Path
from PIL import Image, ImageFilter


class Runner(BaseRunner):
    def setup(self):
        """Lightweight task — no model to load, but the structure stays in place"""
        pass

    def run(
        self,
        image: Path = Input(description="Image to process"),
        scale: float = Input(
            description="Scaling factor", default=2.0, ge=0.1, le=8.0
        ),
        effect: str = Input(
            description="Effect to apply",
            default="none",
            choices=["none", "blur", "sharpen", "grayscale"],
        ),
    ) -> Path:
        """Resize the image and optionally apply an effect"""
        img = Image.open(image).convert("RGB")
        new_size = (int(img.width * scale), int(img.height * scale))
        img = img.resize(new_size, Image.LANCZOS)

        if effect == "blur":
            img = img.filter(ImageFilter.GaussianBlur(4))
        elif effect == "sharpen":
            img = img.filter(ImageFilter.SHARPEN)
        elif effect == "grayscale":
            img = img.convert("L")

        output_path = Path("/tmp/output.png")
        img.save(output_path)
        return output_path
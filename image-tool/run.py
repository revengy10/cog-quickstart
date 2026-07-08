import tempfile

from cog import BaseModel, BaseRunner, Input, Path
from PIL import Image, ImageFilter


class Output(BaseModel):
    image: Path
    width: int
    height: int
    applied_effect: str


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
    ) -> Output:
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

        self.record_metric("output_pixels", new_size[0] * new_size[1])

        output_path = Path(tempfile.mkdtemp()) / "output.png"
        img.save(output_path)
        return Output(
            image=output_path,
            width=new_size[0],
            height=new_size[1],
            applied_effect=effect,
        )
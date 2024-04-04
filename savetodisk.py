from invokeai.invocation_api import (
    BaseInvocation,
    InvocationContext,
    invocation,
    InputField,
    ImageField,
    ImageOutput,
)
import os
from pydantic import BaseModel
from PIL import Image
import PIL


class SaveToDisk(BaseModel):
    message: str


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


@invocation(
    "Save_To_Disk",
    title="Save Image to Disk",
    tags=["image", "board"],
    category="image",
    version="0.1.0",
    use_cache=False,
)
class SaveToDiskInvocation(BaseInvocation):
    """Save Image to a location"""

    output_dir: str = InputField(
        description="Location to save image",
        default='C:/',
    )
    output_name: str = InputField(
        description="Name of the file",
        default="",
    )
    input_image: ImageField = InputField(
        description="Input image to be moved"
    )

    def invoke(self, context: InvocationContext) -> ImageOutput:
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
        picture = context.images.get_pil(self.input_image.image_name)
        if self.output_name == "":
            out_path = os.path.join(self.output_dir, self.input_image.image_name)
        else:
            name = self.output_name + ".png"
            out_path = os.path.join(self.output_dir, name)
        count = 0
        while os.path.isfile(out_path):
            count = count + 1
            countstr = str(count)
            name = self.output_name + "_" + countstr.zfill(5) + ".png"
            out_path = os.path.join(self.output_dir, name)

        picture = picture.save(out_path)

        image_dto = context.images.get_dto(self.input_image.image_name)
        return ImageOutput(
            image=ImageField(image_name=self.input_image.image_name),
            width=image_dto.width,
            height=image_dto.height,
        )

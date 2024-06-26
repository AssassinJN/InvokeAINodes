from invokeai.invocation_api import (
    BaseInvocation,
    InvocationContext,
    invocation,
    InputField,
    ImageField,
    ImageOutput,
    BoardField,
)


from pydantic import BaseModel


@invocation(
    "Move_Boards",
    title="Move Image to Board",
    tags=["image", "board"],
    category="image",
    version="0.1.0",
    use_cache=False,
)
class MoveBoardsInvocation(BaseInvocation):
    """Move image to a different board"""

    input_image: ImageField = InputField(
        description="Input image to be moved"
    )
	
    output_board: BoardField = InputField(
        description="Output board where images will be moved"
    )

    def invoke(self, context: InvocationContext) -> ImageOutput:
        context._services.board_images.remove_image_from_board(self.input_image.image_name)
        context._services.board_images.add_image_to_board(self.output_board.board_id, self.input_image.image_name)
        image_dto = context.images.get_dto(self.input_image.image_name)
        return ImageOutput(
            image=ImageField(image_name=self.input_image.image_name),
            width=image_dto.width,
            height=image_dto.height,
        )

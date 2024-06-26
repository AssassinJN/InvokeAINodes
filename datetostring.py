from invokeai.invocation_api import (
    BaseInvocation,
    InvocationContext,
    invocation,
    InputField,
    StringOutput,
)

from pydantic import BaseModel

from datetime import datetime

now = datetime.now()


class DateToString(BaseModel):
    message: str

@invocation(
    "Date_To_String",
    title="Output Date as String",
    tags=["string"],
    category="string",
    version="0.1.0",
    use_cache=False,
)
class DateToStringInvocation(BaseInvocation):
    """Output Date as String"""

    date_format: str = InputField(
        description="Enter format of date",
        default="%m_%d",
    )


    def invoke(self, context: InvocationContext) -> StringOutput:
        
        return StringOutput(
            value = now.strftime(self.date_format)
        )

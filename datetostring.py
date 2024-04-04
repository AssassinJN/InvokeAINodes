from invokeai.app.invocations.baseinvocation import (
    BaseInvocation,
    invocation,
)
from invokeai.app.services.shared.invocation_context import InvocationContext
from invokeai.app.invocations.fields import InputField
from invokeai.app.invocations.primitives import (
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

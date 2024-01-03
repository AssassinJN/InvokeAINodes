from invokeai.app.invocations.baseinvocation import (
    BaseInvocation,
    InvocationContext,
    invocation,
    InputField,
)
from invokeai.app.invocations.primitives import (
    StringCollectionOutput,
)

from pydantic import BaseModel
from random import randrange
import json


@invocation(
    "Random_Models",
    title="Random Models",
    tags=["model"],
    category="model",
    version="0.1.0",
    use_cache=False,
)
class RandomModelInvocation(BaseInvocation):
    """Return Models as a collection of strings"""

    model_count: int = InputField(
        description="How many models to include"
    )

    def invoke(self, context: InvocationContext) -> StringCollectionOutput:
        modelList = context.services.model_manager.list_models('sd-1', 'main')
        newModelList = []
        outputModelList = []
        for model in modelList:
            newModelList.append(json.dumps(model))
        if len(newModelList) < self.model_count:
            self.model_count = len(newModelList)
        for x in range(0,self.model_count):
            outputModelList.append(newModelList.pop(randrange(len(newModelList))))
        print(outputModelList)
        return StringCollectionOutput(
            collection=outputModelList
        )

from invokeai.app.invocations.baseinvocation import (
    BaseInvocation,
    invocation,
)
from invokeai.app.services.shared.invocation_context import InvocationContext
from invokeai.app.invocations.fields import InputField
from invokeai.app.invocations.primitives import (
    StringCollectionOutput,
)

from pydantic import BaseModel
from random import randrange
from typing import Literal
import json

typeStart = {
    "main":"main",
    "lora":"lora",
    "controlnet":"controlnet",
    "t2i_adapter":"t2i_adapter",
    "clip_vision":"clip_vision",
    "ip_adapter":"ip_adapter",
    "vae":"vae",
    "embedding":"embedding",
    }
baseStart = {
    "sd-1":"sd-1",
    "sdxl":"sdxl",
    "any":"any"
    }

modelTypes: list = typeStart
baseModels: list = baseStart

@invocation(
    "Random_Models",
    title="Random Models",
    tags=["model","random"],
    category="model",
    version="0.1.0",
    use_cache=False,
)
class RandomModelInvocation(BaseInvocation):
    """Return Models as a collection of strings"""
    model_count: int = InputField(
        description="How many models to include"
    )
    """model_type: list[str] = InputField(default=[], description="The X collection")"""
    base_model: Literal[tuple(baseModels.keys())] = InputField(
        description="Base Model"
    )
    model_type: Literal[tuple(modelTypes.keys())] = InputField(
        description="Model Type"
    )

    def invoke(self, context: InvocationContext) -> StringCollectionOutput:
        """
        allModels = context.services.model_manager.list_models()
        modelTypes = []
        baseModels = []
        for tempmodel in allModels:
            modelTypes.append(json.dumps(tempmodel['model_type']))
            baseModels.append(json.dumps(tempmodel['base_model']))
        modelTypes = list(set(modelTypes))
        baseModels = list(set(baseModels))
        print(modelTypes)
        print(baseModels)
        """


        modelList = context.services.model_manager.list_models(self.base_model, self.model_type)
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
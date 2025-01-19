from llms.Llama_init import Llama
from llms.Qwen_init import Qwen
from llms.Llama_init import LLM

model: LLM = None


def set_llm(model_name):
    global model

    model_cat = model_name.split('-')[0]
    if model_cat == 'Qwen':
        # from llms.LLM_init import Qwen
        model = Qwen(model_name)
    elif model_cat == 'llama':
        # from llms.Llama_init import Llama
        model = Llama(model_name)
    else:
        raise Exception(f'不支持的模型 {model_name}')


def request_llm(sys_prompt: str, user_prompt: list, stream=False):
    return model.request(sys_prompt, user_prompt, stream)
from llms.Llama_init import Llama
from llms.Qwen_init import Qwen
# from llms.Llama_init import LLM
from llms.Qwen_init import LLM_init

model: LLM_init = None

MODEL_PATH = './models/hub/deepseek-ai/DeepSeek-R1-Distill-Qwen-7B'

def set_llm(model_name = MODEL_PATH):
    global model
    model = Qwen(model_name) # 加载模型
"""
    # global model
    # model_cat = model_name.split('-')[0]
    # if model_cat == 'Qwen':
    #     # from llms.LLM_init import Qwen
    #     model = Qwen(model_name)
    # elif model_cat == 'llama':
    #     # from llms.Llama_init import Llama
    #     model = Llama(model_name)
    # else:
    #     raise Exception(f'不支持的模型 {model_name}')
"""

def request_llm(sys_prompt: str, user_prompt: list, stream=False):
    return model.request(sys_prompt, user_prompt, stream)
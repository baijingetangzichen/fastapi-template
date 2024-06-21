from os import getenv


class ProxyConfig(object):
    """
    代理服务的配置
    """
    COMFYUI_PROTOCOL = getenv("COMFYUI_PROTOCOL", "http://")
    COMFYUI_HOST = getenv("COMFYUI_HOST", "60.28.101.143:8849")
    COMFYUI_API_PREFIX = getenv("COMFYUI_API_PREFIX", "/text2video")
    COMFYUI_API_URL = f"{COMFYUI_PROTOCOL}{COMFYUI_HOST}{COMFYUI_API_PREFIX}"
    COMFYUI_UPLOAD_IMAGE = getenv("COMFYUI_UPLOAD_IMAGE", f"{COMFYUI_API_URL}/upload/image")
    COMFYUI_PROMPT = getenv("COMFYUI_PROMPT", f"{COMFYUI_API_URL}/prompt")
    COMFYUI_PROMPT_HIS = getenv("COMFYUI_PROMPT_HIS", f"{COMFYUI_API_URL}/history")
    COMFYUI_PROMPT_VIEW = getenv("COMFYUI_PROMPT_VIEW", f"{COMFYUI_API_URL}/view")
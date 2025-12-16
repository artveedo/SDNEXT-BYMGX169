import os

# 1. Setup Environment (Drivers are already present in OpenXLab, do not install them)
os.chdir(f"/home/xlab-app-center")

# 2. Clone SDNext (Vladmandic's Automatic fork)
# Using SDNext as requested. If you prefer standard A1111, change URL to: https://github.com/AUTOMATIC1111/stable-diffusion-webui
if not os.path.exists("/home/xlab-app-center/stable-diffusion-webui"):
    os.system(f"git clone https://github.com/vladmandic/automatic /home/xlab-app-center/stable-diffusion-webui")

os.chdir(f"/home/xlab-app-center/stable-diffusion-webui")
os.system(f"git lfs install")
os.system(f"git reset --hard")

# 3. Install Extensions (Only necessary ones)
extensions_dir = "/home/xlab-app-center/stable-diffusion-webui/extensions"

# Image Browser
if not os.path.exists(f"{extensions_dir}/sd-webui-infinite-image-browsing"):
    os.system(f"git clone https://github.com/zanllp/sd-webui-infinite-image-browsing {extensions_dir}/sd-webui-infinite-image-browsing")

# Aspect Ratio Helper
if not os.path.exists(f"{extensions_dir}/sd-webui-aspect-ratio-helper"):
    os.system(f"git clone -b dev https://github.com/camenduru/sd-webui-aspect-ratio-helper {extensions_dir}/sd-webui-aspect-ratio-helper")

# ControlNet
if not os.path.exists(f"{extensions_dir}/sd-webui-controlnet"):
    os.system(f"git clone https://github.com/Mikubill/sd-webui-controlnet {extensions_dir}/sd-webui-controlnet")

# Deforum (Since you included settings for it)
if not os.path.exists(f"{extensions_dir}/deforum-for-automatic1111-webui"):
    os.system(f"git clone https://github.com/deforum-art/deforum-for-automatic1111-webui {extensions_dir}/deforum-for-automatic1111-webui")

# 4. Download Models (Switched to Hugging Face to fix download errors)
# We use aria2c for fast multi-connection downloading.
model_dir = "/home/xlab-app-center/stable-diffusion-webui/models/Stable-diffusion"
vae_dir = "/home/xlab-app-center/stable-diffusion-webui/models/VAE"
lora_dir = "/home/xlab-app-center/stable-diffusion-webui/models/Lora"
controlnet_dir = "/home/xlab-app-center/stable-diffusion-webui/extensions/sd-webui-controlnet/models"

# --- CHECKPOINTS (Famous Models) ---
# Realistic Vision V6.0 (Standard for photorealism)
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/SG161222/Realistic_Vision_V6.0_B1_noVAE/resolve/main/Realistic_Vision_V6.0_B1_noVAE.safetensors -d {model_dir} -o Realistic_Vision_V6.0.safetensors")

# DreamShaper 8 (Great for art/general)
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/Lykon/DreamShaper/resolve/main/DreamShaper_8_pruned.safetensors -d {model_dir} -o DreamShaper_8.safetensors")

# SDXL Base 1.0 (Newer high-res standard)
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/resolve/main/sd_xl_base_1.0.safetensors -d {model_dir} -o sd_xl_base_1.0.safetensors")

# Rev Animated (Good for 2.5D/Anime style)
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/stablediffusionapi/rev-animated/resolve/main/rev-animated.safetensors -d {model_dir} -o rev_animated.safetensors")

# --- VAE ---
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/stabilityai/sd-vae-ft-mse-original/resolve/main/vae-ft-mse-840000-ema-pruned.ckpt -d {vae_dir} -o vae-ft-mse-840000-ema-pruned.ckpt")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/madebyollin/sdxl-vae-fp16-fix/resolve/main/sdxl_vae.safetensors -d {vae_dir} -o sdxl_vae.safetensors")

# --- CONTROLNET MODELS (Essentials only to save space/time) ---
# Canny
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11p_sd15_canny_fp16.safetensors -d {controlnet_dir} -o control_v11p_sd15_canny_fp16.safetensors")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/raw/main/control_v11p_sd15_canny_fp16.yaml -d {controlnet_dir} -o control_v11p_sd15_canny_fp16.yaml")

# OpenPose
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11p_sd15_openpose_fp16.safetensors -d {controlnet_dir} -o control_v11p_sd15_openpose_fp16.safetensors")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/raw/main/control_v11p_sd15_openpose_fp16.yaml -d {controlnet_dir} -o control_v11p_sd15_openpose_fp16.yaml")

# Depth
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11f1p_sd15_depth_fp16.safetensors -d {controlnet_dir} -o control_v11f1p_sd15_depth_fp16.safetensors")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/raw/main/control_v11f1p_sd15_depth_fp16.yaml -d {controlnet_dir} -o control_v11f1p_sd15_depth_fp16.yaml")

# 5. Launch
# Using webui.sh with arguments for cloud environments
# --listen makes it accessible over network
# --xformers enables faster generation
# --no-half-vae prevents black images
print("Launching SDNext...")
os.system(f"bash webui.sh --listen --xformers --enable-insecure-extension-access --theme dark --no-half-vae --disable-console-progressbars")

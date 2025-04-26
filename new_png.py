from PIL import Image

# 创建192x192的黑色图像
image_192x192 = Image.new('RGB', (192, 192), color='black')
image_192x192.save(r'D:\py\myself\html_chief\192x192_icon.png')

# 创建512x512的黑色图像
image_512x512 = Image.new('RGB', (512, 512), color='black')
image_512x512.save(r'D:\py\myself\html_chief\icon.png')

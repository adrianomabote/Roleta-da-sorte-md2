from PIL import Image, ImageDraw
img = Image.new('RGB', (300, 300), color='white')
draw = ImageDraw.Draw(img)
colors = ['#FF6B6B', '#FFA500', '#FFD93D', '#6BCB77', '#4D96FF', '#D84A51']
angle_step = 360 / len(colors)
for i, color in enumerate(colors):
    start = i * angle_step
    end = start + angle_step
    draw.pieslice([(50, 50), (250, 250)], start, end, fill=color, outline='black', width=2)
img.save('/home/runner/workspace/images/cQc9WWa.png')

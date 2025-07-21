from PIL import Image, ImageDraw, ImageFont
import os

# Create placeholder images
images = [
    ('hero-campus.jpg', 'St. Mary\'s Campus'),
    ('elementary-students.jpg', 'Elementary Students'),
    ('middle-school-students.jpg', 'Middle School Students'),
    ('high-school-students.jpg', 'High School Students'),
    ('students-learning.jpg', 'Students Learning'),
    ('athletics.jpg', 'Athletics Program'),
    ('arts-program.jpg', 'Arts Program'),
    ('student-activities.jpg', 'Student Activities'),
    ('service-learning.jpg', 'Service Learning')
]

for filename, text in images:
    # Create image
    img = Image.new('RGB', (800, 600), color='#1E3A8A')
    draw = ImageDraw.Draw(img)
    
    # Try to use a font, fallback to default if not available
    try:
        font = ImageFont.truetype('/System/Library/Fonts/Arial.ttf', 40)
        small_font = ImageFont.truetype('/System/Library/Fonts/Arial.ttf', 24)
    except:
        font = ImageFont.load_default()
        small_font = ImageFont.load_default()
    
    # Add gradient effect by drawing rectangles with varying opacity
    for i in range(600):
        alpha = int(255 * (1 - i/600))
        color = (196, 30, 58, alpha)  # Red with varying alpha
        draw.rectangle([(0, i), (800, i+1)], fill=(196, 30, 58))
    
    # Add text
    draw.text((400, 250), "St. Mary's Academy", fill='white', font=font, anchor='mm')
    draw.text((400, 350), text, fill='white', font=small_font, anchor='mm')
    
    # Save image
    img.save(filename)
    print(f"Created {filename}")

print("All placeholder images created!")
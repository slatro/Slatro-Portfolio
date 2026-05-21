import sys
from PIL import Image, ImageDraw

def create_glowing_favicon(profile_path, output_path, size=512):
    # 1. Load and crop profile image to square
    try:
        im = Image.open(profile_path).convert("RGBA")
    except Exception as e:
        print(f"Error opening image: {e}")
        sys.exit(1)
        
    width, height = im.size
    min_dim = min(width, height)
    left = (width - min_dim) / 2
    top = (height - min_dim) / 2
    right = (width + min_dim) / 2
    bottom = (height + min_dim) / 2
    im_cropped = im.crop((left, top, right, bottom))
    im_resized = im_cropped.resize((size, size), Image.Resampling.LANCZOS)
    
    # 2. Create base canvas with transparency
    canvas = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    
    # 3. Create gradient background
    # Emerald: #10b981 -> RGB(16, 185, 129)
    # Cyan: #06b6d4 -> RGB(6, 182, 212)
    gradient = Image.new("RGBA", (size, size))
    draw_grad = ImageDraw.Draw(gradient)
    
    # Linear gradient along the diagonal (from bottom-left to top-right)
    for y in range(size):
        for x in range(size):
            # Calculate interpolation factor along diagonal
            # (0, size) is bottom-left, (size, 0) is top-right
            # Projection of point (x, y) onto the diagonal vector (size, -size)
            # normalized factor from 0 to 1
            factor = (x + (size - y)) / (2 * size)
            factor = max(0.0, min(1.0, factor))
            
            r = int(16 + (6 - 16) * factor)
            g = int(185 + (182 - 185) * factor)
            b = int(129 + (212 - 129) * factor)
            gradient.putpixel((x, y), (r, g, b, 255))
            
    # 4. Create mask for outer rounded square
    # Outer radius is 20% of size (e.g. 100px for 512)
    outer_radius = int(size * 0.20)
    outer_mask = Image.new("L", (size, size), 0)
    draw_outer = ImageDraw.Draw(outer_mask)
    draw_outer.rounded_rectangle([0, 0, size, size], radius=outer_radius, fill=255)
    
    # Apply outer mask to gradient
    glowing_border = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    glowing_border.paste(gradient, (0, 0), mask=outer_mask)
    
    # 5. Create mask for inner rounded square
    # Inset is about 4% of size (e.g. 20px for 512)
    inset = int(size * 0.04)
    inner_size = size - 2 * inset
    inner_radius = int(inner_size * 0.16) # rounded-[10px] is slightly less rounded than the outer [12px]
    
    inner_mask = Image.new("L", (inner_size, inner_size), 0)
    draw_inner = ImageDraw.Draw(inner_mask)
    draw_inner.rounded_rectangle([0, 0, inner_size, inner_size], radius=inner_radius, fill=255)
    
    # Resize profile image to fit the inset
    im_inner = im_resized.resize((inner_size, inner_size), Image.Resampling.LANCZOS)
    
    # Paste inner image onto glowing_border using the inner mask
    glowing_border.paste(im_inner, (inset, inset), mask=inner_mask)
    
    # Save the resulting image
    glowing_border.save(output_path, "PNG")
    print(f"Successfully created glowing favicon at {output_path}")

if __name__ == "__main__":
    create_glowing_favicon("profile.jpg", "favicon.png")

from PIL import Image, ImageDraw, ImageFont


def create_meme(image_path, text, output_path, font_size=40):
    # Открываем изображение
    img = Image.open(image_path)
    # Создаем объект для рисования
    draw = ImageDraw.Draw(img)

    # Загружаем пользовательский шрифт (например, Arial) с указанным размером
    try:
        font = ImageFont.truetype("arial.ttf", font_size)  # Укажите путь к вашему шрифту
    except IOError:
        print("Шрифт не найден, используется стандартный шрифт.")
        font = ImageFont.load_default()

    # Рассчитываем позицию текста (центр)
    left, top, right, bottom = draw.textbbox((0, 0), text, font=font)
    text_width = right - left
    text_height = bottom - top

    x = (img.width - text_width) / 2
    y = img.height - text_height - 20

    # Рисуем текст
    draw.text((x, y), text, font=font, fill="white")

    # Сохраняем результат
    img.save(output_path)


if __name__ == "__main__":
    create_meme(r"pics/cat.jpg", "Hello World", "meme.jpg", font_size=120)
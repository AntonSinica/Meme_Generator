from PIL import Image, ImageDraw, ImageFont
import argparse


def create_meme(image_path, text, output_path,
                font_path="arial.ttf", font_size=40,
                color="white", position="bottom"):
    # Открываем изображение
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)

    # Загружаем шрифт
    try:
        font = ImageFont.truetype(font_path, font_size)
    except IOError:
        print(f"Шрифт {font_path} не найден, используется стандартный.")
        font = ImageFont.load_default()

    # Рассчитываем размер текста
    left, top, right, bottom = draw.textbbox((0, 0), text, font=font)
    text_width = right - left
    text_height = bottom - top

    # Определяем позицию
    if position == "top":
        x = (img.width - text_width) / 2
        y = 20
    elif position == "center":
        x = (img.width - text_width) / 2
        y = (img.height - text_height) / 2
    else:  # bottom
        x = (img.width - text_width) / 2
        y = img.height - text_height - 20

    # Рисуем текст
    draw.text((x, y), text, font=font, fill=color)

    # Сохраняем результат
    img.save(output_path)


def main():
    parser = argparse.ArgumentParser(description="Генератор мемов")
    parser.add_argument("--image", required=True, help="Путь к исходному изображению")
    parser.add_argument("--text", required=True, help="Текст для мема")
    parser.add_argument("--output", required=True, help="Путь для сохранения")
    parser.add_argument("--font", default="arial.ttf", help="Путь к файлу шрифта (.ttf)")
    parser.add_argument("--font_size", type=int, default=40, help="Размер шрифта (по умолчанию: 40)")
    parser.add_argument("--color", default="white", help="Цвет текста (название или HEX)")
    parser.add_argument("--position", choices=["top", "center", "bottom"],
                        default="bottom", help="Позиция текста")

    args = parser.parse_args()

    try:
        create_meme(
            image_path=args.image,
            text=args.text,
            output_path=args.output,
            font_path=args.font,
            font_size=args.font_size,
            color=args.color,
            position=args.position
        )
        print("Мем успешно создан!")
    except Exception as e:
        print(f"Ошибка: {str(e)}")


if __name__ == "__main__":
    main()

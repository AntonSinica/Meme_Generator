from PIL import Image, ImageDraw, ImageFont
import argparse


def create_meme(image_path, text, output_path, font_size=40):
    # Открываем изображение
    img = Image.open(image_path)
    # Создаем объект для рисования
    draw = ImageDraw.Draw(img)

    # Загружаем пользовательский шрифт
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except IOError:
        print("Шрифт не найден, используется стандартный шрифт.")
        font = ImageFont.load_default()

    # Рассчитываем позицию текста
    left, top, right, bottom = draw.textbbox((0, 0), text, font=font)
    text_width = right - left
    text_height = bottom - top

    x = (img.width - text_width) / 2
    y = img.height - text_height - 20

    # Рисуем текст
    draw.text((x, y), text, font=font, fill="white")

    # Сохраняем результат
    img.save(output_path)


def main():
    parser = argparse.ArgumentParser(description="Генератор мемов")
    parser.add_argument("--image", required=True, help="Путь к исходному изображению")
    parser.add_argument("--text", required=True, help="Текст для мема")
    parser.add_argument("--output", required=True, help="Путь для сохранения результата")
    parser.add_argument("--font_size", type=int, default=40, help="Размер шрифта (по умолчанию: 40)")

    args = parser.parse_args()

    try:
        create_meme(
            image_path=args.image,
            text=args.text,
            output_path=args.output,
            font_size=args.font_size
        )
        print("Мем успешно создан!")
    except Exception as e:
        print(f"Ошибка: {str(e)}")


if __name__ == "__main__":
    main()

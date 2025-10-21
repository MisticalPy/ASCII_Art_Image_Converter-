from PIL import Image
import os

# ASCII символы, используемые для построения ASCII-арта
ASCII_CHAR = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]


class Convert_img:
    def __init__(self):
        self.original_image = None
        self.original_image_filename = None
        self.ascii_text = None

    def resize_img(self, image, new_width=100):
        """Вычисляем высоту и ширину уменьшенного изображения, сохраняя соотношение сторон"""
        width, height = image.size
        ratio = height / width
        new_height = int(new_width * ratio)
        resized_img = image.resize((new_width, new_height-50))
        return resized_img

    def pixel_to_grayscale(self, image):
        """Преобразование изображения в оттенки серого"""
        grayscale_img = image.convert("L")
        return grayscale_img

    # Сопоставление каждого пикселя с соответствующим ASCII-символом. Метод pixel_to_ascii принимает изображение
    # в оттенках серого и извлекает данные о пикселях с помощью метода getdata().
    # Затем для каждого пикселя вычисляется индекс в списке ASCII_CHAR,
    # который зависит от его яркости. Этот список содержит символы,
    # отражающие различные уровни яркости, начиная от самых темных (@) до самых светлых (.)
    # Для вычисления индекса яркость пикселя делится на 25 (поскольку в списке ASCII_CHAR 25 символов,
    # каждый из которых представляет определенный диапазон яркости), и результат округляется вниз до ближайшего целого числа.
    # В результате получается строка, состоящая из ASCII-символов, представляющих исходное изображение.

    def pixel_to_ascii(self, image):
        # Преобразованиe пикселей изображения в ASCII символы
        pixels = image.getdata()
        characters = "".join(ASCII_CHAR[pixel // 25] for pixel in pixels)
        return characters

    def save_ascii_art(self):
        # Получаем путь к исходному изображению
        original_image_path = self.original_image_filename
        # Извлекаем имя файла без расширения
        original_filename = os.path.splitext(
            os.path.basename(original_image_path))[0]
        # Создаем путь для сохранения ASCII-арта, используя имя исходного файла
        ascii_art_path = os.path.join(os.path.dirname(
            original_image_path), f"{original_filename}_ascii.txt")

        # Сохраняем ASCII-арт в файл
        with open(ascii_art_path, "w") as file:
            ascii_art = self.ascii_text
            file.write(ascii_art)
            print(f"ASCII-арт сохранен в файл: {ascii_art_path}")

    def convert_to_ascii(self, file_path, new_width=100) -> str:
        """Конвертация изображения в ASCII-арт. Метод convert_to_ascii объединяет предыдущие три шага
        sначала изображение уменьшается до желаемого размера, затем преобразуется в оттенки
        серого и, наконец, каждый пиксель преобразуется в ASCII-символ. Полученная строка
        ASCII-символов форматируется так, чтобы каждый символ соответствовал одному
        пикселю исходного изображения, и разбивается на строки с заданной шириной.
        """
        self.original_image_filename = file_path
        self.original_image = Image.open(file_path)
        grayscale_image = self.pixel_to_grayscale(
            self.resize_img(self.original_image))
        new_image_data = self.pixel_to_ascii(grayscale_image)
        pixel_nb = len(new_image_data)
        ascii_img = "\n".join(
            new_image_data[i: i + new_width] for i in range(0, pixel_nb, new_width))
        self.ascii_text = ascii_img

        self.save_ascii_art()
        return ascii_img


app = Convert_img()
res = app.convert_to_ascii(
    '/home/misticalpy/Desktop/my_project_with_aio_script/ASCII_Art_Image_Converter-/536be9b9c2e43f505e325e369b3b4909-no-bg-preview (carve.photos).png', 100)

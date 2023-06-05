from rembg import remove
from PIL import Image
from pathlib import Path

# основная функция для удаления фона в изображении
def remove_bg():
    list_exs = ['*.jpg', '*.png']   # список расширений, с которыми буду работать
    all_files = []    #создам пустой список, куда помещу пути изображений

    for exs in list_exs:
        all_files.extend(Path('/media/andrew/75A74AA74301978F/PycharmProjects/bgCleaner/Input images').glob(exs))    #добавляю изображения, пробегая по выбранным расширениям

    for index, item in enumerate(all_files):
        file_name = Path(item).stem   # получу имя каждого исходного файла (Path(item)) - адрес каждого файла

        output_path = f'/media/andrew/75A74AA74301978F/PycharmProjects/bgCleaner/Output images/{file_name}_ed.png' #сформирую путь для сохранения отредактированного файла (в .png)

        input_image = Image.open(Path(item))    #открываем исходное изображение
        output_image = remove(input_image)    #удаляем фон в изображении
        output_image.save(output_path)    #сохраняем отредактированный файл

        print(f'Completed: {index+1}/{len(all_files)}')    #сделаю информационный принт в терминале, чтобы выдеть ход работы скрипта


def main():
    remove_bg()

if __name__=='__main__':
    main()


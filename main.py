from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.config import Config

# Настройка размера окна для тестирования
Config.set('graphics', 'width', '720')
Config.set('graphics', 'height', '1280')


class MainApp(App):
    def build(self):
        # Создаем основной layout
        layout = FloatLayout()

        # Создаем кнопку
        button = Button(
            text='Люблю тебя!',
            size_hint=(0.3, 0.1),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            font_size=20
        )

        # Привязываем функцию к нажатию кнопки
        button.bind(on_press=self.on_button_click)

        # Добавляем кнопку в layout
        layout.add_widget(button)

        return layout

    def on_button_click(self, instance):
        print("Кнопка нажата!")
        instance.text = "Ага)"


if __name__ == '__main__':
    MainApp().run()

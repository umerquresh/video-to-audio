from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserListView
from moviepy.editor import VideoFileClip

class VideoToAudioApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        self.file_chooser = FileChooserListView(path='.', filters=['*.mp4'])
        self.extract_button = Button(text='Extract Audio', size_hint_y=None, height=50)
        self.extract_button.bind(on_press=self.extract_audio)

        layout.add_widget(Label(text='Video to Audio Converter'))
        layout.add_widget(self.file_chooser)
        layout.add_widget(self.extract_button)

        return layout

    def extract_audio(self, instance):
        selected_file = self.file_chooser.selection and self.file_chooser.selection[0]
        if selected_file:
            video_path = selected_file
            audio_path = video_path.replace('.mp4', '.mp3')

            try:
                video_clip = VideoFileClip(video_path)
                audio_clip = video_clip.audio
                audio_clip.write_audiofile(audio_path)
                audio_clip.close()
                video_clip.close()
                print("Audio extracted successfully!")
            except Exception as e:
                print("Error:", e)

if __name__ == '__main__':
    VideoToAudioApp().run()

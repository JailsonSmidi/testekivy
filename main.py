from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
import cv2
import face_recognition
from simple_facerec import SimpleFacerec

Builder.load_file('main.kv')

class Comp(BoxLayout):
    def reconhecimento(self):
        # Encode rostos a partir da pasta
        sfr = SimpleFacerec()
        sfr.load_encoding_images('db/')

        # Carrega a Camera
        cam = cv2.VideoCapture(0)

        while True:
            ret, frame = cam.read()

            # Detectar Rostos
            face_locations, face_names = sfr.detect_known_faces(frame)
            #for face_loc, name in zip(face_locations, face_names):
            #    y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

            #    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200))
            #    cv2.rectangle(frame, (x1, y2 + 20), (x2, y2), (0, 0, 200), -1)
            #    cv2.putText(frame, name, (x1, y2 + 15), cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 255, 255), 1)

            if len(face_locations) == 1:
                print(f'{face_names[0]} Reconhecido!')
                self.ids['label1'].text = face_names[0]
            elif len(face_locations) == 0:
                print('Nenhum rosto encontrado!')
            elif len(face_locations) > 1:
                print('Há mais de um rosto na imagem!')

            key = cv2.waitKey(1)
            if len(face_locations) == 1:
                break

        cam.release()


class Comparador(App):
    def build(self):
        return Comp()


Comparador().run()
from PySide6.QtWidgets import QWidget, QPushButton, QLabel, QLineEdit, QMessageBox, QHBoxLayout
from PySide6.QtGui import QPixmap, QFont, QFontDatabase, QIcon
from PySide6.QtCore import Qt,QSize
from thread_classe import VideoRead
from thread_classe import Recognition


class Home(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.user = None
        # Initialisation de la fenêtre
        self.setFixedSize(1200, 600)
        self.parent.set_win_title("Accueil")
         # Charger les polices depuis des fichiers
        semibold_id = QFontDatabase.addApplicationFont('fonts/Poppins/Poppins-SemiBold.ttf')
        italic_font_id = QFontDatabase.addApplicationFont('fonts/Poppins/Poppins-Italic.ttf')
        regular_font_id = QFontDatabase.addApplicationFont('fonts/Poppins/Poppins-Regular.ttf')
        medium_font_id = QFontDatabase.addApplicationFont('fonts/Poppins/Poppins-Medium.ttf')
        inter_font_id = QFontDatabase.addApplicationFont('fonts/Inter/Inter-Black.otf')

        # Récupérer les noms de famille des polices
        self.semibold_family = QFontDatabase.applicationFontFamilies(semibold_id)[0]
        self.italic_family = QFontDatabase.applicationFontFamilies(italic_font_id)[0]
        self.regular_family = QFontDatabase.applicationFontFamilies(regular_font_id)[0]
        self.medium_family = QFontDatabase.applicationFontFamilies(medium_font_id)[0]
        self.inter_family = QFontDatabase.applicationFontFamilies(inter_font_id)[0]


        # Définir l'image de fond
        back_view = QLabel(self)
        back_view.setPixmap(QPixmap("icons\\back_home.png").scaled(1200, 600))
        back_view.setGeometry(0, 0, 1200, 600)
        
        self.decoration()
        self.entry_info()

    def entry_info(self):
        # Créer un QHBoxLayout pour la disposition horizontale
        flex_direction_win = QHBoxLayout()
        flex_direction_win.setSpacing(50)
        flex_direction_win.setContentsMargins(5, 5, 5, 5)
        
        # Créer une nouvelle fenêtre (QWidget) pour contenir les éléments
        win = QWidget(self)
        win.setGeometry(202, 428, 343, 61)
        win.setStyleSheet("border-radius: 30px; background: rgba(255, 255, 255, 1);")
        
        # Champ email
        self.email = QLineEdit(win)
        self.email.setPlaceholderText("Email Adress")
        self.email.setFixedSize(213,44)
        self.email.setFont(QFont(self.inter_family,16))
        self.email.setStyleSheet("""
        QLineEdit {
            font-family: Poppins;
            background: transparent;
            font-size: 16px;
            border: none;
            color: rgba(0, 0, 0, 1); 
        }
        QLineEdit::placeholder {
            font-weight: 400px;
            line-height: 24px;
            text-align: left;
            color: rgba(0, 0, 0, 0.5);
        }
    """)

        # Bouton de soumission (submit)
        self.submit = QPushButton(win)
        self.submit.setIcon(QIcon("icons\\email.png"))
        self.submit.setIconSize(QSize(24,22)) 
        self.submit.setFixedSize(46,46)
        self.submit.setStyleSheet("""
            QPushButton {
                border-radius: 23px;
                background-color: rgba(57, 120, 242, 1);
            }
            QPushButton:pressed {
                background-color: rgba(57, 120, 242, 1);
            }
            QPushButton:hover {
                background-color: rgba(57, 120, 242, 0.5);
            }
        """)
        self.submit.clicked.connect(self.connection)
        self.submit.setCursor(Qt.PointingHandCursor)

        # Ajouter les widgets au layout
        flex_direction_win.addWidget(self.email)
        flex_direction_win.addWidget(self.submit)

        # Appliquer le layout à la fenêtre
        win.setLayout(flex_direction_win)
        

    def decoration(self):
        # Bouton "Commencer"
        self.btn_start = QPushButton("Get started", self)
        self.btn_start.setFont(QFont(self.medium_family, 16))
        self.btn_start.setStyleSheet("""
            font-family: Poppins;
            font-size: 16px;
            font-weight: 500px;
            line-height: 24px;
            text-align: center;
            color: rgba(255, 255, 255, 1);
            border-radius: 20px;
            background: rgba(57, 120, 242, 1);
        """)
        self.btn_start.setGeometry(973, 50, 145, 40)
       
        # Titre principal
        title = QLabel(self)
        title.setText("Silent Voice: Giving Signs\na Voice, Everyone Can\nHear.")
        title.setFont(QFont(self.semibold_family, 35, QFont.Weight.Bold))
        title.setGeometry(163, 186, 525, 140)
        title.setStyleSheet("""
            font-family: Poppins;
            font-size: 35px;
            font-weight: 600px;
            line-height: 50px;
            color: rgba(0, 0, 0, 1);
            background: transparent;
        """)
        
        # Sous-titre
        subtitle = QLabel(self)
        subtitle.setText("Breaking Barriers, Building Connections")
        subtitle.setFont(QFont(self.regular_family, 16))
        subtitle.setGeometry(163, 337, 312, 40)
        subtitle.setStyleSheet("""
            font-family: Poppins;
            font-size: 16px;
            font-weight: 400px;
            line-height: 50px;
            color: rgba(0, 0, 0, 1);
            background: transparent;
        """)

        # Logo
        logo = QLabel(self)
        logo.setText('<span style="color: black;">SVOICE</span><span style="color:#FD7E41;">.</span>')
        logo.setFont(QFont(self.inter_family, 16, QFont.Weight.Bold))
        logo.setGeometry(93, 58, 139, 48)
        logo.setStyleSheet("""
            font-family: Inter;
            font-size: 24px;
            font-weight: 900px;
            line-height: 29.05px;
            text-align: left;
            color: rgba(0, 0, 0, 1);
            background: transparent;
        """)
        
        # Label d'informations
        label_info = QLabel(self)
        label_info.setText("WHERE SILENCE MEETS UNDERSTANDING")
        label_info.setFont(QFont(self.semibold_family, 12, QFont.Weight.Bold))
        label_info.setGeometry(163, 151, 379, 18)
        label_info.setStyleSheet("""
            font-family: Poppins;
            font-size: 12px;
            font-weight: 600px;
            line-height: 18px;
            background: transparent;
            color: rgba(51, 154, 103, 1);
        """)
        
        # Texte "I love you !"
        sign = QLabel(self)
        sign.setText("I love you !")
        sign.setFont(QFont(self.italic_family, 18))
        sign.setGeometry(714, 171, 159, 54)
        sign.setStyleSheet("""
            background: transparent;
            color: rgba(0, 0, 0, 1);
            font-family: Poppins;
            font-size: 18px;
            font-style: italic;
            font-weight: 300px;
            line-height: 50px;
            text-align: center;
        """)
        sign.setAlignment(Qt.AlignCenter)
        
    
    def on_link_clicked(self):
        dashboard = Dashboard(self.parent)  # Correction de la création de l'objet Dashboard
        self.parent.setframe(dashboard)
        
    def connection(self):
        email = self.email.text().strip().lower()
        # Vérifier si l'email est fourni
        if not email:
            QMessageBox.warning(self, "Erreur", "Veuillez entrer un email valide.")
            return   
        self.on_link_clicked()
                
        



        
        
      

class Dashboard(QWidget):
    def __init__(self,parent):
        super().__init__()
        self.parent_root = parent
        # Initialisation de la fenêtre
        self.setFixedSize(1200, 600)
        
        # Charger les polices depuis des fichiers
        semibold_id = QFontDatabase.addApplicationFont('fonts/Poppins/Poppins-SemiBold.ttf')
        italic_font_id = QFontDatabase.addApplicationFont('fonts/Poppins/Poppins-Italic.ttf')
        regular_font_id = QFontDatabase.addApplicationFont('fonts/Poppins/Poppins-Regular.ttf')
        medium_font_id = QFontDatabase.addApplicationFont('fonts/Poppins/Poppins-Medium.ttf')
        inter_font_id = QFontDatabase.addApplicationFont('fonts/Inter/Inter-Black.otf')

        # Récupérer les noms de famille des polices
        self.semibold_family = QFontDatabase.applicationFontFamilies(semibold_id)[0]
        self.italic_family = QFontDatabase.applicationFontFamilies(italic_font_id)[0]
        self.regular_family = QFontDatabase.applicationFontFamilies(regular_font_id)[0]
        self.medium_family = QFontDatabase.applicationFontFamilies(medium_font_id)[0]
        self.inter_family = QFontDatabase.applicationFontFamilies(inter_font_id)[0]

        # Définir l'image de fond
        back_view = QLabel(self)
        back_view.setPixmap(QPixmap("icons\\back_info.png").scaled(1200, 600))
        back_view.setGeometry(0, 0, 1200, 600)
        
        self.decoration()
        self.start_video_view()
        
    def next_valide(self):
        try:
            page = SVoice(self.parent_root)
            #self.start_v.stop()
            self.parent_root.setframe(page)
        except Exception as e:
            QMessageBox.critical(self, "Erreur", f"Une erreur est survenue lors de la transition : {str(e)}")
            print(f"Erreur lors de la transition vers le widget suivant : {e}")

        

    def decoration(self):
        # Bouton "Commencer"
        self.btn_start = QPushButton("Start Learning ASL", self)
        self.btn_start.clicked.connect(self.next_valide)
        self.btn_start.setFont(QFont(self.medium_family, 16))
        self.btn_start.setStyleSheet("""
            QPushButton {
            font-family: Poppins;
            font-size: 16px;
            font-weight: 500px;
            line-height: 24px;
            text-align: center;
            color: rgba(255, 255, 255, 1);
            border-radius: 25px;
            background: rgba(57, 120, 242, 1);
            }
            QPushButton:pressed {
                background-color: rgba(57, 120, 242, 1);
            }
            QPushButton:hover {
                background-color: rgba(57, 120, 242, 0.5);
            }
        """)
        self.btn_start.setGeometry(846, 106, 206, 50)
       
        # Titre principal
        title = QLabel(self)
        title.setText("Breaking communication barriers by teaching sign language\nthrough gesture imitation, with validation each time the gesture is\ncorrectly performed, making conversations accessible and\nseamless for everyone.")
        title.setFont(QFont(self.semibold_family, 20,QFont.Weight.Bold))
        title.setGeometry(116, 195, 667, 114)
        title.setStyleSheet("""
            font-family: Poppins;
            font-size: 20px;
            font-weight: 400px;
            line-height: 35px;
            color: rgba(108, 104, 104, 1);
            background: transparent;
        """)

        # Logo
        logo = QLabel(self)
        logo.setText('<span style="color: black;">SVOICE</span><span style="color:#FD7E41;">.</span>')
        logo.setFont(QFont(self.inter_family, 16, QFont.Weight.Bold))
        logo.setGeometry(93, 58, 139, 48)
        logo.setStyleSheet("""
            font-family: Inter;
            font-size: 24px;
            font-weight: 900px;
            line-height: 29.05px;
            text-align: left;
            color: rgba(0, 0, 0, 1);
            background: transparent;
        """)

        # How
        How = QLabel(self)
        How.setText("How it works")
        How.setFont(QFont(self.regular_family, 24))
        How.setGeometry(116, 330, 207, 57)
        How.setStyleSheet("""
            background: transparent;
            color: rgba(0, 0, 0, 1);
            font-family: Poppins;
            font-size: 24px;
            font-weight: 600;
            line-height: 35px;
            text-align: left;
        """)

        # Mission
        mission = QLabel(self)
        mission.setText("Our Mission")
        mission.setFont(QFont(self.semibold_family, 24, QFont.Weight.Bold))
        mission.setGeometry(116, 137, 207, 57)
        mission.setStyleSheet("""
            background: transparent;
            color: rgba(0, 0, 0, 1);
            font-family: Poppins;
            font-size: 24px;
            font-weight: 600;
            line-height: 35px;
            text-align: left;
        """)

        # Texte "Recognition"
        r_c = QLabel(self)
        r_c.setText("Recognition")
        r_c.setFont(QFont(self.italic_family, 15))
        r_c.setGeometry(195, 423, 113, 31)
        r_c.setStyleSheet("""
            background: transparent;
            color: rgba(0, 0, 0, 1);
            font-family: Poppins;
            font-size: 15px;
            font-weight: 500;
            line-height: 35px;
            text-align: left;
        """)

        # Texte "Interpretation"
        int_er = QLabel(self)
        int_er.setText("Interpretation")
        int_er.setFont(QFont(self.italic_family, 15))
        int_er.setGeometry(431, 423, 113, 31)
        int_er.setStyleSheet("""
            background: transparent;
            color: rgba(0, 0, 0, 1);
            font-family: Poppins;
            font-size: 15px;
            font-weight: 500;
            line-height: 35px;
            text-align: left;
        """)

        # Texte "Output"
        utpu = QLabel(self)
        utpu.setText("Output")
        utpu.setFont(QFont(self.italic_family, 15))
        utpu.setGeometry(663, 423, 113, 31)
        utpu.setStyleSheet("""
            background: transparent;
            color: rgba(0, 0, 0, 1);
            font-family: Poppins;
            font-size: 15px;
            font-weight: 500;
            line-height: 35px;
            text-align: left;
        """)

        # Texte "Real-time gesture capture"
        c_a = QLabel(self)
        c_a.setText("Real-time gesture capture")
        c_a.setFont(QFont(self.italic_family, 13))
        c_a.setGeometry(136, 472, 184, 53)
        c_a.setStyleSheet("""
            background: transparent;
            color: rgba(108, 104, 104, 1);
            font-family: Poppins;
            font-size: 13px;
            font-weight: 400;
            line-height: 35px;
        """)
        c_a.setAlignment(Qt.AlignCenter)

        # Texte "AI-powered ASL processing"
        a_p = QLabel(self)
        a_p.setText("AI-powered ASL processing")
        a_p.setFont(QFont(self.italic_family, 13))
        a_p.setGeometry(367, 472, 186, 53)
        a_p.setStyleSheet("""
            background: transparent;
            color: rgba(108, 104, 104, 1);
            font-family: Poppins;
            font-size: 13px;
            font-weight: 400;
            line-height: 35px;
        """)
        a_p.setAlignment(Qt.AlignCenter)

        # Texte "Instant voice generation"
        T_v = QLabel(self)
        T_v.setText("Instant voice Detection")
        T_v.setFont(QFont(self.italic_family, 13))
        T_v.setGeometry(607, 472, 176, 53)
        T_v.setStyleSheet("""
            background: transparent;
            color: rgba(108, 104, 104, 1);
            font-family: Poppins;
            font-size: 13px;
            font-weight: 400;
            line-height: 35px;
        """)
        T_v.setAlignment(Qt.AlignCenter)

    def start_video_view(self):
        # Afficher la vidéo
        self.video_view = QLabel(self)
        self.video_view.setGeometry(775, 220, 395, 363)
        self.video_view.setAlignment(Qt.AlignCenter)
        
        self.start_v = VideoRead()
        self.start_v.video_signal.connect(self.update_video_View)  # Correction du nom de la méthode
        self.start_v.start()

    def update_video_View(self, frame):
        pixmap = QPixmap.fromImage(frame)  # Convertir le frame en pixmap si nécessaire
        self.video_view.setPixmap(pixmap)  # Afficher l'image dans la QLabel

    def closeEvent(self, event):
        """S'arrête proprement lorsque la fenêtre est fermée."""
        if self.start_v.isRunning():
            self.start_v.stop()
            self.start_v.wait()






class SVoice(QWidget):
    def __init__(self,parent):
        super().__init__()
        self.parent = parent
        
        # Initialisation de la fenêtre
        self.setFixedSize(1200, 600)
        
        try:
            # Charger les polices depuis des fichiers
            semibold_id = QFontDatabase.addApplicationFont('fonts/Poppins/Poppins-SemiBold.ttf')
            italic_font_id = QFontDatabase.addApplicationFont('fonts/Poppins/Poppins-Italic.ttf')
            regular_font_id = QFontDatabase.addApplicationFont('fonts/Poppins/Poppins-Regular.ttf')
            medium_font_id = QFontDatabase.addApplicationFont('fonts/Poppins/Poppins-Medium.ttf')
            inter_font_id = QFontDatabase.addApplicationFont('fonts/Inter/Inter-Black.otf')

            # Récupérer les noms de famille des polices
            self.semibold_family = QFontDatabase.applicationFontFamilies(semibold_id)[0]
            self.italic_family = QFontDatabase.applicationFontFamilies(italic_font_id)[0]
            self.regular_family = QFontDatabase.applicationFontFamilies(regular_font_id)[0]
            self.medium_family = QFontDatabase.applicationFontFamilies(medium_font_id)[0]
            self.inter_family = QFontDatabase.applicationFontFamilies(inter_font_id)[0]
        except Exception as e:
            self.show_error("Font Loading Error", f"An error occurred while loading fonts: {str(e)}")
        
        try:
            # Définir l'image de fond
            back_view = QLabel(self)
            back_view.setPixmap(QPixmap("icons\\end_back.png").scaled(1200, 600))
            back_view.setGeometry(0, 0, 1200, 600)
        except Exception as e:
            self.show_error("Image Loading Error", f"An error occurred while loading the background image: {str(e)}")
        
        self.decoration()
        self.start_video_view()

    def decoration(self):
        try:

            # Bouton "Commencer"
            self.btn_start = QPushButton("Enable Camera",self)
            self.btn_start.setCursor(Qt.PointingHandCursor)
            self.btn_start.setFont(QFont(self.medium_family, 16))
            self.btn_start.setStyleSheet("""
            QPushButton {
                font-family: Poppins;
                font-size: 16px;
                font-weight: 600px;
                border-radius:20px;
                line-height: 24px;
                background:rgba(57, 120, 242, 1);
                color:rgba(255, 255, 255, 1);
            }
            QPushButton:pressed {
                background-color: rgba(57, 120, 242, 1);
            }
            QPushButton:hover {
                background-color: rgba(57, 120, 242, 0.5);
            }
        """)
            self.btn_start.setGeometry(755, 502, 170, 41)
            self.btn_start.clicked.connect(self.start_video)


            # Logo
            logo = QLabel(self)
            logo.setText('<span style="color: black;">SVOICE</span><span style="color:#FD7E41;">.</span>')
            logo.setFont(QFont(self.inter_family, 16, QFont.Weight.Bold))
            logo.setGeometry(93, 58, 139, 48)
            logo.setStyleSheet("""
                font-family: Inter;
                font-size: 24px;
                font-weight: 900px;
                line-height: 29.05px;
                text-align: left;
                color: rgba(0, 0, 0, 1);
                background: transparent;
            """) 
            
            
            sign = QLabel(self)
            sign.setPixmap(QPixmap("icons\\signs.png").scaled(391,291))
            sign.setGeometry(120,177,391,291)
            sign.setStyleSheet("""
                background: transparent;
            """)
            
            lsign = QLabel("List of Signs",self)
            lsign.setFont(QFont(self.semibold_family,20,QFont.Weight.Bold))
            lsign.setGeometry(120,127,174,35)
            lsign.setStyleSheet("""
                font-family: Poppins;
                font-size: 20px;
                font-weight: 600px;
                line-height: 30px;
                color: rgba(57, 120, 242, 1);
                background: transparent;
            """)
            lsign.setAlignment(Qt.AlignCenter)

           
        except Exception as e:
            self.show_error("Decoration Error", f"An error occurred during the UI decoration: {str(e)}")

    def start_video_view(self):
        try:
            # Afficher la vidéo
            self.video_view = QLabel(self)
            self.video_view.setPixmap(QPixmap("icons\\in_v_.png").scaled(42, 42))
            self.video_view.setGeometry(530, 111, 585, 366)
            self.video_view.setAlignment(Qt.AlignCenter)
            self.video_view.setStyleSheet("""
                background:rgba(252, 167, 66, 0.28);
                border-radius:20px;
                border:1px solid rgba(252, 167, 66, 1);
            """)
            self.demarre = False
        except Exception as e:
            self.show_error("Video View Error", f"An error occurred while initializing the video view: {str(e)}")

    def start_video(self):
        try:
            if self.demarre is False:
                self.start_v = Recognition()  # Assurez-vous que la classe Recognition est bien définie
                self.start_v.video_signal.connect(self.update_video_View)  # Connexion correcte du signal
                self.start_v.start()  # Démarre la vidéo
                self.demarre = True
                self.video_view.setStyleSheet("""
                background:transparent;
            """)
        except Exception as e:
            self.show_error("Video Start Error", f"An error occurred while starting the video: {str(e)}")

    def update_video_View(self, frame):
        try:
            # Convertir le frame en pixmap si nécessaire
            pixmap = QPixmap.fromImage(frame).scaled(585, 366)
            self.video_view.setPixmap(pixmap.scaled(self.video_view.size(), Qt.KeepAspectRatioByExpanding))
        except Exception as e:
            self.show_error("Video Update Error", f"An error occurred while updating the video frame: {str(e)}")

    def closeEvent(self, event):
        """S'arrête proprement lorsque la fenêtre est fermée."""
        try:
            if hasattr(self, 'start_v') and self.start_v.isRunning():
                self.start_v.stop()
                self.start_v.wait()
        except Exception as e:
            self.show_error("Close Event Error", f"An error occurred during the close event: {str(e)}")

    def show_error(self, title, message):
        """Affiche un message d'erreur à l'utilisateur."""
        QMessageBox.critical(self, title, message)



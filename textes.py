from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

Builder.load_file("textes.kv")


# ******************************************* Description Principale *****************************************


# ------------------------------------ Présentation Principale Fr En --------------------------------------------


class PresentationFr(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def description_appli_fr(self):
        return (
            "CETTE APPLICATION EST UNE VITRINE PROFESSIONNELLE DE MES COMPETENCES.\n\nELLE EXPLORE LES CONCEPTS CLES DES OUTILS "
            "D'APPLICATION MODERNES.\n\nDE LA FLEXIBILITE DES WIDGETS À LA PUISSANCE DES CANVAS, EN PASSANT PAR L'EFFICACITE DES LAYOUTS, "
            "TOUT CECI EST UN APERCU DU POTENTIEL DE KIVY ET PYTHON DANS LE DEVELOPPEMENT D'INTERFACES.\n\n"
            "APERCU QUI MET EN LUMIERE LES FONDAMENTAUX INDISPENSABLES AU CŒUR DES APPLICATIONS CONCUES AVEC LE FRAMEWORK KIVY, "
            "EN SYNERGIE AVEC LA FLEXIBILITE ET LA PUISSANCE DU LANGAGE DE PROGRAMMATION PYTHON.")


class PresentationEn(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def description_appli_en(self):
        return (
            "THIS APPLICATION IS A PROFESSIONAL SHOWCASE OF MY SKILLS.\n\nIT EXPLORES THE KEY CONCEPTS OF MODERN APPLICATION TOOLS. "
            "FROM THE FLEXIBILITY OF WIDGETS TO THE POWER OF CANVAS, PASSING THROUGH THE EFFICIENCY OF LAYOUTS, ALL THIS IS AN OVERVIEW "
            "OF THE POTENTIAL OF KIVY AND PYTHON IN INTERFACE DEVELOPMENT.\n\nAN OVERVIEW THAT HIGHLIGHTS THE ESSENTIALS AT THE HEART "
            "OF APPLICATIONS DESIGNED WITH THE KIVY FRAMEWORK, IN SYNERGY WITH THE FLEXIBILITY AND POWER OF THE PYTHON PROGRAMMING LANGUAGE.")


# *************************************************** Description du Layout Fr/En ***********************************************************


class LayoutDescriptionFr(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def layout_description_fr(self):
        return ("LES LAYOUTS DANS KIVY SONT DES CONTENEURS QUI ORGANISENT LES WIDGETS ENFANTS DANS UNE STRUCTURE"
                "PARTICULIERE À L'ECRAN.\n\nILS GERENT LA TAILLE, LA POSITION ET L'ORGANISATION DES WIDGETS INTERNES, PERMETTANT "
                "DE CREER DES INTERFACES UTILISATEUR COMPLEXES ET ADAPTATIVES.\n\nKIVY OFFRE PLUSIEURS TYPES DE LAYOUTS, CHACUN "
                "AVEC SA PROPRE STRATEGIE D'ORGANISATION :\n\n"

                "1. BOXLAYOUT :\n\nORGANISE LES WIDGETS EN LIGNE (HORIZONTALEMENT) OU EN COLONNE (VERTICALEMENT), EN FONCTION DE "
                "L'ORIENTATION SPECIFIEE.\n\n"

                "2. GRIDLAYOUT :\n\nDISPOSE LES WIDGETS DANS UNE GRILLE AVEC UN NOMBRE DEFINI DE COLONNES ET/OU DE LIGNES.\n\n"

                "3. ANCHORLAYOUT :\n\nPOSITIONNE LES WIDGETS ENFANTS A UN POINT D'ANCRAGE SPECIFIE (PAR EXEMPLE, HAUT GAUCHE, CENTRE, ETC.).\n\n"

                "4. FLOATLAYOUT :\n\nPERMET UNE DISPOSITION PLUS LIBRE DES WIDGETS, EN UTILISANT DES COORDONNEES RELATIVES OU ABSOLUES POUR "
                "LEUR POSITIONNEMENT.\n\n"

                "5. STACKLAYOUT :\n\nEMPILE LES WIDGETS DE MANIERE HORIZONTALE OU VERTICALE, EN PASSANT A LA LIGNE OU A LA COLONNE SUIVANTE UNE "
                "FOIS L'ESPACE DISPONIBLE REMPLI.\n\n"

                "6. RELATIVELAYOUT :\n\nSEMBLABLE A FLOATLAYOUT MAIS LES POSITIONS DES WIDGETS ENFANTS SONT RELATIVES A LA POSITION DU LAYOUT LUI-MEME.\n\n"

                "7. PAGELAYOUT :\n\nPERMET DE CREER DES INTERFACES À PLUSIEURS PAGES, OU CHAQUE ENFANT DU LAYOUT REPRESENTE UNE PAGE DISTINCTE.\n\n"

                "CHAQUE LAYOUT OFFRE DES PROPRIETES ET OPTIONS DE CONFIGURATION POUR AFFINER L'ARRANGEMENT DES WIDGETS ENFANTS, "
                "COMME L'ESPACEMENT ENTRE LES WIDGETS, L'ALIGNEMENT, LA TAILLE DES WIDGETS PAR RAPPORT AU CONTENEUR, ETC.\n\n"
                "EN COMBINANT ET EN IMBRIQUANT DIFFERENTS LAYOUTS, VOUS POUVEZ CREER DES INTERFACES UTILISATEUR RICHES ET ADAPTEES "
                "A DIVERS APPAREILS ET ORIENTATIONS D'ECRAN.")


class LayoutDescriptionEn(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def layout_description_en(self):
        return ("LAYOUTS IN KIVY ARE CONTAINERS THAT ORGANIZE CHILD WIDGETS IN A STRUCTURE "
                "SPECIFIC TO THE SCREEN.\n\nTHEY MANAGE THE SIZE, POSITION, AND ORGANIZATION OF INTERNAL WIDGETS, ALLOWING FOR "
                "CREATION OF COMPLEX AND ADAPTIVE USER INTERFACES.\n\nKIVY OFFERS SEVERAL TYPES OF LAYOUTS, EACH "
                "WITH ITS OWN ORGANIZATION STRATEGY:\n\n"

                "1. BOXLAYOUT :\n\nORGANIZES WIDGETS IN A ROW (HORIZONTALLY) OR IN A COLUMN (VERTICALLY), BASED ON "
                "THE SPECIFIED ORIENTATION.\n\n"

                "2. GRIDLAYOUT :\n\nARRANGES WIDGETS IN A GRID WITH A DEFINED NUMBER OF COLUMNS AND/OR ROWS.\n\n"

                "3. ANCHORLAYOUT :\n\nPOSITIONS CHILD WIDGETS AT A SPECIFIED ANCHOR POINT (E.G., TOP LEFT, CENTER, ETC.).\n\n"

                "4. FLOATLAYOUT :\n\nALLOWS A MORE FREELY ARRANGED WIDGETS, USING RELATIVE OR ABSOLUTE COORDINATES FOR "
                "THEIR PLACEMENT.\n\n"

                "5. STACKLAYOUT :\n\nSTACKS WIDGETS HORIZONTALLY OR VERTICALLY, MOVING TO THE NEXT ROW OR COLUMN ONCE "
                "AVAILABLE SPACE IS FILLED.\n\n"

                "6. RELATIVELAYOUT :\n\nSIMILAR TO FLOATLAYOUT, BUT CHILD WIDGETS POSITIONS ARE RELATIVE TO THE LAYOUT ITSELF.\n\n"

                "7. PAGELAYOUT :\n\nENABLES CREATION OF MULTI-PAGE INTERFACES, WHERE EACH LAYOUT CHILD REPRESENTS A DISTINCT PAGE.\n\n"

                "EACH LAYOUT OFFERS PROPERTIES AND CONFIGURATION OPTIONS TO FINE-TUNE THE ARRANGEMENT OF CHILD WIDGETS, "
                "SUCH AS SPACING BETWEEN WIDGETS, ALIGNMENT, WIDGET SIZE RELATIVE TO THE CONTAINER, ETC.\n\n"
                "BY COMBINING AND NESTING DIFFERENT LAYOUTS, YOU CAN CREATE RICH AND ADAPTIVE USER INTERFACES "
                "FOR VARIOUS DEVICES AND SCREEN ORIENTATIONS.")


# *************************************************** Description du Widget Fr/En ***********************************************************

class WidgetDescriptionFr(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def widget_description_fr(self):
        return (
            "LES WIDGETS DANS KIVY REPRESENTENT LES ELEMENTS DE BASE DE L'INTERFACE UTILISATEUR, TELS QUE LES BOUTONS, LES ETIQUETTES (LABELS), "
            "LES IMAGES, ETC.\n\nCHAQUE WIDGET DANS KIVY EST CONCU POUR UNE FONCTION SPECIFIQUE ET PEUT ETRE PERSONNALISE AVEC DIVERSES PROPRIETES "
            "TELLES QUE LA TAILLE, LA COULEUR, LE TEXTE ET LES REACTIONS AUX EVENEMENTS UTILISATEUR.\n\nVOICI QUELQUES EXEMPLES COURANTS DE WIDGETS "
            "DANS KIVY :\n\n"

            "1. BUTTON :\n\nUN CONTROLE INTERACTIF QUI PEUT DETECTER LES CLICS OU LES TOUCHES.\n\n"
            "2. LABEL :\n\nUTILISATION POUR AFFICHER DU TEXTE OU DES ICONES.\n\n"
            "3. TEXTINPUT :\n\nPERMET LA SAISIE DE TEXTE PAR L'UTILISATEUR.\n\n"
            "4. IMAGE :\n\nAFFICHE UNE IMAGE.\n\n"
            "5. SLIDER :\n\nUN CURSEUR QUI PERMET A L'UTILISATEUR DE CHOISIR UNE VALEUR DANS UNE PLAGE DEFINIE.\n\n"
            "6. CHECKBOX :\n\nPERMET À L'UTILISATEUR DE FAIRE UN CHOIX BINAIRE, COMME VRAI OU FAUX.\n\n"
            "7. CANVAS :\n\nUNE ZONE DE DESSIN POUR LES GRAPHIQUES PERSONNALISES.\n\n"

            "LES WIDGETS PEUVENT ETRE IMBRIQUES, PERMETTANT LA CREATION D'INTERFACES COMPLEXES.\n\nILS PEUVENT EGALEMENT INTERAGIR AVEC LES LAYOUTS "
            "POUR ORGANISER L'INTERFACE UTILISATEUR DE MANIERE LOGIQUE ET ESTHETIQUE.\n\nKIVY PERMET UNE GRANDE FLEXIBILITE DANS LA PERSONNALISATION "
            "DES WIDGETS, OFFRANT AINSI LA POSSIBILITE DE CREER DES INTERFACES UTILISATEUR UNIQUES ET ATTRAYANTES.\n\n")


class WidgetDescriptionEn(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def widget_description_en(self):
        return (
            "WIDGETS IN KIVY REPRESENT THE BASIC ELEMENTS OF THE USER INTERFACE, SUCH AS BUTTONS, LABELS, IMAGES, ETC.\n\nEACH WIDGET "
            "IN KIVY IS DESIGNED FOR A SPECIFIC FUNCTION AND CAN BE CUSTOMIZED WITH VARIOUS PROPERTIES SUCH AS SIZE, COLOR, TEXT, "
            "AND RESPONSES TO USER EVENTS.\n\nHERE ARE SOME COMMON EXAMPLES OF WIDGETS IN KIVY:\n\n"

            "1. BUTTON :\n\nAN INTERACTIVE CONTROL THAT CAN DETECT CLICKS OR TAPS.\n\n"

            "2. LABEL :\n\nUSED TO DISPLAY TEXT OR ICONS.\n\n"

            "3. TEXTINPUT :\n\nALLOWS TEXT INPUT FROM THE USER.\n\n"

            "4. IMAGE :\n\nDISPLAYS AN IMAGE.\n\n"

            "5. SLIDER :\n\nA SLIDER THAT LETS THE USER CHOOSE A VALUE WITHIN A DEFINED RANGE.\n\n"

            "6. CHECKBOX :\n\nALLOWS THE USER TO MAKE A BINARY CHOICE, LIKE TRUE OR FALSE.\n\n"

            "7. CANVAS :\n\nA DRAWING AREA FOR CUSTOM GRAPHICS.\n\n"

            "WIDGETS CAN BE NESTED, ALLOWING FOR THE CREATION OF COMPLEX INTERFACES.\n\nTHEY CAN ALSO INTERACT WITH LAYOUTS TO ORGANIZE "
            "THE USER INTERFACE IN A LOGICAL AND AESTHETICALLY PLEASING MANNER.\n\nKIVY PROVIDES GREAT FLEXIBILITY IN CUSTOMIZING WIDGETS, "
            "THUS OFFERING THE ABILITY TO CREATE UNIQUE AND ATTRACTIVE USER INTERFACES.")


# ********************************************************* Description de Canevas Fr/En **********************************************************************


class CanevasDescriptionFr(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def canvas_description_fr(self):
        return (
            "LE CANEVAS DANS KIVY EST UNE ZONE DE DESSIN QUI PERMET DE CRÉER DES GRAPHIQUES PERSONNALISÉS AU SEIN DES WIDGETS.\n\n"

            "IL SERT DE BASE POUR LA MANIPULATION GRAPHIQUE ET OFFRE UNE VARIÉTÉ D'INSTRUCTIONS POUR LE DESSIN, COMME LES LIGNES, "
            "LES FORMES GÉOMÉTRIQUES, LES TEXTURES, ET PLUS ENCORE.\n\nVOICI QUELQUES ASPECTS CLÉS DU CANEVAS DANS KIVY :\n\n"

            "1. INSTRUCTIONS DE DESSIN :\n\nLE CANEVAS FOURNIT DES INSTRUCTIONS TELLES QUE `RECTANGLE`, `LINE`, `ELLIPSE`, `TRIANGLE`, "
            "PERMETTANT DE DESSINER DIVERSES FORMES.\n\n"

            "2. GROUPES DE CANEVAS :\n\nPERMET D'ORGANISER LES INSTRUCTIONS DE DESSIN EN GROUPES POUR UN CONTRÔLE PLUS FACILE, PAR EXEMPLE, "
            "POUR METTRE À JOUR OU SUPPRIMER UN GROUPE D'INSTRUCTIONS ENSEMBLE.\n\n"

            "3. TRANSFORMATION :\n\nLE CANEVAS SUPPORTE LES TRANSFORMATIONS, Y COMPRIS LA TRANSLATION, LA ROTATION ET L'ÉCHELLE, PERMETTANT "
            "DE MODIFIER L'ASPECT DES ÉLÉMENTS DESSINÉS.\n\n"

            "4. BINDING :\n\nLES INSTRUCTIONS DE DESSIN PEUVENT ÊTRE LIÉES À DES PROPRIÉTÉS DE WIDGETS, PERMETTANT DES MISES À JOUR DYNAMIQUES "
            "LORSQUE LES PROPRIÉTÉS CHANGENT.\n\n"

            "LE CANEVAS EST PARTICULIÈREMENT UTILE POUR CRÉER DES INTERFACES UTILISATEUR PERSONNALISÉES, DES ANIMATIONS, DES JEUX, ET "
            "TOUT CONTENU GRAPHIQUE INTERACTIF. GRÂCE À SA FLEXIBILITÉ ET SA PUISSANCE, LE CANEVAS EST UN OUTIL ESSENTIEL DANS LA BOÎTE "
            "À OUTILS DE KIVY.\n\n")


class CanevasDescriptionEn(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def canvas_description_en(self):
        return (
            "THE CANVAS IN KIVY IS A DRAWING AREA THAT ALLOWS FOR THE CREATION OF CUSTOM GRAPHICS WITHIN WIDGETS.\n\nIT SERVES AS A FOUNDATION "
            "FOR GRAPHICAL MANIPULATION AND OFFERS A VARIETY OF DRAWING INSTRUCTIONS, SUCH AS LINES, GEOMETRIC SHAPES, TEXTURES, AND MORE.\n\n"
            "HERE ARE SOME KEY ASPECTS OF THE CANVAS IN KIVY:\n\n"

            "[u]1. DRAWING INSTRUCTIONS:[/u]\nTHE CANVAS PROVIDES INSTRUCTIONS LIKE `RECTANGLE`, `LINE`, `ELLIPSE`, `TRIANGLE`, "
            "ALLOWING THE DRAWING OF VARIOUS SHAPES.\n\n"

            "2. CANVAS GROUPS:\n\nALLOWS FOR ORGANIZING DRAWING INSTRUCTIONS INTO GROUPS FOR EASIER CONTROL, FOR EXAMPLE, "
            "TO UPDATE OR REMOVE A GROUP OF INSTRUCTIONS TOGETHER.\n\n"

            "3. TRANSFORMATION:\n\nTHE CANVAS SUPPORTS TRANSFORMATIONS, INCLUDING TRANSLATION, ROTATION, AND SCALING, ALLOWING "
            "FOR MODIFICATIONS TO THE APPEARANCE OF DRAWN ELEMENTS.\n\n"

            "4. BINDING:\n\nDRAWING INSTRUCTIONS CAN BE BOUND TO WIDGET PROPERTIES, ENABLING DYNAMIC UPDATES WHEN PROPERTIES CHANGE.\n\n"

            "THE CANVAS IS PARTICULARLY USEFUL FOR CREATING CUSTOMIZED USER INTERFACES, ANIMATIONS, GAMES, AND ANY INTERACTIVE "
            "GRAPHICAL CONTENT. WITH ITS FLEXIBILITY AND POWER, THE CANVAS IS AN ESSENTIAL TOOL IN THE KIVY TOOLKIT.")
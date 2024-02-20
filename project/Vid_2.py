##############################################################################################################
######################################Acceptors & Transducers#################################################
##############################################################################################################


##############################################################################################################
#############################################LIBRARIES########################################################
##############################################################################################################

from manim import *
from manim import Scene
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService


##############################################################################################################
###############################################MAIN###########################################################
##############################################################################################################

class Main(VoiceoverScene, MovingCameraScene):
    def construct(self):
        #Declare the right language and the language service

        self.set_speech_service(GTTSService(lang="de"))  # Setzt die Sprache auf Deutsch

        #All objects used for the acteptor contain a _a_
        #All objects used for the transductor contain a _t_
        circle_radius = 1.4
        position_a_graph = [-17.5,7.5,0]
        position_t_graph = [12.5,5,0] 
        width_a_graph = 25
        width_t_graph = 36
        #For highlighting Boxes are used. The color can be changed here
        box_color = RED
        #All Circles should have the same color. It can be changed here
        circle_color = WHITE
        self.akzeptor()
        self.transductor()
#scene_akzeptor 
        def akzeptor(self):
            ###Declaration of the explanation for the akzeptor
            #Begin Introduction task akzeptor
            #Show the chapter tile
            t_titel_a = Tex('Akzeptor', font_size = 80).move_to([-20,-6,0])
            #Show the text of the task
            t_aufgabe_a = Tex(r'Aufgabe: \\ Wir haben ein Handy.\\ Nur mit der richtigen PIN \\ wird das Handy entsperrt.', font_size = 60).move_to([-20,-8,0])
            #Show the inputparameters and the solution
            t_loesung = Tex("Die PIN lautet 123").move_to([-20,-10,0])
            t_eingabe = Tex(r"Eingabe:", r" 1,2 oder 3. ").move_to([-20,-11,0])
            #Move camera to starting position
            self.play(self.camera.frame.animate.move_to([-20,-8.5,0]).set_width(t_titel_a.width*6))
            #Move camera to the title and begin voiceover
            with self.voiceover(text="Als ersten der zwei speziellen Automaten schauen wir uns den Akzeptor anhand eines Beispiels an.") as tracker:
                self.play(Create(t_titel_a))
            with self.voiceover(text="\
                            Nehmen wir an, wir haben ein Handy. Dieses ist mit einer PIN gesperrt.") as tracker:
                self.play(Create(t_aufgabe_a))
            with self.voiceover(text="Die PIN lautet eins zwei drei.") as tracker:
                self.play(Create(t_loesung))
            with self.voiceover(text="Wir können die Zahlen eins zwei und drei in jeder beliebigen Reihenfolge eingeben. Wir wollen das Handy entsperren.") as tracker:
                self.play(Create(t_eingabe))
            
            #End Introduction task akzeptor
            self.play(self.camera.frame.animate.move_to(position_a_graph).set_width(width_a_graph))
            #Begin Creating the graph for akzeptor
            #Begin Create all the Circles on the right way      
            position_1 = [-25,5,0]
            text_a_1 = Tex(r" \\ null \\ ").move_to(position_1)
            circle_a_1 = Circle(radius=circle_radius, color=circle_color).move_to(position_1)

            position_2 =[-20,5,0]
            text_a_2 = Tex(r" \\ eins \\").move_to(position_2)
            circle_a_2 = Circle(radius=circle_radius, color=circle_color).move_to(position_2)

            position_3 = [-15,5,0]
            text_a_3 = Tex(r"\\ zwei \\").move_to(position_3)
            circle_a_3 = Circle(radius=circle_radius, color=circle_color).move_to(position_3)

            position_4 = [-10,5,0]
            text_a_4 = Tex(r" \\ entsperrt \\").move_to(position_4)
            circle_a_4 = Circle(radius=circle_radius, color=circle_color).move_to(position_4)

            #Make it an endnode
            circle_a_4_outer = Circle(color=circle_color).surround(circle_a_4, buffer_factor=1).move_to(circle_a_4)#make it an Endnode
        
            #Give the circle on the top a dedicated place
            p = Point(location = [-17.5,10,0], color=RED)
            text_a_5 = Tex("gesperrt").move_to(p)
            circle_a_5 = Circle(color=circle_color, radius=circle_radius).move_to(p)
            ##End Create all the Circles on the right way 

            #Construct the connectionpoints of the arrows to the under circle
            #Get the right points on each circle
            #circle 1
            p_a_1_1 = circle_a_1.point_at_angle(180*DEGREES)
            p_a_1_2 = circle_a_1.point_at_angle(90*DEGREES)
            p_a_1_3 = circle_a_1.point_at_angle(0*DEGREES)
            #circle 2    
            p_a_2_1 = circle_a_2.point_at_angle(180*DEGREES)
            p_a_2_2 = circle_a_2.point_at_angle(90*DEGREES)
            p_a_2_3 = circle_a_2.point_at_angle(0*DEGREES)
            #circle 3
            p_a_3_1 = circle_a_3.point_at_angle(180*DEGREES)
            p_a_3_2 = circle_a_3.point_at_angle(90*DEGREES)
            p_a_3_3 = circle_a_3.point_at_angle(0*DEGREES)
            #circle 4
            p_a_4_1 = circle_a_4_outer.point_at_angle(180*DEGREES)
            p_a_4_2 = circle_a_4_outer.point_at_angle(90*DEGREES)
            #circle 5
            p_a_5_1 = circle_a_5.point_at_angle(180*DEGREES)
            p_a_5_2 = circle_a_5.point_at_angle(225*DEGREES)
            p_a_5_3 = circle_a_5.point_at_angle(315*DEGREES)
            p_a_5_4 = circle_a_5.point_at_angle(0*DEGREES)

            #make the positions into points
            p_a_1_1= Point(color=RED).move_to(p_a_1_1)
            p_a_1_2= Point(color=RED).move_to(p_a_1_2)
            p_a_1_3= Point(color=RED).move_to(p_a_1_3)

            p_a_2_1= Point(color=RED).move_to(p_a_2_1)
            p_a_2_2= Point(color=RED).move_to(p_a_2_2)
            p_a_2_3= Point(color=RED).move_to(p_a_2_3)

            p_a_3_1= Point(color=RED).move_to(p_a_3_1)
            p_a_3_2= Point(color=RED).move_to(p_a_3_2)
            p_a_3_3= Point(color=RED).move_to(p_a_3_3)

            p_a_4_1= Point(color=RED).move_to(p_a_4_1)
            p_a_4_2= Point(color=RED).move_to(p_a_4_2)

            p_a_5_1= Point(color=RED).move_to(p_a_5_1)
            p_a_5_2= Point(color=RED).move_to(p_a_5_2)
            p_a_5_3= Point(color=RED).move_to(p_a_5_3)
            p_a_5_4= Point(color=RED).move_to(p_a_5_4)

            #Create the arrows for the graph using the points
            arrow_a_1 = LabeledArrow(label = r"1", start = p_a_1_3, end = p_a_2_1, buff=0)
            arrow_a_2 = LabeledArrow(label = r"2", start = p_a_2_3, end = p_a_3_1, buff=0)
            arrow_a_3 = LabeledArrow(label = r"3", start = p_a_3_3, end = p_a_4_1, buff=0)
            arrow_a_4 = LabeledArrow(label = r"2,3", start = p_a_1_2, end = p_a_5_1, buff=0)
            arrow_a_5 = LabeledArrow(label = r"1,3", start = p_a_2_2, end = p_a_5_2, buff=0)
            arrow_a_6 = LabeledArrow(label = r"1,2", start = p_a_3_2, end = p_a_5_3, buff=0)
            arrow_a_7 = LabeledArrow(label = r"1,2,3", start = p_a_4_2, end = p_a_5_4, buff=0)

            #Special arrow 
            radius = circle_a_5.width / 1.5
            angle = 52 * DEGREES
            start_x = radius * np.cos(angle)/ 1.6
            start_y = radius * np.sin(angle) 
            start_point = circle_a_5.get_center() + np.array([start_x, start_y, 5])
            end_angle = angle + 45.5
            end_x = radius * np.cos(end_angle) / 1.6 
            end_y = radius * np.sin(end_angle)
            end_point = circle_a_5.get_center() + np.array([end_x, end_y, 2])
            arrow_a_8 = CurvedArrow(start_point, end_point, color=WHITE, angle= 3)
            arrow_a_8_t = Tex("1,2,3").move_to([-17.5,13.5,0])
            arrow_a_8_r = SurroundingRectangle(arrow_a_8_t, color=WHITE)

            #Create the highlighting boxes
            box_a_1 = SurroundingRectangle(circle_a_1, color=box_color)
            box_a_2 = SurroundingRectangle(circle_a_2, color=box_color)
            box_a_3 = SurroundingRectangle(circle_a_3, color=box_color)
            box_a_4 = SurroundingRectangle(circle_a_4_outer, color=box_color)
            box_a_5 = SurroundingRectangle(circle_a_5, color=box_color)

            #add all the components
            self.add(circle_a_1,circle_a_2, circle_a_3, circle_a_4, circle_a_4_outer, circle_a_5, arrow_a_8_t, arrow_a_8_r)
            self.add(text_a_1, text_a_2, text_a_3,text_a_4, text_a_5)
            self.add(arrow_a_1, arrow_a_2, arrow_a_3, arrow_a_4, arrow_a_5, arrow_a_6, arrow_a_7, arrow_a_8)
            #End Creating the graph for akzeptor

            with self.voiceover(text= "Der Prozess zur Entsperrung kann in einem Graphen dargestellt werden. \
                                Nur wenn wir die Zahlen in der richtigen Reihenfolge eingeben, können wir das Handy entsperren. \
                                ") as tracker:
                #Set camera to akzeptor graph
                self.play(self.camera.frame.animate.move_to(position_a_graph).set_width(width_a_graph))
            
            with self.voiceover(text="Wir beginnen im Anfangszustand null. Hier haben wir noch nichts eingegeben. Jetzt können wir eins, zwei oder drei eingeben. \
                                Das entscheidet, in welchen Zustand wir als nächstes kommen.") as tracker:
                #Highlight the beginning state
                self.play(Create(box_a_1))
            self.remove(box_a_1)

            with self.voiceover(text="Wenn wir jetzt eine eins eingeben, dann kommen wir in den Zustand eins. Wir sind auf dem richtigen Weg, um die PIN einzugeben. ") as tracker:
                #Hightlight node eins
                self.play(Create(box_a_2))
            self.remove(box_a_2)

            with self.voiceover(text="Wenn wir eine der anderen Zahlen, also zwei oder drei eingeben, dann landen wir in dem Zustand gesperrt. \
                                Wir sind vom Weg zur richtigen PIN und der Entsperrung abgekommen. Egal was wir jetzt eingeben, wir werden diesen Zustand, gesperrt, nie wieder verlassen können. ") as tracker:
                #Highlight node gesperrt
                self.play(Create(box_a_5))
            self.remove(box_a_5)

            with self.voiceover(text="Doch nun zurück zum Zustand eins. Wir haben zuerst die eins eingegeben und befinden uns deswegen auf dem richtigen Weg. \
                                Wenn wir weiterhin die PIN eingeben, also zwei") as tracker:
                #Highlight node 1
                self.play(Create(box_a_2))
            self.remove(box_a_2)

            with self.voiceover(text="und danach drei, dann werden wir in die Zustände zwei ") as tracker:
                #Hightlight node 2
                self.play(Create(box_a_3))
            self.remove(box_a_3)

            with self.voiceover(text="und entsperrt kommen. Der Zustand entsperrt ist der Einzige, in dem unser Handy entsperrt wird. \
                                Der Akzeptor akzeptiert die Eingabe und wir können das Handy jetzt verwenden.") as tracker:
                #Highlight node entsperrt
                self.play(Create(box_a_4))
            self.remove(box_a_4)

            with self.voiceover(text="Ansonsten ist das Handy im Zustand gesperrt, also gesperrt. ") as tracker:
                #Highlight node gesperrt
                self.play(Create(box_a_5))
            self.remove(box_a_5)

            with self.voiceover(text="Das ist die Aufgabe eines Akzeptors: Er arbeitet verschiedene Zustände ab und bei dem Erreichen von bestimmten Zuständen gibt er etwas frei.") as tracker:
                #Highlight all the nodes
                self.play(Create(box_a_1))
                self.play(Create(box_a_2))
                self.play(Create(box_a_3))
                self.play(Create(box_a_4))
                self.play(Create(box_a_5))
            self.remove(box_a_1, box_a_2, box_a_3, box_a_4, box_a_5)

            #Begin explanation table
            #Elements of the table
            liste_z2 = [["1,2,3","Eingabealphabet"], 
                        ["null, eins, zwei, entsperrt, gesperrt","Zustandsmenge"],  
                        ["null","Anfangszustand"], 
                        ["entsperrt","Endzustand"],
                        ["δ","Überführungsfunktion"],]
            #declaration of all the elements for the 2nd column
            t_a= Table(
                liste_z2,
                #column titles
                col_labels=[Text("Hier"),Text("Formal")],
                include_outer_lines=True
            ).set_column_colors(BLACK,BLACK).move_to([0,-15,0]) #make the entries in the columns invisible
            
            t_a.set_row_colors(WHITE)
            self.add(t_a)
            #start showing the entries in the table
            #make the column title visible (maybe make it visible directly)
            
            #Show Eingabealphabet
            t_a.set_row_colors(WHITE, WHITE)
            self.add(t_a)
            with self.voiceover(text="Doch wie wird ein Akzeptor formal beschrieben? Zuerst haben wir ein Eingabealphabet. ") as tracker:
                self.play(self.camera.frame.animate.move_to(t_a).set_width(t_a.width*1.1))
            box_a_t = SurroundingRectangle(t_eingabe[1])
            self.add(box_a_t)
            with self.voiceover(text="Hier sind es die Zahlen, die wir eingeben können, um das Handy zu entsperren, also eins, zwei und drei. ") as tracker:
                self.play(self.camera.frame.animate.move_to([-20,-8.5,0]).set_width(t_titel_a.width*6))
            self.remove(box_a_t)

            #Show Zustandsmenge
            t_a.set_row_colors(WHITE, WHITE, WHITE)
            self.add(t_a)
            #Highlighten der Zustandsmenge in the graph
            with self.voiceover(text="Als nächstes haben wir die Zustandsmenge.") as tracker:
                self.play(self.camera.frame.animate.move_to(t_a).set_width(t_a.width*1.1))
            self.add(box_a_1,box_a_2,box_a_3,box_a_4,box_a_5)
            with self.voiceover(text="Das sind hier null, eins, zwei, entsperrt und gesperrt. Das sind die Zustände, in die das Handy kommen kann.") as tracker:
                self.play(self.camera.frame.animate.move_to(position_a_graph).set_width(width_a_graph))
            self.remove(box_a_1,box_a_2,box_a_3,box_a_4,box_a_5)

            #Show Anfangszustand
            t_a.set_row_colors(WHITE, WHITE, WHITE, WHITE)
            with self.voiceover(text="Zu Beginn des Vorganges ist das Handy im Zustand null. Das ist der Anfangszustand des Graphen.") as tracker:
                self.play(self.camera.frame.animate.move_to(t_a).set_width(t_a.width*1.1))
            self.add(t_a)
            self.add(box_a_1)
            with self.voiceover(text="Hier beginnt der Entsperrvorgang.") as tracker:
                self.play(self.camera.frame.animate.move_to(position_a_graph).set_width(width_a_graph))
            self.wait(1)
            self.remove(box_a_1)

            #Show Endzustand
            t_a.set_row_colors(WHITE, WHITE, WHITE, WHITE, WHITE)
            with self.voiceover(text="Enden tut er im Endzustand.") as tracker:
                self.play(self.camera.frame.animate.move_to(t_a).set_width(t_a.width*1.1))
            self.add(t_a)
            self.add(box_a_4)
            with self.voiceover(text="Das ist hier entsperrt. Wie bereits vorhin erwähnt, gibt es besondere Zustände, in denen ein Akzeptor etwas frei gibt. \
                                Das sind immer die Endzustände.") as tracker:
                self.play(self.camera.frame.animate.move_to(position_a_graph).set_width(width_a_graph))
            self.add(box_a_1)
            with self.voiceover(text="Beide, sowohl Anfangszustand als auch Endzustand, sind eine Teilmenge der Zustandsmenge.") as tracker:
                self.play(self.camera.frame.animate.move_to(position_a_graph).set_width(width_a_graph))
            self.remove(box_a_4, box_a_1)
            
            #Show Überführungsfunktion
            t_a.set_row_colors(WHITE, WHITE, WHITE, WHITE, WHITE, WHITE)
            with self.voiceover(text="Die Reihenfolge, in der die Zustände der Zustandsmenge angeordnet sind und die Art, wie wir in diese kommen, ist in der Überführungsfunktion abgebildet.") as tracker:
                self.play(self.camera.frame.animate.move_to(t_a).set_width(t_a.width*1.1))
            self.add(t_a)
            #self.wait(2)
            with self.voiceover(text="Diese kann wie hier als Graph dargestellt werden. Soviel zu dem Aktzeptor.") as tracker:
                self.play(self.camera.frame.animate.move_to(position_a_graph).set_width(width_a_graph))
            self.remove(t_a)
                
            self.clear()

#Scene transformator
        def transductor(self):
            #Show the chapter tile
            position_t_text = [20,-9,0]
            t_titel_t = Tex('Transduktor', font_size = 80).move_to([20,-6,0])
            t_aufgabe_t = Tex(r'Aufgabe: \\ Wir wollen eine Fahrkarte kaufen.', font_size = 60).move_to([20,-8,0])
            t_loesung_t = Tex(r"Eine Fahrkarte kostet 5 Euro.").move_to([20,-10,0])
            t_eingabe_t = Tex(r"Eingabe:", r" 1 Euro oder 2 Euro ").move_to([20,-11,0])
            t_ausgabe_t = Tex(r"Ausgabe:", r" Fahrkarte oder nichts ").move_to([20,-12,0])

            #Set the camera to the right position
            self.play(self.camera.frame.animate.set(width = t_titel_t.width*3).move_to(position_t_text))
            with self.voiceover(text="Als nächstes kommen wir zu den Transduktoren. Wir erklären diese am Beispiel eines Fahrkartenautomaten. ") as tracker:
                self.play(Create(t_titel_t))
            with self.voiceover(text="Wir wollen eine Fahrkarte kaufen.") as tracker:
                self.play(Create(t_aufgabe_t))
            with self.voiceover(text="Eine Fahrkarte kostet 5€. Der Automat wechselt nicht.") as tracker:
                self.play(Create(t_loesung_t))
            with self.voiceover(text="Wir können in den Automaten 1€ oder 2€ Stücke einwerfen.") as tracker:
                self.play(Create(t_eingabe_t))
            with self.voiceover(text="Das bedeutet, sobald 5 oder mehr Euro eingeworfen werden, gibt der Automat eine Fahrkarte aus. Ansonsten gibt er nichts aus.") as tracker:
                self.play(Create(t_ausgabe_t))

            #Begin Creating the graph for transduktor
            #Declaration of the positions of the nodes
            position_t_1= [0,5,0]
            position_t_2=[5,10,0]
            position_t_3=[5,0,0]
            position_t_4=[10,5,0]
            position_t_5=[20,5,0]

            #Create the elements for the nodes and move them tho the right position
            text_t_1 = Tex(r"kein Geld \\ eingeworfen").move_to(position_t_1)
            circle_t_1 = Circle(color=circle_color, radius= circle_radius).move_to(position_t_1)

            text_t_2 = Tex(r"1 Euro \\ eingeworfen").move_to(position_t_2)
            circle_t_2 = Circle(color=circle_color, radius= circle_radius).move_to(position_t_2)

            text_t_3 = Tex(r"2 Euro \\ eingeworfen").move_to(position_t_3)
            circle_t_3 = Circle(color=circle_color, radius= circle_radius).move_to(position_t_3)

            text_t_4 = Tex(r"3 Euro \\ eingeworfen").move_to(position_t_4)
            circle_t_4 = Circle(color=circle_color, radius= circle_radius).move_to(position_t_4)

            text_t_5 = Tex(r" 4 Euro \\ eingeworfen").move_to(position_t_5)
            circle_t_5 = Circle(color=circle_color, radius= circle_radius).move_to(position_t_5)

            #add all the elements
            self.add(text_t_1, text_t_2, text_t_3, text_t_4, text_t_5)
            self.add(circle_t_1, circle_t_2, circle_t_3, circle_t_4, circle_t_5)

            #Creating all the positions on the circle for the arrows
            p_t_1_1 = circle_t_1.point_at_angle(45*DEGREES)
            p_t_1_2 = circle_t_1.point_at_angle(315*DEGREES)
            p_t_1_3 = circle_t_1.point_at_angle(270*DEGREES)

            p_t_2_1 = circle_t_2.point_at_angle(225*DEGREES)
            p_t_2_2 = circle_t_2.point_at_angle(270*DEGREES)
            p_t_2_3 = circle_t_2.point_at_angle(315*DEGREES)

            p_t_3_1 = circle_t_3.point_at_angle(135*DEGREES)
            p_t_3_2 = circle_t_3.point_at_angle(90*DEGREES)
            p_t_3_3 = circle_t_3.point_at_angle(45*DEGREES)
            p_t_3_4 = circle_t_3.point_at_angle(0*DEGREES)

            p_t_4_1 = circle_t_4.point_at_angle(135*DEGREES)
            p_t_4_2 = circle_t_4.point_at_angle(225*DEGREES)
            p_t_4_3 = circle_t_4.point_at_angle(0*DEGREES)
            p_t_4_4= circle_t_4.point_at_angle(90*DEGREES)
            
            p_t_5_1 = circle_t_5.point_at_angle(180*DEGREES)
            p_t_5_2 = circle_t_5.point_at_angle(225*DEGREES)
            p_t_5_3= circle_t_5.point_at_angle(270*DEGREES)

            #Transform the positions into points
            p_t_1_1= Point(color=RED).move_to(p_t_1_1)
            p_t_1_2= Point(color=RED).move_to(p_t_1_2)
            p_t_1_3= Point(color=RED).move_to(p_t_1_3)

            p_t_2_1= Point(color=RED).move_to(p_t_2_1)
            p_t_2_2= Point(color=RED).move_to(p_t_2_2)
            p_t_2_3= Point(color=RED).move_to(p_t_2_3)

            p_t_3_1= Point(color=RED).move_to(p_t_3_1)
            p_t_3_2= Point(color=RED).move_to(p_t_3_2)
            p_t_3_3= Point(color=RED).move_to(p_t_3_3)
            p_t_3_4= Point(color=RED).move_to(p_t_3_4)

            p_t_4_1= Point(color=RED).move_to(p_t_4_1)
            p_t_4_2= Point(color=RED).move_to(p_t_4_2)
            p_t_4_3= Point(color=RED).move_to(p_t_4_3)
            p_t_4_4 =Point().move_to(p_t_4_4)

            p_t_5_1= Point(color=RED).move_to(p_t_5_1)
            p_t_5_2= Point(color=RED).move_to(p_t_5_2)
            p_t_5_3 =Point().move_to(p_t_5_3)

            #Create the arrows with the points
            arrow_t_1 = LabeledArrow(label = r"1 Euro,\\ nichts", start = p_t_1_1, end = p_t_2_1, buff=0)
            arrow_t_2 = LabeledArrow(label = r"2 Euro, \\ nichts", start = p_t_1_2, end = p_t_3_1, buff=0)
            arrow_t_3 = LabeledArrow(label = r"1 Euro, \\ nichts", start = p_t_2_2, end = p_t_3_2, buff=0)
            arrow_t_4 = LabeledArrow(label = r"2 Euro \\ nichts", start = p_t_2_3, end = p_t_4_1, buff=0)
            arrow_t_5 = LabeledArrow(label = r"1 Euro, \\ nichts", start = p_t_3_3, end = p_t_4_2, buff=0)
            arrow_t_6 = LabeledArrow(label = r"1 Euro, \\ nichts", start = p_t_4_3, end = p_t_5_1, buff=0)
            arrow_t_7 = LabeledArrow(label = r"2 Euro, \\ nichts", start = p_t_3_4, end = p_t_5_2, buff=0)
                        
            #Create the arrows which turn
            p_t_1_3= circle_t_1.point_at_angle(90*DEGREES)
            p_t_1_3 =Point().move_to(p_t_1_3)
            p_t_1_4= circle_t_1.point_at_angle(270*DEGREES)
            p_t_1_4 =Point().move_to(p_t_1_4)

            p_t_6_1 = Point().move_to([20,-2.5,0])
            p_t_6_2 = Point().move_to([0,-2.5,0])
            p_t_7_1 = Point().move_to([10,12.5,0])
            p_t_7_2 = Point().move_to([0,12.5,0])

            l_t_1 = Line(start=p_t_5_3, end=p_t_6_1)
            l_t_2 = LabeledLine(start=p_t_6_1, end=p_t_6_2, label=r"1 oder 2 Euro,\\ Fahrkarte")
            l_t_8 = Line(start=p_t_6_2, end=p_t_1_4)
            a_t_8 = Arrow(start=p_t_6_2, end=p_t_1_4)

            l_t_3 = Line(start = p_t_4_4, end=p_t_7_1)
            l_t_4 = LabeledLine(start=p_t_7_1, end=p_t_7_2, label= r"2 Euro,\\ Fahrkarte")
            l_t_9 = Line(start=p_t_6_2, end=p_t_1_4)
            a_t_9 = Arrow(start=p_t_7_2, end = p_t_1_3)

            #add the arrows that turn
            self.add(l_t_1, l_t_2, a_t_8, l_t_3, l_t_4, a_t_9, l_t_8, l_t_9)
            self.add(arrow_t_1, arrow_t_2, arrow_t_3, arrow_t_4, arrow_t_5, arrow_t_6, arrow_t_7)
            #End Creating the graph for transduktor

            #Create the highlighting boxes
            box_t_1 = SurroundingRectangle(circle_t_1, color=box_color)
            box_t_2 = SurroundingRectangle(circle_t_2, color=box_color)
            box_t_3 = SurroundingRectangle(circle_t_3, color=box_color)
            box_t_4 = SurroundingRectangle(circle_t_4, color=box_color)
            box_t_5 = SurroundingRectangle(circle_t_5, color=box_color)

            self.play(self.camera.frame.animate.move_to(position_t_graph ).set_width(width_t_graph))

            #Begin explanation transduktor
            with self.voiceover(text="Wir starten im Zustand, dass wir noch kein Geld in den Automaten geworfen haben.") as tracker:
                self.play(Create(box_t_1))
            self.remove(box_t_1)
            with self.voiceover(text="Wir werfen zwei Euro rein und landen im Zustand zwei Euro eingeworfen.") as tracker:
                self.play(Create(box_t_3))
            self.remove(box_t_3)
            with self.voiceover(text="Wir werfen noch einmal zwei Euro rein. Jetzt haben wir vier Euro reingeworfen. Wenn wir jetzt noch einen oder zwei Euro einwerfen, gibt der Automat eine Fahrkarte aus,") as tracker:
                self.play(Create(box_t_5))
            self.remove(box_t_5)
            with self.voiceover(text="bevor er in den Anfangszustand zurückgeht. Wir wollen eine weitere Fahrkarte.") as tracker:
                self.play(Create(box_t_1))
            self.remove(box_t_1)
            #end first graph

            with self.voiceover(text="Diesmal werfen wir zuerst einen,") as tracker:
                self.play(Create(box_t_2))
            self.remove(box_t_2)
            with self.voiceover(text="dann zwei Euro ein. Jetzt sind wir bei drei Euro.") as tracker:
                self.play(Create(box_t_4))
            self.remove(box_t_4)
            with self.voiceover(text="Diesmal bezahlen wir passend und werfen wieder 2 Euro rein. \
                                Wir haben 5 Euro bezahlt und erhalten eine Fahrkarte.") as tracker:
                self.play(Create(box_t_4))
            self.remove(box_t_4)
            #End explanation transduktor
    
            #begin table transduktor   
            #table content
            liste_z2 = [["Eingabealphabet", "1 Euro, 2 Euro"], 
                        ["Zustandsmenge","kein Geld eingeworfen, \n 1 Euro eingeworfen, \n 2 Euro eingeworfen, \n 3 Euro eingeworfen, \n  4 Euro eingeworfen"],  
                        ["Anfangszustand", "kein Geld eingeworfen"], 
                        ["Überführungsfunktion", "δ"],
                        ["Ausgabealphabet", "nichts, Fahrkarte"],
                        ["Ausgabefunktion", "λ"]]
            #declaration of all the elements for the 2nd column
            t2= Table(
                liste_z2,
                #column titles
                col_labels=[Text("Formal"),Text("hier")],
                include_outer_lines=True
            ).set_column_colors(BLACK, BLACK).move_to([0,-15,0]) #make the entries in the columns invisible
            #end table transduktor   

            #self.play(self.camera.frame.animate.move_to(t2).set_width(t2.width*2))
            t2.set_row_colors(WHITE)
            self.add(t2)
            self.wait(2)

            #Start showing the table entries
            #Show Eingabealphabet
            t2.set_row_colors(WHITE, WHITE)
            self.add(t2)
            with self.voiceover(text="Doch wie ist der Automat formal beschrieben? Wieder haben wir ein Eingabealphabet, ") as tracker:
                self.play(self.camera.frame.animate.move_to(t2).set_width(t2.width*1.8))
            box_t_e = SurroundingRectangle(t_eingabe_t[1])
            self.add(box_t_e)
            with self.voiceover(text="hier ist es ein Euro oder zwei Euro. ") as tracker:
                self.play(self.camera.frame.animate.set(width = t_titel_t.width*3).move_to(position_t_text))
            self.remove(box_t_e)

            #Show Zustandsmenge
            t2.set_row_colors(WHITE, WHITE, WHITE)
            self.add(t2)
            with self.voiceover(text="Die Zustandsmenge ist diesmal: ") as tracker:
                self.play(self.camera.frame.animate.move_to(t2).set_width(t2.width*1.8))

            #Move camera to graph
            self.add(box_t_1, box_t_2, box_t_3, box_t_4, box_t_5)
            with self.voiceover(text="kein Geld eingeworfen, 1 Euro eingeworfen, 2 Euro eingeworfen, 3 Euro eingeworfen und 4 Euro eingeworfen") as tracker:
                self.play(self.camera.frame.animate.move_to(position_t_graph ).set_width(width_t_graph))
            self.remove(box_t_1, box_t_2, box_t_3, box_t_4, box_t_5)

            #Show Anfangszustand
            t2.set_row_colors(WHITE, WHITE, WHITE, WHITE)
            self.add(t2)
            with self.voiceover(text="Beginnen tun wir wieder bei dem Anfangszustand") as tracker:
                #show table
                self.play(self.camera.frame.animate.move_to(t2).set_width(t2.width*1.8))

            #Move camera to graph
                self.add(box_t_1)
            with self.voiceover(text="hier “kein Geld eingeworfen”.") as tracker:
                self.play(self.camera.frame.animate.move_to(position_t_graph ).set_width(width_t_graph))
            self.remove(box_t_1)

            #Show Überführungsfunktion
            t2.set_row_colors(WHITE, WHITE, WHITE, WHITE, WHITE)
            self.add(t2)

            #Move camera to table
            with self.voiceover(text="Die Überführungsfunktion") as tracker:
                self.play(self.camera.frame.animate.move_to(t2).set_width(t2.width*2))

            #Move camera to graph
            with self.voiceover(text="ist wieder der Graph.") as tracker:
                self.play(self.camera.frame.animate.move_to(position_t_graph ).set_width(width_t_graph))

            #Show Ausgabealphabet
            t2.set_row_colors(WHITE, WHITE, WHITE, WHITE, WHITE, WHITE)
            self.add(t2)
            with self.voiceover(text="Wir haben auch ein Ausgabealphabet,") as tracker:
                self.play(self.camera.frame.animate.move_to(t2).set_width(t2.width*1.8))
            box_t_a = SurroundingRectangle(t_ausgabe_t[1])
            self.add(box_t_a)
            with self.voiceover(text=" “nichts oder Fahrkarte”") as tracker:
                self.play(self.camera.frame.animate.set(width = t_titel_t.width*3).move_to(position_t_text))
            self.remove(box_t_a)

            #Show Ausgabefunktion
            t2.set_row_colors(WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE)
            self.add(t2)
            with self.voiceover(text="und eine Ausgabefunktion,") as tracker:
                self.play(self.camera.frame.animate.move_to(t2).set_width(t2.width*1.8))
            with self.voiceover(text="die an den Pfeilen steht. ") as tracker:
                self.play(self.camera.frame.animate.move_to(position_t_graph ).set_width(width_t_graph))

            #Ending of transdultor
            with self.voiceover(text="Soviel zu den Transduktoren. Wir hoffen, euch hat unser Video gefallen. \
                                Solltet ihr noch mehr zu endlichen Automaten und der Automatentheorie erfahren wollen, dann freut euch auf unser Paper über endliche Automaten. ") as tracker:
                self.play(self.camera.frame.animate.move_to(position_t_graph ).set_width(width_t_graph))
             
            self.clear()
            #Ending scene; goodbye
            t_wiedersehen = Tex("Vielen Dank für eure Aufmerksamkeit")
            self.add(t_wiedersehen)    
            self.camera.frame.animate.move_to(t_wiedersehen).set_width(t_wiedersehen.width)   
            with self.voiceover(text="Vielen Dank für eure Aufmerksamkeit.") as tracker:
                self.camera.frame.animate.move_to(t_wiedersehen).set_width(t_wiedersehen.width)
            
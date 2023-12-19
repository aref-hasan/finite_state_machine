from manim import *


class video(MovingCameraScene):
    def construct(self):
        self.aktzeptoren()
    
    def aktzeptoren(self):
       
        #Show the chapter tile
        t_titel = Tex('Prüfautomat')
        self.play(self.camera.frame.animate.set(width = t_titel.width*2))
        self.add(t_titel)
        self.wait(1)
        self.clear()
        #Show the text of the task
        t_aufgabe_a = Tex(r'Aufgabe: \\ Wir haben ein Handy. \\ Nur mit der richtigen PIN wird das Handy entsperrt.', font_size = 60)
        self.play(self.camera.frame.animate.set(width = t_aufgabe_a.width*2))
        self.add(t_aufgabe_a)
        self.wait(1)
        self.clear()
        #Show the inputparameters and the solution
        t_loesung = Tex("Die PIN ist 123").move_to([0,4,0])
        self.add(t_loesung)
        self.play(self.camera.frame.animate.move_to(t_loesung).set_width(t_loesung.width))
        self.wait(1)
        t_eingabe = Tex(r"Eingabe:", r" 1,2 oder 3. ").move_to([0,3,0])
        self.add(t_eingabe)
        self.play(self.camera.frame.animate.move_to(t_eingabe).set_width(t_eingabe.width))
        self.wait(1)
        #Here no clear since it is necessary for the explanation
        
        #Create all the arrows on the right way
        arrow_b = Arrow(buff=0) #begin arrow
        arrow_1 = LabeledArrow(label = "1",start = LEFT, end = RIGHT, buff=0)
        arrow_2 = LabeledArrow(label = "2",start = LEFT, end = RIGHT, buff=0)
        arrow_3 = LabeledArrow(label = "3",start = LEFT, end = RIGHT, buff=0)

        #Create all the Circles on the right way
        circle_1 = Circle(radius=1, color=BLUE)
        text_1 = Tex("n")
        circle_2 = Circle(radius=1, color=BLUE)
        text_2 = Tex("eins")
        circle_3 = Circle(radius=1, color=BLUE)
        text_3 = Tex("zwei")
        circle_4 = Circle(radius=1, color=BLUE)
        text_4 = Tex("Frei")
        circle_4_outer = Circle(color=BLUE).surround(circle_4, buffer_factor=1).move_to(circle_4)#make it an Endnode
        
        #Give the circle on the bottom a dedicated place
        p = Point(location = [1,-3,0], color=RED)
        text_u = Tex("gesperrt").move_to(p)
        #Make it an endnode
        circle_u = Circle(color=BLUE).move_to(p).surround(text_u, buffer_factor=1.2)
     
        #Conntect all the circles with text
        g_u = Group(text_u, circle_u)
        g1 = Group(text_1, circle_1)
        g2 = Group(text_2, circle_2)
        g3 = Group(text_3, circle_3)
        g4 = Group(text_4, circle_4, circle_4_outer)
        #Connect the nodes of the right way
        rigth_way= Group(arrow_b,g1,arrow_1, g2,arrow_2,g3,arrow_3,g4).arrange(buff = 0).move_to([0,1,0])

        #Construct the connectionpoints of the arrows to the under circle
        p_u_1 = circle_u.point_at_angle(180*DEGREES)
        p_u_2 = circle_u.point_at_angle(135*DEGREES)
        p_u_3 = circle_u.point_at_angle(45*DEGREES)
        p_u_4 = circle_u.point_at_angle(0*DEGREES)

        #Construct the connectionpoints of the arrows of the right way
        p1 = circle_1.point_at_angle(270*DEGREES)
        p2 = circle_2.point_at_angle(270*DEGREES)
        p3 = circle_3.point_at_angle(270*DEGREES)
        p4 = circle_4_outer.point_at_angle(270*DEGREES)

        #Create the Point type on the points
        p_u_1 = Point().move_to(p_u_1)
        p_u_2 = Point().move_to(p_u_2)
        p_u_3 = Point().move_to(p_u_3)
        p_u_4 = Point().move_to(p_u_4)
        p1 = Point().move_to(p1)
        p2 = Point().move_to(p2)
        p3 = Point().move_to(p3)
        p4 = Point().move_to(p4)
        #Construct the arrows to the under node
        arrow_u_1 = LabeledArrow(label = "2,3", start = p1, end = p_u_1, buff=0)
        arrow_u_2 = LabeledArrow(label = "1,3", start = p2, end = p_u_2, buff=0)
        arrow_u_3 = LabeledArrow(label = "1,2", start= p3, end = p_u_3, buff=0)
        arrow_u_4 = LabeledArrow(label = "1,2,3", start = p4, end = p_u_4, buff=0)
        #Add everything together
        self.add(rigth_way,g_u,arrow_u_1,arrow_u_2,arrow_u_3,arrow_u_4)
        
        #Start of the camera movements for the graph
        self.play(self.camera.frame.animate.move_to(circle_1).set_width(circle_1.radius*4))#.set_run_time(2))
        self.wait(1)
        self.play(self.camera.frame.animate.move_to(circle_2).set_width(circle_2.radius*4).set_run_time(2))
        self.wait(1)
        self.play(self.camera.frame.animate.move_to(circle_1).set_width(circle_1.radius*4))#.set_run_time(2))
        self.wait(1)
        self.play(self.camera.frame.animate.move_to(circle_u).set_width(circle_u.radius*8))
        self.wait(2)
        self.play(self.camera.frame.animate.move_to(circle_2).set_width(circle_2.radius*4).set_run_time(2))
        self.wait(1)
        self.play(self.camera.frame.animate.move_to(circle_3).set_width(circle_3.radius*4).set_run_time(2))
        self.wait(1)
        self.play(self.camera.frame.animate.move_to(circle_4).set_width(circle_4.radius*4).set_run_time(2))
        self.wait(1)
        self.play(self.camera.frame.animate.move_to([0.5,-2,0]).set_width(rigth_way.width*1.4))
        self.wait(2)
        #Show the complete graph 
        self.play(self.camera.frame.animate.move_to(circle_u).set_width(circle_u.radius*8))
        self.wait(2)

        #declaration of all the elements or the 1st column 
        liste_rows = [Tex("1,2,3"), Tex("n, eins, zwei, drei, offen, gesperrt"), Tex("n"), Tex("frei"), MathTex( "\delta")]
        #declaration of all the elements for the 2nd column
        liste_z2= [["Eingabealphabet"], ["Zustandsmenge"], ["Anfangszustand"], ["Endzustand"],["Überführungsfunktion"]]

        t2= Table(
            liste_z2,
            row_labels=liste_rows,
            #column titles
            col_labels=[Tex("Formal")],
            top_left_entry=Text("hier"),
            include_outer_lines=True
        ).set_column_colors(BLACK, BLACK, BLACK).move_to([0,-15,0]) #make the entries in the columns invisible

        
        #start showing the entries in the table
        #make the column title visible (maybe make it visible directly)
        self.play(self.camera.frame.animate.move_to(t2).set_width(t2.width*2))
        t2.set_row_colors(WHITE)
        self.add(t2)
        self.wait(2)
        

        #Show Eingabealphabet
        t2.set_row_colors(WHITE, WHITE)
        self.add(t2)
        self.play(self.camera.frame.animate.move_to(t_eingabe).set_width(t_eingabe.width))
        box_1 = SurroundingRectangle(t_eingabe[1])
        self.add(box_1)
        self.wait(2)
        self.remove(box_1)
        

        #Show Zustandsmenge
        t2.set_row_colors(WHITE, WHITE, WHITE)
        self.add(t2)
        #Highlighten der Zustandsmenge in the graph
        self.play(self.camera.frame.animate.move_to(t2).set_width(t2.width*2))
        box_1 = SurroundingRectangle(circle_1)
        box_2 = SurroundingRectangle(circle_2)
        box_3 = SurroundingRectangle(circle_3)
        box_4 = SurroundingRectangle(circle_u)
        box_5 = SurroundingRectangle(circle_4_outer)
        self.play(self.camera.frame.animate.move_to([0.5,-2,0]).set_width(rigth_way.width*1.4))
        self.wait(1)
        self.add(box_1,box_2,box_3,box_4,box_5)
        self.wait(3)
        self.remove(box_1,box_2,box_3,box_4,box_5)

        self.wait(2)

        #Show Anfangszustand
        t2.set_row_colors(WHITE, WHITE, WHITE, WHITE)
        self.play(self.camera.frame.animate.move_to(t2).set_width(t2.width*2))
        self.add(t2)
        self.wait(2)
        self.play(self.camera.frame.animate.move_to([0.5,-2,0]).set_width(rigth_way.width*1.4))
        self.wait(1)
        self.add(box_1)
        self.wait(3)
        self.remove(box_1)

        #Show Endzustand
        t2.set_row_colors(WHITE, WHITE, WHITE, WHITE, WHITE)
        self.play(self.camera.frame.animate.move_to(t2).set_width(t2.width*2))
        self.add(t2)
        self.wait(2)
        self.play(self.camera.frame.animate.move_to([0.5,-2,0]).set_width(rigth_way.width*1.4))
        self.wait(1)
        self.add(box_5)
        self.wait(3)
        self.remove(box_5)
        
        #Show Überführungsfunktion
        t2.set_row_colors(WHITE, WHITE, WHITE, WHITE, WHITE, WHITE)
        self.play(self.camera.frame.animate.move_to(t2).set_width(t2.width*2))
        self.add(t2)
        self.wait(2)
        self.play(self.camera.frame.animate.move_to([0.5,-2,0]).set_width(rigth_way.width*1.4))
        self.wait(5)
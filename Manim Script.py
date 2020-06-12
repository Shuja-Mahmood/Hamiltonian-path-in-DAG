from manimlib.imports import *

class final(Scene):
    def construct(self):
        
        #> Introduction
        
        presenter1 = TextMobject("Shuja Mahmood")
        presenter2 = TextMobject("Tayyaba Shoukat")
        number1 = TextMobject("BSCS-18008")
        number2 = TextMobject("BSCS-18053")
        
        presenter1.set_height(0.3)
        presenter2.set_height(0.3)
        number1.set_height(0.25)
        number2.set_height(0.25)
        
        presenter1.move_to(np.array([-2, -0.5, 0]))
        presenter2.move_to(np.array([-2, -1.25, 0]))
        number1.move_to(np.array([2, -0.5, 0]))
        number2.move_to(np.array([2, -1.25, 0]))
        
        title_center = TextMobject("Hamiltonian Path in a DAG", tex_to_color_map={"DAG": YELLOW})
        title_center.move_to(np.array([0, 1, 0]))
        description = TextMobject("A path in a graph such that it visits \\\\"
                                "each and every vertex $exactly$ once", tex_to_color_map={"$exactly$": YELLOW})
        title = TextMobject("Hamiltonian Path in a DAG", tex_to_color_map={"Hamiltonian Path in a DAG": BLUE})
        title.to_edge(UP)
        
        self.play(Write(title_center))
        self.wait()
        
        self.play(
            Write(presenter1),
            Write(number1),
            Write(presenter2),
            Write(number2)
        )
        
        self.wait(2)
        
        self.play(
            FadeOutAndShift(title_center, UP, run_time=0.1),
            FadeInFromDown(title),
            FadeOut(title_center),
            FadeOutAndShift(presenter1, LEFT),
            FadeOutAndShift(presenter2, LEFT),
            FadeOutAndShift(number1, RIGHT),
            FadeOutAndShift(number2, RIGHT)
        )
        
        self.play(Write(description))
        self.wait(3)
        self.play(FadeOut(description))
        
        #> Graph
        
        HEIGHT = 0.275
        TEXT = -3
        INDEX = 0
        DARK = rgb_to_color([0.225, 0.225, 0.225])
        LENGTH = 0.45
        RADIUS = 0.2
        STROKE_COLOR = GREEN
        STROKE_WIDTH = 5
        INITIAL_STROKE_WIDTH = 2
        FILL = BLACK
        TRAVERSAL_FILL = BLUE
        OPACITY = 0.8
        OFFSET = [0.4, -0.4, 0]
        
        points = [
            [0.2, 1, 0],    # A: 0
            [2.5, 2.5, 0],  # B: 1
            [1.2, -2, 0],   # C: 2
            [5.6, 2.9, 0],  # D: 3
            [4.3, 1.3, 0],  # E: 4
            [3.5, -1.5, 0], # F: 5
            [2.3, 0, 0],    # G: 6
            [4.5, -3, 0],   # H: 7
            [6, 0, 0]       # I: 8
        ]
        
        for i in range(len(points)):
            points[i] = [points[i][0] + OFFSET[0], points[i][1] + OFFSET[1], points[i][2] + OFFSET[2]]
        
        connections = [
            (0, 1), #0
            (0, 2), #1
            (0, 6), #2
            (1, 3), #3
            (1, 4), #4
            (2, 5), #5
            (2, 6), #6
            (2, 7), #7
            (3, 8), #8
            (4, 3), #9
            (4, 8), #10
            (5, 4), #11
            (5, 6), #12
            (5, 7), #13
            (5, 8), #14
            (6, 1), #15
            (6, 4), #16
            (8, 7)  #17
        ]
        
        stack = [[-6.125+(i/1.25), -2.75, 0] for i in range(len(points))]
        stack.reverse()
        
        nodes = []
        edges = []
        label = []
        
        for i in range(len(points)):
            c = Circle(radius=RADIUS, color=FILL, stroke_color=YELLOW, stroke_width=INITIAL_STROKE_WIDTH)
            t = TextMobject(chr(65+i))

            t.set_height(0.5*c.get_width())
            
            c.move_to(points[i])
            t.move_to(c)
            nodes.append(c)
            label.append(t)
        
        for i in range(len(connections)):
            a = Arrow(points[connections[i][0]], points[connections[i][1]], color=WHITE, stroke_width=3, tip_length=0.15, preserve_tip_size_when_scaling=False)
            edges.append(a)
        
        self.play(
            ShowCreation(nodes[0]),
            ShowCreation(nodes[1]),
            ShowCreation(nodes[2]),
            ShowCreation(nodes[3]),
            ShowCreation(nodes[4]),
            ShowCreation(nodes[5]),
            ShowCreation(nodes[6]),
            ShowCreation(nodes[7]),
            ShowCreation(nodes[8])
        )
        self.play(
            Write(label[0]),
            Write(label[1]),
            Write(label[2]),
            Write(label[3]),
            Write(label[4]),
            Write(label[5]),
            Write(label[6]),
            Write(label[7]),
            Write(label[8])
        )
        self.play(
            ShowCreation(edges[0]),
            ShowCreation(edges[1]),
            ShowCreation(edges[2]),
            ShowCreation(edges[3]),
            ShowCreation(edges[4]),
            ShowCreation(edges[5]),
            ShowCreation(edges[6]),
            ShowCreation(edges[7]),
            ShowCreation(edges[8]),
            ShowCreation(edges[9]),
            ShowCreation(edges[10]),
            ShowCreation(edges[11]),
            ShowCreation(edges[12]),
            ShowCreation(edges[13]),
            ShowCreation(edges[14]),
            ShowCreation(edges[15]),
            ShowCreation(edges[16]),
            ShowCreation(edges[17])
        )

        self.wait()

        
        #> Explaination
        step1 = TextMobject("Perform a Topological sort", tex_to_color_map={"Topological sort": PINK})
        step1.set_height(0.375)
        step1.move_to(np.array([TEXT, 2, 0]))
        
        self.play(Write(step1))
        self.wait()
        
        step2 = TextMobject("Begin by choosing an $arbitary$ vertex", tex_to_color_map={"vertex": BLUE})
        step2.set_height(HEIGHT)
        step2.move_to(np.array([TEXT, 0, 0]))
        
        self.play(Write(step2))
        self.wait()
        
        #! D
        self.play(nodes[3].set_stroke, TRAVERSAL_FILL, STROKE_WIDTH, OPACITY)
        
        step3 = TextMobject("Then perform a DFS on all its outgoing vertices", tex_to_color_map={"DFS": BLUE})
        step3.set_height(HEIGHT)
        step3.move_to(np.array([TEXT, 0, 0]))
        
        self.play(Transform(step2, step3))
        
        step4 = TextMobject("Untill it reaches a vertex with no outgoing vertices", tex_to_color_map={"no outgoing vertices": YELLOW})
        step4.set_height(HEIGHT)
        step4.move_to(np.array([TEXT, -1, 0]))

        self.play(Write(step4))
        self.wait(2)
        
        #> First Traversal
        
        #! D -> I
        self.play(
            nodes[8].set_stroke, TRAVERSAL_FILL, STROKE_WIDTH, OPACITY,
            edges[8].set_stroke, BLUE,
            edges[8].set_fill, BLUE
        )
        
        #! I -> H
        self.play(
            nodes[7].set_stroke, TRAVERSAL_FILL, STROKE_WIDTH, OPACITY,
            edges[17].set_stroke, BLUE,
            edges[17].set_fill, BLUE
        )
        
        
        step5 = TextMobject("Now add it to the stack and remove it from the graph", tex_to_color_map={"stack": BLUE, "remove": RED})
        step5.set_height(HEIGHT)
        step5.move_to(np.array([TEXT, -1, 0]))
        
        self.play(Transform(step4, step5))
        self.wait(2)
        
        #> Store First element
        
        #! stack(H)
        stack_H = TextMobject("H")
        stack_H.set_height(LENGTH-0.2)
        stack_H.move_to(points[7])
        sqr_H = Square(side_length=LENGTH)
        cir_H = Circle(radius=RADIUS, stroke_color=BLUE)
        sqr_H.move_to(stack[INDEX])
        cir_H.move_to(points[7])
        
        self.play(
            stack_H.move_to, stack[INDEX],
            Transform(cir_H, sqr_H),
            nodes[7].set_fill, GREY, 1-OPACITY,
            nodes[7].set_stroke, RED, OPACITY,
            label[7].set_fill, GREY, OPACITY
        )
        INDEX += 1
        self.wait(1)
        
        #! stack(I)
        stack_I = TextMobject("I")
        stack_I.set_height(LENGTH-0.2)
        stack_I.move_to(points[8])
        sqr_I = Square(side_length=LENGTH)
        cir_I = Circle(radius=RADIUS, stroke_color=BLUE)
        sqr_I.move_to(stack[INDEX])
        cir_I.move_to(points[8])
        
        self.play(
            stack_I.move_to, stack[INDEX],
            Transform(cir_I, sqr_I),
            nodes[8].set_fill, GREY, 1-OPACITY,
            nodes[8].set_stroke, RED, OPACITY,
            label[8].set_fill, GREY, OPACITY,
            edges[17].set_fill, DARK, 1,
            edges[17].set_stroke, DARK
        )
        INDEX += 1
        self.wait(0.5)
        
        #! stack(D)
        stack_D = TextMobject("D")
        stack_D.set_height(LENGTH-0.2)
        stack_D.move_to(points[3])
        sqr_D = Square(side_length=LENGTH)
        cir_D = Circle(radius=RADIUS, stroke_color=BLUE)
        sqr_D.move_to(stack[INDEX])
        cir_D.move_to(points[3])
        
        self.play(
            stack_D.move_to, stack[INDEX],
            Transform(cir_D, sqr_D),
            nodes[3].set_fill, GREY, 1-OPACITY,
            nodes[3].set_stroke, RED, OPACITY,
            label[3].set_fill, GREY, OPACITY,
            edges[8].set_fill, DARK, 1,
            edges[8].set_stroke, DARK
        )
        INDEX += 1
        
        step6 = TextMobject("Now repeat the process with another $arbitary$ vertex", tex_to_color_map={"vertex": BLUE})
        step6.set_height(HEIGHT)
        step6.move_to(np.array([TEXT, -1, 0]))
        
        self.wait(0.5)
        self.play(Transform(step4, step6))
        self.wait()
        
        #! F
        self.play(nodes[5].set_stroke, TRAVERSAL_FILL, STROKE_WIDTH, OPACITY)
        self.wait()
        
        #! F -> H
        self.play(
            edges[13].set_stroke, BLUE,
            edges[13].set_fill, BLUE
        )
        self.play(
            edges[13].set_fill, DARK, 1,
            edges[13].set_stroke, DARK
        )
        
        #! F -> I
        self.play(
            edges[14].set_stroke, BLUE,
            edges[14].set_fill, BLUE
        )
        self.play(
            edges[14].set_fill, DARK, 1,
            edges[14].set_stroke, DARK
        )
        
        #! F -> E
        self.play(
            nodes[4].set_stroke, TRAVERSAL_FILL, STROKE_WIDTH, OPACITY,
            edges[11].set_stroke, BLUE,
            edges[11].set_fill, BLUE
        )
        
        #! E -> I
        self.play(
            edges[10].set_stroke, BLUE,
            edges[10].set_fill, BLUE
        )
        self.play(
            edges[10].set_fill, DARK, 1,
            edges[10].set_stroke, DARK
        )
        
        #! E -> D
        self.play(
            edges[9].set_stroke, BLUE,
            edges[9].set_fill, BLUE
        )
        self.play(
            edges[9].set_fill, DARK, 1,
            edges[9].set_stroke, DARK
        )
        
        #! stack(E)
        stack_E = TextMobject("E")
        stack_E.set_height(LENGTH-0.2)
        stack_E.move_to(points[4])
        sqr_E = Square(side_length=LENGTH)
        cir_E = Circle(radius=RADIUS, stroke_color=BLUE)
        sqr_E.move_to(stack[INDEX])
        cir_E.move_to(points[4])
        
        self.play(
            stack_E.move_to, stack[INDEX],
            Transform(cir_E, sqr_E),
            nodes[4].set_fill, GREY, 1-OPACITY,
            nodes[4].set_stroke, RED, OPACITY,
            label[4].set_fill, GREY, OPACITY,
            edges[11].set_fill, DARK, 1,
            edges[11].set_stroke, DARK
        )
        INDEX += 1
        
        #! F -> G
        self.play(
            nodes[6].set_stroke, TRAVERSAL_FILL, STROKE_WIDTH, OPACITY,
            edges[12].set_stroke, BLUE,
            edges[12].set_fill, BLUE
        )
        
        #! G -> E
        self.play(
            edges[16].set_stroke, BLUE,
            edges[16].set_fill, BLUE
        )
        
        self.play(
            edges[16].set_fill, DARK, 1,
            edges[16].set_stroke, DARK
        )
        
        #! G -> B
        self.play(
            nodes[1].set_stroke, TRAVERSAL_FILL, STROKE_WIDTH, OPACITY,
            edges[15].set_stroke, BLUE,
            edges[15].set_fill, BLUE
        )

        #! B -> E
        self.play(
            edges[4].set_stroke, BLUE,
            edges[4].set_fill, BLUE
        )
        
        self.play(
            edges[4].set_stroke, DARK,
            edges[4].set_fill, DARK
        )
        
        #! B -> D
        self.play(
            edges[3].set_stroke, BLUE,
            edges[3].set_fill, BLUE
        )
        
        self.play(
            edges[3].set_stroke, DARK,
            edges[3].set_fill, DARK
        )
                
        #! stack(B)
        stack_B = TextMobject("B")
        stack_B.set_height(LENGTH-0.2)
        stack_B.move_to(points[1])
        sqr_B = Square(side_length=LENGTH)
        cir_B = Circle(radius=RADIUS, stroke_color=BLUE)
        sqr_B.move_to(stack[INDEX])
        cir_B.move_to(points[1])
        
        self.play(
            stack_B.move_to, stack[INDEX],
            Transform(cir_B, sqr_B),
            nodes[1].set_fill, GREY, 1-OPACITY,
            nodes[1].set_stroke, RED, OPACITY,
            label[1].set_fill, GREY, OPACITY,
            edges[15].set_fill, DARK, 1,
            edges[15].set_stroke, DARK
        )
        INDEX += 1
        
        #! stack(G)
        stack_G = TextMobject("G")
        stack_G.set_height(LENGTH-0.2)
        stack_G.move_to(points[6])
        sqr_G = Square(side_length=LENGTH)
        cir_G = Circle(radius=RADIUS, stroke_color=BLUE)
        sqr_G.move_to(stack[INDEX])
        cir_G.move_to(points[6])
        
        self.play(
            stack_G.move_to, stack[INDEX],
            Transform(cir_G, sqr_G),
            nodes[6].set_fill, GREY, 1-OPACITY,
            nodes[6].set_stroke, RED, OPACITY,
            label[6].set_fill, GREY, OPACITY,
            edges[12].set_fill, DARK, 1,
            edges[12].set_stroke, DARK
        )
        INDEX += 1
        
        #! stack(F)
        stack_F = TextMobject("F")
        stack_F.set_height(LENGTH-0.2)
        stack_F.move_to(points[5])
        sqr_F = Square(side_length=LENGTH)
        cir_F = Circle(radius=RADIUS, stroke_color=BLUE)
        sqr_F.move_to(stack[INDEX])
        cir_F.move_to(points[5])
        
        self.play(
            stack_F.move_to, stack[INDEX],
            Transform(cir_F, sqr_F),
            nodes[5].set_fill, GREY, 1-OPACITY,
            nodes[5].set_stroke, RED, OPACITY,
            label[5].set_fill, GREY, OPACITY,
            edges[12].set_fill, DARK, 1,
            edges[12].set_stroke, DARK
        )
        INDEX += 1
        
        #! A
        self.play(nodes[0].set_stroke, TRAVERSAL_FILL, STROKE_WIDTH, OPACITY)
        self.wait()
        
        #! A -> C
        self.play(
            nodes[2].set_stroke, TRAVERSAL_FILL, STROKE_WIDTH, OPACITY,
            edges[1].set_stroke, BLUE,
            edges[1].set_fill, BLUE
        )
        
        #! C -> H
        self.play(
            edges[7].set_stroke, BLUE,
            edges[7].set_fill, BLUE
        )
        
        self.play(
            edges[7].set_stroke, DARK,
            edges[7].set_fill, DARK
        )
        
        #! C -> F
        self.play(
            edges[5].set_stroke, BLUE,
            edges[5].set_fill, BLUE
        )
        
        self.play(
            edges[5].set_stroke, DARK,
            edges[5].set_fill, DARK
        )
        
        #! C -> G
        self.play(
            edges[6].set_stroke, BLUE,
            edges[6].set_fill, BLUE
        )
        
        self.play(
            edges[6].set_stroke, DARK,
            edges[6].set_fill, DARK
        )
        
        #! stack(C)
        stack_C = TextMobject("C")
        stack_C.set_height(LENGTH-0.2)
        stack_C.move_to(points[2])
        sqr_C = Square(side_length=LENGTH)
        cir_C = Circle(radius=RADIUS, stroke_color=BLUE)
        sqr_C.move_to(stack[INDEX])
        cir_C.move_to(points[2])
        
        self.play(
            stack_C.move_to, stack[INDEX],
            Transform(cir_C, sqr_C),
            nodes[2].set_fill, GREY, 1-OPACITY,
            nodes[2].set_stroke, RED, OPACITY,
            label[2].set_fill, GREY, OPACITY,
            edges[1].set_fill, DARK, 1,
            edges[1].set_stroke, DARK
        )
        INDEX += 1
        
        #! A -> G
        self.play(
            edges[2].set_stroke, BLUE,
            edges[2].set_fill, BLUE
        )
        
        self.play(
            edges[2].set_stroke, DARK,
            edges[2].set_fill, DARK
        )
        
        #! A -> B
        self.play(
            edges[0].set_stroke, BLUE,
            edges[0].set_fill, BLUE
        )
        
        self.play(
            edges[0].set_stroke, DARK,
            edges[0].set_fill, DARK
        )
        
        #! stack(A)
        stack_A = TextMobject("A")
        stack_A.set_height(LENGTH-0.2)
        stack_A.move_to(points[0])
        sqr_A = Square(side_length=LENGTH)
        cir_A = Circle(radius=RADIUS, stroke_color=BLUE)
        sqr_A.move_to(stack[INDEX])
        cir_A.move_to(points[0])
        
        self.play(
            stack_A.move_to, stack[INDEX],
            Transform(cir_A, sqr_A),
            nodes[0].set_fill, GREY, 1-OPACITY,
            nodes[0].set_stroke, RED, OPACITY,
            label[0].set_fill, GREY, OPACITY
        )
        INDEX += 1
        
        self.wait()
        
        self.play(
            FadeOut(step2),
            FadeOut(step4)
        )
        
        step7 = TextMobject("We traversed the entire graph once \\\\"
                            "Time Complexity", tex_to_color_map={"entire graph once": YELLOW})
        step7.set_height(0.75)
        step7.move_to(np.array([TEXT, 1, 0]))
        
        time_complexity_1 = TextMobject("$O(|V|+|E|)$")
        time_complexity_1.move_to(np.array([TEXT, -0.75, 0]))

        self.play(Write(step7))
        self.play(Write(time_complexity_1))

        self.wait()
        
        #> Ending
        step8 = TextMobject("Check if path is continuous", tex_to_color_map={"path is continuous": PINK})
        step8.set_height(0.375)
        step8.move_to(np.array([TEXT, 2, 0]))
        
        self.play(
            Transform(step1, step8),
            FadeOut(step7),
            time_complexity_1.set_opacity, 0
        )
        self.wait()
        
        step9 = TextMobject("Since we cannot go back to a vertex in the stack \\\\"
                            "we must traverse $all$ vertices that came before it", tex_to_color_map={"$all$ vertices that came before it": YELLOW})
        step9.set_height(HEIGHT*2)
        step9.move_to(np.array([TEXT, 1, 0]))
        
        self.play(Write(step9))
        self.wait()
        
        extra_text = TextMobject("Meaning we traverse the stack from top to bottom \\\\"
                                 "to check if Hamiltonian path exists", tex_to_color_map={"Hamiltonian path": BLUE})
        extra_text.set_height(HEIGHT*2)
        extra_text.move_to(np.array([TEXT, -0.5, 0]))
        
        self.play(Write(extra_text))
        self.wait(2)
        
        sqr_A = cir_A.copy()
        sqr_B = cir_B.copy()
        sqr_C = cir_C.copy()
        sqr_D = cir_D.copy()
        sqr_E = cir_E.copy()
        sqr_F = cir_F.copy()
        sqr_G = cir_G.copy()
        sqr_H = cir_H.copy()
        sqr_I = cir_I.copy()
        
        sqr_A.set_stroke(GREEN)
        sqr_B.set_stroke(GREEN)
        sqr_C.set_stroke(GREEN)
        sqr_D.set_stroke(GREEN)
        sqr_E.set_stroke(GREEN)
        sqr_F.set_stroke(GREEN)
        sqr_G.set_stroke(GREEN)
        sqr_H.set_stroke(GREEN)
        sqr_I.set_stroke(GREEN)
        
        self.play(
            FadeOut(cir_A),
            LaggedStartMap(ShowCreation, sqr_A),
            run_time=0.75
        )
        self.play(
            nodes[0].set_fill, FILL, 1,
            nodes[0].set_stroke, STROKE_COLOR, STROKE_WIDTH, 1,
            label[0].set_fill, WHITE, 1,
            run_time=0.75
        )
        
        self.play(
            FadeOut(cir_C),
            LaggedStartMap(ShowCreation, sqr_C),
            run_time=0.75
        )
        self.play(
            nodes[2].set_fill, FILL, 1,
            nodes[2].set_stroke, STROKE_COLOR, STROKE_WIDTH, 1,
            label[2].set_fill, WHITE, 1,
            edges[1].set_stroke, GREEN,
            edges[1].set_fill, GREEN,
            run_time=0.75
        )
        
        self.play(
            FadeOut(cir_F),
            LaggedStartMap(ShowCreation, sqr_F),
            run_time=0.75
        )
        self.play(
            nodes[5].set_fill, FILL, 1,
            nodes[5].set_stroke, STROKE_COLOR, STROKE_WIDTH, 1,
            label[5].set_fill, WHITE, 1,
            edges[5].set_stroke, GREEN,
            edges[5].set_fill, GREEN,
            run_time=0.75
        )
        
        self.play(
            FadeOut(cir_G),
            LaggedStartMap(ShowCreation, sqr_G),
            run_time=0.75
        )
        self.play(
            nodes[6].set_fill, FILL, 1,
            nodes[6].set_stroke, STROKE_COLOR, STROKE_WIDTH, 1,
            label[6].set_fill, WHITE, 1,
            edges[12].set_stroke, GREEN,
            edges[12].set_fill, GREEN,
            run_time=0.75
        )
        
        self.play(
            FadeOut(cir_B),
            LaggedStartMap(ShowCreation, sqr_B),
            run_time=0.75
        )
        self.play(
            nodes[1].set_fill, FILL, 1,
            nodes[1].set_stroke, STROKE_COLOR, STROKE_WIDTH, 1,
            label[1].set_fill, WHITE, 1,
            edges[15].set_stroke, GREEN,
            edges[15].set_fill, GREEN,
            run_time=0.75
        )
        
        self.play(
            FadeOut(cir_E),
            LaggedStartMap(ShowCreation, sqr_E),
            run_time=0.75
        )
        self.play(
            nodes[4].set_fill, FILL, 1,
            nodes[4].set_stroke, STROKE_COLOR, STROKE_WIDTH, 1,
            label[4].set_fill, WHITE, 1,
            edges[4].set_stroke, GREEN,
            edges[4].set_fill, GREEN,
            run_time=0.75
        )
        
        self.play(
            FadeOut(cir_D),
            LaggedStartMap(ShowCreation, sqr_D),
            run_time=0.75
        )
        self.play(
            nodes[3].set_fill, FILL, 1,
            nodes[3].set_stroke, STROKE_COLOR, STROKE_WIDTH, 1,
            label[3].set_fill, WHITE, 1,
            edges[9].set_stroke, GREEN,
            edges[9].set_fill, GREEN,
            run_time=0.75
        )
        
        self.play(
            FadeOut(cir_I),
            LaggedStartMap(ShowCreation, sqr_I),
            run_time=0.75
        )
        self.play(
            nodes[8].set_fill, FILL, 1,
            nodes[8].set_stroke, STROKE_COLOR, STROKE_WIDTH, 1,
            label[8].set_fill, WHITE, 1,
            edges[8].set_stroke, GREEN,
            edges[8].set_fill, GREEN,
            run_time=0.75
        )
        
        self.play(
            FadeOut(cir_H),
            LaggedStartMap(ShowCreation, sqr_H),
            run_time=0.75
        )
        self.play(
            nodes[7].set_fill, FILL, 1,
            nodes[7].set_stroke, STROKE_COLOR, STROKE_WIDTH, 1,
            label[7].set_fill, WHITE, 1,
            edges[17].set_stroke, GREEN,
            edges[17].set_fill, GREEN,
            run_time=0.75
        )
        
        self.wait()
        
        step10 = TextMobject("We traversed the entire stack once \\\\"
                            "Time Complexity", tex_to_color_map={"entire stack once": YELLOW})
        step10.set_height(0.75)
        step10.move_to(np.array([TEXT, 1, 0]))
        
        time_complexity_2 = TextMobject("$O(|V|)$")
        time_complexity_2.move_to(np.array([TEXT, 0, 0]))

        self.play(
            Transform(step9, step10),
            FadeOut(extra_text)
        )
        self.play(Write(time_complexity_2))

        self.wait()
        
        step11 = TextMobject("Overall Time Complexity", tex_to_color_map={"Overall Time Complexity": YELLOW})
        step11.set_height(0.375)
        step11.move_to(np.array([TEXT, 1, 0]))
        
        self.play(Transform(step9, step11))
        
        total_time_complexity = VGroup(time_complexity_1, time_complexity_2)
        
        self.play(
            Transform(time_complexity_2, time_complexity_1),
            time_complexity_1.set_opacity, 1
        )
        
        step12 = Rectangle(height=1, width=3.25, color=BLUE)
        step12.move_to(time_complexity_1)
        
        self.play(ShowCreation(step12))
        
        self.wait(3)
        
        clr = Rectangle(height=9, width=16, color=BLACK, fill_color=BLACK)
        self.play(ShowCreation(clr))
        self.play(clr.set_opacity, 1)

        end = TextMobject("Thank You for Watching!")
        self.play(Write(end))
        self.wait(1)
        
        self.play(FadeOut(end))
        self.wait(0.5)

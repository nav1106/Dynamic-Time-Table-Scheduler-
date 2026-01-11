import matplotlib.pyplot as plt
import networkx as nx

class TimetableScheduler:
    def __init__(self):
        self.graph = nx.Graph()
        self.courses = {}
        self.color_map = {}
        self.time_slots = ['9:00-10:30', '10:45-12:15', '13:00-14:30', '14:45-16:15']
        self.days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    
    def initialize_courses(self):
        courses_data = [
            ('CS101', 'Programming'), ('CS102', 'Data Structures'), 
            ('MATH101', 'Calculus I'), ('PHY101', 'Physics I'),
            ('CS201', 'Algorithms'), ('MATH102', 'Calculus II'),
            ('CHEM101', 'Chemistry I'), ('BIO101', 'Biology I'),
            ('CS301', 'Database Systems'), ('PHY102', 'Physics II')
        ]
        
        for course_id, name in courses_data:
            self.courses[course_id] = name
            self.graph.add_node(course_id)
        
        cs_conflicts = [('CS101', 'CS102'), ('CS101', 'CS201'), ('CS102', 'CS201'), ('CS201', 'CS301')]
        math_conflicts = [('MATH101', 'MATH102')]
        science_conflicts = [('PHY101', 'CHEM101'), ('CHEM101', 'BIO101')]
        conflicts = cs_conflicts + math_conflicts + science_conflicts
        
        for c1, c2 in conflicts:
            self.graph.add_edge(c1, c2)
        
        self._graph_coloring()
    
    def _graph_coloring(self):
        nodes_sorted = sorted(self.graph.nodes(), key=lambda x: self.graph.degree(x), reverse=True)
        self.color_map = {}
        
        for node in nodes_sorted:
            neighbor_colors = set()
            for neighbor in self.graph.neighbors(node):
                if neighbor in self.color_map:
                    neighbor_colors.add(self.color_map[neighbor])
            
            color = 0
            while color in neighbor_colors:
                color += 1
            self.color_map[node] = color
    
    def add_course_dynamically(self):
        print("\n" + "="*40)
        print("ADD NEW COURSE")
        print("="*40)
        
        course_id = input("Course code: ").strip().upper()
        if course_id in self.courses:
            print("Course exists!")
            return
        
        course_name = input("Course name: ").strip()
        print(f"Available courses: {', '.join(self.courses.keys())}")
        conflicts_input = input("Conflicts (comma-separated): ").strip()
        conflict_list = [c.strip().upper() for c in conflicts_input.split(',') if c.strip()]
        
        self.courses[course_id] = course_name
        self.graph.add_node(course_id)
        
        for conflict in conflict_list:
            if conflict in self.courses:
                self.graph.add_edge(course_id, conflict)
        
        neighbor_colors = set()
        for neighbor in self.graph.neighbors(course_id):
            if neighbor in self.color_map:
                neighbor_colors.add(self.color_map[neighbor])
        
        chosen_slot = 0
        while chosen_slot in neighbor_colors:
            chosen_slot += 1
        
        self.color_map[course_id] = chosen_slot
        
        day = self.days[chosen_slot // 4]
        time_slot = self.time_slots[chosen_slot % 4]
        
        courses_in_same_slot = [c for c, color in self.color_map.items() 
                               if color == chosen_slot and c != course_id]
        
        if courses_in_same_slot:
            print(f"{course_id} scheduled with {', '.join(courses_in_same_slot)} at: {day} {time_slot}")
        else:
            print(f"{course_id} scheduled at: {day} {time_slot}")
    
    def plot_timetable(self):
        fig, ax = plt.subplots(figsize=(14, 8))
        
        print(f"\n📊 Total courses scheduled: {len(self.courses)}")
        print(f"📊 Time slots used: {len(set(self.color_map.values()))}")
        
        slot_usage = {}
        for course_id, color in self.color_map.items():
            if color not in slot_usage:
                slot_usage[color] = []
            slot_usage[color].append(course_id)
        
        for i, day in enumerate(self.days):
            for j, time_slot in enumerate(self.time_slots):
                slot_idx = i * 4 + j
                courses_here = slot_usage.get(slot_idx, [])
                
                if courses_here:
                    has_conflict = False
                    for course1 in courses_here:
                        for course2 in courses_here:
                            if course1 != course2 and self.graph.has_edge(course1, course2):
                                has_conflict = True
                                break
                        if has_conflict:
                            break
                    
                    cell_color = '#FFCCCB' if has_conflict else '#E8F5E8'
                    course_text = '\n'.join(courses_here)
                else:
                    cell_color = '#F5F5F5'
                    course_text = 'FREE'
                
                rect = plt.Rectangle((i, j), 1, 1, facecolor=cell_color, edgecolor='black', linewidth=1)
                ax.add_patch(rect)
                ax.text(i + 0.5, j + 0.7, course_text, ha='center', va='center', fontsize=9, weight='bold')
                ax.text(i + 0.5, j + 0.3, time_slot, ha='center', va='center', fontsize=8, color='gray')
        
        ax.set_xlim(0, len(self.days))
        ax.set_ylim(0, len(self.time_slots))
        ax.set_xticks([i + 0.5 for i in range(len(self.days))])
        ax.set_yticks([j + 0.5 for j in range(len(self.time_slots))])
        ax.set_xticklabels(self.days, fontsize=12, weight='bold')
        ax.set_yticklabels(['', '', '', ''])
        ax.set_title('DYNAMIC TIMETABLE SCHEDULER', fontsize=14, weight='bold', pad=20)
        
        for i in range(len(self.days) + 1):
            ax.axvline(x=i, color='gray', linewidth=0.8)
        for j in range(len(self.time_slots) + 1):
            ax.axhline(y=j, color='gray', linewidth=0.8)
        
        plt.tight_layout()
        plt.show()
    
    def plot_conflict_graph(self):
        colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7', '#DDA0DD', '#98FB98']
        node_colors = [colors[self.color_map[node] % len(colors)] for node in self.graph.nodes()]
        
        plt.figure(figsize=(12, 8))
        pos = nx.spring_layout(self.graph, seed=42)
        nx.draw_networkx_edges(self.graph, pos, width=2, alpha=0.7, edge_color='gray')
        nx.draw_networkx_nodes(self.graph, pos, node_color=node_colors, node_size=2000)
        nx.draw_networkx_labels(self.graph, pos, font_size=10, font_weight='bold')
        plt.title("COURSE CONFLICT GRAPH", fontsize=14, pad=20)
        plt.axis('off')
        plt.tight_layout()
        plt.show()

def main():
    scheduler = TimetableScheduler()
    scheduler.initialize_courses()
 
    while True:
        print("\n" + "="*30)
        print("MENU")
        print("1. Add New Course")
        print("2. Show Timetable") 
        print("3. Show Conflict Graph")
        print("4. Exit")
        
        choice = input("Choice (1-4): ").strip()
        
        if choice == '1':
            scheduler.add_course_dynamically()
        elif choice == '2':
            print("Generating Timetable...")
            scheduler.plot_timetable()
        elif choice == '3':
            print("Generating Conflict Graph...")
            scheduler.plot_conflict_graph()
        elif choice == '4':
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()

# Dynamic-Time-Table-Scheduler-
Time table scheduler using advanced graph theory

This project implements an automated academic timetable scheduling system using **graph coloring techniques** from graph theory. The objective is to generate **conflict-free timetables** for courses or examinations by modeling scheduling constraints as a graph and applying a **greedy graph coloring algorithm**.

The system supports dynamic updates, allowing new courses or conflicts to be added without recomputing the entire timetable from scratch.

---

## Problem Statement

Manual timetable scheduling is time-consuming, error-prone, and difficult to scale as constraints increase. Conflicts such as overlapping courses, shared faculty, or limited resources make scheduling complex. This project addresses these challenges by applying graph coloring to ensure that no two conflicting courses are assigned the same time slot.

---

## Methodology

- Courses are represented as **vertices** in a graph  
- Conflicts between courses are represented as **edges**  
- Time slots are represented as **colors**  
- A **greedy (First-Fit) graph coloring algorithm** assigns the minimum possible color to each vertex while avoiding conflicts  

---

## System Architecture

1. **User Layer**
   - Add courses and define conflicts
   - View generated timetable and conflict graph

2. **Application Logic Layer**
   - Course Management Module
   - Graph Construction Module
   - Graph Coloring Algorithm (Greedy)

3. **Visualization Layer**
   - Timetable visualization using Matplotlib
   - Conflict graph visualization using NetworkX

---

## Technologies Used

- Python
- NetworkX (graph construction and analysis)
- Matplotlib (visualization)
- Graph Theory concepts

---

## Features

- Conflict-free timetable generation
- Dynamic addition of courses and constraints
- Efficient greedy coloring approach
- Graph-based visualization of conflicts
- Scalable for moderate-sized academic datasets

---

## Screenshots

<img width="1046" height="674" alt="Screenshot 2026-01-11 at 10 40 23 AM" src="https://github.com/user-attachments/assets/09903257-ec19-4ec1-a8b9-c8af81a23422" />
<img width="1394" height="805" alt="Screenshot 2026-01-11 at 10 40 39 AM" src="https://github.com/user-attachments/assets/be20b043-59ab-4a29-824b-b2c7ce13e448" />
<img width="1173" height="805" alt="Screenshot 2026-01-11 at 10 40 57 AM" src="https://github.com/user-attachments/assets/8a43f8e0-304a-49ed-9496-92d1f56338db" />

---

## Results and Analysis

The greedy graph coloring algorithm successfully produces conflict-free schedules with low computational overhead. While it does not guarantee the minimum number of time slots, it provides fast and practical solutions suitable for real-world academic environments. The use of graph abstraction improves flexibility and clarity in handling constraints.

---

## Limitations

- Greedy coloring is heuristic-based and may not produce optimal color usage
- Performance may degrade for very large graphs
- Soft constraints (preferences) are not fully supported

---

## Future Enhancements

- Implement optimized coloring algorithms (DSATUR, backtracking)
- Support soft constraints and priorities
- Web-based user interface
- Integration with institutional databases

---

## How to Run

1. Clone the repository
   ```bash
   git clone https://github.com/your-username/timetable-graph-coloring.git
